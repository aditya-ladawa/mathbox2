---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html"
title: "DecimalMatrix - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# DecimalMatrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html\#decimalmatrix "Link to this heading")

Qualified name: `manim.mobject.matrix.DecimalMatrix`

_class_ DecimalMatrix( _matrix_, _element\_to\_mobject=<class'manim.mobject.text.numbers.DecimalNumber'>_, _element\_to\_mobject\_config={'num\_decimal\_places':1}_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#DecimalMatrix) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#manim.mobject.matrix.DecimalMatrix "Link to this definition")

Bases: [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

A mobject that displays a matrix with decimal entries on the screen.

Examples

Example: DecimalMatrixExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#decimalmatrixexample)

![../_images/DecimalMatrixExample-1.png](https://docs.manim.community/en/stable/_images/DecimalMatrixExample-1.png)

```
from manim import *

class DecimalMatrixExample(Scene):
    def construct(self):
        m0 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")
        self.add(m0)
```

Copy to clipboard

Make interactive

Will round/truncate the decimal places as per the provided config.

Parameters:

- **matrix** ( _Iterable_) – A numpy 2d array or list of lists

- **element\_to\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber

- **element\_to\_mobject\_config** ( _dict_ _\[_ _str_ _,_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}


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

\_original\_\_init\_\_( _matrix_, _element\_to\_mobject=<class'manim.mobject.text.numbers.DecimalNumber'>_, _element\_to\_mobject\_config={'num\_decimal\_places':1}_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#manim.mobject.matrix.DecimalMatrix._original__init__ "Link to this definition")

Will round/truncate the decimal places as per the provided config.

Parameters:

- **matrix** ( _Iterable_) – A numpy 2d array or list of lists

- **element\_to\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber

- **element\_to\_mobject\_config** ( _dict_ _\[_ _str_ _,_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.matrix.DecimalMatrix.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.matrix.DecimalMatrix.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.matrix.DecimalMatrix.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.matrix.DecimalMatrix.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.matrix.DecimalMatrix.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.matrix.DecimalMatrix.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)