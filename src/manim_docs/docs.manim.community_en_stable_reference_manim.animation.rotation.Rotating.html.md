---
url: "https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html"
title: "Rotating - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Rotating [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html\#rotating "Link to this heading")

Qualified name: `manim.animation.rotation.Rotating`

_class_ Rotating( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/rotation.html#Rotating) [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#manim.animation.rotation.Rotating "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#manim.animation.rotation.Rotating.interpolate_mobject "manim.animation.rotation.Rotating.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **axis** ( _np.ndarray_)

- **radians** ( _np.ndarray_)

- **about\_point** ( _np.ndarray_ _\|_ _None_)

- **about\_edge** ( _np.ndarray_ _\|_ _None_)

- **run\_time** ( _float_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


\_original\_\_init\_\_( _mobject_, _axis=array(\[0._, _0._, _1.\])_, _radians=6.283185307179586_, _about\_point=None_, _about\_edge=None_, _run\_time=5_, _rate\_func=<functionlinear>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#manim.animation.rotation.Rotating._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **axis** ( _np.ndarray_)

- **radians** ( _np.ndarray_)

- **about\_point** ( _np.ndarray_ _\|_ _None_)

- **about\_edge** ( _np.ndarray_ _\|_ _None_)

- **run\_time** ( _float_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/rotation.html#Rotating.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html#manim.animation.rotation.Rotating.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.rotation.Rotating.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.rotation.Rotating.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.rotation.Rotating.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.rotation.Rotating.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotating.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.rotation.Rotating.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.rotation.Rotating.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.rotation.Rotating.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.rotation.Rotating.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.rotation.Rotating.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.rotation.Rotating.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.rotation.Rotating.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.rotation.Rotating.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)