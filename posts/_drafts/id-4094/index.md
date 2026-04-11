---
title: "Object orientation in any language"
draft: true
---

It's possible to program in an objectoriented style in almost any language, as long as you accept a subset of object-orientation.

Consider for example encapsulation and virtual mnethods, two of the most important principles of object orientation. You can achieve encapsulation in C by following the following conventions:

- A "class" is defined in a header file and an implementation file. The header file typedefs an alias to a pointer to a struct. It also declares the functions allowed on that class, with the convention that the first argument to each function should be a ponter to that struct.
- The implementation file defines the struct itself, and defines the functions declared in the header file. It also defines other private functions.
- The "public" functions should follow a naming convention, such as <class name>\_<function name>.
