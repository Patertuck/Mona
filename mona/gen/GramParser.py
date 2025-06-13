# Generated from GramParser.g4 by ANTLR 4.13.0
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
        4,1,48,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,3,2,78,8,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,5,4,87,8,4,10,4,12,4,90,9,4,1,4,3,4,93,8,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,126,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,144,8,11,1,12,1,12,1,12,1,12,3,12,150,8,12,1,13,1,13,1,
        13,5,13,155,8,13,10,13,12,13,158,9,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,3,14,168,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,3,15,193,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,
        15,215,8,15,10,15,12,15,218,9,15,1,16,1,16,1,16,1,16,1,16,3,16,225,
        8,16,1,17,1,17,3,17,229,8,17,1,17,1,17,5,17,233,8,17,10,17,12,17,
        236,9,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,244,8,18,10,18,12,18,
        247,9,18,1,18,1,18,1,18,3,18,252,8,18,1,19,1,19,1,19,1,19,5,19,258,
        8,19,10,19,12,19,261,9,19,1,19,1,19,1,19,1,19,3,19,267,8,19,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,3,20,289,8,20,1,20,0,1,30,21,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,5,1,0,16,17,
        1,0,31,34,2,0,28,28,30,30,1,0,26,27,1,0,13,14,320,0,45,1,0,0,0,2,
        73,1,0,0,0,4,77,1,0,0,0,6,79,1,0,0,0,8,84,1,0,0,0,10,94,1,0,0,0,
        12,100,1,0,0,0,14,107,1,0,0,0,16,110,1,0,0,0,18,125,1,0,0,0,20,127,
        1,0,0,0,22,143,1,0,0,0,24,149,1,0,0,0,26,151,1,0,0,0,28,167,1,0,
        0,0,30,192,1,0,0,0,32,224,1,0,0,0,34,226,1,0,0,0,36,251,1,0,0,0,
        38,266,1,0,0,0,40,288,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,
        48,50,5,0,0,1,49,48,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,52,3,6,
        3,0,52,53,5,23,0,0,53,74,1,0,0,0,54,74,3,8,4,0,55,74,3,16,8,0,56,
        57,3,18,9,0,57,58,5,23,0,0,58,74,1,0,0,0,59,74,3,20,10,0,60,61,3,
        22,11,0,61,62,5,23,0,0,62,74,1,0,0,0,63,64,3,24,12,0,64,65,5,23,
        0,0,65,74,1,0,0,0,66,67,3,26,13,0,67,68,5,23,0,0,68,74,1,0,0,0,69,
        70,5,10,0,0,70,74,3,26,13,0,71,72,5,11,0,0,72,74,5,23,0,0,73,51,
        1,0,0,0,73,54,1,0,0,0,73,55,1,0,0,0,73,56,1,0,0,0,73,59,1,0,0,0,
        73,60,1,0,0,0,73,63,1,0,0,0,73,66,1,0,0,0,73,69,1,0,0,0,73,71,1,
        0,0,0,74,3,1,0,0,0,75,78,3,30,15,0,76,78,5,42,0,0,77,75,1,0,0,0,
        77,76,1,0,0,0,78,5,1,0,0,0,79,80,5,1,0,0,80,81,5,42,0,0,81,82,5,
        22,0,0,82,83,3,4,2,0,83,7,1,0,0,0,84,88,3,10,5,0,85,87,3,12,6,0,
        86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,92,1,
        0,0,0,90,88,1,0,0,0,91,93,3,14,7,0,92,91,1,0,0,0,92,93,1,0,0,0,93,
        9,1,0,0,0,94,95,5,20,0,0,95,96,5,36,0,0,96,97,3,30,15,0,97,98,5,
        37,0,0,98,99,3,26,13,0,99,11,1,0,0,0,100,101,5,21,0,0,101,102,5,
        20,0,0,102,103,5,36,0,0,103,104,3,30,15,0,104,105,5,37,0,0,105,106,
        3,26,13,0,106,13,1,0,0,0,107,108,5,21,0,0,108,109,3,26,13,0,109,
        15,1,0,0,0,110,111,5,18,0,0,111,112,5,42,0,0,112,113,3,36,18,0,113,
        114,3,26,13,0,114,17,1,0,0,0,115,116,5,42,0,0,116,126,3,38,19,0,
        117,118,5,9,0,0,118,126,3,38,19,0,119,120,5,6,0,0,120,126,3,38,19,
        0,121,122,5,7,0,0,122,126,3,38,19,0,123,124,5,8,0,0,124,126,3,38,
        19,0,125,115,1,0,0,0,125,117,1,0,0,0,125,119,1,0,0,0,125,121,1,0,
        0,0,125,123,1,0,0,0,126,19,1,0,0,0,127,128,5,12,0,0,128,129,5,36,
        0,0,129,130,3,30,15,0,130,131,5,37,0,0,131,132,3,26,13,0,132,21,
        1,0,0,0,133,134,5,42,0,0,134,135,5,38,0,0,135,136,3,30,15,0,136,
        137,5,39,0,0,137,138,5,22,0,0,138,139,3,4,2,0,139,144,1,0,0,0,140,
        141,5,42,0,0,141,142,5,22,0,0,142,144,3,4,2,0,143,133,1,0,0,0,143,
        140,1,0,0,0,144,23,1,0,0,0,145,146,5,2,0,0,146,150,3,38,19,0,147,
        148,5,3,0,0,148,150,3,38,19,0,149,145,1,0,0,0,149,147,1,0,0,0,150,
        25,1,0,0,0,151,156,5,40,0,0,152,155,3,2,1,0,153,155,3,28,14,0,154,
        152,1,0,0,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,
        157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,5,41,0,0,160,
        27,1,0,0,0,161,162,5,19,0,0,162,163,3,30,15,0,163,164,5,23,0,0,164,
        168,1,0,0,0,165,166,5,19,0,0,166,168,5,23,0,0,167,161,1,0,0,0,167,
        165,1,0,0,0,168,29,1,0,0,0,169,170,6,15,-1,0,170,171,5,36,0,0,171,
        172,3,30,15,0,172,173,5,37,0,0,173,193,1,0,0,0,174,193,3,18,9,0,
        175,176,5,10,0,0,176,193,3,30,15,13,177,178,5,15,0,0,178,193,3,30,
        15,9,179,193,3,34,17,0,180,193,3,32,16,0,181,182,5,4,0,0,182,183,
        5,36,0,0,183,184,3,30,15,0,184,185,5,37,0,0,185,193,1,0,0,0,186,
        187,5,5,0,0,187,188,5,36,0,0,188,189,3,30,15,0,189,190,5,37,0,0,
        190,193,1,0,0,0,191,193,5,42,0,0,192,169,1,0,0,0,192,174,1,0,0,0,
        192,175,1,0,0,0,192,177,1,0,0,0,192,179,1,0,0,0,192,180,1,0,0,0,
        192,181,1,0,0,0,192,186,1,0,0,0,192,191,1,0,0,0,193,216,1,0,0,0,
        194,195,10,12,0,0,195,196,7,0,0,0,196,215,3,30,15,13,197,198,10,
        11,0,0,198,199,7,1,0,0,199,215,3,30,15,12,200,201,10,10,0,0,201,
        202,5,35,0,0,202,215,3,30,15,11,203,204,10,8,0,0,204,205,5,29,0,
        0,205,215,3,30,15,9,206,207,10,7,0,0,207,208,7,2,0,0,208,215,3,30,
        15,8,209,210,10,6,0,0,210,211,7,3,0,0,211,215,3,30,15,7,212,213,
        10,14,0,0,213,215,3,40,20,0,214,194,1,0,0,0,214,197,1,0,0,0,214,
        200,1,0,0,0,214,203,1,0,0,0,214,206,1,0,0,0,214,209,1,0,0,0,214,
        212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        31,1,0,0,0,218,216,1,0,0,0,219,225,5,43,0,0,220,225,5,44,0,0,221,
        225,5,45,0,0,222,225,7,4,0,0,223,225,5,46,0,0,224,219,1,0,0,0,224,
        220,1,0,0,0,224,221,1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,
        33,1,0,0,0,226,228,5,38,0,0,227,229,3,30,15,0,228,227,1,0,0,0,228,
        229,1,0,0,0,229,234,1,0,0,0,230,231,5,25,0,0,231,233,3,30,15,0,232,
        230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,
        237,1,0,0,0,236,234,1,0,0,0,237,238,5,39,0,0,238,35,1,0,0,0,239,
        240,5,36,0,0,240,245,5,42,0,0,241,242,5,25,0,0,242,244,5,42,0,0,
        243,241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,
        246,248,1,0,0,0,247,245,1,0,0,0,248,252,5,37,0,0,249,250,5,36,0,
        0,250,252,5,37,0,0,251,239,1,0,0,0,251,249,1,0,0,0,252,37,1,0,0,
        0,253,254,5,36,0,0,254,259,3,30,15,0,255,256,5,25,0,0,256,258,3,
        30,15,0,257,255,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,
        1,0,0,0,260,262,1,0,0,0,261,259,1,0,0,0,262,263,5,37,0,0,263,267,
        1,0,0,0,264,265,5,36,0,0,265,267,5,37,0,0,266,253,1,0,0,0,266,264,
        1,0,0,0,267,39,1,0,0,0,268,269,5,38,0,0,269,270,3,30,15,0,270,271,
        5,39,0,0,271,289,1,0,0,0,272,273,5,38,0,0,273,274,3,30,15,0,274,
        275,5,24,0,0,275,276,5,39,0,0,276,289,1,0,0,0,277,278,5,38,0,0,278,
        279,5,24,0,0,279,280,3,30,15,0,280,281,5,39,0,0,281,289,1,0,0,0,
        282,283,5,38,0,0,283,284,3,30,15,0,284,285,5,24,0,0,285,286,3,30,
        15,0,286,287,5,39,0,0,287,289,1,0,0,0,288,268,1,0,0,0,288,272,1,
        0,0,0,288,277,1,0,0,0,288,282,1,0,0,0,289,41,1,0,0,0,23,45,49,73,
        77,88,92,125,143,149,154,156,167,192,214,216,224,228,234,245,251,
        259,266,288
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
        self.checkVersion("4.13.0")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_if_block" ):
                listener.enterStmt_if_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_if_block" ):
                listener.exitStmt_if_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if_block" ):
                return visitor.visitStmt_if_block(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_stmt_blockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_stmt_block" ):
                listener.enterStmt_stmt_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_stmt_block" ):
                listener.exitStmt_stmt_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_stmt_block" ):
                return visitor.visitStmt_stmt_block(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_func_declContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_decl(self):
            return self.getTypedRuleContext(GramParser.Func_declContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_func_decl" ):
                listener.enterStmt_func_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_func_decl" ):
                listener.exitStmt_func_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_decl" ):
                return visitor.visitStmt_func_decl(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_assigContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assig(self):
            return self.getTypedRuleContext(GramParser.AssigContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_assig" ):
                listener.enterStmt_assig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_assig" ):
                listener.exitStmt_assig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assig" ):
                return visitor.visitStmt_assig(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_whileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_(self):
            return self.getTypedRuleContext(GramParser.WhileContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_while" ):
                listener.enterStmt_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_while" ):
                listener.exitStmt_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_while" ):
                return visitor.visitStmt_while(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_func_callContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_func_call" ):
                listener.enterStmt_func_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_func_call" ):
                listener.exitStmt_func_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_printContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_(self):
            return self.getTypedRuleContext(GramParser.PrintContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_print" ):
                listener.enterStmt_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_print" ):
                listener.exitStmt_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_print" ):
                return visitor.visitStmt_print(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_spawnContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPAWN(self):
            return self.getToken(GramParser.SPAWN, 0)
        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_spawn" ):
                listener.enterStmt_spawn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_spawn" ):
                listener.exitStmt_spawn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_spawn" ):
                return visitor.visitStmt_spawn(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_joinContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JOIN(self):
            return self.getToken(GramParser.JOIN, 0)
        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_join" ):
                listener.enterStmt_join(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_join" ):
                listener.exitStmt_join(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_join" ):
                return visitor.visitStmt_join(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_var_declrContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var_declr(self):
            return self.getTypedRuleContext(GramParser.Var_declrContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_var_declr" ):
                listener.enterStmt_var_declr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_var_declr" ):
                listener.exitStmt_var_declr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declr" ):
                return visitor.visitStmt_var_declr(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = GramParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 73
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
                pass

            elif la_ == 10:
                localctx = GramParser.Stmt_joinContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 71
                self.match(GramParser.JOIN)
                self.state = 72
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssig_trgt_expr" ):
                listener.enterAssig_trgt_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssig_trgt_expr" ):
                listener.exitAssig_trgt_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig_trgt_expr" ):
                return visitor.visitAssig_trgt_expr(self)
            else:
                return visitor.visitChildren(self)


    class Assig_trgt_idenContext(Assig_trgtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Assig_trgtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssig_trgt_iden" ):
                listener.enterAssig_trgt_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssig_trgt_iden" ):
                listener.exitAssig_trgt_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig_trgt_iden" ):
                return visitor.visitAssig_trgt_iden(self)
            else:
                return visitor.visitChildren(self)



    def assig_trgt(self):

        localctx = GramParser.Assig_trgtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig_trgt)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assig_trgt_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = GramParser.Assig_trgt_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declr" ):
                listener.enterVar_declr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declr" ):
                listener.exitVar_declr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declr" ):
                return visitor.visitVar_declr(self)
            else:
                return visitor.visitChildren(self)




    def var_declr(self):

        localctx = GramParser.Var_declrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(GramParser.VAR)
            self.state = 80
            self.match(GramParser.IDEN)
            self.state = 81
            self.match(GramParser.ASSIGN)
            self.state = 82
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_block" ):
                return visitor.visitIf_block(self)
            else:
                return visitor.visitChildren(self)




    def if_block(self):

        localctx = GramParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.if_stmt()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 85
                    self.elseif_stmt() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 91
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = GramParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GramParser.IF)
            self.state = 95
            self.match(GramParser.LPAREN)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(GramParser.RPAREN)
            self.state = 98
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_stmt" ):
                listener.enterElseif_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_stmt" ):
                listener.exitElseif_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = GramParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GramParser.ELSE)
            self.state = 101
            self.match(GramParser.IF)
            self.state = 102
            self.match(GramParser.LPAREN)
            self.state = 103
            self.expr(0)
            self.state = 104
            self.match(GramParser.RPAREN)
            self.state = 105
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = GramParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GramParser.ELSE)
            self.state = 108
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = GramParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GramParser.DECL)
            self.state = 111
            self.match(GramParser.IDEN)
            self.state = 112
            self.param_lst()
            self.state = 113
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin_call" ):
                listener.enterSin_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin_call" ):
                listener.exitSin_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSin_call" ):
                return visitor.visitSin_call(self)
            else:
                return visitor.visitChildren(self)


    class Floor_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOORINTOF(self):
            return self.getToken(GramParser.FLOORINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_call" ):
                listener.enterFloor_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_call" ):
                listener.exitFloor_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloor_call" ):
                return visitor.visitFloor_call(self)
            else:
                return visitor.visitChildren(self)


    class Ceil_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEILINTOF(self):
            return self.getToken(GramParser.CEILINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeil_call" ):
                listener.enterCeil_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeil_call" ):
                listener.exitCeil_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeil_call" ):
                return visitor.visitCeil_call(self)
            else:
                return visitor.visitChildren(self)


    class Round_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROUNDINTOF(self):
            return self.getToken(GramParser.ROUNDINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRound_call" ):
                listener.enterRound_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRound_call" ):
                listener.exitRound_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRound_call" ):
                return visitor.visitRound_call(self)
            else:
                return visitor.visitChildren(self)


    class Func_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)



    def func_call_expr(self):

        localctx = GramParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_call_expr)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                localctx = GramParser.Func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(GramParser.IDEN)
                self.state = 116
                self.arg_lst()
                pass
            elif token in [9]:
                localctx = GramParser.Sin_callContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(GramParser.SIN)
                self.state = 118
                self.arg_lst()
                pass
            elif token in [6]:
                localctx = GramParser.Floor_callContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(GramParser.FLOORINTOF)
                self.state = 120
                self.arg_lst()
                pass
            elif token in [7]:
                localctx = GramParser.Round_callContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(GramParser.ROUNDINTOF)
                self.state = 122
                self.arg_lst()
                pass
            elif token in [8]:
                localctx = GramParser.Ceil_callContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.match(GramParser.CEILINTOF)
                self.state = 124
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = GramParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(GramParser.WHILE)
            self.state = 128
            self.match(GramParser.LPAREN)
            self.state = 129
            self.expr(0)
            self.state = 130
            self.match(GramParser.RPAREN)
            self.state = 131
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_access" ):
                listener.enterAssign_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_access" ):
                listener.exitAssign_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_access" ):
                return visitor.visitAssign_access(self)
            else:
                return visitor.visitChildren(self)


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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_iden" ):
                listener.enterAssign_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_iden" ):
                listener.exitAssign_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_iden" ):
                return visitor.visitAssign_iden(self)
            else:
                return visitor.visitChildren(self)



    def assig(self):

        localctx = GramParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assig)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assign_accessContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(GramParser.IDEN)
                self.state = 134
                self.match(GramParser.LBRACK)
                self.state = 135
                self.expr(0)
                self.state = 136
                self.match(GramParser.RBRACK)
                self.state = 137
                self.match(GramParser.ASSIGN)
                self.state = 138
                self.assig_trgt()
                pass

            elif la_ == 2:
                localctx = GramParser.Assign_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(GramParser.IDEN)
                self.state = 141
                self.match(GramParser.ASSIGN)
                self.state = 142
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_nl" ):
                listener.enterPrint_nl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_nl" ):
                listener.exitPrint_nl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_nl" ):
                return visitor.visitPrint_nl(self)
            else:
                return visitor.visitChildren(self)


    class Print_baseContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(GramParser.PRINT, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_base" ):
                listener.enterPrint_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_base" ):
                listener.exitPrint_base(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_base" ):
                return visitor.visitPrint_base(self)
            else:
                return visitor.visitChildren(self)



    def print_(self):

        localctx = GramParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = GramParser.Print_baseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(GramParser.PRINT)
                self.state = 146
                self.arg_lst()
                pass
            elif token in [3]:
                localctx = GramParser.Print_nlContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(GramParser.PRINTLN)
                self.state = 148
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_block" ):
                listener.enterStmt_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_block" ):
                listener.exitStmt_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = GramParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(GramParser.LBRACE)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5497559982030) != 0):
                self.state = 154
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 18, 20, 40, 42]:
                    self.state = 152
                    self.stmt()
                    pass
                elif token in [19]:
                    self.state = 153
                    self.ret_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet_stmt" ):
                listener.enterRet_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet_stmt" ):
                listener.exitRet_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet_stmt" ):
                return visitor.visitRet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ret_stmt(self):

        localctx = GramParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ret_stmt)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(GramParser.RET)
                self.state = 162
                self.expr(0)
                self.state = 163
                self.match(GramParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(GramParser.RET)
                self.state = 166
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_pref" ):
                listener.enterBool_expr_pref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_pref" ):
                listener.exitBool_expr_pref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_pref" ):
                return visitor.visitBool_expr_pref(self)
            else:
                return visitor.visitChildren(self)


    class Expr_lst_declContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lst_decl(self):
            return self.getTypedRuleContext(GramParser.Lst_declContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_lst_decl" ):
                listener.enterExpr_lst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_lst_decl" ):
                listener.exitExpr_lst_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst_decl" ):
                return visitor.visitExpr_lst_decl(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_comp_math" ):
                listener.enterBool_expr_comp_math(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_comp_math" ):
                listener.exitBool_expr_comp_math(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_comp_math" ):
                return visitor.visitBool_expr_comp_math(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_paren" ):
                listener.enterExpr_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_paren" ):
                listener.exitExpr_paren(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_paren" ):
                return visitor.visitExpr_paren(self)
            else:
                return visitor.visitChildren(self)


    class Expr_spawnContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPAWN(self):
            return self.getToken(GramParser.SPAWN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_spawn" ):
                listener.enterExpr_spawn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_spawn" ):
                listener.exitExpr_spawn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_spawn" ):
                return visitor.visitExpr_spawn(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_binary" ):
                listener.enterBool_expr_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_binary" ):
                listener.exitBool_expr_binary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_binary" ):
                return visitor.visitBool_expr_binary(self)
            else:
                return visitor.visitChildren(self)


    class Expr_idenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_iden" ):
                listener.enterExpr_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_iden" ):
                listener.exitExpr_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_iden" ):
                return visitor.visitExpr_iden(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_len_of" ):
                listener.enterExpr_len_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_len_of" ):
                listener.exitExpr_len_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_len_of" ):
                return visitor.visitExpr_len_of(self)
            else:
                return visitor.visitChildren(self)


    class Expr_litContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(GramParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_lit" ):
                listener.enterExpr_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_lit" ):
                listener.exitExpr_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lit" ):
                return visitor.visitExpr_lit(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_equals" ):
                listener.enterBool_expr_equals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_equals" ):
                listener.exitBool_expr_equals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_equals" ):
                return visitor.visitBool_expr_equals(self)
            else:
                return visitor.visitChildren(self)


    class Expr_accessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def idx_access(self):
            return self.getTypedRuleContext(GramParser.Idx_accessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_access" ):
                listener.enterExpr_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_access" ):
                listener.exitExpr_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_access" ):
                return visitor.visitExpr_access(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_copy_of" ):
                listener.enterExpr_copy_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_copy_of" ):
                listener.exitExpr_copy_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_copy_of" ):
                return visitor.visitExpr_copy_of(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expr_binary" ):
                listener.enterMath_expr_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expr_binary" ):
                listener.exitMath_expr_binary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expr_binary" ):
                return visitor.visitMath_expr_binary(self)
            else:
                return visitor.visitChildren(self)


    class Expr_func_callContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_func_call" ):
                listener.enterExpr_func_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_func_call" ):
                listener.exitExpr_func_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_func_call" ):
                return visitor.visitExpr_func_call(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = GramParser.Expr_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 170
                self.match(GramParser.LPAREN)
                self.state = 171
                self.expr(0)
                self.state = 172
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = GramParser.Expr_func_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.func_call_expr()
                pass

            elif la_ == 3:
                localctx = GramParser.Expr_spawnContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(GramParser.SPAWN)
                self.state = 176
                self.expr(13)
                pass

            elif la_ == 4:
                localctx = GramParser.Bool_expr_prefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(GramParser.NOT)
                self.state = 178
                self.expr(9)
                pass

            elif la_ == 5:
                localctx = GramParser.Expr_lst_declContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.lst_decl()
                pass

            elif la_ == 6:
                localctx = GramParser.Expr_litContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.literal()
                pass

            elif la_ == 7:
                localctx = GramParser.Expr_len_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.match(GramParser.LENOF)
                self.state = 182
                self.match(GramParser.LPAREN)
                self.state = 183
                self.expr(0)
                self.state = 184
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 8:
                localctx = GramParser.Expr_copy_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 186
                self.match(GramParser.COPYOF)
                self.state = 187
                self.match(GramParser.LPAREN)
                self.state = 188
                self.expr(0)
                self.state = 189
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = GramParser.Expr_idenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.match(GramParser.IDEN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 214
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = GramParser.Bool_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 195
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = GramParser.Bool_expr_comp_mathContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 198
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = GramParser.Bool_expr_equalsContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 201
                        self.match(GramParser.EQUALS)
                        self.state = 202
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 204
                        self.match(GramParser.POW)
                        self.state = 205
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 207
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==30):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 210
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = GramParser.Expr_accessContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 213
                        self.idx_access()
                        pass

             
                self.state = 218
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_lit" ):
                listener.enterInt_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_lit" ):
                listener.exitInt_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)


    class Float_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GramParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_lit" ):
                listener.enterFloat_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_lit" ):
                listener.exitFloat_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)


    class String_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(GramParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_lit" ):
                listener.enterString_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_lit" ):
                listener.exitString_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_lit" ):
                return visitor.visitString_lit(self)
            else:
                return visitor.visitChildren(self)


    class Char_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(GramParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_lit" ):
                listener.enterChar_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_lit" ):
                listener.exitChar_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar_lit" ):
                return visitor.visitChar_lit(self)
            else:
                return visitor.visitChildren(self)


    class Bool_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(GramParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(GramParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_lit" ):
                listener.enterBool_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_lit" ):
                listener.exitBool_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = GramParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                localctx = GramParser.Int_litContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(GramParser.INT)
                pass
            elif token in [44]:
                localctx = GramParser.Float_litContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(GramParser.FLOAT)
                pass
            elif token in [45]:
                localctx = GramParser.Char_litContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(GramParser.CHAR)
                pass
            elif token in [13, 14]:
                localctx = GramParser.Bool_litContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 222
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
                self.state = 223
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLst_decl" ):
                listener.enterLst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLst_decl" ):
                listener.exitLst_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_decl" ):
                return visitor.visitLst_decl(self)
            else:
                return visitor.visitChildren(self)




    def lst_decl(self):

        localctx = GramParser.Lst_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lst_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(GramParser.LBRACK)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 136683039287280) != 0):
                self.state = 227
                self.expr(0)


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 230
                self.match(GramParser.COMMA)
                self.state = 231
                self.expr(0)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_lst" ):
                listener.enterParam_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_lst" ):
                listener.exitParam_lst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = GramParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(GramParser.LPAREN)
                self.state = 240
                self.match(GramParser.IDEN)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 241
                    self.match(GramParser.COMMA)
                    self.state = 242
                    self.match(GramParser.IDEN)
                    self.state = 247
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 248
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(GramParser.LPAREN)
                self.state = 250
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_lst" ):
                listener.enterArg_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_lst" ):
                listener.exitArg_lst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_lst" ):
                return visitor.visitArg_lst(self)
            else:
                return visitor.visitChildren(self)




    def arg_lst(self):

        localctx = GramParser.Arg_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arg_lst)
        self._la = 0 # Token type
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(GramParser.LPAREN)
                self.state = 254
                self.expr(0)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 255
                    self.match(GramParser.COMMA)
                    self.state = 256
                    self.expr(0)
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 262
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(GramParser.LPAREN)
                self.state = 265
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_one" ):
                listener.enterIdx_access_one(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_one" ):
                listener.exitIdx_access_one(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_one" ):
                return visitor.visitIdx_access_one(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_from" ):
                listener.enterIdx_access_from(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_from" ):
                listener.exitIdx_access_from(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_from" ):
                return visitor.visitIdx_access_from(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_until" ):
                listener.enterIdx_access_until(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_until" ):
                listener.exitIdx_access_until(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_until" ):
                return visitor.visitIdx_access_until(self)
            else:
                return visitor.visitChildren(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_range" ):
                listener.enterIdx_access_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_range" ):
                listener.exitIdx_access_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_range" ):
                return visitor.visitIdx_access_range(self)
            else:
                return visitor.visitChildren(self)



    def idx_access(self):

        localctx = GramParser.Idx_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idx_access)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = GramParser.Idx_access_oneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(GramParser.LBRACK)
                self.state = 269
                self.expr(0)
                self.state = 270
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 2:
                localctx = GramParser.Idx_access_fromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(GramParser.LBRACK)
                self.state = 273
                self.expr(0)
                self.state = 274
                self.match(GramParser.COLON)
                self.state = 275
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 3:
                localctx = GramParser.Idx_access_untilContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.match(GramParser.LBRACK)
                self.state = 278
                self.match(GramParser.COLON)
                self.state = 279
                self.expr(0)
                self.state = 280
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 4:
                localctx = GramParser.Idx_access_rangeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(GramParser.LBRACK)
                self.state = 283
                self.expr(0)
                self.state = 284
                self.match(GramParser.COLON)
                self.state = 285
                self.expr(0)
                self.state = 286
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
                return self.precpred(self._ctx, 14)
         




