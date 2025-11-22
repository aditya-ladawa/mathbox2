---
url: "https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html"
title: "logger_utils - Manim Community v0.19.0"
---

ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# logger\_utils [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html\#module-manim._config.logger_utils "Link to this heading")

Utilities to create and set the logger.

Manim’s logger can be accessed as `manim.logger`, or as
`logging.getLogger("manim")`, once the library has been imported. Manim also
exports a second object, `console`, which should be used to print on screen
messages that need not be logged.

Both `logger` and `console` use the `rich` library to produce rich text
format.

Classes

|     |     |
| --- | --- |
| [`JSONFormatter`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#manim._config.logger_utils.JSONFormatter "manim._config.logger_utils.JSONFormatter") | A formatter that outputs logs in a custom JSON format. |

Functions

make\_logger( _parser_, _verbosity_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html#make_logger) [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.make_logger "Link to this definition")

Make the manim logger and console.

Parameters:

- **parser** ( _SectionProxy_) – A parser containing any .cfg files in use.

- **verbosity** ( _str_) – The verbosity level of the logger.


Returns:

The manim logger and consoles. The first console outputs
to stdout, the second to stderr. All use the theme returned by
[`parse_theme()`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.parse_theme "manim._config.logger_utils.parse_theme").

Return type:

`logging.Logger`, `rich.Console`, `rich.Console`

See also

[`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html#manim._config.utils.make_config_parser "manim._config.utils.make_config_parser"), [`parse_theme()`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.parse_theme "manim._config.logger_utils.parse_theme")

Notes

The `parser` is assumed to contain only the options related to
configuring the logger at the top level.

parse\_theme( _parser_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html#parse_theme) [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.parse_theme "Link to this definition")

Configure the rich style of logger and console output.

Parameters:

**parser** ( _SectionProxy_) – A parser containing any .cfg files in use.

Returns:

The rich theme to be used by the manim logger.

Return type:

`rich.Theme`

See also

[`make_logger()`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.make_logger "manim._config.logger_utils.make_logger")

set\_file\_logger( _scene\_name_, _module\_name_, _log\_dir_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html#set_file_logger) [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html#manim._config.logger_utils.set_file_logger "Link to this definition")

Add a file handler to manim logger.

The path to the file is built using `config.log_dir`.

Parameters:

- **scene\_name** ( _str_) – The name of the scene, used in the name of the log file.

- **module\_name** ( _str_) – The name of the module, used in the name of the log file.

- **log\_dir** ( _Path_) – Path to the folder where log files are stored.


Return type:

None

Languages**[en](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html)**[fr](https://docs.manim.community/fr/stable/reference/manim._config.logger_utils.html)[hi](https://docs.manim.community/hi/stable/reference/manim._config.logger_utils.html)[sv](https://docs.manim.community/sv/stable/reference/manim._config.logger_utils.html)Versions[latest](https://docs.manim.community/en/latest/reference/manim._config.logger_utils.html)**[stable](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.html)**[v0.19.0](https://docs.manim.community/en/v0.19.0/reference/manim._config.logger_utils.html)[v0.18.1](https://docs.manim.community/en/v0.18.1/reference/manim._config.logger_utils.html)[v0.18.0.post0](https://docs.manim.community/en/v0.18.0.post0/reference/manim._config.logger_utils.html)[v0.18.0](https://docs.manim.community/en/v0.18.0/reference/manim._config.logger_utils.html)[v0.17.3](https://docs.manim.community/en/v0.17.3/reference/manim._config.logger_utils.html)[v0.17.2](https://docs.manim.community/en/v0.17.2/reference/manim._config.logger_utils.html)[v0.17.1](https://docs.manim.community/en/v0.17.1/reference/manim._config.logger_utils.html)[v0.17.0](https://docs.manim.community/en/v0.17.0/reference/manim._config.logger_utils.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/manimce/?utm_source=manimce&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/manimce/builds/?utm_source=manimce&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=manimce&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=manimce&utm_content=flyout)