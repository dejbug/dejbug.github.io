# Generated from blog.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        4,4,31,8,4,11,4,12,4,32,1,4,3,4,36,8,4,5,4,38,8,4,10,4,12,4,41,9,
        4,1,5,4,5,44,8,5,11,5,12,5,45,1,5,5,5,49,8,5,10,5,12,5,52,9,5,1,
        5,4,5,55,8,5,11,5,12,5,56,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,66,8,7,
        1,8,5,8,69,8,8,10,8,12,8,72,9,8,1,8,4,8,75,8,8,11,8,12,8,76,1,8,
        4,8,80,8,8,11,8,12,8,81,1,9,5,9,85,8,9,10,9,12,9,88,9,9,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,95,0,20,1,0,0,0,2,22,1,0,
        0,0,4,24,1,0,0,0,6,26,1,0,0,0,8,28,1,0,0,0,10,43,1,0,0,0,12,58,1,
        0,0,0,14,65,1,0,0,0,16,70,1,0,0,0,18,86,1,0,0,0,20,21,5,1,0,0,21,
        1,1,0,0,0,22,23,5,2,0,0,23,3,1,0,0,0,24,25,5,6,0,0,25,5,1,0,0,0,
        26,27,5,7,0,0,27,7,1,0,0,0,28,39,5,4,0,0,29,31,3,2,1,0,30,29,1,0,
        0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,36,
        5,4,0,0,35,34,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,30,1,0,0,0,
        38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,9,1,0,0,0,41,39,1,0,
        0,0,42,44,3,0,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,54,1,0,0,0,47,49,3,4,2,0,48,47,1,0,0,0,49,52,1,0,0,0,
        50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,55,3,
        8,4,0,54,50,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,
        11,1,0,0,0,58,59,5,5,0,0,59,13,1,0,0,0,60,66,3,10,5,0,61,66,3,12,
        6,0,62,66,3,8,4,0,63,66,3,4,2,0,64,66,3,2,1,0,65,60,1,0,0,0,65,61,
        1,0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,15,1,0,0,0,
        67,69,3,4,2,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,
        0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,73,75,3,14,7,0,74,73,1,0,0,0,75,
        76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,80,3,6,3,
        0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,17,
        1,0,0,0,83,85,3,16,8,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,
        86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,5,0,0,1,90,19,1,
        0,0,0,11,32,35,39,45,50,56,65,70,76,81,86
    ]

class blogParser ( Parser ):

    grammarFileName = "blog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'" ]

    symbolicNames = [ "<INVALID>", "Hash", "Punct", "Char", "Word", "Link", 
                      "Space", "Feed" ]

    RULE_hash = 0
    RULE_punct = 1
    RULE_space = 2
    RULE_feed = 3
    RULE_word = 4
    RULE_title = 5
    RULE_link = 6
    RULE_item = 7
    RULE_line = 8
    RULE_start = 9

    ruleNames =  [ "hash", "punct", "space", "feed", "word", "title", "link", 
                   "item", "line", "start" ]

    EOF = Token.EOF
    Hash=1
    Punct=2
    Char=3
    Word=4
    Link=5
    Space=6
    Feed=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Hash(self):
            return self.getToken(blogParser.Hash, 0)

        def getRuleIndex(self):
            return blogParser.RULE_hash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHash" ):
                listener.enterHash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHash" ):
                listener.exitHash(self)




    def hash_(self):

        localctx = blogParser.HashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_hash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(blogParser.Hash)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PunctContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Punct(self):
            return self.getToken(blogParser.Punct, 0)

        def getRuleIndex(self):
            return blogParser.RULE_punct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPunct" ):
                listener.enterPunct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPunct" ):
                listener.exitPunct(self)




    def punct(self):

        localctx = blogParser.PunctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_punct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(blogParser.Punct)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Space(self):
            return self.getToken(blogParser.Space, 0)

        def getRuleIndex(self):
            return blogParser.RULE_space

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpace" ):
                listener.enterSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpace" ):
                listener.exitSpace(self)




    def space(self):

        localctx = blogParser.SpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_space)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(blogParser.Space)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Feed(self):
            return self.getToken(blogParser.Feed, 0)

        def getRuleIndex(self):
            return blogParser.RULE_feed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeed" ):
                listener.enterFeed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeed" ):
                listener.exitFeed(self)




    def feed(self):

        localctx = blogParser.FeedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_feed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(blogParser.Feed)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(blogParser.Word)
            else:
                return self.getToken(blogParser.Word, i)

        def punct(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.PunctContext)
            else:
                return self.getTypedRuleContext(blogParser.PunctContext,i)


        def getRuleIndex(self):
            return blogParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)




    def word(self):

        localctx = blogParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(blogParser.Word)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 29
                            self.punct()

                        else:
                            raise NoViableAltException(self)
                        self.state = 32 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 34
                        self.match(blogParser.Word)

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hash_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.HashContext)
            else:
                return self.getTypedRuleContext(blogParser.HashContext,i)


        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.WordContext)
            else:
                return self.getTypedRuleContext(blogParser.WordContext,i)


        def space(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.SpaceContext)
            else:
                return self.getTypedRuleContext(blogParser.SpaceContext,i)


        def getRuleIndex(self):
            return blogParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)




    def title(self):

        localctx = blogParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_title)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.hash_()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 54 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 47
                        self.space()
                        self.state = 52
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 53
                    self.word()

                else:
                    raise NoViableAltException(self)
                self.state = 56 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Link(self):
            return self.getToken(blogParser.Link, 0)

        def getRuleIndex(self):
            return blogParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = blogParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(blogParser.Link)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title(self):
            return self.getTypedRuleContext(blogParser.TitleContext,0)


        def link(self):
            return self.getTypedRuleContext(blogParser.LinkContext,0)


        def word(self):
            return self.getTypedRuleContext(blogParser.WordContext,0)


        def space(self):
            return self.getTypedRuleContext(blogParser.SpaceContext,0)


        def punct(self):
            return self.getTypedRuleContext(blogParser.PunctContext,0)


        def getRuleIndex(self):
            return blogParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = blogParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_item)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.title()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.link()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.word()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.space()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.punct()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.SpaceContext)
            else:
                return self.getTypedRuleContext(blogParser.SpaceContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.ItemContext)
            else:
                return self.getTypedRuleContext(blogParser.ItemContext,i)


        def feed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.FeedContext)
            else:
                return self.getTypedRuleContext(blogParser.FeedContext,i)


        def getRuleIndex(self):
            return blogParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = blogParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.space() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.item()
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 118) != 0)):
                    break

            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.feed()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(blogParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.LineContext)
            else:
                return self.getTypedRuleContext(blogParser.LineContext,i)


        def getRuleIndex(self):
            return blogParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = blogParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 118) != 0):
                self.state = 83
                self.line()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(blogParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





