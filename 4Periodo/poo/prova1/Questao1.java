package cfd;
import java.util.Scanner;

//1. Faça um programa que realize a conversão de celsius para farenheight (F 1 C * 1.8 + 32)

public class Questao1 {

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Insira a temperatura em celsius: ");
        double celsius = teclado.nextDouble();
        
        double farenheight = celsius * 1.8 + 32;
        
        System.out.print("O resultado da conversão de celsius para farenheight: " + farenheight);
        
        teclado.close();
	}
}