# dignity_in_ecthr

## Provision project plan (17 July 2023)

## RQ

What does the court talk about when it talks about dignity? Is it a meaningless concept that is thrown around as an exclamation point? Or does it mark a special dimension of concern?

## Theoretical background

* Gustavo --> Debate around dignity starting in the Bush era.

## Data

Dignity cases - 10 years
Grand chamber cases subset

* Gustavo -> Send cases
* Keyword --> structured search, word dignity in the text of the case
* +- 1200 cases

## Approach 

* Unsupervised learning on
* Chunk the text on "THE FACTS"
* Standard preprocessing + legal stopwords
* TF-IDF
* ngrams
* Word vectors scaled TFIDF (?)
* LDA NMF SVD KMeans other (Louvain communities on text similarity network?)
* Silohuette or perplexity to fix number of clusters.
* Top n_words by cluster
* Word clouds per cluster

Can we get typical cases for the cluster (high probability of falling into cluster 1, and low probability of belonging anywhere else).

> Do we need a metric here, like a purity score, where a case scores higher in purity if it has an extreme inequality between bins, and low in purity if all the bins are equally likely? 

## Expectations

I expect something like this

1) Dignity as honor and reputation
2) Prision conditions
3) Attacts on physical integrity
4) Issues relating to intimacy, family and medical care (bioethics)
5) Assylum and refugee

> Co-decision on number of clusters

## Caveats

Once we have the clusters, I would see in which a violation is more likely to be found (barplot finding of violation per cluster)
So I would not do 2 sets of clusters, one for violation and one for non-violation cases.

## Publication

Maybe send to Jurix 2023 at Maastricht / or journal (AI and Law?)
