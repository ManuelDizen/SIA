import java.util.*;

public class Reproduction {

    private final int IND_SIZE = 11;
    //private final int SINGLE_POINT_IDX = 6; //TODO: Discutir como parametrizar esto. ¿Conviene por var. global?



    public ArrayList<Individual> singlePoint(Individual i1, Individual i2){
        Individual newI1 = new Individual();
        Individual newI2 = new Individual();
        int idx;
        Random rand = new Random();
        do {
            idx = Math.abs(rand.nextInt()%IND_SIZE);
        } while(idx == 0 || idx == IND_SIZE-1);
        //System.out.println("idx: " + idx);
        for(int i = 0; i < IND_SIZE; i++){
            newI1.setValueAtIdx(i, i < idx? i1.getValAtIdx(i) : i2.getValAtIdx(i));
            newI2.setValueAtIdx(i, i < idx? i2.getValAtIdx(i) : i1.getValAtIdx(i));
        }
        ArrayList<Individual> returnList = new ArrayList<>();
        returnList.add(newI1);
        returnList.add(newI2);
        return returnList;
    }

    public ArrayList<Individual> multiplePoint(Individual i1, Individual i2){
        
        Individual newI1 = new Individual();
        Individual newI2 = new Individual();
        int change = 0;
        Random r = new Random();
        int p1, p2;
        ArrayList<Integer> points = new ArrayList<>();
        do {
            p1 = Math.abs(r.nextInt())%IND_SIZE;
        } while(p1 == 0 || p1 == IND_SIZE-1);
        do {
            p2 = Math.abs(r.nextInt())%IND_SIZE;
        } while(p2 == 0 || p2 == IND_SIZE-1 || p2 == p1);
        points.add(p1);
        points.add(p2);
        for(int i = 0; i < IND_SIZE; i++){
            if(points.contains(i)){
                change = ((change == 0)? 1 : 0);
            }
            if(change == 0){
                newI1.setValueAtIdx(i, i1.getValAtIdx(i));
                newI2.setValueAtIdx(i, i2.getValAtIdx(i));
            }
            else{
                newI1.setValueAtIdx(i, i2.getValAtIdx(i));
                newI2.setValueAtIdx(i, i1.getValAtIdx(i));
            }
        }
        ArrayList<Individual> returnList = new ArrayList<Individual>();
        returnList.add(newI1);
        returnList.add(newI2);
        return returnList;
    }

    public ArrayList<Individual> uniform(Individual i1, Individual i2){
        Random r = new Random();
        Individual newI1 = new Individual();
        Individual newI2 = new Individual();
        for(int i = 0; i < IND_SIZE; i++){
            double p = r.nextDouble();
            System.out.println("i: " + i + ", p: " + p);
            newI1.setValueAtIdx(i, p < 0.5? i1.getValAtIdx(i):i2.getValAtIdx(i));
            newI2.setValueAtIdx(i, p < 0.5? i2.getValAtIdx(i):i1.getValAtIdx(i));
        }
        ArrayList<Individual> returnList = new ArrayList<>();
        returnList.add(newI1);
        returnList.add(newI2);
        return returnList;
    }


}

