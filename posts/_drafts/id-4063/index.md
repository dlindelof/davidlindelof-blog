---
title: "Caching chunks when run from RStudio"
draft: true
---

When you execute chunks from RStudio, you would expect those chunks marked with `cache=TRUE` to be, well, cached. Not so. RStudio doesn't seem to honor the chunk options.

[https://community.rstudio.com/t/caching-chunks-in-rstudio-does-not-work/9040](https://community.rstudio.com/t/caching-chunks-in-rstudio-does-not-work/9040)

`rmarkdown::render`
