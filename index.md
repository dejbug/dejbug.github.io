# Gently

I'm rewriting known.py, the URI rewriter. It should be a bit slower by design but cleaner and a bit more powerful.

I've started using type annotations. The first type-checker I'm trying is mypy and already I've run into one or two of its bugs https://github.com/python/mypy/issues/1465 https://github.com/python/mypy/issues/9372 . I'm getting:

```
archive.py:58: error: "object" has no attribute "time"  [attr-defined]
```

with:


```
...
    @property # type: ignore
    def time(self):
        return self.year * 100000 + self.month * 100 + self.day

...
key = cmp_to_key(lambda a, b: a.time - b.time)
return sorted(seq, key = key, reverse = reverse)
```

I've even added the `test: ignore` comment as Guido suggested https://github.com/python/mypy/issues/1362 which does nothing. It doesn't look like they are going to do anything about it soon https://github.com/python/mypy/issues/1465 . So I probably need to move to another checker or, given that Guido himself seems to endorse this tool https://twitter.com/gvanrossum/status/700741601966985216 , I stop using `@property` altogether. Decisions. It's ____like having an ingrown toenail____ and thinking it'll take care of itself. A couple months of living like that and your entire gait will change; the way you navigate around potential obstacles, the way you move through your environment. My wishful-thinking had transformed the most inoccuous things into potential sources of pain that are best to be avoided. Mypy looks like that, given what grander vision it had started with https://www.slideshare.net/jukkaleh/mypy-pyconfi2012 . Wishful-thinking-wise it was powerful enough to even stop another, earlier effort in that same direction http://www.alorelang.org/ .

Damn it. I just realized the problem with mypy. The ArchLinux package is outdated (1.3.0 < 1.5.1) and was flagged https://archlinux.org/packages/extra/any/mypy/ . Ok so the PKGBUILD didn't need any changing at all apart from the obvious version and checksum. The problem with gratuitous build-time deps https://github.com/python/mypy/issues/14171 is still being handled well by the maintainer's sed scripts. But when it runs through all its self-checks (which takes forever) mypy quits with 5 fails out of 1117.

```
=================================================== short test summary info ====================================================
FAILED mypy/test/meta/test_parse_data.py::ParseTestDataSuite::test_bad_eq_version_check - AssertionError: assert 'version==3.7 always false since minimum runtime version is (3, 8)' in ''
FAILED mypy/test/meta/test_parse_data.py::ParseTestDataSuite::test_bad_ge_version_check - AssertionError: assert 'version>=3.8 always true since minimum runtime version is (3, 8)' in ''
FAILED mypy/test/meta/test_parse_data.py::ParseTestDataSuite::test_parse_invalid_case - assert "Invalid testcase id 'foo-XFAIL'" in ''
FAILED mypy/test/meta/test_parse_data.py::ParseTestDataSuite::test_parse_invalid_section - assert ".test:3: Invalid section header [unknownsection] in case 'abc'" in ''
FAILED mypy/test/meta/test_update_data.py::UpdateDataSuite::test_update_data - assert '[case testCorrect]\ns: str = 42  # E: Incompatible types in assignment (expression has type "int", variable has typ...
=============================== 5 failed, 1117 passed, 1 skipped, 2 xfailed in 775.86s (0:12:55) ===============================
```

`test_bad_eq_version_check` is the culprit https://github.com/python/mypy/blob/master/mypy/test/meta/test_parse_data.py . According to the comments it is a meta test, a test that tests the testers. I don't really need this. So:

```
$ diff PKGBUILD-1.3.0 PKGBUILD
6c6
< pkgver=1.3.0
---
> pkgver=1.5.1
21c21
< sha256sums=('e1f4d16e296f5135624b34e8fb741eb0eadedca90862405b1f1fde2040b9bd11')
---
> sha256sums=('b031b9601f1060bf1281feab89697324726ba0c0bae9d7cd7ab4b690940f0b92')
36,39c36,39
< check() {
<     cd "$pkgname-$pkgver"
<     pytest -vv -c /dev/null
< }
---
> # check() {
>     # cd "$pkgname-$pkgver"
>     # pytest -vv -c /dev/null
> # }
$ makepkg -s
# pacman -R mypy
$ pacman -U mypy-1.5.1-1-any.pkg.tar.zst
```

Now let's see about those, ahem, **other** error, yes?

```
def parseLine(line) -> list[tuple[str | None, str, str | None]]:
    ...
    return [m.groups() for m in mm]
```

Causes `known.py:60: error: List comprehension has incompatible type` ...

```
#version-1.3.0 List[Tuple[Union[str, Any], ...]]; expected List[Tuple[Optional[str], str, Optional[str]]]  [misc]
```

```
#version-1.5.1 List[tuple[str | Any, ...]]; expected List[tuple[str | None, str, str | None]]  [misc]

```

What it wants me to write is this:

```
    # return [tuple(m.groups()) for m in mm]                  # Not this.
    # return [(*m.groups(), ) for m in mm]                    # Not this.
    return [(m.group(1), m.group(2), m.group(3)) for m in mm] # This!
```

Or:

```
    def parseLine(line) -> list[tuple[str | None, ...]]:
        ...
        return [m.groups() for m in mm]
```

And this is probably where I give type annotations up https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html . Cython I actually love https://cython.org/ . But this is just not necessary https://mypy.readthedocs.io/en/stable/kinds_of_types.html . This is really for tooling, for people to have auto-completions. I don't do auto-completion anyway. One could argue that if you can't remember the API you're using everyday you should be worrying about more than tooling.

https://pypi.org/project/mypy/#files
https://mypy.readthedocs.io/en/stable/common_issues.html

https://github.com/astral-sh/ruff
https://github.com/psf/black

https://wiki.archlinux.org/title/Pacman#Removing_packages
https://wiki.archlinux.org/title/System_maintenance#Avoid_certain_pacman_commands
https://wiki.archlinux.org/title/Python_package_guidelines#Standards_based_(PEP_517)

https://docs.pytest.org/en/7.4.x/

https://github.com/google/pytype


https://peps.python.org/pep-0484/
https://docs.python.org/3/library/typing.html
https://typing.readthedocs.io/en/latest/
https://typing.readthedocs.io/en/latest/source/unreachable.html


https://adamj.eu/tech/2021/05/25/python-type-hints-specific-type-ignore/
https://realpython.com/python-type-checking/#static-type-checking

# Git

This is so useful: https://stackoverflow.com/questions/26941144/how-do-you-customize-the-color-of-the-diff-header-in-git-diff#26941235

	""" ... Colors may also be given as numbers between 0 and 255 ... https://git-scm.com/docs/git-config#Documentation/git-config.txt-color """

	""" color.diff.<slot> ... is one of ____context____ (or ____plain____), ____meta____ (metainformation), ____frag____ (hunk header), ____func____ (function in hunk header), ____old____ (removed lines), ____new____ (added lines), ____commit____ ... ____whitespace____ (highlighting whitespace errors), ____oldMoved____ (deleted lines), ____newMoved____ (added lines) ... https://git-scm.com/docs/git-config#Documentation/git-config.txt-colordiffltslotgt """

# Awesome Python

https://github.com/uhub/awesome-python

[:rocket:]

/// ""Typed (sigh) interaction with the GitHub API"" https://github.com/PyGithub/PyGithub
/// ""Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere."" https://github.com/python-poetry/poetry
/// ""Never use print() to debug again."" https://github.com/gruns/icecream
/// ""An ASGI web server, for Python."" https://github.com/encode/uvicorn
/// ""REST API framework designed for human beings "" (6.6k stars) https://github.com/pyeve/eve
/// ""It's React, but in Python (6.7k stars) "" https://github.com/reactive-python/reactpy
/// ""Simple PyTorch Tutorials Zero to ALL!"" https://github.com/hunkim/PyTorchZeroToAll
/// ""A collection of design patterns/idioms in Python]"" https://github.com/faif/python-patterns
/// ""Free (as in freedom) open source clone of the Age of Empires II engine"" https://github.com/SFTtech/openage
/// ""A Blender script to procedurally generate 3D spaceships"" https://github.com/a1studmuffin/SpaceshipGenerator
/// ""A swiss army knife for pentesting networks"" https://github.com/Porchetta-Industries/CrackMapExec
/// ""Brython (Browser Python) is an implementation of Python 3 running in the browser"" https://github.com/brython-dev/brython
/// ""Exploit Development and Reverse Engineering with GDB Made Easy"" https://github.com/pwndbg/pwndbg
/// ""A little Python library for making simple Electron-like HTML/JS GUI apps"" https://github.com/python-eel/Eel
/// ""A Python module for learning all major algorithms"" https://github.com/OmkarPathak/pygorithm
/// ""A static type analyzer for Python code"" https://github.com/google/pytype
/// ""Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed."" https://github.com/tornadoweb/tornado
/// ""Cross-platform, fast, feature-rich, GPU based terminal"" https://github.com/kovidgoyal/kitty
/// ""Project documentation with Markdown."" https://github.com/mkdocs/mkdocs
/// ""Open source UI framework written in Python, running on Windows, Linux, macOS, Android and iOS"" https://github.com/kivy/kivy
/// ""A Grammar of Graphics for Python"" https://github.com/has2k1/plotnine
/// ""A very fast and expressive template engine."" https://github.com/pallets/jinja
/// ""A lossless video/GIF/image upscaler achieved with waifu2x, Anime4K, SRMD and RealSR. Started in Hack the Valley 2, 2018."" https://github.com/k4yt3x/video2x
/// ""Every web site provides APIs."" https://github.com/gaojiuli/toapi
/// ""Selenium-python but lighter: Helium is the best Python library for web automation."" https://github.com/mherrmann/selenium-python-helium
/// ""Bittorrent software for cats"" https://github.com/nyaadevs/nyaa
/// ""Reverse engineering framework in Python"" https://github.com/cea-sec/miasm
/// ""A fully tested, abstract interface to creating OAuth clients and servers."" https://github.com/joestump/python-oauth2
/// ""Golem is creating a global market for computing power."" https://github.com/golemfactory/clay
/// ""Fast and powerful SSL/TLS scanning library."" https://github.com/nabla-c0d3/sslyze
/// ""Simple, elegant, Pythonic functional programming."" https://github.com/evhub/coconut
/// ""Data validation using Python type hints"" https://github.com/pydantic/pydantic
/// ""Typed interactions with the GitHub API v3"" https://github.com/PyGithub/PyGithub
/// ""Shadowsocks - Wikipedia"" https://en.wikipedia.org/wiki/Shadowsocks
/// ""The OpenAI Python library provides convenient access to the OpenAI API from applications written in the Python language."" https://github.com/openai/openai-python
/// ""Minimal and clean examples of machine learning algorithms implementations"" https://github.com/rushter/MLAlgorithms
/// ""PEFT: State-of-the-art Parameter-Efficient Fine-Tuning."" https://github.com/huggingface/peft
/// ""The little ASGI framework that shines."" https://github.com/encode/starlette
/// ""Computer Vision and Robotics Library for AI"" https://github.com/kornia/kornia
/// ""The LBRY SDK for building decentralized, censorship resistant, monetized, digital content apps."" https://github.com/lbryio/lbry-sdk
/// ""Python-powered, cross-platform, Unix-gazing shell."" https://github.com/xonsh/xonsh
/// ""Low code web framework for real world applications, in Python and Javascript"" https://github.com/frappe/frappe
/// ""The Web API toolkit."" https://github.com/encode/apistar
/// ""Learning to See in the Dark. CVPR 2018"" https://github.com/cchen156/Learnin
/// ""A free, online learning platform to make quality education accessible for all."" https://github.com/oppia/oppia
/// ""Create web-based user interfaces with Python. The nice way."" https://github.com/zauberzeug/nicegui
/// ""Python Koans - Learn Python through TDD"" https://github.com/gregmalcolm/python_koans
/// ""A dialect of Lisp that's embedded in Python"" https://github.com/hylang/hy
/// ""Python framework for building microservices"" https://github.com/nameko/nameko
/// ""A functional standard library for Python."" https://github.com/pytoolz/toolz
/// ""Tensorflow tutorial from basic to hard"" https://github.com/MorvanZhou/Tensorflow-Tutorial
/// ""Swagger/OpenAPI First framework for Python on top of Flask with automatic endpoint validation & OAuth2 support"" https://github.com/spec-first/connexion
/// ""A full-featured, hackable tiling window manager written and configured in Python (X11 & Wayland)"" https://github.com/qtile/qtile
/// ""A tour in the wonderland of math with python."" https://github.com/neozhaoliang/pywonderland
/// ""A next generation HTTP client for Python."" https://github.com/encode/httpx
/// ""A retro game engine for Python"" https://github.com/kitao/pyxel

# Gait

[:butterfly:]

Here's an animated picture of an Elephant just walking https://en.wikipedia.org/wiki/Gait .

! header = block
! blurb = TypePython?
