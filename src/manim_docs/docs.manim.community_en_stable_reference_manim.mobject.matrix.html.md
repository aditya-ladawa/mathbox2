---
url: "https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html"
title: "matrix - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# matrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html\#module-manim.mobject.matrix "Link to this heading")

Mobjects representing matrices.

Examples

Example: MatrixExamples [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#matrixexamples)

![../_images/MatrixExamples-1.png](https://docs.manim.community/en/stable/_images/MatrixExamples-1.png)

```
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket=r"\{",
            right_bracket=r"\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],\
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)
```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`DecimalMatrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html#manim.mobject.matrix.DecimalMatrix "manim.mobject.matrix.DecimalMatrix") | A mobject that displays a matrix with decimal entries on the screen. |
| [`IntegerMatrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.IntegerMatrix.html#manim.mobject.matrix.IntegerMatrix "manim.mobject.matrix.IntegerMatrix") | A mobject that displays a matrix with integer entries on the screen. |
| [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix") | A mobject that displays a matrix on the screen. |
| [`MobjectMatrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix "manim.mobject.matrix.MobjectMatrix") | A mobject that displays a matrix of mobject entries on the screen. |

Functions

get\_det\_text( _matrix_, _determinant=None_, _background\_rect=False_, _initial\_scale\_factor=2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#get_det_text) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#manim.mobject.matrix.get_det_text "Link to this definition")

Helper function to create determinant.

Parameters:

- **matrix** ( [_Matrix_](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")) – The matrix whose determinant is to be created

- **determinant** ( _int_ _\|_ _str_ _\|_ _None_) – The value of the determinant of the matrix

- **background\_rect** ( _bool_) – The background rectangle

- **initial\_scale\_factor** ( _float_) – The scale of the text det w.r.t the matrix


Returns:

A VGroup containing the determinant

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: DeterminantOfAMatrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#determinantofamatrix)

![../_images/DeterminantOfAMatrix-1.png](https://docs.manim.community/en/stable/_images/DeterminantOfAMatrix-1.png)

```
from manim import *

class DeterminantOfAMatrix(Scene):
    def construct(self):
        matrix = Matrix([\
            [2, 0],\
            [-1, 1]\
        ])

        # scaling down the `det` string
        det = get_det_text(matrix,
                    determinant=3,
                    initial_scale_factor=1)

        # must add the matrix
        self.add(matrix)
        self.add(det)
```

Copy to clipboard

Make interactive

matrix\_to\_mobject( _matrix_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#matrix_to_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#manim.mobject.matrix.matrix_to_mobject "Link to this definition")matrix\_to\_tex\_string( _matrix_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#matrix_to_tex_string) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#manim.mobject.matrix.matrix_to_tex_string "Link to this definition")

Languages**[en](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.mobject.matrix.html)[hi](https://docs.manim.community/hi/stable/reference/manim.mobject.matrix.html)[sv](https://docs.manim.community/sv/stable/reference/manim.mobject.matrix.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.mobject.matrix.html)**[stable](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.mobject.matrix.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.mobject.matrix.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.mobject.matrix.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.mobject.matrix.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.mobject.matrix.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.mobject.matrix.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.mobject.matrix.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.mobject.matrix.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)