/* 
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
 * update Date: 06.22.2024 grammar MT22
*/

grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


//! --------------------------  Lexical structure ----------------------- //
/* @@@ TODO
    * Group : keyword
    * Description: code thì dễ thôi chỉ cần đặt tên và sau đó chuỗi giống ví dụ dưới
    * Example : break, for, false
    * Example code ANTLR :  STRING: 'string';
    * Assignment 232 
        auto break boolean do else
        false float for function if
        integer return string true while
        void out continue of inherit
        array
*/
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


/* @@@ TODO
    * Group : Operators
    * Description: code thì dễ thôi chỉ cần đặt tên và sau đó chuỗi giống ví dụ dưới
    * Example : +, <=, >=
    * Example code ANTLR :  NOT_EQUAL: '!=';
    * Assignment 232 
        + - * / %
        ! && || ==
        != < <= > >=
        ::
*/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
CONCAT: '::';


/* @@@ TODO
    * Group : Separators
    * Description: code thì dễ thôi chỉ cần đặt tên và sau đó chuỗi giống ví dụ dưới
    * Example : [, (, =
    * Example code ANTLR :  ASSIGNINIT: '=';
    * Assignment 232 
        ( ) [ ] . , ; : { } =
*/
LSB: '[';
RSB: ']';
LP: '(';
RP: ')';
CM: ',';
DOT: '.';
SC: ';';
COL: ':';
LCB: '{';
RCB: '}';
ASSIGNINIT: '=';


/* @@@ TODO
    * Name : Identifiers
    * Description: kí tự đầu tiên chỉ báo gồm a-z,A-Z,_ các kí tự tiếp theo có thể có thêm xóa (kích thước tên >= 1)
    * Example : Id, _1, _i, id, _, I, d
    * Example FAIL :  1_, for, if, $a, @c
*/
ID: [a-zA-Z_][a-zA-Z0-9_]*;


/* @@@ TODO
    * name : INTEGER Literal basic
    * Description: trường hợp không có _ thì lúc này kí tự gồm gì, trường có _ thì phần tử đầu tiên cho phép gì và các phần tử sau _ được phép gì
    * Example : 12 1_2 0 1_0_0
    * Example FAIL :  01 0_2 2_ _2
*/
INT_LIT: '0' | [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_", "")};

/* @@@ TODO
    * name : FLOAT Literal basic
    * Description: sử dung lại INT_LIT, nếu eE tồn tại thì bắt buộc phải có phần nguyên or phần thập phân, còn các trường hợp còn lại đều thõa nãn  
    * Example : luôn tồn tại 2 giá trị trong biểu thức
    * Example FAIL :  00.1 .1_2_3 e+1 e-1
*/
FLOAT_LIT: (INT_LIT OPT_FRAC OPT_EXP? | INT_LIT OPT_FRAC? OPT_EXP | INT_LIT? OPT_FRAC OPT_EXP)  {self.text = self.text.replace("_", "")};
fragment OPT_FRAC: '.' [0-9]*;
fragment OPT_EXP: [Ee] [+-]? [0-9]+;


/* @@@ TODO
    * name : STRING Literal basic
    * Description: Tìm kí tự cho phép  STRING_LIT: '"' kí tự cho phép* '"' {self.text = self.text[1:-1] };
*/
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1] };
fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt'"\\];
fragment ESC_ILLEGAL:  '\\' ~[bfrnt'"\\];



// TODO SKIP
COMMENTS: (('//' ~[\n]*) | ('/*' .*? '*/')) -> skip; // Comments
WS : [ \t\r\f\b\n]+ -> skip ; // skip spaces, tabs


// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

/* @@@ TODO
    * name : error
    * Description: tìm được phần cuối của UNCLOSE_STRING, ILLEGAL_ESCAPE => '"' kí tự cho phép* phần cuối {python }
*/
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[1:])
};

//!  -------------------------- end Lexical structure ------------------- //



// //! --------------------------  parser structure ----------------------- //

/* @@@ TODO
    * name : Declarations program
    * Description: program gồm list function và variables
*/
program: list_declared EOF;
list_declared:  declared list_declared |  declared;
declared: function | variables SC;

/* @@@ TODO
    * name : Variable declarations
    * Description: có 2 loại khai báo là khởi tạo và không khởi tạo
*/
variables:  variables_initialization | list_identifier COL all_types;
variables_initialization: ID CM  variables_initialization CM expression | ID COL all_types ASSIGNINIT expression;
list_identifier : ID CM list_identifier | ID;

/* @@@ TODO
    * name : all_types
    * Description: gồm int, float, bool, auto, array (trừ void)
*/
all_types: atomic_type | array_type | AUTO ;
atomic_type:  INTEGER | FLOAT | BOOLEAN | STRING;
array_type: ARRAY LSB dimensions RSB OF atomic_type;
dimensions: INT_LIT CM dimensions | INT_LIT;


/* @@@ TODO
    * name : function declare
    * Description: type của hàm có thể có void, param thì giống khai báo biến 
*/
function: ID COL FUNCTION (all_types  | VOID) LP prameters_list? RP (INHERIT ID)? block_statement; 
prameters_list: prameter CM prameters_list | prameter; 
prameter: INHERIT? OUT? ID COL all_types;


/* @@@ TODO
    * name : Expression, Value
    * Description: đọc pdf BTL1 anh đăng
*/
list_expression: expression CM list_expression | expression;
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT) expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: ID LSB list_expression RSB | expression8;
expression8: ID | literal | LP expression RP | ID LP list_expression? RP;
literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | array_literal;
array_literal: LCB list_expression? RCB;


/* @@@ TODO
    * name : Statements
    * Description: đọc pdf BTL1 anh đăng
*/
statement: ( assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement 
            | block_statement | while_statement | do_while_statement);
declaration_statement: variables SC;
assignment_statement: lhs ASSIGNINIT expression SC;
lhs: ID | ID LSB list_expression RSB;
if_statement: IF LP expression RP statement (ELSE statement)?;
for_statement: FOR LP lhs ASSIGNINIT expression CM expression CM expression RP statement;
while_statement: WHILE  LP expression RP statement;
do_while_statement: DO block_statement WHILE LP expression RP SC;
break_statement: BREAK SC;
continue_statement: CONTINUE SC;
return_statement: RETURN expression? SC;
call_statement: ID LP list_expression? RP SC;
block_statement: LCB list_statement? RCB; 

list_statement: (statement | declaration_statement) list_statement | statement | declaration_statement;



// //! -------------------------- end  parser structure ----------------------- //
