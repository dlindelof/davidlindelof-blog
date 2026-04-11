---
title: "MATLAB Coding Conventions"
date: 2014-09-22
---

Over the course of four years we have developed, at Neurobat, a set of coding conventions for MATLAB that I would like to share here. The goal of these conventions is three-fold:

- Help scientists and engineers write clean MATLAB code
- Help write MATLAB code that will be easily ported to C
- Provide guidelines to external parties that write MATLAB code for us.

Feel free to redistribute and/or adapt these rules to suit your organization.

 

**Rationale**

We have observed that scientists and engineers who use MATLAB tend to write MATLAB code that mirrors their way of thinking: long scripts that perform computations as a series of steps.

Our experience has shown that code written in that style tends to become hard to understand and to modify. Furthermore, it tends also to be hard to port to C. As an alternative, we suggest that both MATLAB and C programs will benefit from the application of the so-called [Opaque Data Type](http://en.wikipedia.org/wiki/Opaque_data_type) programming idiom. Our experience has shown that a disciplined application of this idiom leads to more modular, cleaner code that is also easier to port to C.

In the rest of this article we enumerate the rules that should be followed to apply this idiom to the MATLAB language.

 

**Represent an object with state as a `struct`**

Neither C nor MATLAB has (a satisfying) support for object-oriented programming; however, some degree of encapsulation can be achieved by using `struct`s, which both C and MATLAB support.

We have found `struct`s to be the best way to represent state in MATLAB. The alternatives, namely global variables, or `persistent` variables, are effectively global variables and cannot be used to represent state held by more than one object.

 

**Provide a meaningful name to the structure**

The state-holding structure should represent some kind of object in the real world; provide a name for this structure, so we can understand the purpose of this object.

 

**Represent a module by a folder**

Keep all the code related to a particular data structure (constructor, methods and unit tests) under the same folder, with the same name as the structure. The C language lets you implement all functions in the same file, usually called a module. MATLAB requires each (public) function to be defined as the first function in their own `.m` file. Keep all those `.m` files in the same folder.

 

**Never expect the client code to access fields directly**

No code, except the methods defined in the enclosing folder, is expected (or allowed) to access the fields of the structure directly.

 

**Define a constructor**

Never expect the client code to build the `struct` itself; always provide a suitable function, called a constructor, that will instantiate the proper fields in the structure. The client code should never even be aware that they are dealing with a structure.

 

**Keep a consistent naming convention for functions**

C has no namespace, and neither has MATLAB. It is therefore important to adhere to a naming convention for functions. Keep the following naming convention, where `xxx` is the name of the enclosing folder:

_Constructor:_ `xxx_new(...)`

_Methods:_ `xxx_method_name(xxx, ...)`

_Destructor (if needed):_ `xxx_free(xxx)`

Methods, including the constructor, may accept optional arguments. The first argument to all methods should be an instance of `xxx`, on which it is understood that the operations will apply.

**Keep the [Command-Query Separation](http://en.wikipedia.org/wiki/Command%E2%80%93query_separation) principle**

The Command-Query Separation principle states that a method should either return a computed value, or update the state of the object, but not both. Keep this principle unless doing so would obviously lead to less readable and less maintainable code.

 

**Unit tests**

We believe that the practice of [Test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) leads to better software. We are however aware that applying this practice requires training and discipline. We therefore strongly encourage it for code provided by third parties, without (yet) requiring it. Internally developed code is almost always test-driven.

 

**Code Quality**

We understand that producing quality code requires experience, training and discipline. It would be unreasonable to expect the same code quality from scientists and engineers as from professional software craftsmen; however, we encourage you to remain alert to the following signs of deteriorating quality:

- Duplicated code
- Long functions (more than half a screen)
- Long parameter list
- Too many comments (a sign that the code has become hard to read)

 

**Example**

This is an example of how a simple PI controller could be implemented, following the guidelines above. Put the three files below under a `pid` folder, together with test data and test functions:

```
function pid = pid_new(setpoint, P, I)
pid.setpoint = setpoint;
pid.P = P;
if nargin < 3
  pid.I = 0;
else
  pid.I = I;
end
pid.error = 0;
pid.ui = 0;
end

```

```
function pid = pid_new_value(pid, new_value)
pid.error = pid.setpoint - new_value;
pid.ui = pid.ui + pid.error * pid.I;
end

```

```
function control = pid_control(pid)
control = pid.P * (pid.error + pid.ui);
end

```
