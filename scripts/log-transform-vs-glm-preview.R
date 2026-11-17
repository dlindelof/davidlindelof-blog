# Run from the repository root: Rscript scripts/log-transform-vs-glm-preview.R
# Generate the 1200x630 social preview image for the log(Y + c) vs. GLM post.
suppressPackageStartupMessages({
  library(ggplot2)
})

set.seed(20261110)

n <- 10000
in_treatment <- rep(c(FALSE, TRUE), each = n / 2)
p_pre <- 0.35
p0 <- 0.40
p1 <- 0.48
intensive_mult <- 0.80
phi <- 3.0
true_total_lift <- (p1 / p0) * intensive_mult - 1 # -4.0%

is_pos_pre <- runif(n) < p_pre
mean_mu <- exp(4.0 + 1.4^2 / 2)
mu_i <- ifelse(
  is_pos_pre,
  rlnorm(n, meanlog = 4.0, sdlog = 1.4),
  rlnorm(n, meanlog = log(mean_mu) - 0.5^2 / 2, sdlog = 0.5)
)
y_pre <- ifelse(is_pos_pre, rgamma(n, shape = mu_i / phi, scale = phi), 0)
log_y_pre <- ifelse(is_pos_pre, log(y_pre), 0)

p_new <- ifelse(in_treatment, (p1 - p_pre) / (1 - p_pre), (p0 - p_pre) / (1 - p_pre))
is_pos <- is_pos_pre | (runif(n) < p_new)
mean_post <- mu_i * ifelse(in_treatment, intensive_mult, 1.0)
y <- ifelse(is_pos, rgamma(n, shape = mean_post / phi, scale = phi), 0)

ext_ratio <- mean(is_pos[in_treatment]) / mean(is_pos[!in_treatment])
fit_part2_qp_cov <- glm(
  y ~ in_treatment + is_pos_pre + log_y_pre,
  family = quasipoisson(link = "log"),
  subset = is_pos
)
hurdle_glm_lift <- 100 * (ext_ratio * exp(coef(fit_part2_qp_cov)[["in_treatmentTRUE"]]) - 1)

c_grid <- 10^seq(-3, 3, length.out = 120)
curve_df <- data.frame(
  c_val = c_grid,
  lift_pct = sapply(c_grid, function(cc) {
    100 * (exp(coef(lm(log(y + cc) ~ in_treatment))[["in_treatmentTRUE"]]) - 1)
  })
)

key_points <- data.frame(
  c_val = c(0.01, 1),
  label_top = c("In cents (c = $0.01)", "In dollars (c = $1)"),
  lift_pct = sapply(c(0.01, 1), function(cc) {
    100 * (exp(coef(lm(log(y + cc) ~ in_treatment))[["in_treatmentTRUE"]]) - 1)
  })
)
key_points$val_label <- sprintf("%+.1f%%", key_points$lift_pct)

p <- ggplot(curve_df, aes(x = c_val, y = lift_pct)) +
  geom_hline(yintercept = 0, colour = "#a3adb9", linetype = "dotted", linewidth = 0.7) +
  geom_hline(yintercept = 100 * true_total_lift, colour = "#008574", linetype = "dashed", linewidth = 1.2) +
  geom_line(colour = "#D55E00", linewidth = 1.45) +
  geom_point(
    data = key_points,
    colour = "#D55E00", fill = "white", shape = 21, size = 3.6, stroke = 1.3
  ) +
  geom_text(
    data = key_points,
    aes(label = paste0(label_top, ": ", val_label)),
    nudge_x = 0.16, nudge_y = 10, hjust = 0, size = 4.6, fontface = "bold", colour = "#D55E00"
  ) +
  annotate(
    "text", x = 0.001, y = 123,
    label = "OLS on log(Y + c)",
    hjust = 0, size = 4.6, fontface = "bold", colour = "#D55E00"
  ) +
  annotate(
    "text", x = 0.01, y = -15.5,
    label = sprintf("True total lift: -4.0%%  (Two-part Hurdle GLM: %.1f%%)", hurdle_glm_lift),
    hjust = 0, size = 4.5, fontface = "bold", colour = "#008574"
  ) +
  scale_x_log10(
    breaks = c(0.001, 0.01, 0.1, 1, 10, 100, 1000),
    labels = c("$0.001", "$0.01", "$0.10", "$1", "$10", "$100", "$1,000"),
    limits = c(0.001, 1500)
  ) +
  scale_y_continuous(
    breaks = seq(-25, 125, by = 25),
    labels = function(x) sprintf("%+d%%", x),
    limits = c(-25, 135)
  ) +
  labs(
    title = "Log the outcome, or log the expectation?",
    subtitle = "When zeros and whales collide, OLS on log(Y + c) depends on the unit of currency.",
    x = "Pseudocount c in log(Y + c)",
    y = "Estimated revenue lift",
    caption = paste(
      "Simulated creator experiment (N = 10,000): +20% monetization rate, -20% revenue per active creator, -4.0% net revenue.",
      "David’s blog · blog.davidlindelof.com",
      sep = "\n"
    )
  ) +
  theme_minimal(base_size = 14, base_family = "sans") +
  theme(
    plot.background = element_rect(fill = "white", colour = NA),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(colour = "#e5eaf0", linewidth = 0.4),
    plot.title = element_text(size = 26, face = "bold", colour = "#14243b"),
    plot.subtitle = element_text(size = 14.5, colour = "#40516b", margin = margin(b = 12)),
    axis.text = element_text(size = 12, colour = "#40516b"),
    axis.title = element_text(size = 13, colour = "#14243b"),
    plot.caption = element_text(size = 10.5, colour = "#40516b", hjust = 0, lineheight = 1.3),
    plot.caption.position = "plot",
    plot.margin = margin(20, 24, 16, 20)
  )

ggsave(
  "posts/2026/11/log-transform-vs-glm/preview.png",
  p, width = 10, height = 5.25, units = "in", dpi = 120, bg = "white"
)
