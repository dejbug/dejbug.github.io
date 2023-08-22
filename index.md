# Phantoms

Happiness is waking up and nobody telling you what to do or by when to have done it. But more precisely it is waking up and immediately thinking, being able to think, about some of the many little projects you have going. It's only once you get a good, let's call it overview about a problem that the amorphous blob acquires **structure** and structure is what the mind can get to work on readily.

Happiness is having something for the mind to latch onto.

# TRF Syntax Definition

I would make the syntax file as complex as you want, but for a first version, a version that other people will be looking at and working off of maybe, it would be wise to keep things simple. So let's stick with best-practice and conventional recommendations for a minute.

	"""The scopes documented below are a recommended base set of scope names to use when creating a syntax definition. -- http://www.sublimetext.com/docs/scope_naming.html#syntax-definitions """

The `/opt/sublime_text/Packages/C++.sublime-package` zip is actually all one needs, scope-reference-wise. Morover the `syntax_test_c.c` by itself is already more than sufficient; having the same function as a painter's color palette, essentially.

So _I've moved things into their own repo_ https://github.com/dejbug/SublimeTRF and have written up what had cropped up in the README there https://github.com/dejbug/SublimeTRF/blob/main/README.md .

Ok. I've found an okay use for Sublime Text over and above the highlights. Though in the process I was frequently _wondering whether I should have worked on a **SciTE** integration instead_ .

The old way of adding syntax to SciTE is deprecated https://www.scintilla.org/SciTELexer.html in favor of Lexilla https://www.scintilla.org/LexillaDoc.html https://github.com/ScintillaOrg/lexilla . The last paragraph hints at the possibility of adding new lexers dynamically, without recompilation. Also I remember vaguely that PEG http://bford.info/packrat/ lexers used to be supported via Lua http://www.inf.puc-rio.br/~roberto/lpeg/ https://staff.fnwi.uva.nl/h.vandermeer/docs/lua/lualpeg/lpeg.html .

But the syntax highlighting is half the story. It feels like in SciTE you have more control over the editor. The code is old-school and hierarchical. And the docs are **far** superior!

	"""For languages that can not be lexed with the existing lexers, a new lexer can be coded in C++.  These can either be built into Lexilla, or put into an external module and loaded when SciTE runs. See Lexilla and the lexilla.path property. -- https://www.scintilla.org/SciTEDoc.html#NewLanguage """

# RTFM

The _Sublime Text docs are so abysmal_ that users had to write their own https://github.com/sublimetext-io/docs.sublimetext.io . Futhermore, these unofficial docs were so popular and useful to the hoi polloi that some of them were willing to pay https://app.bountysource.com/teams/st-undocs/fundraiser for it. Even though there is still much more left to write https://trello.com/b/ArLlY4X7/sublime-text-unofficial-documentation !

# Still, Sublime Text

I'm stuck with it for now. The syntax highlighter is fine. And no recompilation necessary, which was its major selling point. The auto hinting system I imagined can be realized after all, I reckon, with ViewEventListener https://www.sublimetext.com/docs/api_reference.html#sublime_plugin.ViewEventListener and (the somewhat under-documented) #Phantoms https://www.sublimetext.com/docs/api_reference.html#sublime.Phantom .

And it **does** look beautiful. With the industrial_coding theme and the Mersi color scheme.

# Auditing

Remind me to go audit all the ST packages I've installed. Mostly themes. For now I've disabled Package Control's auto-upgrade feature, just because one never knows and really there is no need to update anything with the themes I have so far. I don't particularly enjoy people being able to push self-executing code to my machine at will. Such things should be run in a sandbox, WebAssembly style.

I guess I wanted my cake and be eating it too. Pass the potatoes.

	"""A perennial plant (Solanum tuberosum) in the nightshade family that was first cultivated in South America and is widely grown for its starchy edible tubers. -- https://www.wordnik.com/words/potato """


! back=2023-08-22

! blurb=Four eggs, three cups of flour, one cup of sugar, a block of butter and some lemon juice!

! columns=2
! header=block
