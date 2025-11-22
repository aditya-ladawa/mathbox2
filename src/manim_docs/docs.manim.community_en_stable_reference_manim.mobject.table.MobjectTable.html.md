---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html"
title: "MobjectTable - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# MobjectTable [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html\#mobjecttable "Link to this heading")

Qualified name: `manim.mobject.table.MobjectTable`

_class_ MobjectTable( _table_, _element\_to\_mobject=<functionMobjectTable.<lambda>>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#MobjectTable) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#manim.mobject.table.MobjectTable "Link to this definition")

Bases: [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Examples

Example: MobjectTableExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#mobjecttableexample)

![../_images/MobjectTableExample-1.png](https://docs.manim.community/en/stable/_images/MobjectTableExample-1.png)

```
from manim import *

class MobjectTableExample(Scene):
    def construct(self):
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT),
        )
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t0 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],\
            [b.copy(),a.copy(),a.copy()],\
            [a.copy(),b.copy(),b.copy()]]
        )
        line = Line(
            t0.get_corner(DL), t0.get_corner(UR)
        ).set_color(RED)
        self.add(t0, line)
```

Copy to clipboard

Make interactive

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with `element_to_mobject` set to an identity function.
Here, every item in `table` must already be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `lambda m : m` to return itself.

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

\_original\_\_init\_\_( _table_, _element\_to\_mobject=<functionMobjectTable.<lambda>>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#manim.mobject.table.MobjectTable._original__init__ "Link to this definition")

Special case of [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with `element_to_mobject` set to an identity function.
Here, every item in `table` must already be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `lambda m : m` to return itself.

- **kwargs** – Additional arguments to be passed to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").


Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.table.MobjectTable.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.table.MobjectTable.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.table.MobjectTable.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.table.MobjectTable.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.table.MobjectTable.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.table.MobjectTable.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.table.MobjectTable.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.table.MobjectTable.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.table.MobjectTable.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.table.MobjectTable.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.table.MobjectTable.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.table.MobjectTable.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)