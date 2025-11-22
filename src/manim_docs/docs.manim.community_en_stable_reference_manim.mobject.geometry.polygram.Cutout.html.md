---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html"
title: "Cutout - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Cutout [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html\#cutout "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.Cutout`

_class_ Cutout( _main\_shape_, _\*mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#Cutout) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html#manim.mobject.geometry.polygram.Cutout "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A shape with smaller cutouts.

Parameters:

- **main\_shape** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The primary shape from which cutouts are made.

- **mobjects** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The smaller shapes which are to be cut out of the `main_shape`.

- **kwargs** ( _Any_) – Further keyword arguments that are passed to the constructor of
[`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


Warning

Technically, this class behaves similar to a symmetric difference: if
parts of the `mobjects` are not located within the `main_shape`,
these parts will be added to the resulting [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

Examples

Example: CutoutExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html#cutoutexample)

```
from manim import *

class CutoutExample(Scene):
    def construct(self):
        s1 = Square().scale(2.5)
        s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
        s3 = Square().shift(UP + RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
        s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
        self.play(Write(c), run_time=4)
        self.wait()
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

\_original\_\_init\_\_( _main\_shape_, _\*mobjects_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html#manim.mobject.geometry.polygram.Cutout._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **main\_shape** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **mobjects** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.polygram.Cutout.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.polygram.Cutout.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.polygram.Cutout.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.polygram.Cutout.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.polygram.Cutout.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.polygram.Cutout.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)