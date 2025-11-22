---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.utils.html"
title: "utils - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# utils [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html\#module-manim.mobject.utils "Link to this heading")

Utilities for working with mobjects.

Functions

get\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_mobject_class "Link to this definition")

Gets the base mobject class, depending on the currently active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_mobject_class
>>> get_mobject_class().__name__ in ['Mobject', 'OpenGLMobject']
True
```

Copy to clipboard

Return type:

type

get\_point\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_point_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_point_mobject_class "Link to this definition")

Gets the point cloud mobject class, depending on the currently
active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_point_mobject_class
>>> get_point_mobject_class().__name__ in ['PMobject', 'OpenGLPMobject']
True
```

Copy to clipboard

Return type:

type

get\_vectorized\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_vectorized_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_vectorized_mobject_class "Link to this definition")

Gets the vectorized mobject class, depending on the currently
active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_vectorized_mobject_class
>>> get_vectorized_mobject_class().__name__ in ['VMobject', 'OpenGLVMobject']
True
```

Copy to clipboard

Return type:

type

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.utils.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.utils.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.utils.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.utils.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.utils.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.utils.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.utils.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.utils.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.utils.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.utils.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.utils.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.utils.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)