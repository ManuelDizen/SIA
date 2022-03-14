package main;

public class Heuristic3 implements Heuristic{

    @Override
    public int compare(Node o1, Node o2) {
        int HValue1 = getHValue(o1.getState());
        int HValue2 = getHValue(o2.getState());
        return HValue2 - HValue1;
    }

    public int getHValue(State s){
        int firstDisc = calculateDiscs(n);
        int HValue = (int) Math.pow(2, firstDisc-1)-1;
        for(int i=firstDisc; i<7; i++) {
            HValue += Math.pow(2, i+1) - 2;
        }
        return HValue;
    }

    private int calculateDiscs(long n){
        return (int) (n % 10);
    }
}