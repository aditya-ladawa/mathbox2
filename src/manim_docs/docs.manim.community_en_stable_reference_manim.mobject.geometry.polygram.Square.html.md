---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html"
title: "Square - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Square [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html\#square "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.Square`

_class_ Square( _side\_length=2.0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#Square) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "Link to this definition")

Bases: [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

A rectangle with equal side lengths.

Parameters:

- **side\_length** ( _float_) – The length of the sides of the square.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle").


Examples

Example: SquareExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#squareexample)

![../_images/SquareExample-1.png](https://docs.manim.community/en/stable/_images/SquareExample-1.png)

```
from manim import *

class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)
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
| `side_length` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _side\_length=2.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **side\_length** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.polygram.Square.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.polygram.Square.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.polygram.Square.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.polygram.Square.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.polygram.Square.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.polygram.Square.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.polygram.Square.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.polygram.Square.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.polygram.Square.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.polygram.Square.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.polygram.Square.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.polygram.Square.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)