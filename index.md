# Link

I'm branching out again https://live-risc-v.pantheonsite.io/technical/specifications/ but I have no link register. https://en.wikipedia.org/wiki/I_Have_No_Mouth%2C_and_I_Must_Scream Tournament season is around the corner and I am definitely feeling it. The pressure to write myself some study tools for chess, rather than just go and study chess. Ego-syntonic much? https://en.wikipedia.org/wiki/Egosyntonic_and_egodystonic

# GUI

So we have an old 32-bit laptop running Windows 7 in the club and I need to put some PuppyLinux on a stick already. https://puppylinux-woof-ce.github.io/ Meanwhile I've spent a day to find a good-enough cross-platform Python GUI framework and I'm not surprised to see it's Tkinter or bust. https://wiki.python.org/moin/GuiProgramming Well, or curses, there's always curses.

## Tkinter

Long story short, I'm learning to love Tk's design. https://tcl.tk/man/tcl8.6/TkCmd/contents.htm . I'll be leaning in to commit to it for quite some while. #aside Scid https://scid.sourceforge.net/ is written in Tk so maybe that will come in handy. Those Scid guys have made design decisions that I can not comprehend. They took something simple and usable and turned it into a clickfest. That's the reason why I need my own opinionated tools.

## wxPython

I need a tournament pairer frontend https://github.com/dejbug/bbpy and was thinking of going back to wxPython https://github.com/dejbug/bbpy/blob/main/gui/w.py since, sadly, I'm more familiar with its Win32 API than GTK. Only that the GTK port of the Windows ListCtrl https://docs.wxpython.org/wx.ListCtrl.html?highlight=listctrl#wx.ListCtrl , amazingly, is utter rubbish. I had to quickly emulate a grid control with a FlexGridSizer https://docs.wxpython.org/wx.FlexGridSizer.html which of course is rubbish too. There is a real cell table in there somewhere, but I didn't like its feel. Still, here's a demo of something more powerful than what I need https://wiki.wxpython.org/GridCellChoiceEditor . More powerful often means more buggy and less portable. Docs are here https://extras.wxpython.org/wxPython4/extras/4.2.1/ . One rather disheartening detail I ran into immediately with wx on Linux is that with GTK you apparently need to put a dummy Panel in a Frame, otherwise Accelerators simply will not work! https://github.com/dejbug/dejan7/blob/master/wx/Accels.py wxPython has disappointed me too often in the past. I won't be using it again. And what's with the non-alphabetic ordering of their docs?

## Win32 API

Really, all you need is a more powerful `DrawFrameControl` https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-drawframecontrol . You can write your layout managers, your blinking cursors, your so called 'virtual lists', really anything, yourself. All you need is the look and feel. And there's text metrics https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-textmetrica . There's `ExtTextOutW` https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-exttextoutw or the slower `DrawText` https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-drawtext . The first things I look for in a new framework. I don't know why browsers do not have this still.

## PyImGUI

Well now. https://pyimgui.readthedocs.io/en/latest/guide/first-steps.html Although from curses it is just a tiny step. But let's not get overboard just yet with GPUs.

## Curses!

Curses is an option though https://github.com/dejbug/bbpy/blob/main/gui/c.py . I've really started using curses while struggling with that Tetris challenge during AOC2022 last winter https://adventofcode.com/2022/day/14 . It was my first time there and I enjoyed it way too much. Hope it runs another year. Which means I'll need to brush up on algorithms and do more leetcode https://leetcode.com/ and/or hackerrank https://www.hackerrank.com/ etc. Here's suggestions for a competetive edge https://gist.github.com/mcpower/87427528b9ba5cac6f0c679370789661 .

## Pygame

Given that I had to effectively rewrite the Grid control (steadily approaching the familiar ListCtrl REPORT mode) I stopped to ponder anyway what good a bloated framework like that was if it couldn't get this single thing I needed right and whether drawing a Grid with straightup SDL was indeed the better way forward. The question is with what to fill my working memory right now. And Pygame are still updating their wheels, even for these old machines. https://www.pygame.org/news The most recent python version running on a Windows 7 box is v3.8 https://www.python.org/downloads/release/python-386/ . Pygame has a 32-bit wheel for it, of Aug 14, 2023 vintage. https://pypi.org/project/pygame/#files . And the docs https://docs.wxpython.org/ don't have to be crawled but are available locally with `python -m pygame.docs`. Also check out **pyglet** https://github.com/pyglet/pyglet .

## PyGTK

Going straight to GTK or Qt is to be seriously pondered in the future. https://wiki.python.org/moin/PyGtk https://pygobject.readthedocs.io/en/latest/ .

https://www.gtk.org/docs/language-bindings/python/
https://www.gtk.org/docs/installations/windows/

## PyFLTK

^^^
Burning chrome ///
and midnight oil
^^^

I can't look away though when I see bare metal. FLTK soon came to mind https://www.fltk.org/ and so I searched for a Python port and sure enough there's something there as well. https://sourceforge.net/projects/pyfltk/

## Python in the back...

Web-wise I've decided to be working with a Python backend. I'll be faster with it.
https://github.com/pallets/flask/tree/2.3.x/docs
https://flask.palletsprojects.com/en/2.3.x/patterns/
https://flask.palletsprojects.com/en/2.3.x/#api-reference
https://flask.palletsprojects.com/en/2.3.x/deploying/
https://docs.gunicorn.org/en/stable/install.html .

I've spent too much time looking at backbone https://github.com/jashkenas/backbone/wiki/Backbone%2C-The-Primer and Vue and such. Who needs this, really? It's time to stick with VanillaJS and HTML5's web components. Maybe go with Svelte, later. https://svelte.dev/

# Business in the front

I was wasting too much time writing autosuggestion boxes. First in JS, so I wouldn't neglect the "leg days" (web dev). Can't say that it's my cup of noodles yet. Afterwards went back to Python. Almost went down the wrong rabbit hole there. Been looking for a fast Levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance implementation (after my naive three-liner turned out too slow for 'human name'-sized strings). This is of course just one of a couple string distance algos https://en.wikipedia.org/wiki/Edit_distance and jellyfish has you covered Python-wise. https://github.com/jamesturk/jellyfish Anything bespoke would have to be interfaced with SWIG https://swig.org/ or pure ctypes or rephrased in Cython http://docs.cython.org/en/latest/ but then I'd need a build environment on that target machine http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html . Turns out none of that is needed. A simple substring matcher does a perfect job of speeding up my tournament entries. It's almost as if each player is coming with their own three letter name mnemonic. I don't even have to think about it. This really surprised me.

# JsDoc

I like this style of documenting libraries, autogen'd from source annotations https://underscorejs.org/docs/underscore-esm.html (think doxygen for millenials https://www.doxygen.nl/index.html ). But to use the tools https://jsdoc.app/about-getting-started.html you need to use the npm package manager which I still can't get myself to do. Maybe someday and if `npm install --ignore-scripts` https://stackoverflow.com/questions/23505318/npm-disable-postinstall-script-for-package won't break dependencies. But there must be something better out there https://en.wikipedia.org/wiki/Comparison_of_documentation_generators that doesn't require you to trust https://blog.npmjs.org/post/141702881055/package-install-scripts-vulnerability an entire ecosystem of dependencies. I like my dependencies **few** and **matured**. I detest all background magic. Instead, npm reminds me of that Duchovny movie Evolution. Monsters (2012) is a better one https://www.imdb.com/title/tt1470827/ . """On balance, it’s npm’s belief that the utility of having installation scripts is greater than the risk of worms. This is a tradeoff that we will continue to evaluate. --- https://blog.npmjs.org/post/141702881055/package-install-scripts-vulnerability """ Diminuitive much?

# Home

I really want to find a web framework I like. Am not happy with our club page.

#Index
https://en.wikipedia.org/wiki/Comparison_of_JavaScript-based_web_frameworks
#Python
https://jinja.palletsprojects.com/en/3.1.x/
https://github.com/pyodide/pyodide
https://flet.dev/docs/
#JS
https://es5.github.io/
#DOM
https://zeptojs.com/
http://underscorejs.org/#template
https://github.com/lodash/lodash/wiki/FP-Guide
http://www.quasipartikel.at/data-js/
#CSS
http://getskeleton.com/#examples
https://tailwindcss.com/docs/browser-support
#MVC
https://dojotoolkit.org/documentation/tutorials/1.10/mobile/flickrview/part1/index.html
https://v2.vuejs.org/v2/guide/comparison.html
http://backbonejs.org/
https://github.com/jashkenas/backbone/wiki/Backbone%2C-The-Primer#using-views
https://github.com/gmac/backbone.containerview
#Android
https://ionicframework.com/
https://capacitorjs.com/docs/getting-started
https://capacitor.nativescript.org/installation.html
https://docs.nativescript.org/tutorial/svelte.html
#Misc
https://github.com/h5bp/html5-boilerplate#quick-start
https://github.com/h5bp/server-configs-apache
https://incubator.apache.org/projects/weex.html

# But wait, there's more...

Functional toolbelt for python  https://toolz.readthedocs.io/en/latest/ https://pypi.org/project/cytoolz/ .

"libavg allows programmers, media artists and designers to quickly develop media applications. It uses python as scripting language, is written in high-speed C++ and uses modern OpenGL for display output." https://www.libavg.de/site/

"PARI/GP is a cross platform and open-source computer algebra system designed for fast computations in number theory..." http://pari.math.u-bordeaux.fr/ .

https://kivy.org/ https://flet.dev/


# TIL

I had never heard about the QUIC protcol before https://en.wikipedia.org/wiki/QUIC . My CCNA days are obviously long past. "QUIC: A UDP-Based Multiplexed and Secure Transport" https://datatracker.ietf.org/doc/html/rfc9000 .


This needs to be looked at soon https://www.pypy.org/ .

# Closing Tabs

Some may call it escapism when it's really inspiration. Looking at old photographs. https://en.wikipedia.org/wiki/List_of_chess_grandmasters

""" He was known as "Richard the Fifth" because he often finished in fifth place in tournaments. --- https://en.wikipedia.org/wiki/Richard_Teichmann """

""" Janowski played very quickly and was known as a sharp tactician who was devastating with the bishop pair. Capablanca annotated some Janowski games with great admiration, and said, "when in form [he] is one of the most feared opponents who can exist". Capablanca noted that Janowski's greatest weakness as a player was in the endgame, and Janowski reportedly told him, "I detest the endgame." --- https://en.wikipedia.org/wiki/Dawid_Janowski """

""" He was one of the very few modern grandmasters to have employed Bird's Opening (1.f4) with any regularity, and had a long-term association with the move 1.b3, a system commonly known as Larsen's Opening or the Nimzo–Larsen Attack in his (and Aron Nimzowitsch's) honor. He played the Dutch Defence with success at a time when the opening was rarely seen at the top level. --- https://en.wikipedia.org/wiki/Bent_Larsen """ But see here: https://en.wikipedia.org/wiki/Mijo_Udov%C4%8Di%C4%87.

""" Boleslavsky, together with fellow Ukrainians Bronstein, Geller ... , turned the King's Indian Defence from a suspect variation into one of the most popular defences today. Hans Kmoch ... calls the King's Indian configuration of black pawns on c6 and d6 (especially if the d-pawn is on a semi-open file) "the Boleslavsky Wall". --- https://en.wikipedia.org/wiki/Isaac_Boleslavsky """

""" He noticed that the little girl liked to stare at glass chess pieces behind the window. He later bought his daughter her first chess set. The three-year-old was able to beat her father and grandmother after a few weeks. --- https://en.wikipedia.org/wiki/Hou_Yifan """

""" Many of Koltanowski's relatives were murdered in the Holocaust. Koltanowski survived because he happened to be on a chess tour of South America and was in Guatemala when the war broke out. In 1940, the United States Consul in Cuba saw Koltanowski giving a chess exhibition in Havana and decided to grant him a U.S. visa. Koltanowski met his wife Leah on a blind date in New York in 1944. They settled in San Francisco in 1947. --- https://en.wikipedia.org/wiki/George_Koltanowski """

"""
Since Keres lost his first four games against Botvinnik in the 1948 tournament, suspicions have sometimes been raised that Keres was forced to "throw" games to allow Botvinnik to win the championship. Chess historian Taylor Kingston investigated the available evidence and arguments, concluded that Soviet chess officials had given Keres "strong hints" that he should not hinder Botvinnik's attempt to win the World Championship, and that Botvinnik only discovered this about halfway through the tournament and reportedly protested so strongly that he angered Soviet officials
--- https://en.wikipedia.org/wiki/Paul_Keres
"""

I suffer from this.
"""
"Kotov syndrome" In Kotov's 1971 book Think Like a Grandmaster, he described a situation when a player thinks very hard for a long time in a complicated position but does not find a clear path, then, running low on time, quickly makes a poor move, often a blunder.
--- https://en.wikipedia.org/wiki/Alexander_Kotov
"""


"""
In a conversation at the event, Fischer quoted Krogius' observation that "[m]istakes are often made when a player persists in his delusions", to which Krogius replied: "Perhaps this thought guided you when you were preparing for the match? We saw a completely new Fischer in Reykjavik, very different from the old one."[3] The match was won 12½ to 8½ by Fischer.
--- https://en.wikipedia.org/wiki/Nikolai_Krogius
"""

"""
We reached a very complicated position where I was intending to sacrifice a knight. The sacrifice was not obvious; there was a large number of possible variations; but when I began to study hard and work through them, I found to my horror that nothing would come of it. Ideas piled up one after another. I would transport a subtle reply by my opponent, which worked in one case, to another situation where it would naturally prove to be quite useless. As a result my head became filled with a completely chaotic pile of all sorts of moves, and the infamous "tree of variations", from which the chess trainers recommend that you cut off the small branches, in this case spread with unbelievable rapidity.
And then suddenly, for some reason, I remembered the classic couplet by Korney Ivanović Chukovsky https://en.wikipedia.org/wiki/Korney_Chukovsky : "Oh, what a difficult job it was. To drag out of the marsh the hippopotamus." https://en.wikipedia.org/wiki/Hippopotamus_Defence ... After a lengthy consideration I admitted defeat as an engineer, and thought spitefully to myself: "Well, just let it drown!"
--- https://en.wikipedia.org/wiki/Mikhail_Tal
"""

"""
He was considered to be a brilliant attacking genius, but nevertheless played very sound chess, being less willing than Tal to complicate with unforeseeable results.
--- https://en.wikipedia.org/wiki/Leonid_Stein
"""

"""
Zaitsev had been born with a clubfoot. In 1971, he had an operation to correct the problem. Details are hard to come by, but Zaitsev died of complications from the surgery.
--- https://en.wikipedia.org/wiki/Alexander_Zaitsev_(chess_player)
"""

"""
Kurnosov was hit and killed by a motorist on 8 August 2013 at 2:45 am in his home town Chelyabinsk, aged 28.
--- https://en.wikipedia.org/wiki/Igor_Kurnosov
"""

"""
One of Gligorić's most famous games was this win against the former world champion Tigran Petrosian at the great "Tournament of Peace" held in Zagreb in 1970. It displays Gligorić's virtuosity on the Black side of the King's Indian and his willingness to play for a sacrificial attack against one of history's greatest defenders.
--- https://en.wikipedia.org/wiki/Svetozar_Gligori%C4%87
"""

"""
"It wasn't so bad in the early morning when the streets were empty, but when it got light and the crowds came out I really hated it." ... Petrosian used his rations to buy Chess Praxis by Danish grandmaster Aron Nimzowitsch, https://en.wikipedia.org/wiki/Aron_Nimzowitsch the book which Petrosian later stated had the greatest influence on him as a chess player. He also purchased The Art of Sacrifice in Chess by Rudolf Spielmann. https://en.wikipedia.org/wiki/Rudolf_Spielmann The other player to have had an early effect on Petrosian's chess was José Raúl Capablanca. https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca
--- https://en.wikipedia.org/wiki/Tigran_Petrosian
"""

"""
Bolbochán qualified to play in the Sousse interzonal but didn't participate due to the Argentine Chess Federation not having enough funds to send him.
--- https://en.wikipedia.org/wiki/Julio_Bolboch%C3%A1n

"""