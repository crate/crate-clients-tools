(framework)=
# Using Programming Frameworks with CrateDB

Application programming frameworks integrating with CrateDB.

Many of them are built on top of the Python programming language, making it easy
to use the Python libraries that you know and love.

:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`lightbulb;2em` Examples

A few quick examples about how to use relevant frameworks together with CrateDB.

- https://github.com/crate/cratedb-examples/tree/main/framework
+++
{tag-info}`Gradio` {tag-info}`Streamlit`
::::

::::{grid-item-card} {material-outlined}`read_more;2em` SQLAlchemy
CrateDB's SQLAlchemy dialect implementation provides fundamental database adapter
infrastructure to framework integrations.
+++
[ORM Guides](inv:guide#orm) •
{ref}`ORM Catalog <orm>`
::::

:::::


(gradio)=
## Gradio

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://raw.githubusercontent.com/gradio-app/gradio/main/readme_files/gradio.svg){w=180px}](https://www.gradio.app/)
```

[Gradio] is an open source programming framework for quickly creating and sharing
machine learning model demo applications, written in Python.

- Creating a user interface only requires adding a couple lines of code to your project.
- It does not require any experience with HTML/JS/CSS, or web hosting.
- Gradio can be embedded in Python notebooks, or presented as a web application.
- Once you've created an interface, you can permanently host it on [Hugging Face].

```{div}
:style: "clear: both"
```

<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/44vi31hehw4?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

_How to Build Machine Learning APIs Using Gradio._


(streamlit)=
## Streamlit

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://github.com/crate/crate-clients-tools/assets/453543/0fffb2d4-1d17-49c9-96e3-fd6ae42a39c4){w=180px}](https://streamlit.io/)
```

[Streamlit] is an open source application programming framework for quickly sketching
out Python data applications. It provides fast, interactive prototyping, and live editing.

- Build dashboards, generate reports, or create chat apps using beautiful, easy-to-read code.
- No in-depth knowledge of HTML/JS/CSS needed, the framework offers elegant default
  styling, which can be adjusted when applicable.
- Transform Python scripts into interactive web apps in minutes, instead of weeks.
- Build upon a range of [Streamlit components](https://streamlit.io/components).
- Optionally use their [Community Cloud platform](https://streamlit.io/cloud) to deploy, 
  manage, and share your application.

```{div}
:style: "clear: both"
```

<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/UI4f4iiVT6c?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

_Streamlit 101 - A faster way to build and share data applications._



[Gradio]: https://www.gradio.app/
[Hugging Face]: https://en.wikipedia.org/wiki/Hugging_Face
[Streamlit]: https://streamlit.io/
