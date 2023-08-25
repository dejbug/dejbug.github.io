# High Light

We had a thunderstorm this morning and the air is breathable again. Some storms are more civilized than others. I like those. Nice storms. Real enough to be pleasantly disturbing on a subconscious level but not violent enough to inconvenience.

# Susurrous

The sounds are noticeably different after an **event**. Like something's missing. What is missing is the carelessness and \\arrogance\\that's right!\\ of people going through the various motions of mundane existence --- only partially coreographed but often mostly improvised. People are animals who enjoy creative freedoms. I am very much an animal like that of course and so I need to come up with a little task today. Something small enough to be finishable in a couple hours. Because tonight is chess night and I have not seriously looked at chess in weeks.

# Tasuke-te

I have been thinking about what Kernighen & Plauger wrote in the first pages of their book ""Software Tools"" (1976) and in their article of the same title:

"""
Building on the work of others is the only way to make substantial progress in any field. Yet computer programming continues as a cottage industry because programmers insist on reinventing programs for each new application, instead of using what already exists. https://dl.acm.org/doi/abs/10.1145/1010726.1010728 https://scholar.google.com/citations?view_op=view_citation&hl=en&citation_for_view=Add33R8AAAAJ:SeFeTyx0c_EC
"""

I have read something like this before.
https://www.unep.org/news-and-stories/speech/moving-throwaway-culture
https://www.oneearth.org/repair-reuse-recycle-how-britain-is-tackling-throwaway-culture/
https://en.wikipedia.org/wiki/Throw-away_society
https://en.wikipedia.org/wiki/Tragedy_of_the_commons

The thing is that we love reinventing the wheel https://en.wikipedia.org/wiki/Stovepipe_system . Given the somewhat pointless, undirected leisure that comes with long-term unemployment and if you're lucky enough to derive some pleasure from looking at screenfuls of pretty-colored text. After all, with anything a bit more complex than a wheel, it's a perfect learning experience. A perfect time-passing experience at that. And there's the nagging feeling that you may be able to do it better https://en.wikipedia.org/wiki/Anti-pattern https://en.wikipedia.org/wiki/Not_invented_here . What else are you to do with lots of time and no liquidity?

# Tools

So I've been looking through the GNU docs https://www.gnu.org/manual/manual.html and was reminded of M4 https://www.gnu.org/software/m4/manual/ but was totally surprised by https://www.gnu.org/software/src-highlite/source-highlight.html ! Obvious that I had to add it to my little quick-and-dirty render script. Remind me to take a look at the `noref` "color" https://www.gnu.org/software/src-highlite/source-highlight.html#Generating-References later #todo but first the mise-en-scene:

```shell
$ source-highlight --outlang-list | head -n 3
docbook = docbook.outlang
esc = esc.outlang
esc256 = esc256.outlang
$ expac -H M "%F" source-highlight | tr -s ' ' '\n' | xargs dirname | uniq | tail -n 3
usr/share/man/man1
usr/share
usr/share/source-highlight
$ cp /usr/share/source-highlight/default.style .
$ vim default.style
$ source-highlight --out-format=esc256 --style-file=./default.style -i known.py
```

# Actions

It seems that GNU's `source-highlight` https://www.gnu.org/software/src-highlite/source-highlight.html is not preinstalled https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software on the GH build server I use https://github.com/actions/runner-images/blob/main/images/linux/Ubuntu2204-Readme.md (Ubuntu Jammy Jellyfish). Which means back to fiddling with the workspace config. It was a bit frustrating writing one more or less blindly and it took a couple of first runs to get it right, but adding little things like this should be straight-forward. Here goes nothing!

# TIL

	""" In early aviation, the Wright brothers held patents on certain aspects of aircraft, while Glenn Curtiss held patents on ailerons https://en.wikipedia.org/wiki/Ailerons which was an advance on the Wrights' system, but antipathy between the patent holders https://en.wikipedia.org/wiki/Wright_brothers_patent_war prevented their use. The government was forced to step in and create a patent pool https://en.wikipedia.org/wiki/Patent_pool during World War I. --- https://en.wikipedia.org/wiki/Tragedy_of_the_anticommons """


	""" Initially sales were not negatively affected; in a September 1985 interview, the president of the company that manufactured it stated that, in fact, sales had increased as a result of this connection. https://en.wikipedia.org/wiki/Ayds#cite_note-10 Early in 1986, another executive of the manufacturer was quoted, "The product has been around for 45 years. Let the disease change its name." https://en.wikipedia.org/wiki/Ayds#cite_note-11 --- https://en.wikipedia.org/wiki/Ayds """


! header = block
