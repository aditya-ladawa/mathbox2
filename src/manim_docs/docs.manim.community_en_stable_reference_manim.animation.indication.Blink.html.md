---
url: "https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html"
title: "Blink - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Blink [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html\#blink "Link to this heading")

Qualified name: `manim.animation.indication.Blink`

_class_ Blink( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#Blink) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "Link to this definition")

Bases: [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

Blink the mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be blinked.

- **time\_on** ( _float_) – The duration that the mobject is shown for one blink.

- **time\_off** ( _float_) – The duration that the mobject is hidden for one blink.

- **blinks** ( _int_) – The number of blinks

- **hide\_at\_end** ( _bool_) – Whether to hide the mobject at the end of the animation.

- **kwargs** – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor.


Examples

Example: BlinkingExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#blinkingexample)

```
from manim import *

class BlinkingExample(Scene):
    def construct(self):
        text = Text("Blinking").scale(1.5)
        self.add(text)
        self.play(Blink(text, blinks=3))
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

\_original\_\_init\_\_( _mobject_, _time\_on=0.5_, _time\_off=0.5_, _blinks=1_, _hide\_at\_end=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **time\_on** ( _float_)

- **time\_off** ( _float_)

- **blinks** ( _int_)

- **hide\_at\_end** ( _bool_)


Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.indication.Blink.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.indication.Blink.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.indication.Blink.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.indication.Blink.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.indication.Blink.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.indication.Blink.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.indication.Blink.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.indication.Blink.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.indication.Blink.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.indication.Blink.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.indication.Blink.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.indication.Blink.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)