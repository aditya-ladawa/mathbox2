---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html"
title: "ApplyMethod - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ApplyMethod [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html\#applymethod "Link to this heading")

Qualified name: `manim.animation.transform.ApplyMethod`

_class_ ApplyMethod( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyMethod) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Animates a mobject by applying a method.

Note that only the method needs to be passed to this animation,
it is not required to pass the corresponding mobject. Furthermore,
this animation class only works if the method returns the modified
mobject.

Parameters:

- **method** ( _Callable_) – The method that will be applied in the animation.

- **args** – Any positional arguments to be passed when applying the method.

- **kwargs** – Any keyword arguments passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").


Methods

|     |     |
| --- | --- |
| `check_validity_of_input` |  |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _method_, _\*args_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**method** ( _Callable_)

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.ApplyMethod.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.ApplyMethod.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.ApplyMethod.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.ApplyMethod.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.ApplyMethod.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.ApplyMethod.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.ApplyMethod.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.ApplyMethod.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.ApplyMethod.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.ApplyMethod.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.ApplyMethod.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.ApplyMethod.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)