---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html"
title: "StealthTip - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# StealthTip [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html\#stealthtip "Link to this heading")

Qualified name: `manim.mobject.geometry.tips.StealthTip`

_class_ StealthTip( _fill\_opacity=1_, _stroke\_width=3_, _length=0.175_, _start\_angle=3.141592653589793_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/tips.html#StealthTip) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip "Link to this definition")

Bases: [`ArrowTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")

‘Stealth’ fighter / kite arrow shape.

Naming is inspired by the corresponding
[TikZ arrow shape](https://tikz.dev/tikz-arrows#sec-16.3).

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `base` | The base point of the arrow tip. |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| [`length`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip.length "manim.mobject.geometry.tips.StealthTip.length") | The length of the arrow tip. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `tip_angle` | The angle of the arrow tip. |
| `tip_point` | The tip point of the arrow tip. |
| `vector` | The vector pointing from the base point to the tip point. |
| `width` | The width of the mobject. |

Parameters:

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **length** ( _float_)

- **start\_angle** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _fill\_opacity=1_, _stroke\_width=3_, _length=0.175_, _start\_angle=3.141592653589793_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **length** ( _float_)

- **start\_angle** ( _float_)

- **kwargs** ( _Any_)


_property_ length _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip.length "Link to this definition")

The length of the arrow tip.

In this case, the length is computed as the height of
the triangle encompassing the stealth tip (otherwise,
the tip is scaled too large).

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.tips.StealthTip.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.tips.StealthTip.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.tips.StealthTip.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.tips.StealthTip.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.tips.StealthTip.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.tips.StealthTip.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)