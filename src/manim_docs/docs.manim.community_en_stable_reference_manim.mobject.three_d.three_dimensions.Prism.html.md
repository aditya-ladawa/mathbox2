---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html"
title: "Prism - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Prism [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html\#prism "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`

_class_ Prism( _dimensions=\[3,2,1\]_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Prism) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "Link to this definition")

Bases: [`Cube`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cube.html#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube")

A right rectangular prism (or rectangular cuboid).
Defined by the length of each side in `[x, y, z]` format.

Parameters:

**dimensions** ( _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\|_ _np.ndarray_) – Dimensions of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism") in `[x, y, z]` format.

Examples

Example: ExamplePrism [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#exampleprism)

![../_images/ExamplePrism-1.png](https://docs.manim.community/en/stable/_images/ExamplePrism-1.png)

```
from manim import *

class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism.generate_points "manim.mobject.three_d.three_dimensions.Prism.generate_points") | Creates the sides of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism"). |

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

\_original\_\_init\_\_( _dimensions=\[3,2,1\]_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**dimensions** ( _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\|_ _ndarray_)

Return type:

None

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Prism.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism.generate_points "Link to this definition")

Creates the sides of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism").

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.three_d.three_dimensions.Prism.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.three_d.three_dimensions.Prism.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.three_d.three_dimensions.Prism.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)