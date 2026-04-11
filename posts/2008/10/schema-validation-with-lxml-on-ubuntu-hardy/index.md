---
title: "Schema validation with LXML on Ubuntu Hardy"
date: 2008-10-21
categories: 
  - "programming"
  - "tools"
---

[LXML](http://codespeak.net/lxml/index.html) is an amazing Python module that picks up where the standard xml.dom(.minidom) left off.

It's basically a set of wrapper code around the libxml2 and libxslt libraries, and provides functionality missing in Python's standard library, including XML validation and XPaths.

On a project I'm currently working on I needed a good XML library for Python and ended up trying out lxml. But I simply could not get the schema validation to work, and after several wasted hours I understood that the default lxml that ships with Ubuntu Hardy (the distro I'm using) used the relatively old 1.3.6 python-lxml package.

I'm usually _very_ reluctant to install anything as root that does not come from the "official" repository, but for lxml I made an exception and installed the python-lxml package from the upcoming Intrepid distribution.

Add the following line to your /etc/apt/sources.list file:

`deb http://ch.archive.ubuntu.com/ubuntu intrepid main`

Then run Synaptic as usual and install python-lxml version 2.1.1. To verify that it works fine, you can test schema validation thus:

`>>>> from lxml import etree >>>> schema_tree = etree.parse('path_to_schema.xsd') >>>> schema = etree.XMLSchema(schema_tree) >>>> doc = etree.parse('path_to_some_document') >>>> schema.validate(doc)`

That last command returns as a boolean the result of the validation.
