---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html"
title: "Ellipse - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Ellipse [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html\#ellipse "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.Ellipse`

_class_ Ellipse( _width=2_, _height=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Ellipse) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#manim.mobject.geometry.arc.Ellipse "Link to this definition")

Bases: [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

A circular shape; oval, circle.

Parameters:

- **width** ( _float_) – The horizontal width of the ellipse.

- **height** ( _float_) – The vertical height of the ellipse.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").


Examples

Example: EllipseExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#ellipseexample)

![../_images/EllipseExample-1.png](https://docs.manim.community/en/stable/_images/EllipseExample-1.png)

```
from manim import *

class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        self.add(ellipse_group)
```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _width=2_, _height=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#manim.mobject.geometry.arc.Ellipse._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **width** ( _float_)

- **height** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.arc.Ellipse.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.arc.Ellipse.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.arc.Ellipse.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.arc.Ellipse.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.arc.Ellipse.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.arc.Ellipse.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)