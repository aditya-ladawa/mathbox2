---
url: "https://docs.manim.community/en/stable/reference/manim.animation.fading.html"
title: "fading - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# fading [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.html\#module-manim.animation.fading "Link to this heading")

Fading in and out of view.

Example: Fading [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#fading)

```
from manim import *

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))
```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") | Fade in [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |
| [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut") | Fade out [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.fading.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.fading.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.fading.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.fading.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.fading.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.fading.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.fading.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.fading.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.fading.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.fading.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.fading.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.fading.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.fading.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.fading.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)