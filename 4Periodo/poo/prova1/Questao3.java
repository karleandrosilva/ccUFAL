package poo;

import java.util.Scanner;

public class Questao3 {
	
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Informe um número inteiro: ");
        int numero = teclado.nextInt();
        
        System.out.println("Os divisores do número " + numero + " são: ");
        FuncaoDivisores(numero);
        
        teclado.close();
	}
	
	public static void FuncaoDivisores(int numero) {
        for (int c = 1; c <= numero; c++) {
            if (numero % c == 0) {
                System.out.println(c + " ");
            }
        }
    }
}
