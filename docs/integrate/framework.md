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


(dash)=
## Dash

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/8b679c0b-2740-4dcc-88f0-1106aee7fa95){w=180px}](https://dash.plotly.com/)
```

[Dash] is a low-code framework for rapidly building data apps in Python,
based on [Plotly]. Built on top of Plotly.js, React and Flask, Dash ties
modern UI elements like dropdowns, sliders, and graphs, directly to your
analytical Python code.

Dash is a trusted Python framework for building ML & data science web apps. Many
specialized open-source Dash libraries exist that are tailored for building
domain-specific Dash components and applications.

```{div}
:style: "clear: both"
```
:::

![](https://github.com/crate/crate-clients-tools/assets/453543/cc538982-e351-437b-97ec-f1fc6ca34948){h=200px}
![](https://github.com/crate/crate-clients-tools/assets/453543/24908861-f0ad-43f3-b229-b2bfcc61596d){h=200px}

:::{dropdown} **Dash Enterprise**
```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/8b679c0b-2740-4dcc-88f0-1106aee7fa95){w=180px}](https://plotly.com/dash/)
```

Dash Enterprise is Plotly’s paid product for building, testing, deploying, managing,
and scaling Dash applications organization-wide, advertised as the Premier Data App
Platform for Python.

When building Dash apps in a business setting, Dash Enterprise supports you to deploy
and scale them, plus integrate them with IT infrastructure such as authentication and
VPC services, in order to deliver faster and more impactful business outcomes on AI
and data science initiatives.

Dash Enterprise enables the rapid development of production-grade data apps within your
business. Python has taken over the world, and traditional BI dashboards no longer
cut it in today’s AI and ML driven world. Production-grade, low-code Python data apps
are needed to visualize the sophisticated data analytics and data pipelines that run
modern businesses.

```{div}
:style: "clear: both"
```
![](https://github.com/crate/crate-clients-tools/assets/453543/161a9b73-25eb-4ec4-aa3e-5fa73757b440){h=200px}
![](https://github.com/crate/crate-clients-tools/assets/453543/d199b9c9-8be0-4ff7-a7b5-835dc122cc6d){h=200px}
:::

<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/Qx5eFVUdDxk?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

_Plotly Dash Course - Session 1._


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


(hvplot)=
## hvPlot and Datashader

```{div}
:style: "float: right"
[![](https://hvplot.holoviz.org/_static/logo_horizontal.svg){w=220px}](https://hvplot.holoviz.org/)

[![](https://datashader.org/_static/logo_horizontal.svg){w=220px}](https://datashader.org/)
```

[hvPlot] is a familiar and high-level API for data exploration and visualization.
[Datashader] is a graphics pipeline system for creating meaningful representations of
large datasets quickly and flexibly.

It is used on behalf of the [hvPlot] package, which is based on [HoloViews], from the
family of [HoloViz] packages of the [PyViz] ecosystem.

With Datashader, you can "just plot" large datasets and explore them instantly, with no
parameter tweaking, magic numbers, subsampling, or approximation, up to the resolution
of the display.

[hvPlot] sources its power in the [HoloViz] ecosystem. With [HoloViews], you get the
ability to easily layout and overlay plots, with [Panel], you can get more interactive
control of your plots with widgets, with [DataShader], you can visualize and interactively
explore very large data, and with [GeoViews], you can create geographic plots.

```{div}
:style: "clear: both"
```

![](https://github.com/crate/crate-clients-tools/assets/453543/7f38dff6-04bc-429e-9d31-6beeb9289c4b){h=200px}
![](https://github.com/crate/crate-clients-tools/assets/453543/23561a87-fb4f-4154-9891-1b3068e40579){h=200px}


<iframe width="480" height="320" src="https://www.youtube-nocookie.com/embed/eWpVUPHrCIA?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

_hvPlot and Panel: Visualize all your data easily, from notebooks to dashboards | SciPy 2023._


(plotly)=
## Plotly

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/8b679c0b-2740-4dcc-88f0-1106aee7fa95){w=180px}](https://plotly.com/)
```

[Plotly] Open Source Graphing Libraries make interactive, publication-quality graphs.
Line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms,
heatmaps, subplots, multiple-axes, polar charts, bubble charts, and maps.

The supported programming languages / libraries / frameworks are Python, R, Julia,
JavaScript, ggplot2, F#, MATLAB®, and Dash.

Based on Plotly, [Dash] is a low-code framework for rapidly building data apps in Python.

```{div}
:style: "clear: both"
```

![](https://github.com/crate/crate-clients-tools/assets/453543/380114a8-7984-4966-929b-6e6d52ddd48a){h=200px}
![](https://github.com/crate/crate-clients-tools/assets/453543/f6a99ae7-b730-4587-bd23-499e1be02c92){h=200px}


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


[Dash]: https://plotly.com/dash/
[Datashader]: https://datashader.org/
[Gradio]: https://www.gradio.app/
[HoloViews]: https://www.holoviews.org/
[HoloViz]: https://holoviz.org/
[hvPlot]: https://hvplot.holoviz.org/
[Hugging Face]: https://en.wikipedia.org/wiki/Hugging_Face
[Panel]: https://panel.holoviz.org/
[Plotly]: https://plotly.com/graphing-libraries/
[PyViz]: https://pyviz.org/
[Streamlit]: https://streamlit.io/
