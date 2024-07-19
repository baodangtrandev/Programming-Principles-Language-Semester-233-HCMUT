

grammar MT22;
// Trần Đăng Bảo 2210270
@lexer::header {
from lexererr import *
# 2210270 Trần Đăng Bảo
}

options {
	language=Python3;
}

// --------------------------  Lexical structure -----------------------

fragment CPPCOMMENT: '//' (~[\r\n])*;
fragment CCOMMENT: '/*' .*? '*/';

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';
fragment INTPART: '0' | [1-9] DIGIT* (UNDERSCORE DIGIT+)*;
fragment FRACPART: '.' DIGIT*;
fragment SIGN: '+' | '-';
fragment EXPPART: ('e' | 'E') SIGN? DIGIT+;
fragment NESCAPE: '\\' ~[btnfr"'\\];
fragment STR: (~[\n\\"] | ESCAPE);
fragment ESCAPE: '\\' [bfrnt'"\\] | '\'"';
fragment TWO_QUOTE: '"';



    AUTO: 'auto';
    BREAK: 'break';
    BOOLEAN: 'boolean';
    DO: 'do';
    ELSE: 'else';
    FALSE: 'false';
    FLOAT: 'float';
    FOR: 'for';
    FUNCTION: 'function';
    IF: 'if';
    INTEGER: 'integer';
    RETURN: 'return';
    STRING: 'string';
    TRUE: 'true';
    WHILE: 'while';
    VOID: 'void';
    OUT: 'out';
    CONTINUE: 'continue';
    OF: 'of';
    INHERIT: 'inherit';
    ARRAY: 'array';



    ADD: '+';
    MINUS: '-';
    MUL: '*';
    DIV: '/';
    MOD: '%';
    NOT: '!';
    AND: '&&';
    OR: '||';
    EQUAL: '==';
    NOT_EQUAL: '!=';
    LESS_THAN: '<';
    LESS_EQUAL: '<=';
    GREATER_THAN: '>';
    GREATER_EQUAL: '>=';
    TWO_COLON: '::';


    LP: '(';
    RP: ')';
    LSB: '[';
    RSB: ']';
    DOT: '.';
    COMMA: ',';
    SEMI: ';';
    COLON: ':';
    LB: '{';
    RB: '}';
    ASSIGN: '=';


// 3.4 IDENTIFIERS
IDENTIFIER: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;



INTLIT: INTPART {self.text = self.text.replace("_","")};
FLOATLIT: ( INTPART FRACPART EXPPART? | INTPART EXPPART | FRACPART EXPPART) {self.text = self.text.replace("_","")};
BOOLEAN_LIT: TRUE | FALSE;
STRING_LIT: TWO_QUOTE STR*? TWO_QUOTE {self.text = str(self.text[1:-1])};




COMMENT: (CPPCOMMENT | CCOMMENT) -> skip;
WS : [ \t\r\f\b\n]+ -> skip ; // skip spaces, tabs



UNCLOSE_STRING: TWO_QUOTE (~[\r\n\\"] | ESCAPE )* ('\r\n' | '\n' | EOF) {
    if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: TWO_QUOTE (~[\r\n\\"] | ESCAPE )* ([\r] | NESCAPE) {
    raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};


//  -------------------------- End Lexical structure -------------------------------



//  -------------------------- syntax analyzer structure -----------------------

program: list_declared EOF;



list_declared: declaration list_declared | declaration;

declaration: var_declaration | function_declaration;

var_declaration: (var_decl_non_assign | var_decl_assign) SEMI;
var_decl_non_assign: identifier_list COLON type_;
var_decl_assign: IDENTIFIER COMMA var_decl_assign COMMA expression | IDENTIFIER COLON type_ ASSIGN expression;
identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;


type_: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | array_type;

type_n_auto: BOOLEAN | INTEGER | FLOAT | STRING;
array_type: ARRAY LSB dimensions RSB OF type_n_auto;
dimensions: INTLIT COMMA dimensions | INTLIT;


parameter_list: parameter_prime | ;
parameter_prime: parameter COMMA parameter_prime | parameter;
parameter: INHERIT? OUT? IDENTIFIER COLON type_;


function_declaration: IDENTIFIER COLON FUNCTION return_type LP parameter_list RP inherit_function? block_statement;
return_type: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO | array_type;
inherit_function: INHERIT IDENTIFIER;




expression: expression1 TWO_COLON expression1 | expression1;
expression1: expression2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | MINUS) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: (MINUS | ADD) expression6 | expression7;
expression7: index_operator | expression8;
expression8: LP expression RP | factor;
factor: INTLIT | FLOATLIT | TRUE | FALSE | STRING_LIT | IDENTIFIER
 | function_call | array_literal;

array_literal: LB exp_list RB;
exp_list: exp_prime | ;
exp_prime: expression COMMA exp_prime | expression;
index_operator: IDENTIFIER LSB (exp_prime) RSB;


statement: var_declaration | assign_statement | if_statement | for_statement | while_statement | dowhile_statement 
| break_statement | continue_statement | return_statement | call_statement | block_statement;


assign_statement: lhs ASSIGN expression SEMI;
lhs: IDENTIFIER LSB exp_prime RSB | IDENTIFIER;

if_statement: IF LP expression RP statement (ELSE statement)?;

for_statement: FOR LP scalar_var ASSIGN expression COMMA expression COMMA  expression RP statement;

scalar_var: IDENTIFIER | IDENTIFIER LSB expression RSB;

while_statement: WHILE LP expression RP statement;

dowhile_statement: DO block_statement WHILE LP expression RP SEMI;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

return_statement: RETURN expression? SEMI;

call_statement: function_call SEMI;
function_call: IDENTIFIER LP exp_list RP;


block_statement: LB statement_list RB; 
statement_list: statement_prime | ;
statement_prime: statement statement_list | statement;


// -------------------------- End syntax analyzer structure ----------------------- //