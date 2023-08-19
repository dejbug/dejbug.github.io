# Fermyon! #2

This morning I notice that (again) my weforum feed fails: AssertionError: Error::Io("error trying to connect: tcp connect error: Connection timed out (os error 110)") https://atoms.fermyon.app/weforum . Testing locally worked fine so maybe "the imperfection is yours" http://transcripts.terrafirmascapers.com/104.htm http_send? https://github.com/fermyon/spin-python-sdk/issues/48

## Testing

To find more out, first I will need a way to relay requests through fermyon e.g. `curl xyz.fermyon.app/get/<url>?user-agent=X`. Sadly, this won't work. I had a lapse of memory and forgot that every app has "allowed_http_hosts" permissions hard-coded into it. Which is probably a good idea.

### Testing the tester

In any case! To run the thing locally I wanted a nice way to send it arguments on the console. Instead of e.g. `python xyz.py /get/<url>?User-Agent=X` just `python xyz.py /get -u <url> -agent X`.

The general idea is from `handle_request(request)` to call `parseRequest(request, shortopts, longopts)` and get the correct meta regardless of whether it runs *spinned* or local.

Right now I'm doing things with argparse https://docs.python.org/3/library/argparse.html which is a bit unwieldy. I long for the elegance of getopt https://www.man7.org/linux/man-pages/man1/getopt.1.html (not to be confused with getopts https://man7.org/linux/man-pages/man1/getopts.1p.html ) and found that python stdlib has it! https://docs.python.org/3/library/getopt.html This would have made things simple *if only* it didn't have this quirk

	https://docs.python.org/3/library/getopt.html#getopt.getopt :

	"Unlike GNU getopt(), after a non-option argument, all further arguments are considered also non-options. This is similar to the way non-GNU Unix systems work."

Compare and contrast with the manpage.

	https://www.man7.org/linux/man-pages/man1/getopt.1.html#SCANNING_MODES :

	"If the first character is '+', or if the environment variable
	POSIXLY_CORRECT is set, parsing stops as soon as the first
	non-option parameter ... is found"

There is also, in the proper getopt, a '-' prefix which suppresses any re-sorting done on the processed arguments and I feel that this, too, is a #need-to-have.

#### TODO

North of Pangalin! is this shoddy craftsmanship. We can do better than that. Considering how simple it is, I shall build a custom getopt and maybe publish my first repo package. Chances are somebody beat me to it https://pypi.org/project/getopts/ and made a beautiful getopt clone already but I feel the rising need to minimize dependencies on known unknowns https://en.wikipedia.org/wiki/There_are_unknown_unknowns and besides it is good exercise to find small problems and write some simple https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html code. Simplicity being a more complex thought than "easy", mind you.

# PEX Issue

I was hoping to have more control of how PEX packaging and my shy (necro) comment https://github.com/pantsbuild/pex/issues/963 was answered rather quickly pointing me to a new, "additive" alternative https://github.com/pantsbuild/pex/releases/tag/v2.1.139 to my "subtractive" approach . Sweet!

# Murrine

Just peeked into the logs and was reminded that https://security.archlinux.org/package/gtk-engine-murrine was missing which https://www.gnupg.org/related_software/pinentry/index.html seems rather fond of. So I installed it. Looking forward to seeing the effects! https://en.wikipedia.org/wiki/Murrine

Also found the https://kaosx.us/ project by chance. It sure uses all the right words. Let's keep an eye on it.

# Shameful fact #1

I was driven home from chess club last night and a song was playing on the radio. I never really listen to german radio nor do I own a television set so I must have grown rather susceptible to its occasional charms. Long story short, I've got Streisand's Woman in Love running in the background. Let's see how long until those particular receptors become saturated. Let's hope they aren't re-uptake inhibited. For the love of good music!

## Radioactive Skies

A propos good music. Please do support the folks in Boise: https://radioboise.org/ ! They are doing wonderful things over there.

Also throw a buck or two at https://somafm.com/ to keep it going.

Remember gothicradio.com? https://web.archive.org/web/20230000000000*/http://gothicradio.com/ I wonder what those guys are doing now. Back then it was pretty much the only thing that had the power to please this queer old brain. It was a simpler time. A magical time. There seemed to be much harmony in a certain dissonance with life. Ah! was it not good to be young. Sitting quietly in my room, listening to gothicradio.com, reading stuff on textfiles.com and coding...., looking back I feel I've made the most of it. There were other things, of course, but this was at the core of that. Ah, but too much #nostalgia for the good old days may make a fashist out of you yet!

# Digressions

While I'm writing these lines I realize that some of the urls _didn't render well_. Due, of course, to my primitive `blog.py` parser which is innocent of context. https://en.wikipedia.org/wiki/Contextualism

The #toomanytabs so far: 1. deal with the weforum feed error ; 1.1. isolate the point of failure ; 1.1.1 use a command line parser to make testing a pleasure ; 1.1.1.1 write a better getopt ; 2. writing a stream-of-consciousness blog about 1. ; 2.1 either/or (or both) : 2.1.1 switching to my ANTLR grammar earlier than hoped ; 2.1.2 fixing blog.py elegantly to handle the most basic contexts well .

## Adventure Time

	You arrive at a fork in the road. The path to the right looks well trampled
	and is littered with bedoodled napkins of all kinds. You can make out
	flowcharts of some sort on some of them.

	>look at flowcharts.

	One of them is actually a sprawling binary tree and shows what looks to be a
	perfect illustration of your early morning train of thought.

	>define train.

	The word "train" here is of course unfortunate for it suggests a certain
	linearity and would therefore be very much misleading.

	>go left

	Good choice! Plowing onward, comrade.


! back=2023-08-18

! blurb=Digressions are like.... wait! That reminds me of something about left recursive grammars but first let me go off on a tangent about bats! Aren't they just marvellous feats of natural selection? It really makes you believe in the inevitability of things. The emergence of all that is physically possible. You should really read the first chapter of The Blind Watchmaker. And wasn't Hedy Lamarr just *swoon*? But first go re-watch that Seinfeld episode where they go: Is he very well-read or is he very ... well ... red!?
