%{
#include "analisador.tab.h"
#include <string.h>

char texto[100];
%}

DIGITO [0-9]
LETRA [a-zA-Z]
IDR {LETRA}({LETRA}|{DIGITO})*

%%

"int"       { strcpy(texto, yytext); return INT; }
"while"     { strcpy(texto, yytext); return WHILE; }
"if"        { strcpy(texto, yytext); return IF; }
"else"      { strcpy(texto, yytext); return ELSE; }
"return"    { strcpy(texto, yytext); return RETURN; }

"!="        { strcpy(texto, yytext); return DIF; }
">"         { strcpy(texto, yytext); return MAIOR; }
"="         { strcpy(texto, yytext); return ATRIB; }
"-"         { strcpy(texto, yytext); return MENOS; }

"("         { return '('; }
")"         { return ')'; }
"{"         { return '{'; }
"}"         { return '}'; }
";"         { return ';'; }

{DIGITO}+   { strcpy(texto, yytext); return NUM; }
{IDR}       { strcpy(texto, yytext); return ID; }

[ \t\r\n]+ ;

. ;

%%

int yywrap()
{
    return 1;
}
