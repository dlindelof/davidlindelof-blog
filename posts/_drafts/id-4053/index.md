---
title: "Do we need runnable R packages?"
draft: true
---

I have been using R for almost 20 years now and there’s one issue that’s been bugging me of late.

R has traditionally been used for running short scripts or data analysis notebooks---that is, relatively short, interactive sessions. But there’s a growing interest in developing full applications with the language. Three examples come to mind:

1. The [Shiny web application framework](https://shiny.rstudio.com/), which facilitates the development of rich, interactive web applications
2. The [plumber](https://www.rplumber.io/) package, which provides lower-level facilities than Shiny for writing web services
3. Batch jobs intended to be run on a regular schedule

The `Rscript` program is generally used to run an R script (provided as a single `.R` file) or an arbitrary R expression, but I feel it suffers from a few problems:

1. It encourages developers of batch jobs to provide their code in a single R file (bad for code structure and unit-testability)
2. It provides no way to deal with dependencies on other packages: the developer is responsible for ensuring that all dependencies are installed
3. It is not designed to execute R code provided as an R package

But today, people write applications in R that can easily be too large and/or too complex to comfortably fit the single script model. Compared with other languages, R’s support for multi-file applications is rather poor; the best we have are R packages, which are meant to be software libraries, not executable artefacts.

If I had my way I would like to be able to:

- package a set of files as a single application
- specify the main entry point to the application
- declare the application's dependencies
- easily run unit tests for my application

Other environments let me do that; in particular, let's compare R with Python and Java on these dimensions:

|  | **Java** | **Python** | **R** |
| --- | --- | --- | --- |
| _Packaging mechanism_ | JAR file: a zipped archive of `.class` files and some metadata, such as the `MANIFEST` file | Several distribution formats, including Python Wheel: an archive of Python code and metadata | R package: a `.tar.gz` file that packages R code and metadata |
| _Main entry point_ | A `public static void main()` method of a class chosen by the developer and specified as `Main-Class`in the JAR file's M`ANIFEST` | A special `__main__.py` module that gets run when calling the package withe `-m` option | No mechanism yet |
| _Dependencies_ | No formal mechanism. Dependencies are usually packaged together with the JAR file. | Specified in `setup.py` | Declared in `DESCRIPTION`, but only installed when downloading the package from CRAN. Other tools exist to install the dependencies of a local R package. |
| _Support for testing_ | Most build systems will let you run unit tests before packaging the production code |    Most build systems will let you run unit tests before packaging the production code | Excluded when building the package, provided the conventional file layout is followed |

This table shows that a lot of machinery is already in place to support R applications shipped as packages. But two crucial elements are missing: 1) the ability to specify an entry point into the package, and 2) the ability to automatically install a package's dependencies without publishing it to a CRAN server. For example, let’s say I want to run a Shiny application that I provide as an R package (to keep the code modular, to benefit from unit tests, and to declare dependencies properly). I would then need to:

- uncompress my R package
- somehow (usually manually) ensure my dependencies are installed
- call `runApp()`

This gets tedious, fast. Other languages (such as Python and Java, discussed above) let the developer package their code in "runnable" artefacts, and let the developer specify the main entry point. The mechanics depend on the language but are remarkably similar, and suggest a way to implement this in R. Through meta-data declarations, the developer can often specify dependencies and declare where the program’s "main" function resides.

I recently suggested this idea on the R-devel mailing list, whose members were generally supportive of this idea, but not as an extension to the language itself---at least, not yet. Best was to test the waters by providing this functionality as an R package, so I created the `run` package ([https://github.com/dlindelof/run](https://github.com/dlindelof/run)). The idea is simple: assuming your package `myapp_0.1.0.tar.gz` has a `main()` function, you can now install your package (and its dependencies), and run the `main()` function, with a simple command:

```
 $ Rscript -e "run::run('myapp_0.1.0.tar.gz')" 
```
