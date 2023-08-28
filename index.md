# EOL

In the current "iteration"(the next two weeks) I'm going to ditch `blog.py` for a proper lexer https://github.com/users/dejbug/projects/1/views/4 .

First I'll need to define and freeze the "input format"(the markdown flavor of my blog). I've probably arrived at the logical conclusion of what is possible with a "local"(context-less) rewriter. From here on out I'll need some global grokking.

For footnotes, for example.

# Tag it and bag it

The word foot-note reminds me of the little yellow plastic tags that mortuaries probably keep boxes of.

# Boxes among trees

So there is a display property called "contents" https://drafts.csswg.org/css-display/#valdef-display-contents https://drafts.csswg.org/css-display/#unbox which I didn't know about. Serves to show that I really need to forget everyting I thought I knew 20 years ago and re-learn the stuff. Well, someday. Nobody is paying me to be a front-end dev. So for now I'll learn the stuff on a need-to-know basis.

# Pushing up the daisies

A couple of things to look at: "inline floats"(( https://developer.mozilla.org/en-US/docs/Web/CSS/Inline_formatting_context#effect_of_floats )) ":target"(( https://developer.mozilla.org/en-US/docs/Web/CSS/:target )) ":popover-open"(( https://developer.mozilla.org/en-US/docs/Web/CSS/:popover-open )) ":local-link"(( https://developer.mozilla.org/en-US/docs/Web/CSS/:local-link )) ":host"(( https://developer.mozilla.org/en-US/docs/Web/CSS/:host )) "::slotted()"(( https://developer.mozilla.org/en-US/docs/Web/CSS/::slotted ) "::part()"(( https://developer.mozilla.org/en-US/docs/Web/CSS/::part )) "::marker"(( https://developer.mozilla.org/en-US/docs/Web/CSS/::marker )).

"""The details element is not appropriate for footnotes. https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element """

I've abused the details element a little. https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details For the new lexer I should be looking at "<dfn>"( https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn ) and "<dt>"( https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt ) etc. .

# Dead Parrot

The examples in https://html.spec.whatwg.org/multipage/semantics-other.html#footnotes show great taste and erudition on the part of the technical writers at Mozilla. I must say!

# Firefox in Firefox

This is the uri: `chrome://browser/content/browser.xhtml` . It was linked from the developer tools console (<C-S-j>).

# Digressions

I made the mistake of looking at a page and then wondering whether it had syndication and then looking at its `rss.xml` and then thinking "Wait a second...!" why didn't I write an addon yet to reformat the xml into a rss reader-like affair?

## De-Atomizer (temporary name)

Or Union Buster! or Scab! (as in de-syndicator) or Unionice? (as in syndication niceifier)...

Basically you load an xml file that happens to be an RSS or Atom feed and this Web Extension will make it humanly readable. If it recognizes the feed's source it will apply stylesheets that match the soure's corporate identity.

Everything went smoothly, since you could just build upon the very first example Mozilla gives you, which is a content script that adds a border. But the progress came to a full stop when I realized that there is no intuitive way to set the document's `contentType`.

The problem is, once you've surfed to an XML page the `window.document` will point to an `XMLDocument` instance. Now `window.document` is a read-only property so you can't just `window.document = new HTMLDocument()` and `document.contentType` is readonly too.

There **used to be** a two-argument version of "document.open()" that could do it. I found that out almost by chance while scouring the docs. There's no alternative given on that sorry excuse for a proper reference page. You can't even click your way from "api.method" back to "api". So, again by chance, I stumbled upon something that reminded me of a thing I never used before except for SVGs: `createElementNS()`. Note the ominous "NS".

### Regex

Experimentation turned out that if you remove all elements from the XMLDocument and add some elements created with an explicit namespace https://infra.spec.whatwg.org/#html-namespace it will all print as it would in an HTMLDocument.

So this is a way to do it by hand. Just regex through the XML and then replace it with html-namespaced elements.

# XSLT

The more elegant but far less powerful way would be to use XSLT.

Now I've tried simply rewriting the root ...

# XSLT (two days later)

I am writing these words ____two days later____. I have just now found the solution to a problem so frustrating that it made me scream. And yes it has to do with XSLT. I don't want to look at this pile of rubbish any longer than I have to but well, now that I see the logic in it, I just might revise that sentiment once I've thoroughly calmed down. It's been 20 years since last I had been dealing with this stuff. My hovercraft is full of eels.

## The Problem

I was trying to parse an **RDF-style RSS**. https://web.resource.org/rss/1.0/spec The freaking `xmlns="...rss..."` tripped me up. It made all the tags that weren't explicitly prefixed with a shorthand (e.g. `dc:creator`) fall into this anonymous namespace. So there was no way to select the nodes just by their names.

```xml
<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns="http://purl.org/rss/1.0/"
>
<item><title>...</title></item>
<item><title>...</title></item>
</rdf:RDF>
```

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
>
<xsl:template match="RDF">
	Found the root?
</xsl:template>
</xsl:stylesheet>
```

Doesn't work. You need to add the rdf namespace.

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
<xsl:template match="rdf:RDF">
	Found the root!
</xsl:template>
</xsl:stylesheet>
```

But now how do you get to the items? I found nothing at

https://www.w3.org/Style/XSL/
https://www.w3.org/TR/xslt.html
https://www.w3.org/RDF/
https://www.w3.org/community/rax/wiki/XML_to_RDF_Transformation_processes_using_XSLT
https://www.w3.org/XML/2000/04rdf-parse/
https://www.oreilly.com/library/view/xslt-cookbook/0596003722/ch04.html
https://www.w3schools.com/xml/xpath_syntax.asp .

Interesting, perhaps:

https://www.w3.org/DesignIssues/Toolbox
https://en.wikipedia.org/wiki/Embedded_RDF
https://www.w3.org/2004/02/skos/

Anyway. Here's what I thought:

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
<xsl:output method="text" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
	<xsl:value-of select="/rdf:RDF/channel/title"/>
</xsl:template>
</xsl:stylesheet>
```

This doesn't work.

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns="http://purl.org/rss/1.0/"
>
<xsl:output method="text" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
	<xsl:value-of select="/rdf:RDF/channel/title"/>
</xsl:template>
</xsl:stylesheet>
```

This neither. But eventually, after lots of fiddling, the following produced the hint I needed.


```xml
<xsl:template match="/*/*">
	<xsl:value-of select="name(.)"/><xsl:text>:
</xsl:text>
	<xsl:for-each select="*">
	<xsl:text>	</xsl:text>
	<xsl:value-of select="name(.)"/>
	<xsl:text> (</xsl:text>
	<xsl:value-of select="namespace-uri(.)"/>
	<xsl:text>)
</xsl:text>
	</xsl:for-each>
</xsl:template>
```

It was `namespace-uri()` that I had to have to excavate the root cause of my suffering. I found it while looking through the list of XPath functions here https://www.w3.org/2005/xpath-functions/ . I've been looking for anything that could reveal the hidden structure behind the a simple name like `title`.

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rss="http://purl.org/rss/1.0/"
>
<xsl:output method="text" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
	<xsl:value-of select="/rdf:RDF/rss:channel/rss:title"/>
</xsl:template>
</xsl:stylesheet>
```

The summit is reached. It's all downhill from here.

```xml
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rss="http://purl.org/rss/1.0/"
>
<xsl:output method="text" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
	<xsl:value-of select="/rdf:RDF/rss:channel/rss:title"/>
	<xsl:text>
	</xsl:text>
	<xsl:for-each select="//rss:item">
		<xsl:value-of select="rss:title"/>
		<xsl:text>
	</xsl:text>
	</xsl:for-each>
	<xsl:text>
</xsl:text>
</xsl:template>
</xsl:stylesheet>
```

Why do I need this? The answer is I really didn't. I just had to find the error. It was driving me nuts. What I wanted it for is to **quickly** run the slashdot RSS http://rss.slashdot.org/Slashdot/slashdot through it and get an HTML I wanted to test my Firefox extension on. The constant reloading of the temp addon was destabilizing my overall serenity. So, yes, digressions. Wheels within wheels.

# Black Adder

I'm listening to something called ____"SoundTV Dub Techno Mix (NASA Special 2)"____ ( https://www.youtube.com/watch?v=swpi0QsDYZU ? ) on Radio Schizoid's **Dub** channel http://schizoid.in/ .

Before I had to spend two hours in XML maze I was trying to replicate GitHub Doc's TOC. I find it nice how the current subtopic is highlighted as you scroll through the page. I've seen this before in other places but never really thought about it much.

There are a couple near-misses here. There's `position: sticky` https://developer.mozilla.org/en-US/docs/Web/CSS/position#sticky_positioning . There's `:target` https://developer.mozilla.org/en-US/docs/Web/CSS/:target . Real solutions start with `getBoundingClientRect` https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect . But you'll find something much dearer to the heart called the **Intersection Observer API** https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API .

Currently I'm using it to toggle some classes on and off on `h3` elements as they're scrolling in and out of view. After each event I find the first header in the scrolled-into-view class and take the one before it to be the sticky header. All is working well so far. I'm showing the current topic in a little overhead strip as if `position: sticky` were used on the header but nicer.

There is a nasty edge-case here where the previous title overlays the current title as it scrolls into view, but the `rootMargin` option solves this nicely.

# Carnival Dogs Consume The Lines

Men don't get tired. Men get exhausted. But I think I've done enough today. I was close to crying at one point. But no, men don't cry, men weep. I was close to weeping. Today, I guess, I was built too close to water as the germans say. Don't mention the war. What else. I binged through season three of Lower Decks because it was going behind Prime's paywall soon. I didn't find a single flaw with it. I really enjoyed it and also the fact that I had caught it just in time. Oh! And. I got a text from a stranger today. It was either a phishing attempt or it was somebody of substance who was to get me out of my solipsistic/idiotic funk and into a grand new future life of purpose and reward. But do go ahead and guess.

! header = block
