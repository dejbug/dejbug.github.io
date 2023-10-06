# Balance

"""
Thus to foresee the modification of the hierarchy of strategic factors is nothing other than to be able to define critical positions.
--- Iossif Dorfman
"""

# Lichess

Put this into the URL field of a bookmark and put the bookmark on the toolbar. Click it when you're playing/watching games on Lichess.

```js
javascript:(() => {
	document.querySelectorAll(".time")
		.forEach(e => e.style.display="none");
	document.querySelectorAll(".bar")
		.forEach(e => e.style.backgroundColor="grey")
})()
```

It will make the board somewhat more distraction-free by removing the redundantly big clocks and dimming the bars. The following will dim the whole page.

```js
javascript:(() => {
	const style = document.body.style;
	style.filter = style.filter ? "" : "brightness(.7)"
})();
```

# Profiles

Instead of their names, I wanted to show a little photo of each player in the seatings view of the still #todo swiss pairer. Since we don't really do photos at our club, I decided to finally jump on the generative AI bandwagon and try to talk up a couple visual approximations in lieu of the actual facial facsimiles. https://deepai.org But writing prompts is a minor artform. https://en.wikipedia.org/wiki/Prompt_engineering https://arxiv.org/abs/2309.16797 One of our players has a Santa beard so I started with this low hanging fruit. Alas, to sobering results. Once you've said "Santa" it's difficult to get him to wear anything but Santa clothes. "Santa in plaids..." got me nowhere. "Homeless Santa..."? Zilch. It's the full Santa or bust. Could be Santa is a package deal?

https://stablehorde.net/
https://github.com/Haidra-Org/AI-Horde/blob/main/FAQ.md
https://dbzer0.com/blog/the-kudos-based-economy-for-the-koboldai-horde/

https://deepai.org/machine-learning-model/abstract-painting-generator

https://docs.midjourney.com/docs/quick-start

https://en.wikipedia.org/wiki/Stable_Diffusion
https://github.com/invoke-ai/InvokeAI

https://www.howtogeek.com/830179/how-to-run-stable-diffusion-on-your-pc-to-generate-ai-images/

https://www.howtogeek.com/830870/best-ai-image-generators/
https://www.howtogeek.com/830211/stable-diffusion-brings-local-ai-art-generation-to-your-pc/

https://github.com/steven2358/awesome-generative-ai
https://github.com/XingangPan/DragGAN

https://github.com/filipecalegario/awesome-generative-ai

https://en.wikipedia.org/wiki/Generative_artificial_intelligence
https://en.wikipedia.org/wiki/Artificial_intelligence_art
https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2tre_D%27op%C3%A9ra_Spatial
https://en.wikipedia.org/wiki/Technological_unemployment

https://en.wikipedia.org/wiki/Chiaroscuro
https://en.wikipedia.org/wiki/Intaglio_(printmaking)

https://www.deeplearning.ai/courses/generative-ai-with-llms/
https://github.com/huggingface/diffusion-models-class
https://www.udacity.com/course/deep-learning-pytorch--ud188
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
https://huggingface.co/

# GNU

"""
In most cases, it is a bad idea to take advantage of this feature.
--- GCC Manual: "Self-Referential-Macros" https://gcc.gnu.org/onlinedocs/cpp/Self-Referential-Macros.html
"""

# Interalia

Here's a snapshot of my .gitconfig. Writing comments is the difficult part. So I quit writing them.

```conf
[alias]
    a   = add
    aaa = add --all
    s  = status -s -uall
    s- = status -s
#   ....
	ignored      = "ls-files -o"
	ignored-     = "ls-files -o --directory"
	ignored--    = "ls-files -o --directory --no-empty-directory"
	tracked      = "ls-files -c"
#	modified     = "ls-files -m"
	modified     = "! git s  --porcelain | sed -En '/^.[^ ?]/s/.*? (.*)$/\\1/p'"
	modified-    = "! git s- --porcelain | sed -En '/^.[^ ?]/s/.*? (.*)$/\\1/p'"
	re-modified  = "! git s  --porcelain | sed -En '/^[^ ?][^ ?]/s/.*? (.*)$/\\1/p'"
	re-modified- = "! git s- --porcelain | sed -En '/^[^ ?][^ ?]/s/.*? (.*)$/\\1/p'"
	untracked    = "! git s  --porcelain | sed -En '/^[?][?]/s/.*? (.*)$/\\1/p'"
	untracked-   = "! git s- --porcelain | sed -En '/^[?][?]/s/.*? (.*)$/\\1/p'"
	staged       = "! git s  --porcelain | sed -En '/^[^ ?]./s/.*? (.*)$/\\1/p'"
	staged-      = "! git s- --porcelain | sed -En '/^[^ ?]./s/.*? (.*)$/\\1/p'"
	not-staged   = "! git s  --porcelain | sed -En '/^[ ?]./s/.*? (.*)$/\\1/p'"
	not-staged-  = "! git s- --porcelain | sed -En '/^[ ?]./s/.*? (.*)$/\\1/p'"
	su           = untracked    # not tracked, not ignored
	su-          = untracked-   # not tracked, not ignored (compact folder)
	sm           = modified     # modified, not staged
	sm-          = modified-    # modified, not staged (compact folder)
	ss           = staged       # staged, not modified since
	ss-          = staged-      # staged, not modified since (compact folder)
	sr           = re-modified  # staged, modified since
	sr-          = re-modified- # staged, modified since (compact folder)
	sn           = not-staged   # inverse of "ss"
	sn-          = not-staged-  # inverse of "ss-"
# Unstage staged files.
	unstage = "! for f in `git staged`; do git restore --staged -- $f; done"
# Stage all tracked but modified files.
	aa      = "! for f in `git modified`; do git a -- $f; done"
# Stage only the staged files that were modified since.
	aa-     = "! for f in `git mod-staged`; do git a -- $f; done"
	restage = aa-
```

"""
Please, please!  No more!  We shall find a shrubbery.
--- MPatHG https://sacred-texts.com/neu/mphg/mphg.htm
"""

# Porphyrian Tree

https://en.wikipedia.org/wiki/Porphyrian_tree

```
      all files
            \
         git files
          /     \
   untracked   tracked
        /         \
  ignored         modified
                    \
                    staged
                      \
                      re-modified
```

^^^
[:wilted!:]
^^^

A #stream of bits your life compiles /
Substrings of which you call your #files /
Subsets of #which you'll #track with git /
The world's a stage #you can't commit

# bbpPairings-wagi

It will be a minor challenge to remove all exception handling. Maybe `longjmp`. Using `std::optional` might not be enough. We might need to fallback on `std::pair` and some long error code enum in an `--include globals.h`. But rewriting everything will have the side-effect of getting to fully understand the code, which I wanted to avoid since all I need is a quick tool. I wasn't planning on becoming an expert on this particular subset of the universe. Neither does it's coding style appeal to me, not particularly.

# Exceptions

https://emscripten.org/docs/porting/files/index.html
https://emscripten.org/docs/porting/exceptions.html

https://github.com/WebAssembly/exception-handling/blob/master/proposals/exception-handling/Exceptions.md

https://webassembly.org/roadmap/
https://developer.mozilla.org/en-US/docs/WebAssembly

# Todo

https://github.com/pyodide/pyodide
https://pyodide.org/en/stable/console.html
https://pyodide.org/en/stable/usage/sdl.html

https://www.pygame.org/docs/

https://stackoverflow.com/questions/23934370/pygame-on-android
https://stackoverflow.com/questions/101754/is-there-a-way-to-run-python-on-android

https://github.com/damonkohler/sl4a

https://kivy.org/

https://github.com/kivy/python-for-android
https://python-for-android.readthedocs.io/en/latest/quickstart/
https://python-for-android.readthedocs.io/en/latest/buildoptions/#bootstrap-build-options

https://github.com/py-sdl/py-sdl2

http://nightly.renpy.org/current/

https://love2d.org/
https://love2d.org/wiki/Game_Distribution
https://github.com/love2d/love/releases/latest
https://github.com/love2d/love-android
https://github.com/love2d/love-android/wiki
https://github.com/love2d/love-android/wiki/Game-Packaging#how-to-package-the-apk-with-your-own-l%C3%96ve-game

https://github.com/love2d/love/releases/download/11.4/love-11.4-android-src.tar.gz
https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk
https://github.com/love2d/love/releases/download/11.4/love-11.4-linux-src.tar.gz
https://github.com/love2d/love/releases/download/11.4/love-11.4-x86_64.AppImage

https://github.com/love-actions

https://github.com/TannerRogalsky/love.js
https://github.com/Davidobot/love.js

https://github.com/pfirsich/makelove

Android SDK (exactly API 31 for 11.4)
Android NDK (exactly version 21.3.6528147 or r21d for 11.4).

API Levels https://developer.android.com/tools/releases/platforms

https://github.com/AppImage/AppImageKit
https://appimage.github.io/apps/

# You take the high road

https://github.com/libsdl-org/highway


# Synthaera

""Bop - Lucid Dreaming (feat. Elsa Esmeralda)""
https://www.youtube.com/watch?v=fBWB6YTrdjM
""Lapalux - Flower""
https://www.youtube.com/watch?v=xbWBHKjHzuk
""Shiny Objects - Outerlimits""
https://www.youtube.com/watch?v=hhN0QmGQiFY
""Kodak To Graph - Zagroz""
https://www.youtube.com/watch?v=41N2F_h6hsk
""Machinedrum - Infinite Us""
https://www.youtube.com/watch?v=u5BPgKB58Xs
""Audiokonstrukte - Dusty Atmosphere""
https://www.youtube.com/watch?v=F6yWqQ1qLBM
""Trentemoller & Trentemoller - Silver Surfer, Ghost Rider Go !!! (Andrew Weatherall Prinz Mix)""
https://www.youtube.com/watch?v=PLORIXoBSrU
""Martin Sturtzer - Third Planet""
https://www.youtube.com/watch?v=UeLTpCgraC0
""Ascendant - Radiance""
https://www.youtube.com/watch?v=8eqO61wqF48
""One Arc Degree - Jellyfish Ballet - The Glow Beneath""
https://www.youtube.com/watch?v=ctxrmk_7vl8
""Spinnet - Centroid""
https://www.youtube.com/watch?v=zEnUwpCfas0

"""
If for one of the players the static balance is negative, he must without hesitation employ dynamic means and be ready to go in for extreme measures.
--- Iossif Dorfman
"""

! --color-title=#afe
! --color-status-1=#58cc8f
! --color-purple-haze-text=navajowhite
