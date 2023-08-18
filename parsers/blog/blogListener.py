# Generated from blog.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .blogParser import blogParser
else:
    from blogParser import blogParser

# This class defines a complete listener for a parse tree produced by blogParser.
class blogListener(ParseTreeListener):

    # Enter a parse tree produced by blogParser#hash.
    def enterHash(self, ctx:blogParser.HashContext):
        pass

    # Exit a parse tree produced by blogParser#hash.
    def exitHash(self, ctx:blogParser.HashContext):
        pass


    # Enter a parse tree produced by blogParser#punct.
    def enterPunct(self, ctx:blogParser.PunctContext):
        pass

    # Exit a parse tree produced by blogParser#punct.
    def exitPunct(self, ctx:blogParser.PunctContext):
        pass


    # Enter a parse tree produced by blogParser#space.
    def enterSpace(self, ctx:blogParser.SpaceContext):
        pass

    # Exit a parse tree produced by blogParser#space.
    def exitSpace(self, ctx:blogParser.SpaceContext):
        pass


    # Enter a parse tree produced by blogParser#feed.
    def enterFeed(self, ctx:blogParser.FeedContext):
        pass

    # Exit a parse tree produced by blogParser#feed.
    def exitFeed(self, ctx:blogParser.FeedContext):
        pass


    # Enter a parse tree produced by blogParser#word.
    def enterWord(self, ctx:blogParser.WordContext):
        pass

    # Exit a parse tree produced by blogParser#word.
    def exitWord(self, ctx:blogParser.WordContext):
        pass


    # Enter a parse tree produced by blogParser#title.
    def enterTitle(self, ctx:blogParser.TitleContext):
        pass

    # Exit a parse tree produced by blogParser#title.
    def exitTitle(self, ctx:blogParser.TitleContext):
        pass


    # Enter a parse tree produced by blogParser#link.
    def enterLink(self, ctx:blogParser.LinkContext):
        pass

    # Exit a parse tree produced by blogParser#link.
    def exitLink(self, ctx:blogParser.LinkContext):
        pass


    # Enter a parse tree produced by blogParser#item.
    def enterItem(self, ctx:blogParser.ItemContext):
        pass

    # Exit a parse tree produced by blogParser#item.
    def exitItem(self, ctx:blogParser.ItemContext):
        pass


    # Enter a parse tree produced by blogParser#line.
    def enterLine(self, ctx:blogParser.LineContext):
        pass

    # Exit a parse tree produced by blogParser#line.
    def exitLine(self, ctx:blogParser.LineContext):
        pass


    # Enter a parse tree produced by blogParser#start.
    def enterStart(self, ctx:blogParser.StartContext):
        pass

    # Exit a parse tree produced by blogParser#start.
    def exitStart(self, ctx:blogParser.StartContext):
        pass



del blogParser