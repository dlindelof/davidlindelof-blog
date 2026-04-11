---
title: "When and how to rename variables in data frames"
draft: true
---

In thebeginning, the data scintist read a CSV file. Or more precisely, he figured out the right set of options passed to read\_csv to handle the CSV flavor-du-jour. He ends up with a data frame with columns of the right type and when column names match the original feaders in the CSV file.

Now he tries to do anything with the data, like plotting one column against another, and realizes that the column names are long and have spaces and other special symbols in them. What do you do?

The first option is to tough it out and stick to your prinple, and work with the original column names. I've recently worked with a CSV file produced froma whole-building simulation program and here is how I had to plot the temperature over time in the heating water storage tank:

<call to ggplot from S4B report>

The advantage is that the legend uses the original names, making it easier to discuss the results with the team that produced the data.

The second option is to change some or all variables to more easier names. That will save typing when building models at the expense of making results more difficult to communicate. The new names will be somewhat arbitrary and reflect the taste of the data analyst. I like to use a form that will make it clear what the old name was, so instea of, say, assigning new name to `names, I prefer using` `rename: results <-...`

I think that a better option is a compromise between the two. I want to keep close to the original names, but also make it easy to use the names in calls to, for example, in without having to use backtiks. So I change the variable names, in such a way that they become syntactically acceptable. Spaces and colons became underscores, ...
