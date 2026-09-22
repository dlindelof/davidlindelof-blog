# Run from the repository root: Rscript scripts/non-inferiority-preview.R
# Match the independent-metric simulation in the non-inferiority post.
library(ggplot2)

set.seed(20260911)
alpha <- 0.05
n_per_arm <- 200
se <- sqrt(2 / n_per_arm)
delta <- 0.4
critical_z <- qnorm(1 - alpha)
n_sim <- 100000
metric_counts <- c(1, 2, 5, 10, 20, 50)
power_no_regression <- pnorm(delta / se - critical_z)

rules <- c("Any test rejects", "Every test passes")
colours <- setNames(c("#D55E00", "#008574"), rules)

simulated <- do.call(rbind, lapply(metric_counts, function(N) {
  noise <- matrix(rnorm(n_sim * N, sd = se), nrow = n_sim)
  ordinary_error <- rowSums(noise / se > critical_z) > 0
  noise[, 1] <- noise[, 1] - delta
  ni_error <- rowSums((noise + delta) / se > critical_z) == N
  data.frame(
    N = N,
    probability = c(mean(ordinary_error), mean(ni_error)),
    rule = rules
  )
}))

N <- 1:50
theory <- rbind(
  data.frame(N, probability = 1 - (1 - alpha)^N, rule = rules[1]),
  data.frame(N, probability = alpha * power_no_regression^(N - 1), rule = rules[2])
)
endpoints <- subset(theory, N == 50)
endpoints$label <- sprintf("%.1f%%", 100 * endpoints$probability)
endpoints$label_y <- pmax(endpoints$probability, 0.12)

p <- ggplot(theory, aes(N, probability, colour = rule)) +
  geom_hline(yintercept = alpha, colour = "#a3adb9", linetype = "dashed") +
  geom_line(linewidth = 1.35) +
  geom_point(data = simulated, size = 2.8, shape = 21, fill = "white", stroke = 1) +
  geom_text(
    data = endpoints, aes(y = label_y, label = label),
    nudge_x = 1.5, hjust = 0, size = 5.5, fontface = "bold", show.legend = FALSE
  ) +
  annotate("text", x = 28, y = 0.12, label = "5% per test", colour = "#66758a", size = 4) +
  scale_colour_manual(values = colours, breaks = rules) +
  scale_x_continuous(breaks = c(1, 10, 20, 30, 40, 50), limits = c(1, 59)) +
  scale_y_continuous(
    breaks = c(0, 0.25, 0.5, 0.75, 1),
    labels = function(x) paste0(100 * x, "%"),
    limits = c(0, 1), expand = expansion(mult = c(0.02, 0.02))
  ) +
  labs(
    title = "More tests. More trouble?",
    subtitle = "It depends on what counts as a pass.",
    x = "Number of metrics", y = "Probability of a false decision", colour = NULL,
    caption = paste(
      "Ordinary tests: all effects zero. Non-inferiority: one metric at the harm threshold; all others zero.",
      "Independent metrics | Lines: theory | Dots: 100,000 simulations",
      "David’s blog · blog.davidlindelof.com", sep = "\n"
    )
  ) +
  theme_minimal(base_size = 14, base_family = "sans") +
  theme(
    plot.background = element_rect(fill = "white", colour = NA),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(colour = "#e5eaf0", linewidth = 0.4),
    plot.title = element_text(size = 28, face = "bold", colour = "#14243b"),
    plot.subtitle = element_text(size = 15, colour = "#40516b", margin = margin(b = 8)),
    legend.position = "top", legend.justification = "left",
    legend.text = element_text(size = 14),
    axis.text = element_text(size = 12, colour = "#40516b"),
    axis.title = element_text(size = 13, colour = "#14243b"),
    plot.caption = element_text(size = 10.5, colour = "#40516b", hjust = 0, lineheight = 1.3),
    plot.caption.position = "plot",
    plot.margin = margin(20, 24, 16, 20)
  )

ggsave(
  "posts/2026/09/controlling-for-multiple-testing-with-non-inferiority-tests/preview.png",
  p, width = 10, height = 5.25, units = "in", dpi = 120, bg = "white"
)
