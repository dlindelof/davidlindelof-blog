---
title: "Reading S3 data from a local PySpark session"
date: 2020-09-25
categories: 
  - "python"
---

## For the impatient

To read data on S3 to a local PySpark dataframe using temporary security credentials, you need to:

1. Download a Spark distribution bundled with Hadoop 3.x
2. Build and install the `pyspark` package
3. Tell PySpark to use the `hadoop-aws` library
4. Configure the credentials

## The problem

When you attempt read S3 data from a local PySpark session for the first time, you will naturally try the following:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
foo = spark.read.parquet('s3a://<some_path_to_a_parquet_file>')
```

But running this yields an exception with a fairly long stacktrace, the first lines of which are shown here:

```
Py4JJavaError: An error occurred while calling o574.parquet.
 : java.lang.RuntimeException: java.lang.ClassNotFoundException: Class org.apache.hadoop.fs.s3a.S3AFileSystem not found
```

Solving this is, fortunately, trivial. You need the `hadoop-aws` library; the correct way to add it to PySpark's classpath is to ensure the [Spark property](https://spark.apache.org/docs/latest/configuration.html) `spark.jars.packages` includes `org.apache.hadoop:hadoop-aws:3.2.0`. (Be sure to set the same version as your Hadoop version.)

<figure>

![](images/will_it_work_2x.png)

<figcaption>

[xkcd 1742 Will It Work](https://xkcd.com/1742/)

</figcaption>

</figure>

(There's some advice out there telling you to download those jar files manually and copy them to PySpark's classpath. Don't do that. Using the `spark.jars.packages` method ensures you also pull in any transitive dependencies of the `hadoop-aws` package, such as the AWS SDK. You don't want to do that manually.)

### So what's this talk of Hadoop 3.x?

Spark 2.x ships with, at best, Hadoop 2.7. But Hadoop didn't support all AWS authentication mechanisms until Hadoop 2.8. So if you need to access S3 locations protected by, say, temporary AWS credentials, you **must** use a Spark distribution with a more recent version of Hadoop.

It's probably possible to combine a plain Spark distribution with a Hadoop distribution of your choice; but the easiest way is to just use Spark 3.x. However there's a catch: `pyspark` on PyPI provides Spark 3.x bundled with Hadoop 2.7. [There's work under way](https://issues.apache.org/jira/browse/SPARK-32017) to also provide Hadoop 3.x, but until that's done the easiest is to just download and build pyspark yourself.

[Download Spark from their website](https://spark.apache.org/downloads.html), be sure you select a 3.x release built with Hadoop 3.x. Unzip the distribution, go to the `python` subdirectory, built the package and install it:

```bash
cd spark-3.0.0-bin-hadoop3.2
cd python
python setup.py dist
pip install dist/*.tgz
```

(Of course, do this in a virtual environment unless you know what you're doing.)

With this out of the way you should be able to read any publicly available data on S3, but first you need to tell Hadoop to use the correct authentication provider. For public data you want `org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider`:

```python
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider')

spark = SparkSession.builder.config(conf=conf).getOrCreate()

df = spark.read.csv('s3a://noaa-ghcn-pds/csv/2020.csv', inferSchema=True)
```

After a while, this will give you a Spark dataframe representing one of the [NOAA Global Historical Climatology Network Daily](https://registry.opendata.aws/noaa-ghcn/) datasets.

## Ok what about AWS credentials then?

That's why you need Hadoop 3.x, which provides [several authentication providers to choose from](https://hadoop.apache.org/docs/r2.8.0/hadoop-aws/tools/hadoop-aws/index.html#Changing_Authentication_Providers). For example, say your company uses temporary session credentials; then you need to use the `org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider` authentication provider. The name of that class must be given to Hadoop before you create your Spark session. The Hadoop documentation says you should set the `fs.s3a.aws.credentials.provider` property to the full class name, but how do you do that when instantiating the Spark session? There's documentation out there that advises you to use the `_jsc` member of the `SparkContext`, e.g.

```python
sc._jsc.hadoopConfiguration().set('fs.s3n.awsAccessKeyId',<access_key_id>)
```

But the leading underscore shows clearly that this is a bad idea. Instead, all Hadoop properties can be set while configuring the Spark Session by prefixing the property name with `spark.hadoop`:

```python
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider')
conf.set('spark.hadoop.fs.s3a.access.key', <access_key>)
conf.set('spark.hadoop.fs.s3a.secret.key', <secret_key>)
conf.set('spark.hadoop.fs.s3a.session.token', <token>)

spark = SparkSession.builder.config(conf=conf).getOrCreate()
```

And you've got a Spark session ready to read from your confidential S3 location.

### Oh and one more thing

The temporary session credentials are typically provided by a tool like `aws_key_gen`. Running that tool will create a file `~/.aws/credentials` with the credentials needed by Hadoop to talk to S3, but surely you don't want to copy/paste those credentials to your Python code. Instead you can also use `aws_key_gen` to set the right environment variables, for example with

eval \``aws_key_gen shell`\`

before running your Python program. If you do so, you don't even need to set the credentials in your code.
