---
url: "https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html"
title: "autoaliasattr_directive - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# autoaliasattr\_directive [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html\#module-manim.utils.docbuild.autoaliasattr_directive "Link to this heading")

A directive for documenting type aliases and other module-level attributes.

Classes

|     |     |
| --- | --- |
| [`AliasAttrDocumenter`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter.html#manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter "manim.utils.docbuild.autoaliasattr_directive.AliasAttrDocumenter") | Directive which replaces Sphinx's Autosummary for module-level attributes: instead, it manually crafts a new "Type Aliases" section, where all the module-level attributes which are explicitly annotated as `TypeAlias` are considered as such, for their use all around the Manim docs. |

Functions

setup( _app_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/autoaliasattr_directive.html#setup) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html#manim.utils.docbuild.autoaliasattr_directive.setup "Link to this definition")Parameters:

**app** ( _Sphinx_)

Return type:

None

smart\_replace( _base_, _alias_, _substitution_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/autoaliasattr_directive.html#smart_replace) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html#manim.utils.docbuild.autoaliasattr_directive.smart_replace "Link to this definition")

Auxiliary function for substituting type aliases into a base
string, when there are overlaps between the aliases themselves.

Parameters:

- **base** ( _str_) – The string in which the type aliases will be located and
replaced.

- **alias** ( _str_) – The substring to be substituted.

- **substitution** ( _str_) – The string which will replace every occurrence of `alias`.


Returns:

The new string after the alias substitution.

Return type:

str

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.docbuild.autoaliasattr_directive.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.autoaliasattr_directive.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.docbuild.autoaliasattr_directive.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.docbuild.autoaliasattr_directive.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)