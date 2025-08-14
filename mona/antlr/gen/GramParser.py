# Generated from GramParser.g4 by ANTLR 4.13.2
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
        4,1,48,295,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,3,2,80,8,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,4,3,4,95,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,128,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,3,11,146,8,11,1,12,1,12,1,12,1,12,3,12,152,8,12,1,
        13,1,13,1,13,5,13,157,8,13,10,13,12,13,160,9,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,170,8,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,197,8,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,5,15,219,8,15,10,15,12,15,222,9,15,1,16,1,16,1,
        16,1,16,1,16,3,16,229,8,16,1,17,1,17,3,17,233,8,17,1,17,1,17,5,17,
        237,8,17,10,17,12,17,240,9,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,
        248,8,18,10,18,12,18,251,9,18,1,18,1,18,1,18,3,18,256,8,18,1,19,
        1,19,1,19,1,19,5,19,262,8,19,10,19,12,19,265,9,19,1,19,1,19,1,19,
        1,19,3,19,271,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,293,
        8,20,1,20,0,1,30,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,0,5,1,0,16,17,1,0,31,34,2,0,28,28,30,30,1,0,26,27,1,
        0,13,14,325,0,45,1,0,0,0,2,75,1,0,0,0,4,79,1,0,0,0,6,81,1,0,0,0,
        8,86,1,0,0,0,10,96,1,0,0,0,12,102,1,0,0,0,14,109,1,0,0,0,16,112,
        1,0,0,0,18,127,1,0,0,0,20,129,1,0,0,0,22,145,1,0,0,0,24,151,1,0,
        0,0,26,153,1,0,0,0,28,169,1,0,0,0,30,196,1,0,0,0,32,228,1,0,0,0,
        34,230,1,0,0,0,36,255,1,0,0,0,38,270,1,0,0,0,40,292,1,0,0,0,42,44,
        3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,
        46,49,1,0,0,0,47,45,1,0,0,0,48,50,5,0,0,1,49,48,1,0,0,0,49,50,1,
        0,0,0,50,1,1,0,0,0,51,52,3,6,3,0,52,53,5,23,0,0,53,76,1,0,0,0,54,
        76,3,8,4,0,55,76,3,16,8,0,56,57,3,18,9,0,57,58,5,23,0,0,58,76,1,
        0,0,0,59,76,3,20,10,0,60,61,3,22,11,0,61,62,5,23,0,0,62,76,1,0,0,
        0,63,64,3,24,12,0,64,65,5,23,0,0,65,76,1,0,0,0,66,67,3,26,13,0,67,
        68,5,23,0,0,68,76,1,0,0,0,69,70,5,10,0,0,70,71,3,26,13,0,71,72,5,
        23,0,0,72,76,1,0,0,0,73,74,5,11,0,0,74,76,5,23,0,0,75,51,1,0,0,0,
        75,54,1,0,0,0,75,55,1,0,0,0,75,56,1,0,0,0,75,59,1,0,0,0,75,60,1,
        0,0,0,75,63,1,0,0,0,75,66,1,0,0,0,75,69,1,0,0,0,75,73,1,0,0,0,76,
        3,1,0,0,0,77,80,3,30,15,0,78,80,5,42,0,0,79,77,1,0,0,0,79,78,1,0,
        0,0,80,5,1,0,0,0,81,82,5,1,0,0,82,83,5,42,0,0,83,84,5,22,0,0,84,
        85,3,4,2,0,85,7,1,0,0,0,86,90,3,10,5,0,87,89,3,12,6,0,88,87,1,0,
        0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,90,
        1,0,0,0,93,95,3,14,7,0,94,93,1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,
        96,97,5,20,0,0,97,98,5,36,0,0,98,99,3,30,15,0,99,100,5,37,0,0,100,
        101,3,26,13,0,101,11,1,0,0,0,102,103,5,21,0,0,103,104,5,20,0,0,104,
        105,5,36,0,0,105,106,3,30,15,0,106,107,5,37,0,0,107,108,3,26,13,
        0,108,13,1,0,0,0,109,110,5,21,0,0,110,111,3,26,13,0,111,15,1,0,0,
        0,112,113,5,18,0,0,113,114,5,42,0,0,114,115,3,36,18,0,115,116,3,
        26,13,0,116,17,1,0,0,0,117,118,5,42,0,0,118,128,3,38,19,0,119,120,
        5,9,0,0,120,128,3,38,19,0,121,122,5,6,0,0,122,128,3,38,19,0,123,
        124,5,7,0,0,124,128,3,38,19,0,125,126,5,8,0,0,126,128,3,38,19,0,
        127,117,1,0,0,0,127,119,1,0,0,0,127,121,1,0,0,0,127,123,1,0,0,0,
        127,125,1,0,0,0,128,19,1,0,0,0,129,130,5,12,0,0,130,131,5,36,0,0,
        131,132,3,30,15,0,132,133,5,37,0,0,133,134,3,26,13,0,134,21,1,0,
        0,0,135,136,5,42,0,0,136,137,5,38,0,0,137,138,3,30,15,0,138,139,
        5,39,0,0,139,140,5,22,0,0,140,141,3,4,2,0,141,146,1,0,0,0,142,143,
        5,42,0,0,143,144,5,22,0,0,144,146,3,4,2,0,145,135,1,0,0,0,145,142,
        1,0,0,0,146,23,1,0,0,0,147,148,5,2,0,0,148,152,3,38,19,0,149,150,
        5,3,0,0,150,152,3,38,19,0,151,147,1,0,0,0,151,149,1,0,0,0,152,25,
        1,0,0,0,153,158,5,40,0,0,154,157,3,2,1,0,155,157,3,28,14,0,156,154,
        1,0,0,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,5,41,0,0,162,27,
        1,0,0,0,163,164,5,19,0,0,164,165,3,30,15,0,165,166,5,23,0,0,166,
        170,1,0,0,0,167,168,5,19,0,0,168,170,5,23,0,0,169,163,1,0,0,0,169,
        167,1,0,0,0,170,29,1,0,0,0,171,172,6,15,-1,0,172,173,5,36,0,0,173,
        174,3,30,15,0,174,175,5,37,0,0,175,197,1,0,0,0,176,197,3,18,9,0,
        177,178,5,10,0,0,178,197,3,26,13,0,179,180,5,10,0,0,180,197,3,30,
        15,13,181,182,5,15,0,0,182,197,3,30,15,9,183,197,3,34,17,0,184,197,
        3,32,16,0,185,186,5,4,0,0,186,187,5,36,0,0,187,188,3,30,15,0,188,
        189,5,37,0,0,189,197,1,0,0,0,190,191,5,5,0,0,191,192,5,36,0,0,192,
        193,3,30,15,0,193,194,5,37,0,0,194,197,1,0,0,0,195,197,5,42,0,0,
        196,171,1,0,0,0,196,176,1,0,0,0,196,177,1,0,0,0,196,179,1,0,0,0,
        196,181,1,0,0,0,196,183,1,0,0,0,196,184,1,0,0,0,196,185,1,0,0,0,
        196,190,1,0,0,0,196,195,1,0,0,0,197,220,1,0,0,0,198,199,10,12,0,
        0,199,200,7,0,0,0,200,219,3,30,15,13,201,202,10,11,0,0,202,203,7,
        1,0,0,203,219,3,30,15,12,204,205,10,10,0,0,205,206,5,35,0,0,206,
        219,3,30,15,11,207,208,10,8,0,0,208,209,5,29,0,0,209,219,3,30,15,
        9,210,211,10,7,0,0,211,212,7,2,0,0,212,219,3,30,15,8,213,214,10,
        6,0,0,214,215,7,3,0,0,215,219,3,30,15,7,216,217,10,15,0,0,217,219,
        3,40,20,0,218,198,1,0,0,0,218,201,1,0,0,0,218,204,1,0,0,0,218,207,
        1,0,0,0,218,210,1,0,0,0,218,213,1,0,0,0,218,216,1,0,0,0,219,222,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,31,1,0,0,0,222,220,1,
        0,0,0,223,229,5,43,0,0,224,229,5,44,0,0,225,229,5,45,0,0,226,229,
        7,4,0,0,227,229,5,46,0,0,228,223,1,0,0,0,228,224,1,0,0,0,228,225,
        1,0,0,0,228,226,1,0,0,0,228,227,1,0,0,0,229,33,1,0,0,0,230,232,5,
        38,0,0,231,233,3,30,15,0,232,231,1,0,0,0,232,233,1,0,0,0,233,238,
        1,0,0,0,234,235,5,25,0,0,235,237,3,30,15,0,236,234,1,0,0,0,237,240,
        1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,0,240,238,
        1,0,0,0,241,242,5,39,0,0,242,35,1,0,0,0,243,244,5,36,0,0,244,249,
        5,42,0,0,245,246,5,25,0,0,246,248,5,42,0,0,247,245,1,0,0,0,248,251,
        1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,252,1,0,0,0,251,249,
        1,0,0,0,252,256,5,37,0,0,253,254,5,36,0,0,254,256,5,37,0,0,255,243,
        1,0,0,0,255,253,1,0,0,0,256,37,1,0,0,0,257,258,5,36,0,0,258,263,
        3,30,15,0,259,260,5,25,0,0,260,262,3,30,15,0,261,259,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,
        263,1,0,0,0,266,267,5,37,0,0,267,271,1,0,0,0,268,269,5,36,0,0,269,
        271,5,37,0,0,270,257,1,0,0,0,270,268,1,0,0,0,271,39,1,0,0,0,272,
        273,5,38,0,0,273,274,3,30,15,0,274,275,5,39,0,0,275,293,1,0,0,0,
        276,277,5,38,0,0,277,278,3,30,15,0,278,279,5,24,0,0,279,280,5,39,
        0,0,280,293,1,0,0,0,281,282,5,38,0,0,282,283,5,24,0,0,283,284,3,
        30,15,0,284,285,5,39,0,0,285,293,1,0,0,0,286,287,5,38,0,0,287,288,
        3,30,15,0,288,289,5,24,0,0,289,290,3,30,15,0,290,291,5,39,0,0,291,
        293,1,0,0,0,292,272,1,0,0,0,292,276,1,0,0,0,292,281,1,0,0,0,292,
        286,1,0,0,0,293,41,1,0,0,0,23,45,49,75,79,90,94,127,145,151,156,
        158,169,196,218,220,228,232,238,249,255,263,270,292
    ]

class GramParser ( Parser ):

    grammarFileName = "GramParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'print'", "'println'", "'lenof'", 
                     "'copyof'", "'floorintof'", "'roundintof'", "'ceilintof'", 
                     "'sin'", "'spawn'", "'join'", "'while'", "'True'", 
                     "'False'", "'not'", "'and'", "'or'", "'decl'", "'ret'", 
                     "'if'", "'else'", "'='", "';'", "':'", "','", "'+'", 
                     "'-'", "'*'", "'**'", "'/'", "'<'", "'<='", "'>'", 
                     "'>='", "'=='", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "VAR", "PRINT", "PRINTLN", "LENOF", "COPYOF", 
                      "FLOORINTOF", "ROUNDINTOF", "CEILINTOF", "SIN", "SPAWN", 
                      "JOIN", "WHILE", "TRUE", "FALSE", "NOT", "AND", "OR", 
                      "DECL", "RET", "IF", "ELSE", "ASSIGN", "SEMI", "COLON", 
                      "COMMA", "PLUS", "MINUS", "TIMES", "POW", "DIV", "LESSTHAN", 
                      "LESSTHANOREQUAL", "GREATERTHAN", "GREATERTHANOREQUAL", 
                      "EQUALS", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "IDEN", "INT", "FLOAT", "CHAR", 
                      "STRING", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_assig_trgt = 2
    RULE_var_declr = 3
    RULE_if_block = 4
    RULE_if_stmt = 5
    RULE_elseif_stmt = 6
    RULE_else_stmt = 7
    RULE_func_decl = 8
    RULE_func_call_expr = 9
    RULE_while = 10
    RULE_assig = 11
    RULE_print = 12
    RULE_stmt_block = 13
    RULE_ret_stmt = 14
    RULE_expr = 15
    RULE_literal = 16
    RULE_lst_decl = 17
    RULE_param_lst = 18
    RULE_arg_lst = 19
    RULE_idx_access = 20

    ruleNames =  [ "program", "stmt", "assig_trgt", "var_declr", "if_block", 
                   "if_stmt", "elseif_stmt", "else_stmt", "func_decl", "func_call_expr", 
                   "while", "assig", "print", "stmt_block", "ret_stmt", 
                   "expr", "literal", "lst_decl", "param_lst", "arg_lst", 
                   "idx_access" ]

    EOF = Token.EOF
    VAR=1
    PRINT=2
    PRINTLN=3
    LENOF=4
    COPYOF=5
    FLOORINTOF=6
    ROUNDINTOF=7
    CEILINTOF=8
    SIN=9
    SPAWN=10
    JOIN=11
    WHILE=12
    TRUE=13
    FALSE=14
    NOT=15
    AND=16
    OR=17
    DECL=18
    RET=19
    IF=20
    ELSE=21
    ASSIGN=22
    SEMI=23
    COLON=24
    COMMA=25
    PLUS=26
    MINUS=27
    TIMES=28
    POW=29
    DIV=30
    LESSTHAN=31
    LESSTHANOREQUAL=32
    GREATERTHAN=33
    GREATERTHANOREQUAL=34
    EQUALS=35
    LPAREN=36
    RPAREN=37
    LBRACK=38
    RBRACK=39
    LBRACE=40
    RBRACE=41
    IDEN=42
    INT=43
    FLOAT=44
    CHAR=45
    STRING=46
    LINE_COMMENT=47
    WS=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramParser.StmtContext,i)


        def EOF(self):
            return self.getToken(GramParser.EOF, 0)

        def getRuleIndex(self):
            return GramParser.RULE_program




    def program(self):

        localctx = GramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5497559457742) != 0):
                self.state = 42
                self.stmt()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(GramParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Stmt_if_blockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_block(self):
            return self.getTypedRuleContext(GramParser.If_blockContext,0)



    class Stmt_stmt_blockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_func_declContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_decl(self):
            return self.getTypedRuleContext(GramParser.Func_declContext,0)



    class Stmt_assigContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assig(self):
            return self.getTypedRuleContext(GramParser.AssigContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_whileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_(self):
            return self.getTypedRuleContext(GramParser.WhileContext,0)



    class Stmt_func_callContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_printContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_(self):
            return self.getTypedRuleContext(GramParser.PrintContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_spawnContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPAWN(self):
            return self.getToken(GramParser.SPAWN, 0)
        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_joinContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JOIN(self):
            return self.getToken(GramParser.JOIN, 0)
        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)


    class Stmt_var_declrContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var_declr(self):
            return self.getTypedRuleContext(GramParser.Var_declrContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)



    def stmt(self):

        localctx = GramParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = GramParser.Stmt_var_declrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.var_declr()
                self.state = 52
                self.match(GramParser.SEMI)
                pass

            elif la_ == 2:
                localctx = GramParser.Stmt_if_blockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.if_block()
                pass

            elif la_ == 3:
                localctx = GramParser.Stmt_func_declContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.func_decl()
                pass

            elif la_ == 4:
                localctx = GramParser.Stmt_func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.func_call_expr()
                self.state = 57
                self.match(GramParser.SEMI)
                pass

            elif la_ == 5:
                localctx = GramParser.Stmt_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.while_()
                pass

            elif la_ == 6:
                localctx = GramParser.Stmt_assigContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.assig()
                self.state = 61
                self.match(GramParser.SEMI)
                pass

            elif la_ == 7:
                localctx = GramParser.Stmt_printContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.print_()
                self.state = 64
                self.match(GramParser.SEMI)
                pass

            elif la_ == 8:
                localctx = GramParser.Stmt_stmt_blockContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.stmt_block()
                self.state = 67
                self.match(GramParser.SEMI)
                pass

            elif la_ == 9:
                localctx = GramParser.Stmt_spawnContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.match(GramParser.SPAWN)
                self.state = 70
                self.stmt_block()
                self.state = 71
                self.match(GramParser.SEMI)
                pass

            elif la_ == 10:
                localctx = GramParser.Stmt_joinContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 73
                self.match(GramParser.JOIN)
                self.state = 74
                self.match(GramParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assig_trgtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_assig_trgt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assig_trgt_exprContext(Assig_trgtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Assig_trgtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)



    class Assig_trgt_idenContext(Assig_trgtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Assig_trgtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)



    def assig_trgt(self):

        localctx = GramParser.Assig_trgtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig_trgt)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assig_trgt_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = GramParser.Assig_trgt_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(GramParser.IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GramParser.VAR, 0)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)

        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_var_declr




    def var_declr(self):

        localctx = GramParser.Var_declrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(GramParser.VAR)
            self.state = 82
            self.match(GramParser.IDEN)
            self.state = 83
            self.match(GramParser.ASSIGN)
            self.state = 84
            self.assig_trgt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(GramParser.If_stmtContext,0)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(GramParser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(GramParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_if_block




    def if_block(self):

        localctx = GramParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.if_stmt()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.elseif_stmt() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 93
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GramParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_if_stmt




    def if_stmt(self):

        localctx = GramParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(GramParser.IF)
            self.state = 97
            self.match(GramParser.LPAREN)
            self.state = 98
            self.expr(0)
            self.state = 99
            self.match(GramParser.RPAREN)
            self.state = 100
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GramParser.ELSE, 0)

        def IF(self):
            return self.getToken(GramParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_elseif_stmt




    def elseif_stmt(self):

        localctx = GramParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(GramParser.ELSE)
            self.state = 103
            self.match(GramParser.IF)
            self.state = 104
            self.match(GramParser.LPAREN)
            self.state = 105
            self.expr(0)
            self.state = 106
            self.match(GramParser.RPAREN)
            self.state = 107
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GramParser.ELSE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_else_stmt




    def else_stmt(self):

        localctx = GramParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(GramParser.ELSE)
            self.state = 110
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL(self):
            return self.getToken(GramParser.DECL, 0)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(GramParser.Param_lstContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_func_decl




    def func_decl(self):

        localctx = GramParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(GramParser.DECL)
            self.state = 113
            self.match(GramParser.IDEN)
            self.state = 114
            self.param_lst()
            self.state = 115
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_func_call_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Sin_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(GramParser.SIN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)



    class Floor_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOORINTOF(self):
            return self.getToken(GramParser.FLOORINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)



    class Ceil_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEILINTOF(self):
            return self.getToken(GramParser.CEILINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)



    class Round_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROUNDINTOF(self):
            return self.getToken(GramParser.ROUNDINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)



    class Func_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)




    def func_call_expr(self):

        localctx = GramParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_call_expr)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                localctx = GramParser.Func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(GramParser.IDEN)
                self.state = 118
                self.arg_lst()
                pass
            elif token in [9]:
                localctx = GramParser.Sin_callContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(GramParser.SIN)
                self.state = 120
                self.arg_lst()
                pass
            elif token in [6]:
                localctx = GramParser.Floor_callContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(GramParser.FLOORINTOF)
                self.state = 122
                self.arg_lst()
                pass
            elif token in [7]:
                localctx = GramParser.Round_callContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(GramParser.ROUNDINTOF)
                self.state = 124
                self.arg_lst()
                pass
            elif token in [8]:
                localctx = GramParser.Ceil_callContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.match(GramParser.CEILINTOF)
                self.state = 126
                self.arg_lst()
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


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GramParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_while




    def while_(self):

        localctx = GramParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GramParser.WHILE)
            self.state = 130
            self.match(GramParser.LPAREN)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(GramParser.RPAREN)
            self.state = 133
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_assig

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assign_accessContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)
        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)
        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)



    class Assign_idenContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)
        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)




    def assig(self):

        localctx = GramParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assig)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assign_accessContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(GramParser.IDEN)
                self.state = 136
                self.match(GramParser.LBRACK)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(GramParser.RBRACK)
                self.state = 139
                self.match(GramParser.ASSIGN)
                self.state = 140
                self.assig_trgt()
                pass

            elif la_ == 2:
                localctx = GramParser.Assign_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(GramParser.IDEN)
                self.state = 143
                self.match(GramParser.ASSIGN)
                self.state = 144
                self.assig_trgt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_print

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Print_nlContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINTLN(self):
            return self.getToken(GramParser.PRINTLN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)



    class Print_baseContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(GramParser.PRINT, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)




    def print_(self):

        localctx = GramParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = GramParser.Print_baseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(GramParser.PRINT)
                self.state = 148
                self.arg_lst()
                pass
            elif token in [3]:
                localctx = GramParser.Print_nlContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(GramParser.PRINTLN)
                self.state = 150
                self.arg_lst()
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


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GramParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GramParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramParser.StmtContext,i)


        def ret_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.Ret_stmtContext)
            else:
                return self.getTypedRuleContext(GramParser.Ret_stmtContext,i)


        def getRuleIndex(self):
            return GramParser.RULE_stmt_block




    def stmt_block(self):

        localctx = GramParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(GramParser.LBRACE)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5497559982030) != 0):
                self.state = 156
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 18, 20, 40, 42]:
                    self.state = 154
                    self.stmt()
                    pass
                elif token in [19]:
                    self.state = 155
                    self.ret_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(GramParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET(self):
            return self.getToken(GramParser.RET, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def getRuleIndex(self):
            return GramParser.RULE_ret_stmt




    def ret_stmt(self):

        localctx = GramParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ret_stmt)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(GramParser.RET)
                self.state = 164
                self.expr(0)
                self.state = 165
                self.match(GramParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(GramParser.RET)
                self.state = 168
                self.match(GramParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Bool_expr_prefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(GramParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)



    class Expr_lst_declContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lst_decl(self):
            return self.getTypedRuleContext(GramParser.Lst_declContext,0)



    class Bool_expr_comp_mathContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def LESSTHAN(self):
            return self.getToken(GramParser.LESSTHAN, 0)
        def LESSTHANOREQUAL(self):
            return self.getToken(GramParser.LESSTHANOREQUAL, 0)
        def GREATERTHAN(self):
            return self.getToken(GramParser.GREATERTHAN, 0)
        def GREATERTHANOREQUAL(self):
            return self.getToken(GramParser.GREATERTHANOREQUAL, 0)


    class Expr_parenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)


    class Expr_spawnContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPAWN(self):
            return self.getToken(GramParser.SPAWN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)



    class Bool_expr_binaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def AND(self):
            return self.getToken(GramParser.AND, 0)
        def OR(self):
            return self.getToken(GramParser.OR, 0)


    class Expr_spawn_blockContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPAWN(self):
            return self.getToken(GramParser.SPAWN, 0)
        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)



    class Expr_idenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)


    class Expr_len_ofContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LENOF(self):
            return self.getToken(GramParser.LENOF, 0)
        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)


    class Expr_litContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(GramParser.LiteralContext,0)



    class Bool_expr_equalsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def EQUALS(self):
            return self.getToken(GramParser.EQUALS, 0)


    class Expr_accessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def idx_access(self):
            return self.getTypedRuleContext(GramParser.Idx_accessContext,0)



    class Expr_copy_ofContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COPYOF(self):
            return self.getToken(GramParser.COPYOF, 0)
        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)


    class Math_expr_binaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def POW(self):
            return self.getToken(GramParser.POW, 0)
        def TIMES(self):
            return self.getToken(GramParser.TIMES, 0)
        def DIV(self):
            return self.getToken(GramParser.DIV, 0)
        def PLUS(self):
            return self.getToken(GramParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(GramParser.MINUS, 0)


    class Expr_func_callContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)




    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = GramParser.Expr_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 172
                self.match(GramParser.LPAREN)
                self.state = 173
                self.expr(0)
                self.state = 174
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = GramParser.Expr_func_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 176
                self.func_call_expr()
                pass

            elif la_ == 3:
                localctx = GramParser.Expr_spawn_blockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(GramParser.SPAWN)
                self.state = 178
                self.stmt_block()
                pass

            elif la_ == 4:
                localctx = GramParser.Expr_spawnContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.match(GramParser.SPAWN)
                self.state = 180
                self.expr(13)
                pass

            elif la_ == 5:
                localctx = GramParser.Bool_expr_prefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.match(GramParser.NOT)
                self.state = 182
                self.expr(9)
                pass

            elif la_ == 6:
                localctx = GramParser.Expr_lst_declContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.lst_decl()
                pass

            elif la_ == 7:
                localctx = GramParser.Expr_litContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.literal()
                pass

            elif la_ == 8:
                localctx = GramParser.Expr_len_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(GramParser.LENOF)
                self.state = 186
                self.match(GramParser.LPAREN)
                self.state = 187
                self.expr(0)
                self.state = 188
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = GramParser.Expr_copy_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(GramParser.COPYOF)
                self.state = 191
                self.match(GramParser.LPAREN)
                self.state = 192
                self.expr(0)
                self.state = 193
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = GramParser.Expr_idenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(GramParser.IDEN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 218
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = GramParser.Bool_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 198
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 199
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = GramParser.Bool_expr_comp_mathContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 201
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = GramParser.Bool_expr_equalsContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 204
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 205
                        self.match(GramParser.EQUALS)
                        self.state = 206
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 207
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 208
                        self.match(GramParser.POW)
                        self.state = 209
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 210
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 211
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==30):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 212
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 213
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 214
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 215
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = GramParser.Expr_accessContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 216
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 217
                        self.idx_access()
                        pass

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Int_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GramParser.INT, 0)


    class Float_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GramParser.FLOAT, 0)


    class String_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(GramParser.STRING, 0)


    class Char_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(GramParser.CHAR, 0)


    class Bool_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(GramParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(GramParser.FALSE, 0)



    def literal(self):

        localctx = GramParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                localctx = GramParser.Int_litContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(GramParser.INT)
                pass
            elif token in [44]:
                localctx = GramParser.Float_litContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(GramParser.FLOAT)
                pass
            elif token in [45]:
                localctx = GramParser.Char_litContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(GramParser.CHAR)
                pass
            elif token in [13, 14]:
                localctx = GramParser.Bool_litContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [46]:
                localctx = GramParser.String_litContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.match(GramParser.STRING)
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


    class Lst_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_lst_decl




    def lst_decl(self):

        localctx = GramParser.Lst_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lst_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(GramParser.LBRACK)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 136683039287280) != 0):
                self.state = 231
                self.expr(0)


            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 234
                self.match(GramParser.COMMA)
                self.state = 235
                self.expr(0)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self.match(GramParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.IDEN)
            else:
                return self.getToken(GramParser.IDEN, i)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_param_lst




    def param_lst(self):

        localctx = GramParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(GramParser.LPAREN)
                self.state = 244
                self.match(GramParser.IDEN)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 245
                    self.match(GramParser.COMMA)
                    self.state = 246
                    self.match(GramParser.IDEN)
                    self.state = 251
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 252
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(GramParser.LPAREN)
                self.state = 254
                self.match(GramParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_arg_lst




    def arg_lst(self):

        localctx = GramParser.Arg_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arg_lst)
        self._la = 0 # Token type
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(GramParser.LPAREN)
                self.state = 258
                self.expr(0)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 259
                    self.match(GramParser.COMMA)
                    self.state = 260
                    self.expr(0)
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 266
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(GramParser.LPAREN)
                self.state = 269
                self.match(GramParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_idx_access

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Idx_access_oneContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)


    class Idx_access_fromContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)


    class Idx_access_untilContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)


    class Idx_access_rangeContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)



    def idx_access(self):

        localctx = GramParser.Idx_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idx_access)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = GramParser.Idx_access_oneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(GramParser.LBRACK)
                self.state = 273
                self.expr(0)
                self.state = 274
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 2:
                localctx = GramParser.Idx_access_fromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(GramParser.LBRACK)
                self.state = 277
                self.expr(0)
                self.state = 278
                self.match(GramParser.COLON)
                self.state = 279
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 3:
                localctx = GramParser.Idx_access_untilContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(GramParser.LBRACK)
                self.state = 282
                self.match(GramParser.COLON)
                self.state = 283
                self.expr(0)
                self.state = 284
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 4:
                localctx = GramParser.Idx_access_rangeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.match(GramParser.LBRACK)
                self.state = 287
                self.expr(0)
                self.state = 288
                self.match(GramParser.COLON)
                self.state = 289
                self.expr(0)
                self.state = 290
                self.match(GramParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 15)
         




