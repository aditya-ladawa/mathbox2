---
url: "https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html"
title: "config_ops - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# config\_ops [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html\#module-manim.utils.config_ops "Link to this heading")

Utilities that might be useful for configuration dictionaries.

Classes

|     |     |
| --- | --- |
| [`DictAsObject`](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.DictAsObject.html#manim.utils.config_ops.DictAsObject "manim.utils.config_ops.DictAsObject") |  |

Functions

merge\_dicts\_recursively( _\*dicts_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html#merge_dicts_recursively) [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#manim.utils.config_ops.merge_dicts_recursively "Link to this definition")

Creates a dict whose keyset is the union of all the
input dictionaries. The value for each key is based
on the first dict in the list with that key.

dicts later in the list have higher priority

When values are dictionaries, it is applied recursively

Parameters:

**dicts** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)

Return type:

dict\[ _Any_, _Any_\]

update\_dict\_recursively( _current\_dict_, _\*others_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html#update_dict_recursively) [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#manim.utils.config_ops.update_dict_recursively "Link to this definition")Parameters:

- **current\_dict** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)

- **others** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html)**[fr](https://docs.manim.community/fr/stable/reference/manim.utils.config_ops.html)[hi](https://docs.manim.community/hi/stable/reference/manim.utils.config_ops.html)[sv](https://docs.manim.community/sv/stable/reference/manim.utils.config_ops.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim.utils.config_ops.html)**[stable](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim.utils.config_ops.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim.utils.config_ops.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim.utils.config_ops.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim.utils.config_ops.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim.utils.config_ops.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim.utils.config_ops.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim.utils.config_ops.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim.utils.config_ops.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)