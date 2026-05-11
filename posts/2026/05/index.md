---
title: "Beyond DAU: How to Measure Habit Formation with Survival Analysis"
author: "dlindelof"
date: "2026-05-08"
format: html
---

# The Product Dilemma: Spike and Fade

Have you ever launched a feature, watched the Day 1 adoption metrics spike beautifully, and then spent the next month wondering if anyone actually *kept* using it? 

If you work in product management or software engineering, you know that getting a user to click a shiny new button once is the easy part. The true test of a feature's value is whether it builds a sustained habit. If our treatment (a UI overhaul, a new recommendation algorithm) activates users on Day 1 but they never return, we haven't built a successful product.

To measure this rigorously, let's define an **"event"** as any calendar day where a user engages with our feature at least once. Aggregating by day smooths out the noise of a user frantically double-clicking within a single session while perfectly capturing the core heartbeat of daily active usage.

Crucially, the psychology behind trying a feature for the very first time (initial activation) is completely different from the psychology of returning for the fifth time (habitual usage). Therefore, when we analyze our data, we need to separate these two phases.

# The "7-Day DAU" Trap

When tasked with measuring retention, it is incredibly tempting to reach for simple binary outcomes. We ask questions like, *"Did the user return within 7 days?"* or we simply count the number of Daily Active Users (DAU) inside a fixed observation window.

While simple to query and easy to explain, this approach is statistically inefficient and can actively mislead product decisions:

1.  **Arbitrary Time Horizons**: Why 7 days? Why 30 days? Fixed windows are arbitrary. If your feature is highly successful at bringing users back on Day 8, a 7-day metric labels your launch a total failure.
2.  **Masking Acceleration**: A fantastic feature might not just bring users back; it might bring them back *faster*. A fixed-window binary metric only asks *if* they returned, completely missing the valuable insight that they returned sooner than they otherwise would have.
3.  **Confounding Activation with Retention**: If your UI change successfully activates a massive wave of new users, a simple population-wide return metric can be heavily skewed. We need a framework that isolates the effect on initial activation from the effect on sustained repeat usage among those already activated.

# Visualizing Engagement: Meet Alice and Bob

To see how we can analyze this better, let's look at the timelines of two representative users who enroll in our experiment on different calendar days. We observe each user over a 10-day follow-up window post-exposure.

Instead of just staring at tables, let's visualize their engagement on a calendar scale using R:

```{r}
suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
})

# Create dummy timelines for our two characters
data <- data.frame(
  user = c(rep("Alice (Habitual)", 4), "Bob (Bounced)"),
  day = c(1, 3, 6, 9, 4), # Alice starts Day 1, Bob starts Day 4
  event_type = c("Exposure", "First Event", "Repeat Event", "Repeat Event", "Exposure"),
  censored = c(FALSE, FALSE, FALSE, FALSE, FALSE)
)

# Add administrative censoring points at 10 days post-exposure
censoring_data <- data.frame(
  user = c("Alice (Habitual)", "Bob (Bounced)"),
  day = c(11, 14), # 1 + 10, 4 + 10
  event_type = c("Censored", "Censored"),
  censored = c(TRUE, TRUE)
)

full_data <- rbind(data, censoring_data)

# Plot their journeys
ggplot(full_data, aes(x = day, y = user, color = event_type, shape = event_type)) +
  geom_point(size = 4) +
  geom_line(aes(group = user), color = "gray") +
  scale_shape_manual(values = c("Exposure" = 17, "First Event" = 18, "Repeat Event" = 16, "Censored" = 4)) +
  scale_color_manual(values = c("Exposure" = "#2b8cbe", "First Event" = "#8856a7", "Repeat Event" = "#2ca25f", "Censored" = "#de2d26")) +
  theme_minimal() +
  labs(title = "User Engagement Timelines (Calendar Scale)",
       x = "Calendar Day",
       y = "",
       color = "Milestone",
       shape = "Milestone") +
  ylim("Bob (Bounced)", "Alice (Habitual)")
```

Notice the rich story here:

-   **Alice** enrolls on Day 1, tries the feature on Day 3, and triggers multiple repeat events before her observation window ends (is censored) on Day 11.
-   **Bob** enrolls on Day 4, gets exposed, but never triggers a single event before his window ends on Day 14.

Standard metrics struggle to handle Alice's multiple events and Bob's right-censoring elegantly. Survival analysis handles both natively.

# Flipping the Cox Model for Product Growth

To analyze these timelines rigorously, we use the **Cox Proportional Hazards model**. 

If you took a statistics class, you might remember survival analysis being used in medical research where an "event" means failure or death. For product growth, we flip that interpretation on its head: an **event** is a positive milestone (product usage). 

### The Core Intuition

-   **The Hazard Rate ($h(t)$)**: Think of this as a user's *instantaneous momentum*—the speed and likelihood of them engaging with the product at time $t$, given they haven't done so yet in the current interval.
-   **The Hazard Ratio (HR)**: This is our ultimate success metric. It compares the engagement momentum of our treatment group to the control group ($HR = h_{treatment}(t) / h_{control}(t)$).
    -   **$HR > 1$**: The treatment accelerates usage. Users return faster and more frequently. **This is what we want to build.**
    -   **$HR = 1$**: Flat impact.
    -   **$HR < 1$**: The treatment slows down engagement.

### Key Model Assumptions

When applying this model, we rely on three fundamental assumptions:

1.  **Proportional Hazards**: We assume the treatment boost is constant over time. If our shiny new UI doubles a user's likelihood of returning on Day 2, it should also roughly double it on Day 8.
2.  **Non-informative Censoring**: We assume that users being censored (their window ending) tells us nothing about their underlying habits. Because our censoring happens purely because the calendar window ran out (administrative censoring), this assumption holds perfectly.
3.  **Independence Across Clusters**: While Alice's repeat events are obviously correlated with each other, we assume Alice's behavior is completely independent of Bob's.

# Tutorial: A Realistic R Simulation

Let's put this into practice by simulating a highly realistic dataset. We will generate 200 users who experience varying numbers of repeat events within a fixed 10-day window. 

To make it truly realistic, we inject a **Gamma frailty** (a random effect) per user. This simulates the fact that some people are inherently "power users" while others are inherently casual, inducing true within-user correlation.

Here is the complete, copy-pasteable tutorial code:

```{r}
library(survival)
library(dplyr)

# Set seed for reproducibility
set.seed(123)

n_users <- 200 
obs_window <- 10 # 10-day follow-up window per user

# 1. Simulate Treatment Allocation and Inherent Frailty
# A Gamma distribution with mean 1 perfectly centers our "average" user
user_frailty <- rgamma(n_users, shape = 2, rate = 2) 
users <- data.frame(
  user_id = 1:n_users,
  treatment = rbinom(n_users, 1, 0.5),
  frailty = user_frailty
)

simulated_data <- list()

# 2. Generate Timelines using a Gap-Time Formulation
for (i in 1:n_users) {
  u <- users[i, ]
  current_time <- 0
  event_count <- 0
  
  while (current_time < obs_window) {
    is_first <- (event_count == 0)
    
    # Baseline rates: harder to activate initially, easier to trigger repeat usage
    base_rate <- if (is_first) 0.05 else 0.15
    
    # Let's say our treatment is amazing: doubles activation (HR=2), triples repeat usage (HR=3)
    hr <- if (u$treatment == 1) {
      if (is_first) 2.0 else 3.0
    } else {
      1.0
    }
    
    # Total hazard combines baseline, treatment boost, and personal frailty
    rate <- base_rate * hr * u$frailty
    t_next <- rexp(1, rate)
    
    if (current_time + t_next <= obs_window) {
      # Event occurs inside the window! Reset the gap-time clock.
      event_count <- event_count + 1
      current_time <- current_time + t_next
      
      simulated_data[[length(simulated_data) + 1]] <- data.frame(
        user_id = u$user_id,
        treatment = u$treatment,
        is_first_event = is_first,
        time = t_next, # Gap time since last event
        event = 1
      )
    } else {
      # Window ends before the next event occurs. Censor the remaining time.
      t_censored <- obs_window - current_time
      simulated_data[[length(simulated_data) + 1]] <- data.frame(
        user_id = u$user_id,
        treatment = u$treatment,
        is_first_event = is_first,
        time = t_censored,
        event = 0 # Censored observation
      )
      break 
    }
  }
}

df <- do.call(rbind, simulated_data)

# 3. Fit a Marginal Cox Model with SE Clustering
# Notice the elegant syntax: treatment * strata(...) automatically handles baseline absorption
model <- coxph(Surv(time, event) ~ treatment * strata(is_first_event) + cluster(user_id), data = df)
summary(model)
```

# The "Frailty Attenuation" Gotcha

If you run the code above, you might notice something mind-bending when you exponentiate the coefficients (`exp(coef)`): **the recovered hazard ratios will be noticeably lower than our true simulated values of 2.0 and 3.0.**

Did the math fail? Not at all. You are witnessing a classic statistical gotcha known as **frailty attenuation**.

### The Depleting Pool Analogy

Think of our gap-time risk intervals as a waiting pool. Because our treatment is highly successful, the treated "power users" (high frailty) trigger their events incredibly fast and reset their clocks. 

If you look at the tail end of any gap interval (say, users who have gone 7 days without an event), the treated pool is heavily depleted of fast users. Almost everyone left waiting is an inherently slow, casual user. 

Because marginal models (`cluster(user_id)`) simply average engagement across the population day-by-day without tracking individual frailty identities, this sorting mechanism mathematically pulls the estimated population-averaged effect down towards 1.

### How to Read the Output

Despite the conservative attenuation, marginal reporting is exactly what we want for product decisions because it answers the aggregate business question: *"What happens to the population engagement rate at scale?"*

When reading your summary tables, keep these rules in mind:

1.  **Exponentiate**: Always run `exp(coef)` to convert log-hazards into interpretable Hazard Ratios.
2.  **Reference Level**: The main `treatment` coefficient represents the impact on repeat usage (where `is_first_event = FALSE`).
3.  **Interaction as Difference**: The interaction term `treatment:strata(...)` is the *difference* between activation and repeat usage. Add this to the main effect before exponentiating to find your true initial activation impact.

***

*Want to run this on your own production data? We've open-sourced a companion Colab notebook that handles the heavy lifting. Just plug in your experiment IDs:* [Launch Colab Notebook](URL_PLACEHOLDER)
