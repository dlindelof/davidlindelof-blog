---
title: "Never ever worrying about file formats again"
date: 2012-11-17
draft: true
---

Anyone who's ever run a scientific experiment has had to deal with the following question:

> How on Earth should I organize all my data?

Whether you've done labwork during your undergraduate studies, or collected data during your doctoral thesis, eventually you must have made a decision concerning the organization of your test data: folder structure, file naming convention, file format etc.

At Neurobat we are regularly testing our products on real, occupied buildings. Since we deal with heating controllers, our data acquisition campaigns usually cover the heating seasons, loosely defined as the period between October and March inclusive, i.e. 6 months. We are currently running our third consecutive test campaign, and finding a rational way to organize all our data has always been a bit of a challenge. Up to now, we have mostly relied on parsing the data collected on each test site, loading it into MATLAB and saving everything as `.mat` files. Needless to say, this solution is far from ideal, because:

1. It binds us to MATLAB (or alternatively, Octave) as the platform for doing our analysis;
2. It doesn't really solve the problem of data file multiplicity. A `.mat` file can only represent a single matrix, not a collection of data.

However, this approach is still the predominant one in academic and, I suspect, industrial circles. In this post I will describe our experience in using a completely different approach.

I've taken the current 2012--2013 heating season as an excuse to explore a possible alternative to using flat text files as the main way to organize my data. In this post I'd like to show you some of the lessons I've learned in using SQLite as my main data storage solution.

## What is SQLite?

SQLite is a relational database management system (RDMS). What sets SQLite apart from the other RDMSs out there is its simplicity: the entire database lives in a single file, and there is no separate server to configure. This means that if you do it right, you can collect all your data in a single file. Perfect simplicity, perfect for sharing data and, I may add, perfect "Dropboxability" of your data.

Once you have installed SQLite on your system (which on Ubuntu is as simple as `sudo apt-get install sqlite3`), you can create your first database, your first table and your first data row easily:

```
$ sqlite3 demo.db
```

\-- Loading resources from /Users/dlindelof/.sqliterc SQLite version 3.7.12 2012-04-03 19:43:07 Enter ".help" for instructions Enter SQL statements terminated with a ";" sqlite> create table demo ( ...> patient integer, ...> temperature real); sqlite>

In our test campaign we measure essentially two sets of data: sensors and energy meters. Let's look at how to organize logically each set of data.

### Sensor data

Let's look at the sensor data first as it is probably the easiest.

On each test site (10 of them a the time of writing) we sample the sensors every 5 minutes. We sample the outdoor temperature, the indoor temperature, the solar irradiance and the flow temperature. Note that in our application, all sensors must be sampled simultaneously to be of any use for us. It made therefore sense to define a table with all sensor readings defined thus:

```
CREATE TABLE SensorReadings (
  Site REFERENCES Sites,
  Time INTEGER,
  OutdoorTemp REAL,
  IndoorTemp REAL,
  FlowTemp REAL,
  Irradiance REAL,
  PRIMARY KEY (Site, Time)
);
```

The {{Sites}} table holds the list of all valid test site names:

```
CREATE TABLE Sites (
  SiteName TEXT PRIMARY KEY,
  Surface INTEGER DEFAULT 200
);
```

Note that I've also started to collect miscellaneous data about each test site here, starting with its floor area. I want to check whether a site's energy consumption scales linearly with it.

Coming back to the `SensorReadings` table, each row will hold the data for one sensor sample done on a particular site at a particular time, and the pair `(Site, Time)` makes for a natural (composite) primary key: you cannot have two distinct readings done at the same time on the same site.

After seven weeks of data collection, this table has now just over 100 thousand rows.

Let's now consider the other part of the test campaign, the energy measurements.

### Energy measurements

The fundamental unit of time in our test campaign is the week, and for each week and each test site we want to record:

- The total heating energy
- The average temperatures and irradiance
- Whether the Neurobat controller or the reference controller was running.

Initially I create a table with a structure roughly equivalent to this:

```
CREATE TABLE Meters (
  Week REFERENCES Weeks,
  Site REFERENCES Sites,
  Control REFERENCES Controllers,
  MeterStart REAL,
  MeterWeek REAL,
  AvgIndoorTemp REAL,
  AvgOutdoorTemp REAL,
  AvgFlowTemp REAL,
  AvgIrradiance REAL
);
```

The `Weeks` and `Controllers` tables are references tables similar to `Sites` and will be described shortly. For the remaining columns, my intention was that I would record their values each week as they became known to me. `MeterStart` records the value read out on the energy meter at the start of the week, `MeterWeek` is the total energy consumed that week, and the `Avg*` columns are the average sensor values for that week.

It struck me that many (most) of these columns are actually derived values, and are therefore Evil. For instance, the `Avg*` columns are clearly derivable from the `SensorReadings` table. For that reason I tried to figure out a view that would compute all these values upon request. But before I describe this I need to explain the `Weeks` and `Controllers` tables.

The `Weeks` table is defined thus:

```
CREATE TABLE Weeks (
  WeekId TEXT PRIMARY KEY,
  WeekStart TEXT,
  WeekEnd TEXT
);
```

The `WeekId` column holds the [ISO Week date](http://en.wikipedia.org/wiki/ISO_week_date) identifier for that particular week, e.g. `'2012W51'` is the week that began on Monday, 17th December and ends on Sunday, 23rd December 2012. The `WeekStart` and `WeekEnd` columns hold the starting and ending dates for each week. Here is for instance the row describing week `2012W51`:

```
sqlite> SELECT * FROM Weeks
   ...>   WHERE WeekId='2012W51';
WeekId      WeekStart   WeekEnd   
---------- ---------- ----------
2012W51     2012-12-17  2012-12-24
```

Note that there is still some redundancy here: the `WeekEnd` field is _usually_ the `WeekStart` field of the next week; that is however not always the case, especially if we interrupt the test campaign when the heating season is over.

The `Controllers` table holds simply a list of all possible control schemes:

```
CREATE TABLE Controllers (
  Control TEXT PRIMARY KEY
);
```

And takes on values such as `NBM`, `NIQ`, `REF`, etc.

We can now write a query that will compute the average sensor values for a given week:

```
SELECT WeekId AS Week,
       Site,
       AVG(OutdoorTemp) AS MeanOutdoorTemp,
       AVG(IndoorTemp) AS MeanIndoorTemp,
       AVG(Irradiance) AS MeanIrradiance
FROM SensorReadings
JOIN Weeks
ON Time BETWEEN WeekStart AND WeekEnd
GROUP BY Week, Site
```

This is the result one gets by adding a `LIMIT 10` clause to the query above:

```
Week        Site        MeanOutdoorTemp   MeanIndoorTemp    MeanIrradiance
---------- ---------- ---------------- ---------------- ----------------
2012W44     azzurab     6.65740149007937  24.1809523809524  135.100694444444
2012W44     azzurac     6.62668989335317  24.0597718253969  142.499503968254
2012W44     brugg       8.74155068390805  23.2071170043691                  
2012W44     fey         6.21731976593625  23.730533764442                   
2012W44     hedingen    7.85095137420718  23.075523255814   37.9866279069767
2012W44     jd1         5.37238171325228  24.0045275412784  136.701250084536
2012W44     niklausen   7.50972384368117  20.6435302055831  130.315072102405
2012W44     ruswil      7.55513969425408  19.2363591269841  178.765873015873
2012W44     unterengst  7.44682539682542  20.2474702380952  94.9588293650794
2012W44     villa       9.59356175717973  21.3090583455014  129.699467612164
```

Note that for week `2012W44` two of the sites had missing irradiance data.

It's always a good idea to double-check the results of complex queries like this, so let's do it manually for one site and one week:

```
select * from weeks where weekid='2012W44';
WeekId      WeekStart   WeekEnd   
---------- ---------- ----------
2012W44     2012-10-29  2012-11-05

select Site, AVG(OutdoorTemp) from sensorreadings where time between '2012-10-29' and '2012-11-05' and site='azzurab';
Site        AVG(OutdoorTemp)
---------- ----------------
azzurab     6.65740149007937
```

which is indeed the right value returned by the query above. This is pretty good so far; we have defined a query that will return the average values for each sensor for each site and for each week. All we need, then, are tables that will record:

1. Which controller was running in a given week on each site;
2. The energy consumption for each week.

These two elements are clearly completely independent of each others; it makes therefore sense to split this information into two tables. I call the first table `Runs` (as in "controller runs"):

```
CREATE TABLE Runs (
  Week REFERENCES Weeks,
  Site REFERENCES Sites,
  Control REFERENCES Controllers,
  Confidence INTEGER DEFAULT 5,
  Comment TEXT,
  PRIMARY KEY (Week, Site));
```

Note that I'm adding two pieces of information here: `Confidence` is an integer between 1 and 5 and is a subjective appreciation of how reliable that week's data has been. If there have been interruptions or other mishaps, that column gets a score less than 5. In the subsequent data analysis I will exclude all weeks whose confidence is less than 4. I am also including a `Comment` field, usually for explaining the `Confidence` score if needed.

For the energy consumption, I could have created a table giving directly the energy used for each week. But we don't get this value directly; instead we have to read out the energy meters every week (or rather, have a computer do it for us), and calculate the difference between two consecutive weeks. Well, I'm not much for calculating things if I can have a computer do it for me, so I figured all I had to really record in this table (which I call `Meters`) is the energy reading of the meter at the beginning of the week, i.e. at or around midnight between Sunday and Monday:

```
CREATE TABLE Meters (
  Week REFERENCES Weeks,
  Site REFERENCES Sites,
  MeterStart REAL,
  PRIMARY KEY (Week, Site));
```

## Bringing it all together

We have now cleanly separated the sensor data from the energy measurement. As a bonus we have also identified a separate table recording which controller was running when on which site. For the data analysis there are now two virtual tables, or _views_, that we want to have.

### Sensors

At each timestep we want to know not only the
