(ml)=
(ml-tools)=
# Machine Learning with CrateDB

This documentation section lists machine learning applications and frameworks
which can be used together with CrateDB.


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

**See also**
- [LangChain and CrateDB]

- CrateDB's `FLOAT_VECTOR` type and its `KNN_MATCH` function can be used for storing and
  retrieving embeddings, and for conducting similarity searches.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fvector_search.ipynb)

- Database tables in CrateDB can be used as a source provider for LangChain documents.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fdocument_loader.ipynb)

- CrateDB supports managing LangChain's conversation history.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fconversational_memory.ipynb)

- What can you build with LangChain?

  - [LangChain: Retrieval augmented generation]
  - [LangChain: Analyzing structured data]
  - [LangChain: Chatbots]


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

**See also**
- Blog series on "Running Time Series Models in Production using CrateDB"
  - Part 1: [Introduction to Time Series Modeling using Machine Learning]

- [MLflow and CrateDB]: Guidelines and runnable code to get started with MLflow and
  CrateDB, exercising time series anomaly detection and timeseries forecasting /
  prediction using NumPy, Merlion, and Matplotlib.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb)


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

**See also**
- [AutoML with PyCaret and CrateDB]
- The `automl_classification_with_pycaret.ipynb` example notebook explores the PyCaret
  framework and shows how to use it to train different classification models.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb)

- The `automl_timeseries_forecasting_with_pycaret.ipynb` example notebook explores the PyCaret
  framework and shows how to use it to train various timeseries forecasting models.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb)


## scikit-learn

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/240px-Scikit_learn_logo_small.svg.png){w=180px}](https://scikit-learn.org/)

[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)

[![](https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg){w=180px}](https://jupyter.org/)
```

Using [pandas] and [scikit-learn] to run a regression analysis within a [Jupyter Notebook].

- [Machine Learning and CrateDB: An introduction]
- [Machine Learning and CrateDB: Getting Started With Jupyter]
- [Machine Learning and CrateDB: Experiment Design & Linear Regression]

**See also**
- [Automating financial data collection and storage in CrateDB with Python and pandas 2.0.0]
- [From data storage to data analysis: Tutorial on CrateDB and pandas]

```{div}
:style: "clear: both"
```


[Automating financial data collection and storage in CrateDB with Python and pandas 2.0.0]: https://community.crate.io/t/automating-financial-data-collection-and-storage-in-cratedb-with-python-and-pandas-2-0-0/916
[AutoML with PyCaret and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/automl
[From data storage to data analysis: Tutorial on CrateDB and pandas]: https://community.crate.io/t/from-data-storage-to-data-analysis-tutorial-on-cratedb-and-pandas/1440/1
[Introduction to Time Series Modeling using Machine Learning]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[Jupyter Notebook]: https://jupyter.org/
[LangChain]: https://python.langchain.com/
[LangChain: Analyzing structured data]: https://python.langchain.com/docs/use_cases/qa_structured/sql
[LangChain: Chatbots]: https://python.langchain.com/docs/use_cases/chatbots
[LangChain: Retrieval augmented generation]: https://python.langchain.com/docs/use_cases/question_answering/
[LangChain adapter for CrateDB]: https://github.com/crate-workbench/langchain
[LangChain and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llm-langchain
[Machine Learning and CrateDB: An introduction]: https://crate.io/blog/machine-learning-and-cratedb-part-one
[Machine Learning and CrateDB: Getting Started With Jupyter]: https://crate.io/blog/machine-learning-cratedb-jupyter
[Machine Learning and CrateDB: Experiment Design & Linear Regression]: https://crate.io/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression
[MLflow]: https://mlflow.org/
[mlflow-cratedb]: https://pypi.org/project/mlflow-cratedb/
[MLflow adapter for CrateDB]: https://github.com/crate-workbench/mlflow-cratedb
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlops-mlflow
[MLflow Tracking]: https://mlflow.org/docs/latest/tracking.html
[pandas]: https://pandas.pydata.org/
[PyCaret]: https://www.pycaret.org
[scikit-learn]: https://scikit-learn.org/
