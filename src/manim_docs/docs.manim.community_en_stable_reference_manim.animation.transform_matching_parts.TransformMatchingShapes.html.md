---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html"
title: "TransformMatchingShapes - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# TransformMatchingShapes [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html\#transformmatchingshapes "Link to this heading")

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`

_class_ TransformMatchingShapes( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html#TransformMatchingShapes) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#manim.animation.transform_matching_parts.TransformMatchingShapes "Link to this definition")

Bases: [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

An animation trying to transform groups by matching the shape
of their submobjects.

Two submobjects match if the hash of their point coordinates after
normalization (i.e., after translation to the origin, fixing the submobject
height at 1 unit, and rounding the coordinates to three decimal places)
matches.

See also

[`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

Examples

Example: Anagram [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#anagram)

```
from manim import *

class Anagram(Scene):
    def construct(self):
        src = Text("the morse code")
        tar = Text("here come dots")
        self.play(Write(src))
        self.wait(0.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait(0.5)
```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_mobject_key` |  |
| `get_mobject_parts` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **transform\_mismatches** ( _bool_)

- **fade\_transform\_mismatches** ( _bool_)

- **key\_map** ( _dict_ _\|_ _None_)


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _transform\_mismatches=False_, _fade\_transform\_mismatches=False_, _key\_map=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#manim.animation.transform_matching_parts.TransformMatchingShapes._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **transform\_mismatches** ( _bool_)

- **fade\_transform\_mismatches** ( _bool_)

- **key\_map** ( _dict_ _\|_ _None_)


Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)