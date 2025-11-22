---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html"
title: "Tetrahedron - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Tetrahedron [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html\#tetrahedron "Link to this heading")

Qualified name: `manim.mobject.three\_d.polyhedra.Tetrahedron`

_class_ Tetrahedron( _edge\_length=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html#Tetrahedron) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#manim.mobject.three_d.polyhedra.Tetrahedron "Link to this definition")

Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron")

A tetrahedron, one of the five platonic solids. It has 4 faces, 6 edges, and 4 vertices.

Parameters:

**edge\_length** ( _float_) – The length of an edge between any two vertices.

Examples

Example: TetrahedronScene [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#tetrahedronscene)

![../_images/TetrahedronScene-1.png](https://docs.manim.community/en/stable/_images/TetrahedronScene-1.png)

```
from manim import *

class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Tetrahedron()
        self.add(obj)
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

\_original\_\_init\_\_( _edge\_length=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#manim.mobject.three_d.polyhedra.Tetrahedron._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**edge\_length** ( _float_)

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)