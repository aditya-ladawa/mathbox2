---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html"
title: "ApplyPointwiseFunction - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ApplyPointwiseFunction [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html\#applypointwisefunction "Link to this heading")

Qualified name: `manim.animation.transform.ApplyPointwiseFunction`

_class_ ApplyPointwiseFunction( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyPointwiseFunction) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Animation that applies a pointwise function to a mobject.

Examples

Example: WarpSquare [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#warpsquare)

```
from manim import *

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
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
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **function** ( _types.MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)


\_original\_\_init\_\_( _function_, _mobject_, _run\_time=3.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **function** ( _MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.ApplyPointwiseFunction.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.ApplyPointwiseFunction.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.ApplyPointwiseFunction.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)