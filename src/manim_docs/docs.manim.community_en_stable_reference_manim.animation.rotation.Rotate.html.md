---
url: "https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html"
title: "Rotate - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Rotate [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html\#rotate "Link to this heading")

Qualified name: `manim.animation.rotation.Rotate`

_class_ Rotate( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/rotation.html#Rotate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#manim.animation.rotation.Rotate "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Animation that rotates a Mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be rotated.

- **angle** ( _float_) – The rotation angle.

- **axis** ( _np.ndarray_) – The rotation axis as a numpy vector.

- **about\_point** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The rotation center.

- **about\_edge** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – If `about_point` is `None`, this argument specifies
the direction of the bounding box point to be taken as
the rotation center.


Examples

Example: UsingRotate [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#usingrotate)

```
from manim import *

class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _angle=3.141592653589793_, _axis=array(\[0.,0.,1.\])_, _about\_point=None_, _about\_edge=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#manim.animation.rotation.Rotate._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **angle** ( _float_)

- **axis** ( _np.ndarray_)

- **about\_point** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_)

- **about\_edge** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.rotation.Rotate.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.rotation.Rotate.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.rotation.Rotate.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.rotation.Rotate.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.rotation.Rotate.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.rotation.Rotate.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.rotation.Rotate.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.rotation.Rotate.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.rotation.Rotate.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.rotation.Rotate.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.rotation.Rotate.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.rotation.Rotate.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)