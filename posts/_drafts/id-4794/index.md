---
title: "test"
draft: true
---

* * *

## editor: visual title: Test toc-title: Table of contents

## Quarto

Quarto enables you to weave together content and executable code into a finished document. To learn more about Quarto see [https://quarto.org](https://quarto.org).

## Running Code

When you click the **Render** button a document will be generated that includes both content and the output of embedded code. You can embed code like this:

::: cell \`\`\` {.r .cell-code} power.t.test(delta = 0.02, power = .8, alternative = 'one.sided')

````

::: {.cell-output .cell-output-stdout}

         Two-sample t test power calculation 

                  n = 30913.46
              delta = 0.02
                 sd = 1
          sig.level = 0.05
              power = 0.8
        alternative = one.sided

    NOTE: n is number in *each* group
:::

``` {.r .cell-code}
control <- rnorm(n = 31000, mean = 0.5)
treat <- rnorm(n = 31000, mean = 0.52)

t.test(control, treat, mu = -0.02)
````

::: {.cell-output .cell-output-stdout}

```
    Welch Two Sample t-test

data:  control and treat
t = 0.086716, df = 61997, p-value = 0.9309
alternative hypothesis: true difference in means is not equal to -0.02
95 percent confidence interval:
 -0.035094863 -0.003507628
sample estimates:
mean of x mean of y 
0.5016276 0.5209289 
```

::: :::

You can add options to executable code like this

::: cell ::: {.cell-output .cell-output-stdout} \[1\] 4 ::: :::

The `echo: false` option disables the printing of code (only output is displayed).
