---
url: "https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html"
title: "CapStyleType - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# CapStyleType [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html\#capstyletype "Link to this heading")

Qualified name: `manim.constants.CapStyleType`

_class_ CapStyleType( _value_, _names=<notgiven>_, _\*values_, _module=None_, _qualname=None_, _type=None_, _start=1_, _boundary=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/constants.html#CapStyleType) [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#manim.constants.CapStyleType "Link to this definition")

Bases: `Enum`

Collection of available cap styles.

See the example below for a visual illustration of the different
cap styles.

Examples

Example: CapStyleVariants [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#capstylevariants)

![../_images/CapStyleVariants-1.png](https://docs.manim.community/en/stable/_images/CapStyleVariants-1.png)

```
from manim import *

class CapStyleVariants(Scene):
    def construct(self):
        arcs = VGroup(*[\
            Arc(\
                radius=1,\
                start_angle=0,\
                angle=TAU / 4,\
                stroke_width=20,\
                color=GREEN,\
                cap_style=cap_style,\
            )\
            for cap_style in CapStyleType\
        ])
        arcs.arrange(RIGHT, buff=1)
        self.add(arcs)
        for arc in arcs:
            label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
            self.add(label)
```

Copy to clipboard

Make interactive

Attributes

|     |     |
| --- | --- |
| `AUTO` |  |
| `ROUND` |  |
| `BUTT` |  |
| `SQUARE` |  |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.constants.CapStyleType.html)[hi](https://docs.manim.community/hi/stable/reference/manim.constants.CapStyleType.html)[sv](https://docs.manim.community/sv/stable/reference/manim.constants.CapStyleType.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.constants.CapStyleType.html)**[stable](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.constants.CapStyleType.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.constants.CapStyleType.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.constants.CapStyleType.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.constants.CapStyleType.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.constants.CapStyleType.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.constants.CapStyleType.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.constants.CapStyleType.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.constants.CapStyleType.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)