---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html"
title: "Arc - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Arc [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html\#arc "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.Arc`

_class_ Arc( _radius=1.0_, _start\_angle=0_, _angle=1.5707963267948966_, _num\_components=9_, _arc\_center=array(\[0.,0.,0.\])_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Arc) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "Link to this definition")

Bases: [`TipableVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject")

A circular arc.

Examples

A simple arc of angle Pi.

Example: ArcExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#arcexample)

![../_images/ArcExample-1.png](https://docs.manim.community/en/stable/_images/ArcExample-1.png)

```
from manim import *

class ArcExample(Scene):
    def construct(self):
        self.add(Arc(angle=PI))
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc.generate_points "manim.mobject.geometry.arc.Arc.generate_points") | Initializes `points` and therefore the shape. |
| [`get_arc_center`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc.get_arc_center "manim.mobject.geometry.arc.Arc.get_arc_center") | Looks at the normals to the first two anchors, and finds their intersection points |
| `init_points` |  |
| `move_arc_center_to` |  |
| `stop_angle` |  |

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

- **radius** ( _float_ _\|_ _None_)

- **start\_angle** ( _float_)

- **angle** ( _float_)

- **num\_components** ( _int_)

- **arc\_center** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _radius=1.0_, _start\_angle=0_, _angle=1.5707963267948966_, _num\_components=9_, _arc\_center=array(\[0.,0.,0.\])_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **radius** ( _float_ _\|_ _None_)

- **start\_angle** ( _float_)

- **angle** ( _float_)

- **num\_components** ( _int_)

- **arc\_center** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Arc.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc.generate_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

None

get\_arc\_center( _warning=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Arc.get_arc_center) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc.get_arc_center "Link to this definition")

Looks at the normals to the first two
anchors, and finds their intersection points

Parameters:

**warning** ( _bool_)

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.geometry.arc.Arc.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.geometry.arc.Arc.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.geometry.arc.Arc.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.geometry.arc.Arc.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.geometry.arc.Arc.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.geometry.arc.Arc.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.geometry.arc.Arc.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.geometry.arc.Arc.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.geometry.arc.Arc.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.geometry.arc.Arc.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.geometry.arc.Arc.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.geometry.arc.Arc.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)