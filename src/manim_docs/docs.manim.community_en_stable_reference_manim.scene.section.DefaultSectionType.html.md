---
url: "https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html"
title: "DefaultSectionType - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# DefaultSectionType [¶](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html\#defaultsectiontype "Link to this heading")

Qualified name: `manim.scene.section.DefaultSectionType`

_class_ DefaultSectionType( _value_, _names=<notgiven>_, _\*values_, _module=None_, _qualname=None_, _type=None_, _start=1_, _boundary=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/section.html#DefaultSectionType) [¶](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html#manim.scene.section.DefaultSectionType "Link to this definition")

Bases: `str`, `Enum`

The type of a section can be used for third party applications.
A presentation system could for example use the types to created loops.

Examples

This class can be reimplemented for more types:

```
class PresentationSectionType(str, Enum):
    # start, end, wait for continuation by user
    NORMAL = "presentation.normal"
    # start, end, immediately continue to next section
    SKIP = "presentation.skip"
    # start, end, restart, immediately continue to next section when continued by user
    LOOP = "presentation.loop"
    # start, end, restart, finish animation first when user continues
    COMPLETE_LOOP = "presentation.complete_loop"
```

Copy to clipboard

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `NORMAL` |  |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.scene.section.DefaultSectionType.html)[hi](https://docs.manim.community/hi/stable/reference/manim.scene.section.DefaultSectionType.html)[sv](https://docs.manim.community/sv/stable/reference/manim.scene.section.DefaultSectionType.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.scene.section.DefaultSectionType.html)**[stable](https://docs.manim.community/en/stable/reference/manim.scene.section.DefaultSectionType.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.scene.section.DefaultSectionType.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.scene.section.DefaultSectionType.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.scene.section.DefaultSectionType.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.scene.section.DefaultSectionType.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.scene.section.DefaultSectionType.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.scene.section.DefaultSectionType.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.scene.section.DefaultSectionType.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.scene.section.DefaultSectionType.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)