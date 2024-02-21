(ml)=
(ml-tools)=
# Machine Learning with CrateDB

This documentation section lists machine learning applications and frameworks
which can be used together with CrateDB. Relevant tutorials can be found within
the [CrateDB Guide: Machine Learning Tutorials] section of the documentation.


## LangChain

```{div}
:style: "float: right; font-size: 4em; margin-left: 0.3em"
🦜️🔗
```

[LangChain] is a framework for developing applications powered by language models,
written in Python, and with a strong focus on composability. As a language model
integration framework, LangChain's use-cases largely overlap with those of language
models in general, including document analysis and summarization, chatbots, and
code analysis.

LangChain supports retrieval-augmented generation (RAG), which is a technique for
augmenting LLM knowledge with additional, often private or real-time, data, and mixing
in "prompt engineering" as the process of structuring text that can be interpreted and
understood by a generative AI model. A prompt is natural language text describing the
task that an AI should perform.

The [LangChain adapter for CrateDB] provides support to use CrateDB as a vector store
database, to load documents using LangChain's DocumentLoader, and also supports
LangChain's conversational memory subsystem.

```{div}
:style: "clear: both"
```


## MLflow

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/d1d4f4ac-1b44-46b8-ba6f-4a82607c57d3){w=180px}](https://mlflow.org/)
```

[MLflow] is an open source platform to manage the whole ML lifecycle, including
experimentation, reproducibility, deployment, and a central model registry.

The [MLflow adapter for CrateDB], available through the [mlflow-cratedb] package,
provides support to use CrateDB as a storage database for the [MLflow Tracking]
subsystem, which is about recording and querying experiments, across code, data,
config, and results.

```{div}
:style: "clear: both"
```


## PyCaret

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/b17a59e2-6801-4f53-892f-ff472491095f){w=180px}](https://pycaret.org/)
```

[PyCaret] is an open-source, low-code machine learning library for Python that
automates machine learning workflows.

It is a high-level interface and AutoML wrapper on top of your loved machine learning
libraries like scikit-learn, xgboost, ray, lightgbm, and many more. PyCaret provides a
universal interface to utilize these libraries without needing to know the details
of the underlying model architectures and parameters.

```{div}
:style: "clear: both"
```


## scikit-learn

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/240px-Scikit_learn_logo_small.svg.png){w=180px}](https://scikit-learn.org/)

[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)

[![](https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg){w=180px}](https://jupyter.org/)
```

```{div}
:style: "clear: both"
```


[CrateDB Guide: Machine Learning Tutorials]: inv:guide:*:label#ml
[LangChain]: https://python.langchain.com/
[LangChain adapter for CrateDB]: https://github.com/crate-workbench/langchain
[MLflow]: https://mlflow.org/
[mlflow-cratedb]: https://pypi.org/project/mlflow-cratedb/
[MLflow adapter for CrateDB]: https://github.com/crate-workbench/mlflow-cratedb
[MLflow Tracking]: https://mlflow.org/docs/latest/tracking.html
[pandas]: https://pandas.pydata.org/
[PyCaret]: https://www.pycaret.org
[scikit-learn]: https://scikit-learn.org/
