---
url: "https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html"
title: "ZoomedScene - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ZoomedScene [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html\#zoomedscene "Link to this heading")

Qualified name: `manim.scene.zoomed\_scene.ZoomedScene`

_class_ ZoomedScene( _camera\_class=<class'manim.camera.multi\_camera.MultiCamera'>_, _zoomed\_display\_height=3_, _zoomed\_display\_width=3_, _zoomed\_display\_center=None_, _zoomed\_display\_corner=array(\[1._, _1._, _0.\])_, _zoomed\_display\_corner\_buff=0.5_, _zoomed\_camera\_config={'background\_opacity':1_, _'default\_frame\_stroke\_width':2}_, _zoomed\_camera\_image\_mobject\_config={}_, _zoomed\_camera\_frame\_starting\_position=array(\[0._, _0._, _0.\])_, _zoom\_factor=0.15_, _image\_frame\_stroke\_width=3_, _zoom\_activated=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene "Link to this definition")

Bases: [`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene")

This is a Scene with special configurations made for when
a particular part of the scene must be zoomed in on and displayed
separately.

Methods

|     |     |
| --- | --- |
| [`activate_zooming`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "manim.scene.zoomed_scene.ZoomedScene.activate_zooming") | This method is used to activate the zooming for the zoomed\_camera. |
| [`get_zoom_factor`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor") | Returns the Zoom factor of the Zoomed camera. |
| [`get_zoom_in_animation`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation") | Returns the animation of camera zooming in. |
| [`get_zoomed_display_pop_out_animation`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation") | This is the animation of the popping out of the mini-display that shows the content of the zoomed camera. |
| [`setup`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.setup "manim.scene.zoomed_scene.ZoomedScene.setup") | This method is used internally by Manim to setup the scene for proper use. |

Attributes

|     |     |
| --- | --- |
| `camera` |  |
| `time` | The time since the start of the scene. |

activate\_zooming( _animate=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.activate_zooming) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "Link to this definition")

This method is used to activate the zooming for
the zoomed\_camera.

Parameters:

**animate** ( _bool_) – Whether or not to animate the activation
of the zoomed camera.

get\_zoom\_factor() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_factor) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "Link to this definition")

Returns the Zoom factor of the Zoomed camera.
Defined as the ratio between the height of the
zoomed camera and the height of the zoomed mini
display.
:returns: The zoom factor.
:rtype: float

get\_zoom\_in\_animation( _run\_time=2_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_in_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "Link to this definition")

Returns the animation of camera zooming in.

Parameters:

- **run\_time** ( _float_) – The run\_time of the animation of the camera zooming in.

- **\*\*kwargs** – Any valid keyword arguments of ApplyMethod()


Returns:

The animation of the camera zooming in.

Return type:

[ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

get\_zoomed\_display\_pop\_out\_animation( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoomed_display_pop_out_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "Link to this definition")

This is the animation of the popping out of the
mini-display that shows the content of the zoomed
camera.

Returns:

The Animation of the Zoomed Display popping out.

Return type:

[ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

setup() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.setup) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.setup "Link to this definition")

This method is used internally by Manim to
setup the scene for proper use.

Languages**[en](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html)[hi](https://docs.manim.community/hi/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html)[sv](https://docs.manim.community/sv/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.scene.zoomed_scene.ZoomedScene.html)**[stable](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.scene.zoomed_scene.ZoomedScene.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.scene.zoomed_scene.ZoomedScene.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)