---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html"
title: "SurroundingRectangle - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SurroundingRectangle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html\#surroundingrectangle "Link to this heading")

Qualified name: `manim.mobject.geometry.shape\_matchers.SurroundingRectangle`

_class_ SurroundingRectangle( _\*mobjects_, _color=ManimColor('#FFFF00')_, _buff=0.1_, _corner\_radius=0.0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html#SurroundingRectangle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "Link to this definition")

Bases: [`RoundedRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RoundedRectangle.html#manim.mobject.geometry.polygram.RoundedRectangle "manim.mobject.geometry.polygram.RoundedRectangle")

A rectangle surrounding a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

Example: SurroundingRectExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#surroundingrectexample)

![../_images/SurroundingRectExample-1.png](https://docs.manim.community/en/stable/_images/SurroundingRectExample-1.png)

```
from manim import *

class SurroundingRectExample(Scene):
    def construct(self):
        title = Title("A Quote from Newton")
        quote = Text(
            "If I have seen further than others, \n"
            "it is by standing upon the shoulders of giants.",
            color=BLUE,
        ).scale(0.75)
        box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

        t2 = Tex(r"Hello World").scale(1.5)
        box2 = SurroundingRectangle(t2, corner_radius=0.2)
        mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
        self.add(title, mobjects)
```

Copy to clipboard

Make interactive

Methods

|
|

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

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **buff** ( _float_)

- **corner\_radius** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _\*mobjects_, _color=ManimColor('#FFFF00')_, _buff=0.1_, _corner\_radius=0.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **buff** ( _float_)

- **corner\_radius** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)