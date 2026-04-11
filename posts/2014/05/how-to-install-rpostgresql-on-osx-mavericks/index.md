---
title: "How to install RPostgreSQL on OSX Mavericks"
date: 2014-05-23
---

Even if you've installed the PostgreSQL client binaries via Brew (i.e., `brew install postgres`), you will run into problems if you try to install the RPostgreSQL package in the usual way, i.e. `install.packages('RPostgreSQL')` from the R console. That's simply because there are no binaries on CRAN for Mavericks. If you look at http://cran.r-project.org/web/checks/check\_results\_RPostgreSQL.html you'll see that OSX Mavericks is the only flavor that runs into problems building the package.

Fortunately the solution is trivial. Install it from source, and yes, this sounds way scarier than it really is.

Download the source tarball from http://cran.r-project.org/web/packages/RPostgreSQL/index.html. Now resist for a moment the urge to untar the file. Instead, install first the DBI package from the R console:

```
install.packages('DBI')
```

and then run this from the directory where you downloaded the tarball:

```
sudo R CMD INSTALL RPostgreSQL_0.4.tar.gz
```

And you're ready to go.
