---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html"
title: "IntegerTable - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# IntegerTable [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html\#integertable "Link to this heading")

Qualified name: `manim.mobject.table.IntegerTable`

_class_ IntegerTable( _table_, _element\_to\_mobject=<class'manim.mobject.text.numbers.Integer'>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#IntegerTable) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#manim.mobject.table.IntegerTable "Link to this definition")

Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

Examples

Example: IntegerTableExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#integertableexample)

![../_images/IntegerTableExample-1.png](https://docs.manim.community/en/stable/_images/IntegerTableExample-1.png)

```
from manim import *

class IntegerTableExample(Scene):
    def construct(self):
        t0 = IntegerTable(
            [[0,30,45,60,90],\
            [90,60,45,30,0]],
            col_labels=[\
                MathTex(r"\frac{\sqrt{0}}{2}"),\
                MathTex(r"\frac{\sqrt{1}}{2}"),\
                MathTex(r"\frac{\sqrt{2}}{2}"),\
                MathTex(r"\frac{\sqrt{3}}{2}"),\
                MathTex(r"\frac{\sqrt{4}}{2}")],
            row_labels=[MathTex(r"\sin"), MathTex(r"\cos")],
            h_buff=1,
            element_to_mobject_config={"unit": r"^{\circ}"})
        self.add(t0)
```

Copy to clipboard

Make interactive

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
Will round if there are decimal entries in the table.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\]_ _\]_) – A 2d array or list of lists. Content of the table has to be valid input
for [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

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

\_original\_\_init\_\_( _table_, _element\_to\_mobject=<class'manim.mobject.text.numbers.Integer'>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#manim.mobject.table.IntegerTable._original__init__ "Link to this definition")

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
Will round if there are decimal entries in the table.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\]_ _\]_) – A 2d array or list of lists. Content of the table has to be valid input
for [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

- **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.table.IntegerTable.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.table.IntegerTable.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.table.IntegerTable.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.table.IntegerTable.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.table.IntegerTable.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.table.IntegerTable.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.table.IntegerTable.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.table.IntegerTable.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.table.IntegerTable.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.table.IntegerTable.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.table.IntegerTable.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.table.IntegerTable.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)