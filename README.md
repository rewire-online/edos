# Explainable Detection of Online Sexism (EDOS)

This is the public repository for SemEval 2023 - Task 10. The [overview paper](https://arxiv.org/abs/2303.04222) summarises the dataset, task and participant systems.

Sexism is a growing problem online. It can inflict harm on women who are targeted, make online spaces inaccessible and unwelcoming, and perpetuate social asymmetries and injustices. Automated tools are now widely deployed to find, and assess sexist content at scale but most only give classifications for generic, high-level categories, with no further explanation. *Flagging what is sexist content and also explaining why it is sexist* improves interpretability, trust and understanding of the decisions that automated tools use, empowering both users and moderators.

This task supports the development of English-language models for sexism detection that are more accurate as well as explainable, with fine-grained classifications for sexist content from Gab and Reddit.

The task contains three hierarchical subtasks:

* TASK A - Binary Sexism Detection: a two-class (or binary) classification where systems have to predict whether a post is sexist or not sexist.
* TASK B - Category of Sexism: for posts which are sexist, a four-class classification where systems have to predict one of four categories: (1) threats, (2)  derogation, (3) animosity, (4) prejudiced discussion. 
* TASK C - Fine-grained Vector of Sexism: for posts which are sexist, an 11-class classification where systems have to predict one of 11 fine-grained vectors.

Our competition was hosted on [CodaLab](https://codalab.lisn.upsaclay.fr/competitions/7124).

If you use the dataset or accompanying materials, please cite: 

```
@inproceedings{kirkSemEval2023,
title = {{SemEval}-2023 {Task} 10: {Explainable} {Detection} of {Online} {Sexism}},
url = {http://arxiv.org/abs/2303.04222},
doi = {10.48550/arXiv.2303.04222},
author = {Kirk, Hannah Rose and Yin, Wenjie and Vidgen, Bertie and Röttger, Paul},
booktitle = {Proceedings of the 17th {{International Workshop}} on {{Semantic Evaluation}} ({{SemEval-2023}})},
publisher = {{Association for Computational Linguistics}},
year = {2023}
}
```


![Our Taxonomy](https://github.com/rewire-online/edos/blob/main/edos_vectors.png?raw=true)
