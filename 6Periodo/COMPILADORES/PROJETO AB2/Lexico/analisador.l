%{
#include <stdio.h>
%}

DIGITO [0-9]
LETRA [a-zA-Z]
ID {LETRA}({LETRA}|{DIGITO})*

%%

"int"       { printf("TOKEN: INT\n"); }
"while"     { printf("TOKEN: WHILE\n"); }
"if"        { printf("TOKEN: IF\n"); }
"else"      { printf("TOKEN: ELSE\n"); }
"return"    { printf("TOKEN: RETURN\n"); }

"!="        { printf("TOKEN: !=\n"); }
">"         { printf("TOKEN: >\n"); }
"="         { printf("TOKEN: =\n"); }
"-"         { printf("TOKEN: -\n"); }

"("         { printf("TOKEN: (\n"); }
")"         { printf("TOKEN: )\n"); }
"{"         { printf("TOKEN: {\n"); }
"}"         { printf("TOKEN: }\n"); }
";"         { printf("TOKEN: ;\n"); }

{DIGITO}+   { printf("NUMERO: %s\n", yytext); }
{ID}        { printf("IDENTIFICADOR: %s\n", yytext); }

[ \t\r\n]+ ;

. { printf("DESCONHECIDO: %s\n", yytext); }

%%

int main()
{
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
