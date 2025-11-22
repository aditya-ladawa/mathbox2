---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html"
title: "BraceBetweenPoints - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# BraceBetweenPoints [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html\#bracebetweenpoints "Link to this heading")

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

_class_ BraceBetweenPoints( _point\_1_, _point\_2_, _direction=array(\[0.,0.,0.\])_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html#BraceBetweenPoints) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints "Link to this definition")

Bases: [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace")

Similar to Brace, but instead of taking a mobject it uses 2
points to place the brace.

A fitting direction for the brace is
computed, but it still can be manually overridden.
If the points go from left to right, the brace is drawn from below.
Swapping the points places the brace on the opposite side.

Parameters:

- **point\_1** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_) – The first point.

- **point\_2** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_) – The second point.

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") _\|_ _None_) – The direction from which the brace faces towards the points.


Examples

Example: BraceBPExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#bracebpexample)

```
from manim import *

class BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)
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

\_original\_\_init\_\_( _point\_1_, _point\_2_, _direction=array(\[0.,0.,0.\])_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **point\_1** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)

- **point\_2** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") _\|_ _None_)


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.svg.brace.BraceBetweenPoints.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)