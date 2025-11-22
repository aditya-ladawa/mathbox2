---
url: "https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html"
title: "HSV - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# HSV [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html\#hsv "Link to this heading")

Qualified name: `manim.utils.color.core.HSV`

_class_ HSV( _hsv_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#HSV) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "Link to this definition")

Bases: [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

HSV Color Space

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `h` |  |
| `hue` |  |
| `s` |  |
| `saturation` |  |
| `v` |  |
| `value` |  |

Parameters:

- **hsv** ( [_HSV\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSV_Array_Float "manim.typing.HSV_Array_Float") _\|_ [_HSV\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSV_Tuple_Float "manim.typing.HSV_Tuple_Float") _\|_ [_HSVA\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSVA_Array_Float "manim.typing.HSVA_Array_Float") _\|_ [_HSVA\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSVA_Tuple_Float "manim.typing.HSVA_Tuple_Float"))

- **alpha** ( _float_)


_classmethod_\_from\_internal( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#HSV._from_internal) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV._from_internal "Link to this definition")

This method is intended to be overwritten by custom color space classes
which are subtypes of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

The method constructs a new object of the given class by transforming the value
in the internal format `[r,g,b,a]` into a format which the constructor of the
custom class can understand. Look at [`HSV`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "manim.utils.color.core.HSV") for an example.

Parameters:

**value** ( [_ManimColorInternal_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal"))

Return type:

_Self_

_property_\_internal\_space _:ndarray\[tuple\[int,...\],dtype\[\_ScalarType\_co\]\]_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV._internal_space "Link to this definition")

This is a readonly property which is a custom representation for color space
operations. It is used for operators and can be used when implementing a custom
color space.

_property_\_internal\_value _: [ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV._internal_value "Link to this definition")

Return the internal value of the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") as an
`[r,g,b,a]` float array.

Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.color.core.HSV.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.color.core.HSV.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.color.core.HSV.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.color.core.HSV.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.color.core.HSV.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.color.core.HSV.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.color.core.HSV.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.color.core.HSV.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.color.core.HSV.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.color.core.HSV.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.color.core.HSV.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.color.core.HSV.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)