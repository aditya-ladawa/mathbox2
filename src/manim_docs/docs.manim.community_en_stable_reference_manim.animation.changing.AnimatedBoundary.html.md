---
url: "https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html"
title: "AnimatedBoundary - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# AnimatedBoundary [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html\#animatedboundary "Link to this heading")

Qualified name: `manim.animation.changing.AnimatedBoundary`

_class_ AnimatedBoundary( _vmobject,colors=\[ManimColor('#29ABCA'),ManimColor('#9CDCEB'),ManimColor('#236B8E'),ManimColor('#736357')\],max\_stroke\_width=3,cycle\_rate=0.5,back\_and\_forth=True,draw\_rate\_func=<functionsmooth>,fade\_rate\_func=<functionsmooth>,\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/changing.html#AnimatedBoundary) [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#manim.animation.changing.AnimatedBoundary "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Boundary of a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with animated color change.

Examples

Example: AnimatedBoundaryExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#animatedboundaryexample)

```
from manim import *

class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `full_family_become_partial` |  |
| `update_boundary_copies` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _vmobject,colors=\[ManimColor('#29ABCA'),ManimColor('#9CDCEB'),ManimColor('#236B8E'),ManimColor('#736357')\],max\_stroke\_width=3,cycle\_rate=0.5,back\_and\_forth=True,draw\_rate\_func=<functionsmooth>,fade\_rate\_func=<functionsmooth>,\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#manim.animation.changing.AnimatedBoundary._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.changing.AnimatedBoundary.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.changing.AnimatedBoundary.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.changing.AnimatedBoundary.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.changing.AnimatedBoundary.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.changing.AnimatedBoundary.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.changing.AnimatedBoundary.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.changing.AnimatedBoundary.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.changing.AnimatedBoundary.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.changing.AnimatedBoundary.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.changing.AnimatedBoundary.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.changing.AnimatedBoundary.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.changing.AnimatedBoundary.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)