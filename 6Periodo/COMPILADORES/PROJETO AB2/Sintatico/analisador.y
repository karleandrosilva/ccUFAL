%code requires {
    typedef struct Node {
        char nome[50];
        struct Node *filho1;
        struct Node *filho2;
        struct Node *filho3;
    } Node;
}

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* duplicado propositalmente */
typedef struct Node {
    char nome[50];
    struct Node *filho1;
    struct Node *filho2;
    struct Node *filho3;
} Node;

Node* criar_no(char *nome, Node *f1, Node *f2, Node *f3)
{
    Node *novo = (Node*) malloc(sizeof(Node));

    strcpy(novo->nome, nome);
    novo->filho1 = f1;
    novo->filho2 = f2;
    novo->filho3 = f3;

    return novo;
}

void imprimir_arvore(Node *raiz, int nivel)
{
    if (raiz == NULL)
        return;

    for(int i = 0; i < nivel; i++)
        printf("    ");

    printf("%s\n", raiz->nome);

    imprimir_arvore(raiz->filho1, nivel + 1);
    imprimir_arvore(raiz->filho2, nivel + 1);
    imprimir_arvore(raiz->filho3, nivel + 1);
}

void yyerror(const char *s);
int yylex();

Node *raiz_final;
%}

%union {
    Node *node;
}

%token INT WHILE IF ELSE RETURN ID NUM DIF MAIOR ATRIB MENOS

%type <node> programa funcao bloco declaracoes declaracao comandos comando atribuicao expressao repeticao condicional

%%

programa:
    funcao
    {
        raiz_final = criar_no("Programa", $1, NULL, NULL);
    }
;

funcao:
    INT ID '(' ')' bloco
    {
        $$ = criar_no("Funcao main", $5, NULL, NULL);
    }
;

bloco:
    '{' declaracoes comandos RETURN NUM ';' '}'
    {
        Node *retorno = criar_no("Return 0", NULL, NULL, NULL);
        $$ = criar_no("Bloco", $2, $3, retorno);
    }
;

declaracoes:
    declaracoes declaracao
    {
        $$ = criar_no("Declaracoes", $1, $2, NULL);
    }
|
    {
        $$ = NULL;
    }
;

declaracao:
    INT ID ';'
    {
        $$ = criar_no("Declaracao", NULL, NULL, NULL);
    }
;

comandos:
    comandos comando
    {
        $$ = criar_no("Comandos", $1, $2, NULL);
    }
|
    {
        $$ = NULL;
    }
;

comando:
    atribuicao
    {
        $$ = $1;
    }
|
    repeticao
    {
        $$ = $1;
    }
;

atribuicao:
    ID ATRIB expressao ';'
    {
        $$ = criar_no("Atribuicao", $3, NULL, NULL);
    }
;

expressao:
    NUM
    {
        $$ = criar_no("Numero", NULL, NULL, NULL);
    }
|
    ID MENOS ID
    {
        $$ = criar_no("Subtracao", NULL, NULL, NULL);
    }
;

repeticao:
    WHILE '(' ID DIF ID ')' '{' condicional '}'
    {
        $$ = criar_no("While", $8, NULL, NULL);
    }
;

condicional:
    IF '(' ID MAIOR ID ')' '{' atribuicao '}' ELSE '{' atribuicao '}'
    {
        $$ = criar_no("If-Else", $8, $12, NULL);
    }
;

%%

void yyerror(const char *s)
{
    printf("Erro sintatico: %s\n", s);
}

int main()
{
    yyparse();

    printf("\n===== ARVORE SINTATICA =====\n\n");
    imprimir_arvore(raiz_final, 0);

    return 0;
}
