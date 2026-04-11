---
title: "LaTeX to Word format conversion how-to"
date: 2007-06-08
categories: 
  - "tools"
---

Grant that I will never ever have to submit a paper in Word format again...

But in case that should happen, here is David's step-by-step cookbook for converting a ground-breaking paper on building physics from LaTeX to Word format. The idea is to first convert it to HTML, and use Word to convert it---something that Word actually does quite well.

1. Insert
    
    ```
    \\usepackage{tex4ht}
    ```
    
    somewhere towards the end of the document preamble. (Your document will produce rubbish from this point on, so make sure to remove this when you want to typeset the real thing again.)

3. Run LaTeX on the document. You should end up with a DVI file. (I say _should_, because on my system, for instance, /usr/bin/latex is a symbolic link to /usr/bin/pdfetex. The original LaTeX is invoked with /urs/bin/latexnoetex. Go figure.)

5. Run tex4ht _filename_.

7. Run t4ht _filename_. This will produce the HTML file itself and all accompanying pictures in the current directory. See t4ht's documentation for alternative directories---I like having everything put in its own html/ directory by invoking t4ht -dhtml/ _filename_. And yes, that slash after html is needed.

9. At this point you could upload your nice paper on this server and bypass the peer-review process altogether. Since you don't want to do that, you should now open the _filename_.html file with Word.

11. Select File->Save As and save the document in Word's format.

13. NO, we are not done yet... You _must_ now also embed the pictures in the Word file or your paper's addressee will only see small red crosses instead of your equations. You do this by following Edit->Links, select all the links and click on _Save picture in document_. Save the document again.

That should do it. Note that the whole TEX->HTML conversion should be doable in one step with the htlatex or similar program. On my system it fails because, as said above, latex does not produce DVI files by default, which is why I had to do it the pedestrian way.
