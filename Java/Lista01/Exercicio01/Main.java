import java.util.Scanner;

public class Main {
    private static final Scanner SCAN = new Scanner(System.in);
    private static final int TAMANHO_VETOR = 10;
    private static final int Numero = 14;
    
    public static void main(String[] args){
      int[] Vetor = new int[TAMANHO_VETOR];
      
      PreencherVetor(Vetor);
      
      int numeroBuscado = Integer.parseInt(SCAN.nextLine());
      
      if(ValidarVetor(numeroBuscado)){
        System.out.println("ACHEI");
      }
      else{
        System.out.println("NAO ACHEI");
      }
  }
  
  public static void PreencherVetor(int[] Vetor){
    for(int i = 0; i < Vetor.length; i++){
      Vetor[i] = Integer.parseInt(SCAN.nextLine());
    }
  }
  
  public static Boolean ValidarVetor(int Vetor){
    Boolean temNumero = true;
    for(int i = 0; i < TAMANHO_VETOR; i++){
      if(Numero == Vetor){
        temNumero = true;
      }
      else{
        temNumero = false;
      }
    }
    return temNumero;
  }
}