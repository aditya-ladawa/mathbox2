---
url: "https://docs.manim.community/en/stable/reference/manim._config.html"
title: "_config - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim._config.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim._config.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# \_config [¶](https://docs.manim.community/en/stable/reference/manim._config.html\#module-manim._config "Link to this heading")

Set the global config and logger.

Functions

tempconfig( _temp_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config.html#tempconfig) [¶](https://docs.manim.community/en/stable/reference/manim._config.html#manim._config.tempconfig "Link to this definition")

Context manager that temporarily modifies the global `config` object.

Inside the `with` statement, the modified config will be used. After
context manager exits, the config will be restored to its original state.

Parameters:

**temp** ( [_ManimConfig_](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") _\|_ _dict_ _\[_ _str_ _,_ _Any_ _\]_) – Object whose keys will be used to temporarily update the global
`config`.

Return type:

_Generator_\[None, None, None\]

Examples

Use `with tempconfig({...})` to temporarily change the default values of
certain config options.

```
>>> config["frame_height"]
8.0
>>> with tempconfig({"frame_height": 100.0}):
...     print(config["frame_height"])
100.0
>>> config["frame_height"]
8.0
```

Copy to clipboard

Languages**[en](https://docs.manim.community/en/stable/reference/manim._config.html)**[fr](https://docs.manim.community/fr/stable/reference/manim._config.html)[hi](https://docs.manim.community/hi/stable/reference/manim._config.html)[sv](https://docs.manim.community/sv/stable/reference/manim._config.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim._config.html)**[stable](https://docs.manim.community/en/stable/reference/manim._config.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim._config.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim._config.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim._config.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim._config.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim._config.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim._config.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim._config.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim._config.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)