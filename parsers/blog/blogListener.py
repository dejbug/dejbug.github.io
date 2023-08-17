# Generated from blog.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .blogParser import blogParser
else:
    from blogParser import blogParser

# This class defines a complete listener for a parse tree produced by blogParser.
class blogListener(ParseTreeListener):

    # Enter a parse tree produced by blogParser#start.
    def enterStart(self, ctx:blogParser.StartContext):
        pass

    # Exit a parse tree produced by blogParser#start.
    def exitStart(self, ctx:blogParser.StartContext):
        pass


    # Enter a parse tree produced by blogParser#item.
    def enterItem(self, ctx:blogParser.ItemContext):
        pass

    # Exit a parse tree produced by blogParser#item.
    def exitItem(self, ctx:blogParser.ItemContext):
        pass


    # Enter a parse tree produced by blogParser#title.
    def enterTitle(self, ctx:blogParser.TitleContext):
        pass

    # Exit a parse tree produced by blogParser#title.
    def exitTitle(self, ctx:blogParser.TitleContext):
        pass


    # Enter a parse tree produced by blogParser#words.
    def enterWords(self, ctx:blogParser.WordsContext):
        pass

    # Exit a parse tree produced by blogParser#words.
    def exitWords(self, ctx:blogParser.WordsContext):
        pass


    # Enter a parse tree produced by blogParser#firsttitle.
    def enterFirsttitle(self, ctx:blogParser.FirsttitleContext):
        pass

    # Exit a parse tree produced by blogParser#firsttitle.
    def exitFirsttitle(self, ctx:blogParser.FirsttitleContext):
        pass



del blogParser