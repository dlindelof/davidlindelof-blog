---
title: "Converting Sweave/R plots for inclusion in Word/OpenOffice"
date: 2011-04-14
---

Just a quick note to myself:

When you use [Sweave](http://www.stat.uni-muenchen.de/~leisch/Sweave/) and produce high-quality plots in both EPS and PDF formats, you sometimes want to include them in Word or OpenOffice documents.

You can't directly include PDF files, and you can only include EPS files when they have a preview, which Sweave will not do by default. And anyway, the EPS version of the graphs are made for black and white printers and will not be in color.

I'm using \`convert\` from the ImageMagick package to convert the PDF plots to PNG files. However, by default \`convert\` will give low-quality pictures. To have better images, I do:

convert -density 300 XXX.pdf XXX.png

If you feel geeky enough you can even include this in a Makefile:

figures: $(patsubst %.pdf, %.png, $(wildcard report-\*.pdf))

report-%.png : report-%.pdf convert -density 300 $< $@
