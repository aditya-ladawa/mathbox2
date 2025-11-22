---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html"
title: "FadeToColor - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# FadeToColor [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html\#fadetocolor "Link to this heading")

Qualified name: `manim.animation.transform.FadeToColor`

_class_ FadeToColor( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeToColor) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#manim.animation.transform.FadeToColor "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Animation that changes color of a mobject.

Examples

Example: FadeToColorExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#fadetocolorexample)

```
from manim import *

class FadeToColorExample(Scene):
    def construct(self):
        self.play(FadeToColor(Text("Hello World!"), color=RED))
```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( _str_)


\_original\_\_init\_\_( _mobject_, _color_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#manim.animation.transform.FadeToColor._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( _str_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.FadeToColor.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.FadeToColor.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.FadeToColor.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.FadeToColor.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.FadeToColor.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.FadeToColor.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.FadeToColor.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.FadeToColor.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.FadeToColor.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.FadeToColor.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.FadeToColor.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.FadeToColor.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)