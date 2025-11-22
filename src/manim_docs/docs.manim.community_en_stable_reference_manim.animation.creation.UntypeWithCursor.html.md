---
url: "https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html"
title: "UntypeWithCursor - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# UntypeWithCursor [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html\#untypewithcursor "Link to this heading")

Qualified name: `manim.animation.creation.UntypeWithCursor`

_class_ UntypeWithCursor( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#UntypeWithCursor) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html#manim.animation.creation.UntypeWithCursor "Link to this definition")

Bases: [`TypeWithCursor`](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor "manim.animation.creation.TypeWithCursor")

Similar to [`RemoveTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter "manim.animation.creation.RemoveTextLetterByLetter") , but with an additional cursor mobject at the end.

Parameters:

- **time\_per\_char** ( _float_) – Frequency of appearance of the letters.

- **cursor** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _None_) – [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") shown after the last added letter.

- **buff** – Controls how far away the cursor is to the right of the last added letter.

- **keep\_cursor\_y** – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.

- **leave\_cursor\_on** – Whether to show the cursor after the animation.

- **tip::** ( _.._) – This is currently only possible for class:~.Text and not for class:~.MathTex.

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))


Examples

Example: DeletingTextExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html#deletingtextexample)

```
from manim import *

class DeletingTextExample(Scene):
    def construct(self):
        text = Text("Deleting", color=PURPLE).scale(1.5).to_edge(LEFT)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor

        self.play(UntypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))
```

Copy to clipboard

Make interactive

References: [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "manim.animation.indication.Blink")

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _text_, _cursor=None_, _time\_per\_char=0.1_, _reverse\_rate\_function=True_, _introducer=False_, _remover=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html#manim.animation.creation.UntypeWithCursor._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **cursor** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _None_)

- **time\_per\_char** ( _float_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.creation.UntypeWithCursor.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.creation.UntypeWithCursor.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.creation.UntypeWithCursor.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.creation.UntypeWithCursor.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.creation.UntypeWithCursor.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.creation.UntypeWithCursor.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.creation.UntypeWithCursor.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.creation.UntypeWithCursor.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.creation.UntypeWithCursor.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.creation.UntypeWithCursor.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.creation.UntypeWithCursor.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.creation.UntypeWithCursor.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.creation.UntypeWithCursor.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)