package poo;

import java.util.Scanner;

public class Semaforo {

	private int cor;
	private boolean ligado;
	
    public Semaforo(int cor) {
    	if (cor >= 1 && cor <= 3) {
            this.cor = cor;
        } else {
            System.out.println("Número inválido! O semaforo será iniciado no vermelho.");
            this.cor = 3; 
        }
        this.ligado = true;
    }
    
    private String getCorTexto() {
        switch (cor) {
            case 1: 
            	return "VERDE";
            case 2: 
            	return "AMARELO";
            case 3: 
            	return "VERMELHO";
            default: 
            	return "ERRO"; 
        }
    }
	
	public void estado() {
        System.out.println("Semaforo está no: " + getCorTexto());
    }
	
	public void transicao(int novaCor) {
		if ((cor == 1 && novaCor == 2) || 
	            (cor == 2 && novaCor == 3) || 
	            (cor == 3 && novaCor == 1)) { 
	            cor = novaCor;
            System.out.println("Transição realizada! O semaforo agora está " + getCorTexto());
        } else {
            System.out.println("Transição inválida! A sequência correta é: [1] - VERDE -> [2] - AMARELO -> [3] - VERMELHO) → [1] - VERDE");
        }
    }
	
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		Semaforo semaforo = new Semaforo(1);
		
		while (true){
			semaforo.estado();
			System.out.print("Informe o número da cor que deseja que o semaforo mude?\n[1] - VERDE\n[2] - AMARELO \n[3] - VERMELHO: ");
	        int novaCor = teclado.nextInt();
	        
	        if (novaCor == 0) {
                System.out.println("Semaforo desligado, programa encerrado.");
                break;
            }
	        semaforo.transicao(novaCor);
		}
        teclado.close();
	}

}