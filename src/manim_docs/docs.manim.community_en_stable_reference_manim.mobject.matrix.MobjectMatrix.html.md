---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html"
title: "MobjectMatrix - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# MobjectMatrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html\#mobjectmatrix "Link to this heading")

Qualified name: `manim.mobject.matrix.MobjectMatrix`

_class_ MobjectMatrix( _matrix_, _element\_to\_mobject=<functionMobjectMatrix.<lambda>>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#MobjectMatrix) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix "Link to this definition")

Bases: [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

A mobject that displays a matrix of mobject entries on the screen.

Examples

Example: MobjectMatrixExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#mobjectmatrixexample)

![../_images/MobjectMatrixExample-1.png](https://docs.manim.community/en/stable/_images/MobjectMatrixExample-1.png)

```
from manim import *

class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)
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

\_original\_\_init\_\_( _matrix_, _element\_to\_mobject=<functionMobjectMatrix.<lambda>>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.matrix.MobjectMatrix.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.matrix.MobjectMatrix.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.matrix.MobjectMatrix.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.matrix.MobjectMatrix.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.matrix.MobjectMatrix.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.matrix.MobjectMatrix.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)