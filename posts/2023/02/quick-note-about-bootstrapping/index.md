---
title: "Quick note about bootstrapping"
date: 2023-02-06
---

Cross-validation---the act of keeping a subset of data to measure the performance of a model trained on the rest of the data---never sounded right to me.

It just doesn't feel optimal to retain an arbitrary fraction of the data when you train your model. Oh and then you're also supposed to keep _another_ fraction for _validating_ the model. So one set for training, one set for testing (to find the best model structure), and one set for validating the model, i.e. measuring its performance. That's throwing away quite a lot of data that could be used for training.

That's why I was excited to learn that bootstrapping provides an alternative. Bootstrapping is an elegant way to maximize the use of the available data, typically when you want to estimate confidence intervals or any other statistic.

In "[Applied Predictive Modelling](https://www.amazon.com/Applied-Predictive-Modeling-Max-Kuhn/dp/1461468485/ref=sr_1_4?crid=OG31K5T3TW79&keywords=Applied+Predictive+Modelling&qid=1652540040&sprefix=applied+predictive+modelling%2Caps%2C192&sr=8-4)", the authors discuss resampling techniques, which include bootstrapping and cross-validation (p. 72). The authors explain that bootstrap validation consists in building _N_ models with bootstrapped data and estimating their performance on the out-of-bag samples, i.e. the samples not used in building the model.

I think that may be an error. I don't have [Efron's seminal book on the bootstrap](https://www.amazon.com/Introduction-Bootstrap-Monographs-Statistics-Probability/dp/0412042312/ref=sr_1_1?crid=1MSUNDIAEZ2A1&keywords=efron+bootstrap&qid=1652540247&sprefix=efron+bootstrap%2Caps%2C170&sr=8-1) anymore but I'm pretty sure the accuracy was evaluated against the entire data set, not just the out-of-bag samples.

In "[Regression Modelling Strategies](https://www.amazon.com/Regression-Modeling-Strategies-Applications-Statistics/dp/331933039X/ref=sr_1_1?crid=3FSNZYETV1W07&keywords=Regression+Modelling+Strategies&qid=1652540658&sprefix=regression+modeling+strategies%2Caps%2C408&sr=8-1)", Frank Harrell describes model validation with the bootstrap thus (emphasis mine):

> With the “simple bootstrap” \[178, p. 247\], one repeatedly fits the model in a bootstrap sample and evaluates the performance of the model on the **original sample**. The estimate of the likely performance of the final model on future data is estimated by the average of all of the indexes computed on the original sample.
> 
> Frank Harrell, Regression Modelling Strategies
