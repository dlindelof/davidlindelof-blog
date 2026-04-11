---
title: "Connecting to SQL Server from R on a Mac with a Windows domain user"
date: 2019-07-23
categories: 
  - "r"
---

Connecting to an SQL Server instance as a Windows domain user is relatively straightforward when you run R on Windows, you have the right ODBC driver installed, and your network is setup properly. You normally don't need to supply credentials, because the ODBC driver uses the built-in Windows authentication scheme. Assuming your `odbcinst.ini` file includes an entry for `SQLServer`, you typically just need the following:

```r
con <- odbc::dbConnect(
  odbc::odbc(),                 
  Driver = "SQLServer",
  Server = "mysqlhost",
  Database = "mydbname",
  Port = 1433
)
```

But if you want to connect to SQL Server from a Mac, things are less simple.

Don't bother installing the ODBC driver supplied by Microsoft; it just doesn't work with a Windows domain user. No matter what I tried, I always got the following error message: `Error: nanodbc/nanodbc.cpp:950: 28000: [Microsoft][ODBC Driver 13 for SQL Server][SQL Server]Login failed for user 'dlindelof'.` I've tried setting the user id to `domain\\username`, I've tried passing an extra parameter `DOMAIN`, all to no avail.

As far as I could determine, it simply is not possible to connect to SQL Server with a domain user using the ODBC driver supplied by Microsoft. Instead, obtain the [open-source FreeTDS driver](https://www.freetds.org/). If you use [Homebrew](https://brew.sh/), this is done with `brew install freetds`. Once installed you should see its libraries installed as `/usr/local/lib/libtdsodbc.so`. Edit your `/usr/local/etc/odbcinst.ini` file accordingly:

```bash
freetds                              = Installed
# ...
[freetds]
Driver = /usr/local/lib/libtdsodbc.so
```

You can, but don't need to, also edit `/usr/local/odbc.ini` and `/usr/local/etc/freetds.conf` if you want to specify human-friendly aliases to specific database connections. I never used that.

You can now create a database source in R using the usual connection parameters, with the important gotcha that (unless you edit `freetds.conf`) you must specify the port number. The username must be prefixed by the domain and a double backslash (to prevent escaping). Putting it all together, my connection call looks like this:

```r
con <- odbc::dbConnect(
   odbc::odbc(),                 
   Driver = "freetds",
   Server = "mysqlhost",
   Database = "mydbname",
   uid = "domainname\\username",
   pwd = "somepassword",
   Port = 1433
 )
```
