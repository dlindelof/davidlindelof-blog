# Run: Rscript ctr-exposure-simulation.R [output-directory]
# Defaults to ctr-simulation-output in the current working directory.
required <- c("ggplot2", "lme4")
missing <- required[!vapply(required, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing)) {
  stop("Missing required R package(s): ", paste(missing, collapse = ", "),
       ". Install them before running this simulation.", call. = FALSE)
}
library(ggplot2)
library(lme4)
set.seed(20261010)
args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 1L) stop("Usage: Rscript ctr-exposure-simulation.R [output-directory]", call. = FALSE)
out <- if (length(args)) args[[1]] else "ctr-simulation-output"
dir.create(out, recursive = TRUE, showWarnings = FALSE)
repetitions <- 200L
beta <- log(1.2)
alpha <- qlogis(0.002)
sigma <- 1.2
# The same items and exposures are used in all repetitions. Exposure is
# independent of baseline propensity, and identical in A and B for every item.
items <- data.frame(item = factor(seq_len(300)),
                    n = rep(c(1000L, 10000L, 100000L), each = 100))
items$u <- rnorm(nrow(items), 0, sigma)
items$p_A <- plogis(alpha + items$u)
items$p_B <- plogis(alpha + items$u + beta)
items$true_lift <- items$p_B / items$p_A - 1
truth <- c(mean = mean(items$true_lift), median = median(items$true_lift),
           pooled = weighted.mean(items$p_B, items$n) /
             weighted.mean(items$p_A, items$n) - 1, beta = beta)
stopifnot(max(abs(qlogis(items$p_B) - qlogis(items$p_A) - beta)) < 1e-12)

simulate_once <- function(k) {
  d <- items
  d$clicks_A <- rbinom(nrow(d), d$n, d$p_A)
  d$clicks_B <- rbinom(nrow(d), d$n, d$p_B)
  d$observed_lift <- d$clicks_B / d$clicks_A - 1
  keep <- d$clicks_A > 0
  dat <- rbind(
    data.frame(item = d$item, arm = 0, clicks = d$clicks_A, n = d$n),
    data.frame(item = d$item, arm = 1, clicks = d$clicks_B, n = d$n))
  messages <- character()
  fit <- withCallingHandlers(glmer(
    cbind(clicks, n - clicks) ~ arm + (1 | item), data = dat,
    family = binomial, nAGQ = 9,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))),
    warning = function(w) { messages <<- c(messages, conditionMessage(w)); invokeRestart("muffleWarning") })
  eta_A <- predict(fit, newdata = transform(dat[dat$arm == 0, ], arm = 0))
  eta_B <- eta_A + fixef(fit)[["arm"]]
  fitted_lift <- plogis(eta_B) / plogis(eta_A) - 1
  se <- sqrt(vcov(fit)["arm", "arm"])
  diagnostics <- c(messages, fit@optinfo$conv$lme4$messages)
  ok <- length(diagnostics) == 0 && fit@optinfo$conv$opt == 0 && !isSingular(fit)
  result <- data.frame(repetition = k,
    histogram_mean = mean(d$observed_lift[keep]),
    histogram_median = median(d$observed_lift[keep]),
    model_mean = mean(fitted_lift), model_median = median(fitted_lift),
    pooled = sum(d$clicks_B) / sum(d$clicks_A) - 1,
    beta = fixef(fit)[["arm"]], beta_se = se,
    beta_covered = abs(fixef(fit)[["arm"]] - beta) <= qnorm(.975) * se,
    zero_A = sum(!keep), both_zero = sum(d$clicks_A == 0 & d$clicks_B == 0),
    fit_ok = ok, diagnostics = paste(diagnostics, collapse = " | "))
  list(result = result, items = d, fit = fit)
}

first <- simulate_once(1L)
results <- first$result
for (k in 2:repetitions) {
  results <- rbind(results, simulate_once(k)$result)
  if (k %% 25 == 0) message("Completed ", k, " / ", repetitions)
}
write.csv(results, file.path(out, "simulation-draws.csv"), row.names = FALSE)
write.csv(first$items, file.path(out, "example-items.csv"), row.names = FALSE)
metrics <- c("histogram_mean", "histogram_median", "model_mean", "model_median", "pooled", "beta")
targets <- unname(truth[c("mean", "median", "mean", "median", "pooled", "beta")])
summary <- do.call(rbind, lapply(seq_along(metrics), function(j) {
  x <- results[[metrics[j]]]
  data.frame(method = metrics[j], target = targets[j], estimate = mean(x),
             bias = mean(x) - targets[j], sd = sd(x), mcse = sd(x) / sqrt(repetitions))
}))
write.csv(summary, file.path(out, "simulation-summary.csv"), row.names = FALSE)
capture.output(sessionInfo(), file = file.path(out, "simulation-session.txt"))
capture.output(summary(first$fit), file = file.path(out, "example-model.txt"))
# Diagnostics are saved before assertions so a failure remains inspectable.
stopifnot(all(results$fit_ok))
stopifnot(abs(mean(results$beta) - beta) < 6 * sd(results$beta) / sqrt(repetitions))

theme_set(theme_minimal(base_size = 12) + theme(
  plot.background = element_rect(fill = "white", colour = NA),
  panel.grid.minor = element_blank(), legend.position = "top",
  plot.title = element_text(size = 18, face = "bold"),
  plot.caption = element_text(hjust = 0)))
save_plot <- function(name, p, height = 5.5) {
  ggsave(file.path(out, name), p, width = 10, height = height, dpi = 150)
}
d <- first$items
finite <- subset(d, clicks_A > 0)
lines <- data.frame(value = 100 * c(truth["mean"], first$result$histogram_mean,
                                  first$result$histogram_median),
                    label = c("True mean lift", "Histogram mean", "Histogram median"))
colours <- c("True mean lift" = "#008574", "Histogram mean" = "#D55E00",
             "Histogram median" = "#65459B")
legend_labels <- setNames(sprintf("%s: %.2f%%", lines$label, lines$value), lines$label)
histogram <- ggplot(finite, aes(100 * observed_lift)) +
  geom_histogram(binwidth = 2, boundary = 0, fill = "#9AB6CC", colour = "white") +
  geom_vline(data = lines, aes(xintercept = value, colour = label), linewidth = 1) +
  scale_colour_manual(values = colours, labels = legend_labels) +
  labs(x = "Observed item CTR lift (%)", y = "Number of items", colour = NULL) +
  theme(legend.text = element_text(size = 10))
# Zoom the coordinates only: all finite ratios still contribute to the summaries.
zoom <- c(10, 40)
outside <- sum(100 * finite$observed_lift < zoom[1] |
               100 * finite$observed_lift > zoom[2])
save_plot("lift-histogram.png", histogram +
  coord_cartesian(xlim = zoom, expand = FALSE) +
  scale_x_continuous(breaks = seq(10, 40, 5)) +
  labs(title = "Three summaries, three different answers",
    subtitle = "Zoom around the estimates; equal A/B exposures per item.",
    caption = sprintf(paste0("View restricted to 10–40%% lift; %d finite ratios lie outside this window. Summaries use ALL finite ratios.\n",
                             "%d of 300 items have zero A clicks. The full distribution is shown separately."),
                      outside, first$result$zero_A)))
full_histogram <- histogram
full_histogram$layers[[1]] <- geom_histogram(
  binwidth = 10, boundary = 0, fill = "#9AB6CC", colour = NA)
save_plot("lift-histogram-full.png", full_histogram +
  labs(title = "The full distribution has a long right tail",
    subtitle = "Same data and summary lines; wider bins make the full range readable.",
    caption = sprintf("Full finite range shown; %d of 300 items have zero A clicks and cannot enter this histogram.",
                      first$result$zero_A)))

comparison <- rbind(
  data.frame(target = "Mean item CTR lift", method = "Histogram", value = results$histogram_mean),
  data.frame(target = "Mean item CTR lift", method = "Mixed model predictions", value = results$model_mean),
  data.frame(target = "Median item CTR lift", method = "Histogram", value = results$histogram_median),
  data.frame(target = "Median item CTR lift", method = "Mixed model predictions", value = results$model_median))
reference <- data.frame(target = c("Mean item CTR lift", "Median item CTR lift"),
                         value = 100 * truth[c("mean", "median")])
save_plot("lift-estimators.png", ggplot(comparison, aes(100 * value, colour = method)) +
  geom_density(linewidth = 1) +
  geom_vline(data = reference, aes(xintercept = value), linetype = "dashed", inherit.aes = FALSE) +
  facet_wrap(~target, ncol = 1, scales = "free_y") +
  scale_colour_manual(values = c("Histogram" = "#D55E00", "Mixed model predictions" = "#008574")) +
  labs(title = "Compare each summary with its own true target",
    subtitle = "200 repeated experiments on the same 300 items; dashed lines use the true item probabilities.",
    x = "Estimated CTR lift (%)", y = "Density", colour = NULL,
    caption = "Histogram summaries omit zero-control-click items. The mixed model uses all binomial counts."), height = 7)

save_plot("lift-by-exposure.png", ggplot(finite, aes(factor(n), 100 * observed_lift)) +
  geom_hline(yintercept = 100 * truth["mean"], linetype = "dashed", colour = "#008574") +
  geom_point(position = position_jitter(width = .18, height = 0, seed = 7), alpha = .55, colour = "#0072B2") +
  labs(title = "One histogram gives very different precisions equal weight",
    subtitle = "Each point is one item in the first experiment; A and B have identical impression counts.",
    x = "Impressions per item in EACH arm", y = "Observed item CTR lift (%)",
    caption = "Dashed line: true mean item lift. Zero-control-click items omitted; no finite lifts trimmed."))
print(summary, row.names = FALSE, digits = 5)
cat("First experiment:\n"); print(first$result)
cat("Wald log-odds interval coverage:", mean(results$beta_covered), "\n")
cat("Mean number of zero-control-click items:", mean(results$zero_A), "\n")
