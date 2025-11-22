---
url: "https://docs.manim.community/en/stable/reference/manim.animation.transform.html"
title: "transform - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# transform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.html\#module-manim.animation.transform "Link to this heading")

Animations transforming one mobject into another.

Classes

|     |     |
| --- | --- |
| [`ApplyComplexFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyComplexFunction.html#manim.animation.transform.ApplyComplexFunction "manim.animation.transform.ApplyComplexFunction") |  |
| [`ApplyFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyFunction.html#manim.animation.transform.ApplyFunction "manim.animation.transform.ApplyFunction") |  |
| [`ApplyMatrix`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix "manim.animation.transform.ApplyMatrix") | Applies a matrix transform to an mobject. |
| [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod") | Animates a mobject by applying a method. |
| [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction") | Animation that applies a pointwise function to a mobject. |
| [`ApplyPointwiseFunctionToCenter`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter "manim.animation.transform.ApplyPointwiseFunctionToCenter") |  |
| [`ClockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html#manim.animation.transform.ClockwiseTransform "manim.animation.transform.ClockwiseTransform") | Transforms the points of a mobject along a clockwise oriented arc. |
| [`CounterclockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform "manim.animation.transform.CounterclockwiseTransform") | Transforms the points of a mobject along a counterclockwise oriented arc. |
| [`CyclicReplace`](https://docs.manim.community/en/stable/reference/manim.animation.transform.CyclicReplace.html#manim.animation.transform.CyclicReplace "manim.animation.transform.CyclicReplace") | An animation moving mobjects cyclically. |
| [`FadeToColor`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeToColor.html#manim.animation.transform.FadeToColor "manim.animation.transform.FadeToColor") | Animation that changes color of a mobject. |
| [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform") | Fades one mobject into another. |
| [`FadeTransformPieces`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces "manim.animation.transform.FadeTransformPieces") | Fades submobjects of one mobject into submobjects of another one. |
| [`MoveToTarget`](https://docs.manim.community/en/stable/reference/manim.animation.transform.MoveToTarget.html#manim.animation.transform.MoveToTarget "manim.animation.transform.MoveToTarget") | Transforms a mobject to the mobject stored in its `target` attribute. |
| [`ReplacementTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") | Replaces and morphs a mobject into a target mobject. |
| [`Restore`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#manim.animation.transform.Restore "manim.animation.transform.Restore") | Transforms a mobject to its last saved state. |
| [`ScaleInPlace`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace "manim.animation.transform.ScaleInPlace") | Animation that scales a mobject by a certain factor. |
| [`ShrinkToCenter`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#manim.animation.transform.ShrinkToCenter "manim.animation.transform.ShrinkToCenter") | Animation that makes a mobject shrink to center. |
| [`Swap`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Swap.html#manim.animation.transform.Swap "manim.animation.transform.Swap") |  |
| [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") | A Transform transforms a Mobject into a target Mobject. |
| [`TransformAnimations`](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations "manim.animation.transform.TransformAnimations") |  |
| [`TransformFromCopy`](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy "manim.animation.transform.TransformFromCopy") | Performs a reversed Transform |

Languages**[en](https://docs.manim.community/en/stable/reference/manim.animation.transform.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.animation.transform.html)[hi](https://docs.manim.community/hi/stable/reference/manim.animation.transform.html)[sv](https://docs.manim.community/sv/stable/reference/manim.animation.transform.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.animation.transform.html)**[stable](https://docs.manim.community/en/stable/reference/manim.animation.transform.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.animation.transform.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.animation.transform.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.animation.transform.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.animation.transform.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.animation.transform.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.animation.transform.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.animation.transform.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.animation.transform.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)