---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html"
title: "Restore - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Restore [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html\#restore "Link to this heading")

Qualified name: `manim.animation.transform.Restore`

_class_ Restore( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#Restore) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#manim.animation.transform.Restore "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Transforms a mobject to its last saved state.

To save the state of a mobject, use the [`save_state()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state") method.

Examples

Example: RestoreExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#restoreexample)

```
from manim import *

class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)
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

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

\_original\_\_init\_\_( _mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#manim.animation.transform.Restore._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.Restore.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.Restore.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.Restore.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.Restore.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.Restore.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.Restore.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.Restore.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.Restore.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.Restore.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.Restore.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.Restore.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.Restore.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)