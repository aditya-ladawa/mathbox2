---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html"
title: "BraceLabel - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# BraceLabel [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html\#bracelabel "Link to this heading")

Qualified name: `manim.mobject.svg.brace.BraceLabel`

_class_ BraceLabel( _obj_, _text_, _brace\_direction=array(\[0._, _-1._, _0.\])_, _label\_constructor=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _font\_size=48_, _buff=0.2_, _brace\_config=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html#BraceLabel) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#manim.mobject.svg.brace.BraceLabel "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Create a brace with a label attached.

Parameters:

- **obj** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject adjacent to which the brace is placed.

- **text** ( _str_) – The label text.

- **brace\_direction** ( _np.ndarray_) – The direction of the brace. By default `DOWN`.

- **label\_constructor** ( _type_) – A class or function used to construct a mobject representing
the label. By default [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **font\_size** ( _float_) – The font size of the label, passed to the `label_constructor`.

- **buff** ( _float_) – The buffer between the mobject and the brace.

- **brace\_config** ( _dict_ _\|_ _None_) – Arguments to be passed to [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace").

- **kwargs** – Additional arguments to be passed to [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


Methods

|     |     |
| --- | --- |
| `change_brace_label` |  |
| `change_label` |  |
| `creation_anim` |  |
| `shift_brace` |  |

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

\_original\_\_init\_\_( _obj_, _text_, _brace\_direction=array(\[0._, _-1._, _0.\])_, _label\_constructor=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _font\_size=48_, _buff=0.2_, _brace\_config=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#manim.mobject.svg.brace.BraceLabel._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **obj** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **text** ( _str_)

- **brace\_direction** ( _ndarray_)

- **label\_constructor** ( _type_)

- **font\_size** ( _float_)

- **buff** ( _float_)

- **brace\_config** ( _dict_ _\|_ _None_)


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.svg.brace.BraceLabel.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.svg.brace.BraceLabel.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.svg.brace.BraceLabel.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.svg.brace.BraceLabel.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.svg.brace.BraceLabel.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.svg.brace.BraceLabel.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)