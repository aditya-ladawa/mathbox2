---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html"
title: "ApplyMatrix - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ApplyMatrix [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html\#applymatrix "Link to this heading")

Qualified name: `manim.animation.transform.ApplyMatrix`

_class_ ApplyMatrix( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyMatrix) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix "Link to this definition")

Bases: [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction")

Applies a matrix transform to an mobject.

Parameters:

- **matrix** ( _np.ndarray_) – The transformation matrix.

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **about\_point** ( _np.ndarray_) – The origin point for the transform. Defaults to `ORIGIN`.

- **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction").


Examples

Example: ApplyMatrixExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#applymatrixexample)

```
from manim import *

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `initialize_matrix` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _matrix_, _mobject_, _about\_point=array(\[0.,0.,0.\])_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **matrix** ( _ndarray_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **about\_point** ( _ndarray_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.ApplyMatrix.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.ApplyMatrix.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.ApplyMatrix.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.ApplyMatrix.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.ApplyMatrix.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.ApplyMatrix.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.ApplyMatrix.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.ApplyMatrix.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.ApplyMatrix.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.ApplyMatrix.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.ApplyMatrix.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.ApplyMatrix.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)