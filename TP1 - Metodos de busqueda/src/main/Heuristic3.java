package main;

public class Heuristic3 implements Heuristic{

    @Override
    public int compare(Node o1, Node o2) {
        long d1 = o1.getState().getTower(2);
        long d2 = o2.getState().getTower(2);
        int discsOnRight1 = 7 - calculateDiscs(d1);
        int discsOnRight2 = 7 - calculateDiscs(d2);
        return discsOnRight2 - discsOnRight1; //Si o2 tiene mas discos bien ubicados, h() debe devolver un valor menor y ordenarlos asi
    }

    public int getHValue(State s){
        return 7 - calculateDiscs(s.getTower(2));
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
