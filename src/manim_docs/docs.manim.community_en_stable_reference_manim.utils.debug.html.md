---
url: "https://docs.manim.community/en/stable/reference/manim.utils.debug.html"
title: "debug - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# debug [¶](https://docs.manim.community/en/stable/reference/manim.utils.debug.html\#module-manim.utils.debug "Link to this heading")

Debugging utilities.

Functions

index\_labels( _mobject_, _label\_height=0.15_, _background\_stroke\_width=5_, _background\_stroke\_color=ManimColor('#000000')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/debug.html#index_labels) [¶](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#manim.utils.debug.index_labels "Link to this definition")

Returns a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") mobjects
that shows the index of each submobject.

Useful for working with parts of complicated mobjects.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject that will have its submobjects labelled.

- **label\_height** ( _float_) – The height of the labels, by default 0.15.

- **background\_stroke\_width** ( _float_) – The stroke width of the outline of the labels, by default 5.

- **background\_stroke\_color** ( [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")) – The stroke color of the outline of labels.

- **kwargs** ( _Any_) – Additional parameters to be passed into the :class\`~.Integer\`
mobjects used to construct the labels.


Return type:

[_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: IndexLabelsExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#indexlabelsexample)

![../_images/IndexLabelsExample-1.png](https://docs.manim.community/en/stable/_images/IndexLabelsExample-1.png)

```
from manim import *

class IndexLabelsExample(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=",
            "f(x)\\frac{d}{dx}g(x)",
            "+",
            "g(x)\\frac{d}{dx}f(x)",
        )

        #index the fist term in the MathTex mob
        indices = index_labels(text[0])

        text[0][1].set_color(PURPLE_B)
        text[0][8:12].set_color(DARK_BLUE)

        self.add(text, indices)
```

Copy to clipboard

Make interactive

print\_family( _mobject_, _n\_tabs=0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/debug.html#print_family) [¶](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#manim.utils.debug.print_family "Link to this definition")

For debugging purposes

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **n\_tabs** ( _int_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.debug.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.debug.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.debug.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.debug.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.debug.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.debug.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.debug.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.debug.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.debug.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.debug.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.debug.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.debug.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.debug.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.debug.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)