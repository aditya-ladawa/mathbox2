---
url: "https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html"
title: "RGBA - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# RGBA [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html\#rgba "Link to this heading")

Qualified name: `manim.utils.color.core.RGBA`

RGBA [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html#manim.utils.color.core.RGBA "Link to this definition")

RGBA Color Space

Methods

|     |     |
| --- | --- |
| `contrasting` | Return one of two colors, light or dark (by default white or black), that contrasts with the current color (depending on its luminance). |
| `darker` | Return a new color that is darker than the current color, i.e. interpolated with `BLACK`. |
| `from_hex` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from a hex string. |
| `from_hsl` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSL array. |
| `from_hsv` | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSV array. |
| `from_rgb` | Create a ManimColor from an RGB array. |
| `from_rgba` | Create a ManimColor from an RGBA Array. |
| `gradient` | This method is currently not implemented. |
| `interpolate` | Interpolate between the current and the given [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"), and return the result. |
| `into` | Convert the current color into a different colorspace given by `class_type`, without changing the `_internal_value`. |
| `invert` | Return a new, linearly inverted version of this [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") (no inplace changes). |
| `lighter` | Return a new color that is lighter than the current color, i.e. interpolated with `WHITE`. |
| `opacity` | Create a new [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the given opacity and the same color values as before. |
| `parse` | Parse one color as a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") or a sequence of colors as a list of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")'s. |
| `to_hex` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to a hexadecimal representation of the color. |
| `to_hsl` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSL array. |
| `to_hsv` | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSV array. |
| `to_int_rgb` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of integers. |
| `to_int_rgba` | Convert the current ManimColor into an RGBA array of integers. |
| `to_int_rgba_with_alpha` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of integers. |
| `to_integer` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an integer. |
| `to_rgb` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of floats. |
| `to_rgba` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |
| `to_rgba_with_alpha` | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.color.core.RGBA.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.color.core.RGBA.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.color.core.RGBA.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.color.core.RGBA.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.color.core.RGBA.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.color.core.RGBA.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.color.core.RGBA.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.color.core.RGBA.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.color.core.RGBA.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.color.core.RGBA.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.color.core.RGBA.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.color.core.RGBA.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.color.core.RGBA.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)