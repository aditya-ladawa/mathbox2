---
url: "https://docs.manim.community/en/stable/reference/manim.animation.indication.html"
title: "indication - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# indication [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.html\#module-manim.animation.indication "Link to this heading")

Animations drawing attention to particular mobjects.

Examples

Example: Indications [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.html#indications)

```
from manim import *

class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))
```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`ApplyWave`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#manim.animation.indication.ApplyWave "manim.animation.indication.ApplyWave") | Send a wave through the Mobject distorting it temporarily. |
| [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "manim.animation.indication.Blink") | Blink the mobject. |
| [`Circumscribe`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#manim.animation.indication.Circumscribe "manim.animation.indication.Circumscribe") | Draw a temporary line surrounding the mobject. |
| [`Flash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html#manim.animation.indication.Flash "manim.animation.indication.Flash") | Send out lines in all directions. |
| [`FocusOn`](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#manim.animation.indication.FocusOn "manim.animation.indication.FocusOn") | Shrink a spotlight to a position. |
| [`Indicate`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#manim.animation.indication.Indicate "manim.animation.indication.Indicate") | Indicate a Mobject by temporarily resizing and recoloring it. |
| [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash") | Show only a sliver of the VMobject each frame. |
| [`ShowPassingFlashWithThinningStrokeWidth`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html#manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth "manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth") |  |
| [`Wiggle`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#manim.animation.indication.Wiggle "manim.animation.indication.Wiggle") | Wiggle a Mobject. |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.indication.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.indication.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.indication.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.indication.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.indication.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.indication.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.indication.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.indication.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.indication.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.indication.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.indication.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.indication.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.indication.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.indication.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)