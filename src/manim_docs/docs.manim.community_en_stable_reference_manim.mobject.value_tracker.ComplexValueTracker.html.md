---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html"
title: "ComplexValueTracker - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ComplexValueTracker [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html\#complexvaluetracker "Link to this heading")

Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`

_class_ ComplexValueTracker( _value=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html#ComplexValueTracker) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker "Link to this definition")

Bases: [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

Tracks a complex-valued parameter.

When the value is set through `animate`, the value will take a straight path from the
source point to the destination point.

Examples

Example: ComplexValueTrackerExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#complexvaluetrackerexample)

```
from manim import *

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_value`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker.get_value "manim.mobject.value_tracker.ComplexValueTracker.get_value") | Get the current value of this value tracker as a complex number. |
| [`set_value`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker.set_value "manim.mobject.value_tracker.ComplexValueTracker.set_value") | Sets a new complex value to the ComplexValueTracker |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _value=0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

get\_value() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html#ComplexValueTracker.get_value) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker.get_value "Link to this definition")

Get the current value of this value tracker as a complex number.

The value is internally stored as a points array \[a, b, 0\]. This can be accessed directly
to represent the value geometrically, see the usage example.

set\_value( _z_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/value_tracker.html#ComplexValueTracker.set_value) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html#manim.mobject.value_tracker.ComplexValueTracker.set_value "Link to this definition")

Sets a new complex value to the ComplexValueTracker

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.value_tracker.ComplexValueTracker.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.value_tracker.ComplexValueTracker.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.value_tracker.ComplexValueTracker.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)