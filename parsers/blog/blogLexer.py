# Generated from blog.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,87,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,3,1,23,8,1,1,1,1,1,1,2,1,2,1,3,
        1,3,1,4,1,4,1,5,5,5,34,8,5,10,5,12,5,37,9,5,1,5,4,5,40,8,5,11,5,
        12,5,41,1,5,4,5,45,8,5,11,5,12,5,46,1,6,5,6,50,8,6,10,6,12,6,53,
        9,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,61,8,6,1,6,1,6,1,6,1,6,1,6,4,6,68,
        8,6,11,6,12,6,69,1,7,4,7,73,8,7,11,7,12,7,74,1,8,5,8,78,8,8,10,8,
        12,8,81,9,8,1,8,4,8,84,8,8,11,8,12,8,85,0,0,9,1,0,3,0,5,0,7,0,9,
        0,11,1,13,2,15,3,17,4,1,0,4,2,0,9,9,32,32,3,0,9,10,13,13,32,32,2,
        0,10,10,13,13,1,0,35,35,91,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,1,19,1,0,0,0,3,22,1,0,0,0,5,26,1,0,0,0,7,28,1,0,0,
        0,9,30,1,0,0,0,11,35,1,0,0,0,13,51,1,0,0,0,15,72,1,0,0,0,17,79,1,
        0,0,0,19,20,7,0,0,0,20,2,1,0,0,0,21,23,5,13,0,0,22,21,1,0,0,0,22,
        23,1,0,0,0,23,24,1,0,0,0,24,25,5,10,0,0,25,4,1,0,0,0,26,27,8,1,0,
        0,27,6,1,0,0,0,28,29,8,2,0,0,29,8,1,0,0,0,30,31,8,1,0,0,31,10,1,
        0,0,0,32,34,3,1,0,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,
        36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,38,40,7,3,0,0,39,38,1,0,0,
        0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,45,
        3,7,3,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,
        47,12,1,0,0,0,48,50,3,1,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,104,0,0,
        55,56,5,116,0,0,56,57,5,116,0,0,57,58,5,112,0,0,58,60,1,0,0,0,59,
        61,5,115,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,58,
        0,0,63,64,5,47,0,0,64,65,5,47,0,0,65,67,1,0,0,0,66,68,3,5,2,0,67,
        66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,14,1,0,0,
        0,71,73,3,3,1,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,16,1,0,0,0,76,78,3,1,0,0,77,76,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,79,80,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,82,84,3,
        9,4,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,
        18,1,0,0,0,11,0,22,35,41,46,51,60,69,74,79,85,0
    ]

class blogLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TITLE = 1
    URI = 2
    EOL = 3
    WORD = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "TITLE", "URI", "EOL", "WORD" ]

    ruleNames = [ "SP", "LF", "UrlChars", "LineChars", "WordChars", "TITLE", 
                  "URI", "EOL", "WORD" ]

    grammarFileName = "blog.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


