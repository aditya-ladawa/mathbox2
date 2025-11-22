---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html"
title: "MathTable - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# MathTable [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html\#mathtable "Link to this heading")

Qualified name: `manim.mobject.table.MathTable`

_class_ MathTable( _table_, _element\_to\_mobject=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#MathTable) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#manim.mobject.table.MathTable "Link to this definition")

Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with LaTeX.

Examples

Example: MathTableExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#mathtableexample)

![../_images/MathTableExample-1.png](https://docs.manim.community/en/stable/_images/MathTableExample-1.png)

```
from manim import *

class MathTableExample(Scene):
    def construct(self):
        t0 = MathTable(
            [["+", 0, 5, 10],\
            [0, 0, 5, 10],\
            [2, 2, 7, 12],\
            [4, 4, 9, 14]],
            include_outer_lines=True)
        self.add(t0)
```

Copy to clipboard

Make interactive

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
Every entry in table is set in a Latex align environment.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\]_ _\]_) – A 2d array or list of lists. Content of the table have to be valid input
for [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").


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

\_original\_\_init\_\_( _table_, _element\_to\_mobject=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#manim.mobject.table.MathTable._original__init__ "Link to this definition")

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
Every entry in table is set in a Latex align environment.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\]_ _\]_) – A 2d array or list of lists. Content of the table have to be valid input
for [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.table.MathTable.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.table.MathTable.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.table.MathTable.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.table.MathTable.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.table.MathTable.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.table.MathTable.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.table.MathTable.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.table.MathTable.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.table.MathTable.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.table.MathTable.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.table.MathTable.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.table.MathTable.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)