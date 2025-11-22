---
url: "https://docs.manim.community/en/stable/reference/manim.utils.hashing.html"
title: "hashing - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# hashing [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html\#module-manim.utils.hashing "Link to this heading")

Utilities for scene caching.

Functions

get\_hash\_from\_play\_call( _scene\_object_, _camera\_object_, _animations\_list_, _current\_mobjects\_list_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html#get_hash_from_play_call) [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#manim.utils.hashing.get_hash_from_play_call "Link to this definition")

Take the list of animations and a list of mobjects and output their hashes. This is meant to be used for scene.play function.

Parameters:

- **scene\_object** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene object.

- **camera\_object** ( [_Camera_](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera") _\|_ _OpenGLCamera_) – The camera object used in the scene.

- **animations\_list** ( _Iterable_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The list of animations.

- **current\_mobjects\_list** ( _Iterable_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The list of mobjects.


Returns:

A string concatenation of the respective hashes of camera\_object, animations\_list and current\_mobjects\_list, separated by \_.

Return type:

`str`

get\_json( _obj_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html#get_json) [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#manim.utils.hashing.get_json "Link to this definition")

Recursively serialize object to JSON using the `CustomEncoder` class.

Parameters:

**obj** ( _dict_) – The dict to flatten

Returns:

The flattened object

Return type:

`str`

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.hashing.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.hashing.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.hashing.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.hashing.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.hashing.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.hashing.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.hashing.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.hashing.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.hashing.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.hashing.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.hashing.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.hashing.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)