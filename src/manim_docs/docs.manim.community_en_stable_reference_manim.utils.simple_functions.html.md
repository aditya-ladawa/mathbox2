---
url: "https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html"
title: "simple_functions - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# simple\_functions [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html\#module-manim.utils.simple_functions "Link to this heading")

A collection of simple functions.

TypeVar’s

_class_ ComparableT [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.ComparableT "Link to this definition")

```
TypeVar('ComparableT', bound=Comparable)
```

Copy to clipboard

Classes

|     |     |
| --- | --- |
| [`Comparable`](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.Comparable.html#manim.utils.simple_functions.Comparable "manim.utils.simple_functions.Comparable") |  |

Functions

binary\_search( _function_, _target_, _lower\_bound_, _upper\_bound_, _tolerance=0.0001_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html#binary_search) [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.binary_search "Link to this definition")

Searches for a value in a range by repeatedly dividing the range in half.

To be more precise, performs numerical binary search to determine the
input to `function`, between the bounds given, that outputs `target`
to within `tolerance` (default of 0.0001).
Returns `None` if no input can be found within the bounds.

Examples

Consider the polynomial x2+3x+1 where we search for
a target value of 11. An exact solution is x=2.

```
>>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5)
>>> bool(abs(solution - 2) < 1e-4)
True
>>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5, tolerance=0.01)
>>> bool(abs(solution - 2) < 0.01)
True
```

Copy to clipboard

Searching in the interval \[0,5\] for a target value of 71
does not yield a solution:

```
>>> binary_search(lambda x: x**2 + 3*x + 1, 71, 0, 5) is None
True
```

Copy to clipboard

Parameters:

- **function** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **target** ( _float_)

- **lower\_bound** ( _float_)

- **upper\_bound** ( _float_)

- **tolerance** ( _float_)


Return type:

float \| None

choose( _n_, _k_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html#choose) [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.choose "Link to this definition")

The binomial coefficient n choose k.

(nk) describes the number of possible choices of
k elements from a set of n elements.

References

- [https://en.wikipedia.org/wiki/Combination](https://en.wikipedia.org/wiki/Combination)

- [https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html)


Parameters:

- **n** ( _int_)

- **k** ( _int_)


Return type:

int

clip( _a_, _min\_a_, _max\_a_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html#clip) [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.clip "Link to this definition")

Clips `a` to the interval \[`min_a`, `max_a`\].

Accepts any comparable objects (i.e. those that support <, >).
Returns `a` if it is between `min_a` and `max_a`.
Otherwise, whichever of `min_a` and `max_a` is closest.

Examples

```
>>> clip(15, 11, 20)
15
>>> clip('a', 'h', 'k')
'h'
```

Copy to clipboard

Parameters:

- **a** ( [_ComparableT_](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))

- **min\_a** ( [_ComparableT_](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))

- **max\_a** ( [_ComparableT_](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT"))


Return type:

[_ComparableT_](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.ComparableT "manim.utils.simple_functions.ComparableT")

sigmoid( _x_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/simple_functions.html#sigmoid) [¶](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#manim.utils.simple_functions.sigmoid "Link to this definition")

Returns the output of the logistic function.

The logistic function, a common example of a sigmoid function, is defined
as 11+e−x.

References

- [https://en.wikipedia.org/wiki/Sigmoid\_function](https://en.wikipedia.org/wiki/Sigmoid_function)

- [https://en.wikipedia.org/wiki/Logistic\_function](https://en.wikipedia.org/wiki/Logistic_function)


Parameters:

**x** ( _float_)

Return type:

float

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.simple_functions.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.simple_functions.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.simple_functions.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.simple_functions.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.simple_functions.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.simple_functions.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.simple_functions.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.simple_functions.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.simple_functions.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.simple_functions.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.simple_functions.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.simple_functions.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)