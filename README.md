Documentation
=============

This project aims to cluster scientific papers by using a hybrid method from the [Vector Space Model](http://en.wikipedia.org/wiki/Vector_space_model) (VSM) and [Bibliographic Coupling](http://en.wikipedia.org/wiki/Bibliographic_coupling). 

For Clustering both measures are combined to a single distance measure using Fisher's inverse Xi^2 method. We cluster using [K-Medoids](http://en.wikipedia.org/wiki/K-medoids) setting the initial centroids with [h-index](http://en.wikipedia.org/wiki/H-index)-based [h-Cores](http://link.springer.com/article/10.1007%2Fs11192-012-0639-3). 

Input ist a xml document containing abstracts and references of the papers. We use a corpus from  [CiteSeerX](http://citeseerx.ist.psu.edu/index).The given corpus is big with ~ 500k documents after preprocessing. Therefore, we need to sample documents from it to meet time and main memory constraints. We need to reduce it to ~ 4% of the actual size: __21000 documents__


Workflow Overview
-----------------
![Workflow Diagram](https://github.com/gessulat/txt_mining/blob/master/img/hybrid_clustering_flow.png?raw=true)



------------------------------------



Preprocessing
=============
Before we work with the corpus we remove documents wich we cannot work with. These are:

* __Documents that cite no other document:__ These documents do not contribute to the Tanimoto Distance calculation. Realized by: ``filter_empty_references.py``

* __Documents with no abstract:__ In the VSM documents with an empty abstract are identical, meaning the distance between them is 0. But it makes no sense that documents that have no abstract ( most probably a corpus error) results in our algorithms thinking these documents are very similar. Realized by: ``filter_empty_abstracts.py``

* __Documents that are not in English:__ If we have a corpus that has multiple languages it is difficult to stem the results, because we would have to first guess the language of each abstract and then stemm according to that language. This is:
  a) time consuming and
  b) we would need an own stemmer for each language
Realized by: ``filter_nonEnglish_abstracts.py`` uses the [guessLanguage python package](http://pypi.python.org/pypi/guess-language)

These 3 filter scripts output the new filtered dictionary and a diff file. Since we just reduce either the references or the abstracts dicts, we need to keep both in sync. Realized by: ``synchronize_by_diff.py``.

For further information on how to use these scripts use ``--help``.
Preprocessing steps in detail
----

![Workflow Diagram](https://github.com/gessulat/txt_mining/blob/master/img/preprocessing_diagram.jpg?raw=true)



Sampling
--------
Sampling is necessary to reduce the size of the distance matrix. We consider following sampling methods as options. It makes sense to sample before calculating __Rogers-Tanimoto__ and __Cosine distance__ distance matrices to keep the matrices relatively small.

* __Should the sampling happen before creating the dictionary out of the abstracts?__ If the documents are sampled in advance, the set of words is likely to be smaller. On the other hand, if we store the abstract word lists for every document as adjacency list only the dictionary but not the abstract word lists gets bigger. 
  * __Decision__: Preprocessing including stemming of the whole corpus takes about 4 hours on a 2012 Macbook Air (SSD, 4 GB RAM), which is acceptable. Thus, we decided to do the sampling after stemming the word list - this way we can use different sampling methods and don't need to change our word_base.pickle (the word dictionary generated from stemming).


1. __Random sampling__: x% of the documents are sampled at random. It is most easy to calculate. Keyword: ``random``
* __Reference list size sampling__: The top x% of the documents ordered by the size of their referenze list are considered. With this method there is a good chance (but only chance!) that the documents in the remaining corpus are well connected. Furthermore it is easy to calculate. Keyword: ``most_refs``
* __Most cited sampling__: The top x% of the documents ordered by the number of times a document is cited by other documents. This method is hard to calculate, but it ensures good connection to find h-cores and calculate Rogers-Tanimoto (by their definition)
* __Timestamp based sampling__: Only documents in a given timeframe from timestamp t1 and timestamp t2 are considered. The method is easy to calculate but may have bad effects for the h-core calculation and clustering. This would happen if a significant amount of documents that influence the Rogers-Tanimoto distance and the h-core calculation lay outside of the time frame used. 
*  __Hierarchical sampling__: A combination of other sampling methods.


__Random sampling__ and __Reference list size sampling__ are realized by: ``sampling.py``. The script let's you choose the sampling method by the according keyword. Also see --help


-----
Distances
=========

Rogers-Tanimoto Distance
------------------------
* __Definition:__ Rogers-Tanimoto Distance (RTD) is the distance between between document __x__ and __y__ defined as ``RTD(x,y) = Cxy / (Cx + Cy - Cxy)`` with __Cx__ (documents that are cited by __x__), __Cy__ (documents that are cited by __y__) and __Cxy__ (documented that are cited both by __x__ AND __y__)


Cosine Distance
---------------
* __Definition:__ Cosine Distance (CD) is the distance between between document __x__ and __y__ defined as ``CD(x,y)=cos(x,y)= ( x * y ) / ( |x| * |y| )``. Gewichtung möglich mit [Bag of words](http://en.wikipedia.org/wiki/Bag-of-words_model) oder [TF-IDF](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
* To calculate the cosine distance in the bag-of-words model we need a vector for each abstract. The vector size is the same as the word_base word dictionary from our corpus, and counts the numbers each word appears in the given abstract. __Should we calculate the vectors in advance?__ We tested this on a small sample of 500 documents and the abstracts file went from 400kb to 20 mb in size. Since we assume that we 

Fisher's inverse Xi^2 method
----------------------------
* __Definition:__ Is the distance between document __x__, __y__ defined as ``FD=cos(λ*arccos(RTD(x,y))+(1–λ) *arccos(CD(x,y)))``mit0<=λ<=1.


---------------------------------


Tools
=====
R
-
* K-Medoids



SciPy
-----
* Tanimoto-Rogers
* Cosine Distance


Homebrewn
---------

*	__xml2abstract.py__: extracts abstracts from a xml file (citeseer.xml) and pickles it. Filters for documents before 2010.
*	__xml2refs.py__: extracts references from a xml file (citeseer.xml) and pickles it. Filters for documents before 2010.
*	__abstracts2dict.py__: builds a dictionary from abstracts.pickle (stemming included)
*	__set_extractor.py__: extracts an id sets from reference tokens or a word set from abstract tokens






