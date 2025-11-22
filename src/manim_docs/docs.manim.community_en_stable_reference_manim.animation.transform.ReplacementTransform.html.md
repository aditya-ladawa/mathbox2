---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html"
title: "ReplacementTransform - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ReplacementTransform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html\#replacementtransform "Link to this heading")

Qualified name: `manim.animation.transform.ReplacementTransform`

_class_ ReplacementTransform( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ReplacementTransform) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Replaces and morphs a mobject into a target mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The starting [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **kwargs** – Further keyword arguments that are passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").


Examples

Example: ReplacementTransformOrTransform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#replacementtransformortransform)

```
from manim import *

class ReplacementTransformOrTransform(Scene):
    def construct(self):
        # set up the numbers
        r_transform = VGroup(*[Integer(i) for i in range(1,4)])
        text_1 = Text("ReplacementTransform", color=RED)
        r_transform.add(text_1)

        transform = VGroup(*[Integer(i) for i in range(4,7)])
        text_2 = Text("Transform", color=BLUE)
        transform.add(text_2)

        ints = VGroup(r_transform, transform)
        texts = VGroup(text_1, text_2).scale(0.75)
        r_transform.arrange(direction=UP, buff=1)
        transform.arrange(direction=UP, buff=1)

        ints.arrange(buff=2)
        self.add(ints, texts)

        # The mobs replace each other and none are left behind
        self.play(ReplacementTransform(r_transform[0], r_transform[1]))
        self.play(ReplacementTransform(r_transform[1], r_transform[2]))

        # The mobs linger after the Transform()
        self.play(Transform(transform[0], transform[1]))
        self.play(Transform(transform[1], transform[2]))
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

\_original\_\_init\_\_( _mobject_, _target\_mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.ReplacementTransform.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.ReplacementTransform.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.ReplacementTransform.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.ReplacementTransform.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.ReplacementTransform.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.ReplacementTransform.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.ReplacementTransform.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.ReplacementTransform.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.ReplacementTransform.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.ReplacementTransform.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.ReplacementTransform.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.ReplacementTransform.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)