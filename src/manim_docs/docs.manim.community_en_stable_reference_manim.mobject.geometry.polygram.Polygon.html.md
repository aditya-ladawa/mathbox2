---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html"
title: "Polygon - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Polygon [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html\#polygon "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.Polygon`

_class_ Polygon( _\*vertices_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#Polygon) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "Link to this definition")

Bases: [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

A shape consisting of one closed loop of vertices.

Parameters:

- **vertices** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The vertices of the [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon").

- **kwargs** ( _Any_) – Forwarded to the parent constructor.


Examples

Example: PolygonExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#polygonexample)

![../_images/PolygonExample-1.png](https://docs.manim.community/en/stable/_images/PolygonExample-1.png)

```
from manim import *

class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [\
            [4, 1, 0],  # middle right\
            [4, -2.5, 0],  # bottom right\
            [0, -2.5, 0],  # bottom left\
            [0, 3, 0],  # top left\
            [2, 1, 0],  # middle\
            [4, 3, 0],  # top right\
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)
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

\_original\_\_init\_\_( _\*vertices_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **vertices** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.polygram.Polygon.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.polygram.Polygon.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.polygram.Polygon.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.polygram.Polygon.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.polygram.Polygon.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.polygram.Polygon.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)