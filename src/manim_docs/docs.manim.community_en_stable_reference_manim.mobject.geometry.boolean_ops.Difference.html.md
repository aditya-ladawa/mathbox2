---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html"
title: "Difference - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Difference [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html\#difference "Link to this heading")

Qualified name: `manim.mobject.geometry.boolean\_ops.Difference`

_class_ Difference( _subject_, _clip_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/boolean_ops.html#Difference) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#manim.mobject.geometry.boolean_ops.Difference "Link to this definition")

Bases: `_BooleanOps`

Subtracts one [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") from another one.

Parameters:

- **subject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 1st [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

- **clip** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

- **kwargs** ( _Any_)


Example

Example: DifferenceExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#differenceexample)

![../_images/DifferenceExample-1.png](https://docs.manim.community/en/stable/_images/DifferenceExample-1.png)

```
from manim import *

class DifferenceExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Difference(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0, 0])
        self.add(sq, cr, un)
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

\_original\_\_init\_\_( _subject_, _clip_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#manim.mobject.geometry.boolean_ops.Difference._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **subject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **clip** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.boolean_ops.Difference.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.boolean_ops.Difference.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.boolean_ops.Difference.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)