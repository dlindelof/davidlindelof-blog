---
title: "Developing machine learning apps completely online?"
draft: true
---

Most examples given in machine-learning textbooks assume either that 1) the datasets are small enough to fit in RAM, or 2) all programming is done in online notebooks preconfigured for access to vast datasets, backed by cloud-based filesystems such as S3.

Notebooks are not suitable for application development. They are great tools for 1) running applications, 2) exploring datasets, or 3) documenting how an analysis was done. But for application development you need the facilities provided by a modern IDE.

But to test your application from the comforts of your local machine, you need first to ensure you can run it against some data. Frequently I see data scientists use a notebook to download a hard copy of (possibly a sample of) the cloud data, then test their application using this copy, and finally convert their application to some notebook online. It would be far preferable if the local application could target directly a (sample of a) real dataset.

At Expedia we use Apache Spark for our data-intensive applications; we usually don't have to worry too much about how Spark has been configured and can usually relying on it to just work. But using Spark instances in the cloud comes with a price; we are bound to develop our applications using some sort of managed environment, relying on notebooks that come preconfigured with a `SparkSession` object. And notebooks are not ideally suited for the kind of rapid explorations and iterations you might be accustomed to when working locally.

So many of us prefer prototyping our applications on our local machines, and we typically need to load a sample of our datasets from S3 for quick visualization, modelling, and exploration. Spark, and its Python wrapper `pyspark`, are ideal tools for this but they won't support talking to S3 right out of the box.
