---
title: "Source code filtering with Maven"
date: 2009-04-30
categories: 
  - "programming"
tags: 
  - "ant"
  - "filtering"
  - "java"
  - "maven"
---

Today I searched for a [Maven](http://maven.apache.org/) plugin that would filter some of my source files before compiling them. An equivalent to the [resources](http://maven.apache.org/plugins/maven-resources-plugin/) plugin with filtering turned on, but for Java sources, that would replace occurences of, say, ${token.name} with somevalue wherever that string occurs in the source files.

I could not find such a plugin and I think I understand why. When the resources plugin processes the resources, it simply copies them from src/main/resources to target/classes, optionally filtering them. In the packaging phase, Maven simply zips up everything he finds in target/classes to the target jarfile.

But with source code you cannot simply copy the .java files to, say, target/generated after filtering them, and expect Maven to compile these filtered source files. You would have .java source files with the exact same name and same package declaration in src/main/java **and** in target/generated. So source file filtering cannot work in Maven unless you tell the compiler to change the directory from which to compile files. Well, I don't have that much experience with Maven and I don't know how to do that. I know the build-helper plugin can **add** a directory to the compile path, but I don't know how to remove a directory from it.

On my project I needed to process only one single file. Let's call it mypackage.Locator.java. I declared that class in a file named src/main/java/mypackage/\_Locator.java (note the underscore). Then I configured an [antrun](http://maven.apache.org/plugins/maven-antrun-plugin/) task to copy that file over to target/generated/mypackage/Locator.java, a directory that build-helper had added to the compile path. I then told the compiler plugin to exclude all source files whose names begin with an underscore.

The most important parts of my pom.xml file look like this:

\[code='xml'\]

org.apache.maven.plugins maven-compiler-plugin \*\*/\_\*.java

maven-antrun-plugin generate-locator process-sources run

\[/code\]

Note that you now let Ant filter the source files, so you must use [Ant](http://ant.apache.org/manual/index.html)\-like tokens (e.g. @token.name@). This works reasonably well, but if I can make some time for it I would really like to know how to remove the default source directory from the compile path.
