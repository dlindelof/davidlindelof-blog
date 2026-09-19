png('posts/2023/05/is-the-ratio-of-normal-variables-normal/preview.png', width=1200, height=630, res=120)
par(bg='#101c30', mar=c(0,0,0,0), family='sans')
plot.new(); plot.window(xlim=c(0,1), ylim=c(0,1), xaxs='i', yaxs='i')
text(.07,.91,'STATISTICS  /  R SIMULATIONS',adj=0,col='#83cec8',cex=.92)
text(.07,.79,'Is the ratio of normal',adj=0,col='white',cex=2.2,font=2)
text(.07,.69,'variables normal?',adj=0,col='white',cex=2.2,font=2)
set.seed(20230503)
n <- 100000
z1 <- rnorm(n,100,2)/rnorm(n,50,.5)
z2 <- rnorm(n,100,2)/rnorm(n,10,2)
curve_panel <- function(z,left,right,color,label) {
 d <- density((z-mean(z))/sd(z),from=-3,to=5,n=512)
 x <- left+(d$x+3)/8*(right-left)
 y <- .22+d$y/.55*.30
 polygon(c(x[1],x,x[length(x)]),c(.22,y,.22),col=adjustcolor(color,.22),border=NA)
 lines(x,y,col=color,lwd=3)
 segments(left,.22,right,.22,col='#6c7990')
 text((left+right)/2,.15,label,col='white',cex=1.05)
}
curve_panel(z1,.07,.46,'#65d6c7','Denominator far from zero')
curve_panel(z2,.55,.94,'#ffb576','Denominator nearer zero')
text(.07,.055,'The denominator makes the difference.',adj=0,col='#bac6da',cex=.95)
text(.94,.055,'DAVID LINDELÖF',adj=1,col='#bac6da',cex=.8)
dev.off()
