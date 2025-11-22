---
url: "https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html"
title: "TypeWithCursor - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# TypeWithCursor [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html\#typewithcursor "Link to this heading")

Qualified name: `manim.animation.creation.TypeWithCursor`

_class_ TypeWithCursor( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#TypeWithCursor) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor "Link to this definition")

Bases: [`AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")

Similar to [`AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter") , but with an additional cursor mobject at the end.

Parameters:

- **time\_per\_char** ( _float_) – Frequency of appearance of the letters.

- **cursor** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") shown after the last added letter.

- **buff** ( _float_) – Controls how far away the cursor is to the right of the last added letter.

- **keep\_cursor\_y** ( _bool_) – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.

- **leave\_cursor\_on** ( _bool_) – Whether to show the cursor after the animation.

- **tip::** ( _.._) – This is currently only possible for class:~.Text and not for class:~.MathTex.

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))


Examples

Example: InsertingTextExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#insertingtextexample)

```
from manim import *

class InsertingTextExample(Scene):
    def construct(self):
        text = Text("Inserting", color=PURPLE).scale(1.5).to_edge(LEFT)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor

        self.play(TypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))
```

Copy to clipboard

Make interactive

References: [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "manim.animation.indication.Blink")

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.begin "manim.animation.creation.TypeWithCursor.begin") | Begin the animation. |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.clean_up_from_scene "manim.animation.creation.TypeWithCursor.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.finish "manim.animation.creation.TypeWithCursor.finish") | Finish the animation. |
| `update_submobject_list` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _text_, _cursor_, _buff=0.1_, _keep\_cursor\_y=True_, _leave\_cursor\_on=True_, _time\_per\_char=0.1_, _reverse\_rate\_function=False_, _introducer=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **cursor** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **buff** ( _float_)

- **keep\_cursor\_y** ( _bool_)

- **leave\_cursor\_on** ( _bool_)

- **time\_per\_char** ( _float_)


Return type:

None

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#TypeWithCursor.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#TypeWithCursor.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#TypeWithCursor.finish) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor.finish "Link to this definition")

Finish the animation.

This method gets called when the animation is over.

Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.creation.TypeWithCursor.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.creation.TypeWithCursor.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.creation.TypeWithCursor.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.creation.TypeWithCursor.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.creation.TypeWithCursor.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.creation.TypeWithCursor.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.creation.TypeWithCursor.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.creation.TypeWithCursor.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.creation.TypeWithCursor.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.creation.TypeWithCursor.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.creation.TypeWithCursor.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.creation.TypeWithCursor.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.creation.TypeWithCursor.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)