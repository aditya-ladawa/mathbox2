---
url: "https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html"
title: "Circumscribe - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Circumscribe [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html\#circumscribe "Link to this heading")

Qualified name: `manim.animation.indication.Circumscribe`

_class_ Circumscribe( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#Circumscribe) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#manim.animation.indication.Circumscribe "Link to this definition")

Bases: [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

Draw a temporary line surrounding the mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be circumscribed.

- **shape** ( _type_) – The shape with which to surround the given mobject. Should be either
[`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") or [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

- **fade\_in** – Whether to make the surrounding shape to fade in. It will be drawn otherwise.

- **fade\_out** – Whether to make the surrounding shape to fade out. It will be undrawn otherwise.

- **time\_width** – The time\_width of the drawing and undrawing. Gets ignored if either fade\_in or fade\_out is True.

- **buff** ( _float_) – The distance between the surrounding shape and the given mobject.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the surrounding shape.

- **run\_time** – The duration of the entire animation.

- **kwargs** – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor


Examples

Example: UsingCircumscribe [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#usingcircumscribe)

```
from manim import *

class UsingCircumscribe(Scene):
    def construct(self):
        lbl = Tex(r"Circum-\\scribe").scale(2)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))
```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _shape=<class'manim.mobject.geometry.polygram.Rectangle'>_, _fade\_in=False_, _fade\_out=False_, _time\_width=0.3_, _buff=0.1_, _color=ManimColor('#FFFF00')_, _run\_time=1_, _stroke\_width=4_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#manim.animation.indication.Circumscribe._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **shape** ( _type_)

- **buff** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))


Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.indication.Circumscribe.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.indication.Circumscribe.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.indication.Circumscribe.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.indication.Circumscribe.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.indication.Circumscribe.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.indication.Circumscribe.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.indication.Circumscribe.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.indication.Circumscribe.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.indication.Circumscribe.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.indication.Circumscribe.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.indication.Circumscribe.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.indication.Circumscribe.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)