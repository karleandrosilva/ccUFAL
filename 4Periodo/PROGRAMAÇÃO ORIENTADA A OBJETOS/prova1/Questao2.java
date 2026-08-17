package cfd;

import java.util.Scanner;

public class Questao2 {
	public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Insira o dia (somente DD, exemplo: 05): ");
        int dia = teclado.nextInt();

        System.out.print("Insira o mês (somente MM, exemplo: 12): ");
        int mes = teclado.nextInt();

        System.out.print("Insira o ano (somente AAAA, exemplo: 1999): ");
        int ano = teclado.nextInt();

        if (validarData(dia, mes, ano)) {
            System.out.println("A data " + String.format("%02d/%02d/%04d", dia, mes, ano) + " é válida.");
        } else {
            System.out.println("A data " + String.format("%02d/%02d/%04d", dia, mes, ano) + " não é válida.");
        }

        teclado.close();
    }
	
	public static boolean validarData(int dia, int mes, int ano) {
    	
    	if (ano < 0001 || ano > 9999) {
    		return false;
    	}
        if (mes < 1 || mes > 12) {
            return false;
        }
        boolean anoBissexto = (ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0);

        int diaMaximo;
        switch (mes) {
            case 1, 3, 5, 7, 8, 10, 12:
                diaMaximo = 31;
                break;
            case 4, 6, 9, 11:
                diaMaximo = 30;
                break;
            case 2:
                diaMaximo = anoBissexto ? 29 : 28;
                break;
            default:
                return false;
        } 
        return dia >= 1 && dia <= diaMaximo;
    }
}