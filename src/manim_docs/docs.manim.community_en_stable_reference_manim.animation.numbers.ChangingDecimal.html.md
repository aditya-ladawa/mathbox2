---
url: "https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html"
title: "ChangingDecimal - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ChangingDecimal [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html\#changingdecimal "Link to this heading")

Qualified name: `manim.animation.numbers.ChangingDecimal`

_class_ ChangingDecimal( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html#ChangingDecimal) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Methods

|     |     |
| --- | --- |
| `check_validity_of_input` |  |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal.interpolate_mobject "manim.animation.numbers.ChangingDecimal.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **decimal\_mob** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))

- **number\_update\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **suspend\_mobject\_updating** ( _bool_ _\|_ _None_)


\_original\_\_init\_\_( _decimal\_mob_, _number\_update\_func_, _suspend\_mobject\_updating=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **decimal\_mob** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))

- **number\_update\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **suspend\_mobject\_updating** ( _bool_ _\|_ _None_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html#ChangingDecimal.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.numbers.ChangingDecimal.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.numbers.ChangingDecimal.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.numbers.ChangingDecimal.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.numbers.ChangingDecimal.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.numbers.ChangingDecimal.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.numbers.ChangingDecimal.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.numbers.ChangingDecimal.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.numbers.ChangingDecimal.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.numbers.ChangingDecimal.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.numbers.ChangingDecimal.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.numbers.ChangingDecimal.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.numbers.ChangingDecimal.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)