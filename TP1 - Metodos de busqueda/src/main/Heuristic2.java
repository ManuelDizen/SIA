package main;

public class Heuristic2 implements Heuristic{
    //Suma discos que aun no estan a la derecha + 2*nodos que estan a derecha pero no estanb ien ubicados
    //Fundamento: Discos que no estan a la derecha --> requieren minimo 1 movimiento mas para llegar a derecha
    // Nodos que estan a der mal ubicados: Necesitan minimo un mov para salir de la torre, y otro mov para ubicar
    // el disco correcto (en un caso ideal, claro esta que es un minimo absoluto, lo que la hace admisible)
    @Override
    public int compare(Node o1, Node o2) {
        int HValue1 = getHValue(o1.getState());
        int HValue2 = getHValue(o2.getState());
        return HValue2 - HValue1;
    }

    @Override
    public int getHValue(State s) {
        int discsNotOnRight = (String.valueOf(s.getTower(0)).length() - 1) +
                (String.valueOf(s.getTower(1)).length() - 1);
        int discsOnRightButNotCorrect = (String.valueOf(s.getTower(2)).length()) - 1 - calculateDiscs(s.getTower(2));
        return discsNotOnRight + 2*discsOnRightButNotCorrect;
    }

    private int calculateDiscs(long n){
        String s = String.valueOf(n);
        int pos = 1; //First position is always 8.
        boolean flag = true;
        while(flag && pos < s.length()){
            if(Integer.parseInt(String.valueOf(s.charAt(pos))) == 8 - pos){
                pos++;
            }
            else{
                flag = false;
            }

        }
        return pos;
    }
}
