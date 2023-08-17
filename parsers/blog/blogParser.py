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
        4,1,4,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,
        1,0,5,0,15,8,0,10,0,12,0,18,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        27,8,1,1,2,1,2,1,2,1,2,1,3,4,3,34,8,3,11,3,12,3,35,1,4,1,4,1,4,1,
        4,0,0,5,0,2,4,6,8,0,0,41,0,11,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,
        6,33,1,0,0,0,8,37,1,0,0,0,10,12,3,8,4,0,11,10,1,0,0,0,11,12,1,0,
        0,0,12,16,1,0,0,0,13,15,3,2,1,0,14,13,1,0,0,0,15,18,1,0,0,0,16,14,
        1,0,0,0,16,17,1,0,0,0,17,1,1,0,0,0,18,16,1,0,0,0,19,20,5,2,0,0,20,
        27,6,1,-1,0,21,27,3,4,2,0,22,23,3,6,3,0,23,24,6,1,-1,0,24,27,1,0,
        0,0,25,27,5,3,0,0,26,19,1,0,0,0,26,21,1,0,0,0,26,22,1,0,0,0,26,25,
        1,0,0,0,27,3,1,0,0,0,28,29,5,3,0,0,29,30,5,1,0,0,30,31,6,2,-1,0,
        31,5,1,0,0,0,32,34,5,4,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,7,1,0,0,0,37,38,5,1,0,0,38,39,6,4,-1,0,39,9,
        1,0,0,0,4,11,16,26,35
    ]

class blogParser ( Parser ):

    grammarFileName = "blog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "TITLE", "URI", "EOL", "WORD" ]

    RULE_start = 0
    RULE_item = 1
    RULE_title = 2
    RULE_words = 3
    RULE_firsttitle = 4

    ruleNames =  [ "start", "item", "title", "words", "firsttitle" ]

    EOF = Token.EOF
    TITLE=1
    URI=2
    EOL=3
    WORD=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def firsttitle(self):
            return self.getTypedRuleContext(blogParser.FirsttitleContext,0)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(blogParser.ItemContext)
            else:
                return self.getTypedRuleContext(blogParser.ItemContext,i)


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
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 10
                self.firsttitle()


            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 13
                self.item()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self._URI = None # Token
            self._words = None # WordsContext

        def URI(self):
            return self.getToken(blogParser.URI, 0)

        def title(self):
            return self.getTypedRuleContext(blogParser.TitleContext,0)


        def words(self):
            return self.getTypedRuleContext(blogParser.WordsContext,0)


        def EOL(self):
            return self.getToken(blogParser.EOL, 0)

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
        self.enterRule(localctx, 2, self.RULE_item)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                localctx._URI = self.match(blogParser.URI)
                print(f'<{(None if localctx._URI is None else localctx._URI.text).strip()}>')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.title()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                localctx._words = self.words()
                print(f'({(None if localctx._words is None else self._input.getText(localctx._words.start,localctx._words.stop))})')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(blogParser.EOL)
                pass


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
            self._TITLE = None # Token

        def EOL(self):
            return self.getToken(blogParser.EOL, 0)

        def TITLE(self):
            return self.getToken(blogParser.TITLE, 0)

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
        self.enterRule(localctx, 4, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(blogParser.EOL)
            self.state = 29
            localctx._TITLE = self.match(blogParser.TITLE)
            print(f'[{(None if localctx._TITLE is None else localctx._TITLE.text)}]')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(blogParser.WORD)
            else:
                return self.getToken(blogParser.WORD, i)

        def getRuleIndex(self):
            return blogParser.RULE_words

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWords" ):
                listener.enterWords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWords" ):
                listener.exitWords(self)




    def words(self):

        localctx = blogParser.WordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_words)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.match(blogParser.WORD)

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirsttitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TITLE = None # Token

        def TITLE(self):
            return self.getToken(blogParser.TITLE, 0)

        def getRuleIndex(self):
            return blogParser.RULE_firsttitle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirsttitle" ):
                listener.enterFirsttitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirsttitle" ):
                listener.exitFirsttitle(self)




    def firsttitle(self):

        localctx = blogParser.FirsttitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_firsttitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx._TITLE = self.match(blogParser.TITLE)
            print(f'[{(None if localctx._TITLE is None else localctx._TITLE.text)}]')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





