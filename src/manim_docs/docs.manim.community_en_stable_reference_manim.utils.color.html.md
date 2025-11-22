---
url: "https://docs.manim.community/en/stable/reference/manim.utils.color.html"
title: "color - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.color.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.color.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# color [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#module-manim.utils.color "Link to this heading")

Utilities for working with colors and predefined color constants.

## Color data structure [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#color-data-structure "Link to this heading")

|     |     |
| --- | --- |
| [`core`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#module-manim.utils.color.core "manim.utils.color.core") | Manim's (internal) color data structure and some utilities for color conversion. |

## Predefined colors [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#predefined-colors "Link to this heading")

There are several predefined colors available in Manim:

- The colors listed in [`color.manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors "manim.utils.color.manim_colors") are loaded into
Manim’s global name space.

- The colors in [`color.AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html#module-manim.utils.color.AS2700 "manim.utils.color.AS2700"), [`color.BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html#module-manim.utils.color.BS381 "manim.utils.color.BS381"),
[`color.DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES "manim.utils.color.DVIPSNAMES"), [`color.SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES "manim.utils.color.SVGNAMES"), [`color.X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html#module-manim.utils.color.X11 "manim.utils.color.X11") and
[`color.XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html#module-manim.utils.color.XKCD "manim.utils.color.XKCD") need to be accessed via their module (which are available
in Manim’s global name space), or imported separately. For example:





```
>>> from manim import XKCD
>>> XKCD.AVOCADO
ManimColor('#90B134')
```

Copy to clipboard



Or, alternatively:





```
>>> from manim.utils.color.XKCD import AVOCADO
>>> AVOCADO
ManimColor('#90B134')
```

Copy to clipboard


The following modules contain the predefined color constants:

|     |     |
| --- | --- |
| [`manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors "manim.utils.color.manim_colors") | Colors included in the global name space. |
| [`AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html#module-manim.utils.color.AS2700 "manim.utils.color.AS2700") | Australian Color Standard |
| [`BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html#module-manim.utils.color.BS381 "manim.utils.color.BS381") | British Color Standard |
| [`DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES "manim.utils.color.DVIPSNAMES") | dvips Colors |
| [`SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES "manim.utils.color.SVGNAMES") | SVG 1.1 Colors |
| [`XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html#module-manim.utils.color.XKCD "manim.utils.color.XKCD") | Colors from the XKCD Color Name Survey |
| [`X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html#module-manim.utils.color.X11 "manim.utils.color.X11") | X11 Colors |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.color.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.color.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.color.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.color.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.color.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.color.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.color.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.color.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.color.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.color.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.color.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.color.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.color.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.color.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)