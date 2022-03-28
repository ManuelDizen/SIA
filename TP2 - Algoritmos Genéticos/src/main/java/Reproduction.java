import java.util.*;

public class Reproduction {

    private final int IND_SIZE = 11;
    private final int SINGLE_POINT_IDX = 6; //TODO: Discutir como parametrizar esto. ¿Conviene por var. global?

    public ArrayList<Individual> singlePoint(Individual i1, Individual i2){
        Individual newI1 = new Individual();
        Individual newI2 = new Individual();
        for(int i = 0; i < IND_SIZE; i++){
            newI1.setValueAtIdx(i, i < SINGLE_POINT_IDX? i1.getValAtIdx(i) : i2.getValAtIdx(i));
            newI2.setValueAtIdx(i, i < SINGLE_POINT_IDX? i2.getValAtIdx(i) : i1.getValAtIdx(i));
        }
        ArrayList<Individual> returnList = new ArrayList<>();
        returnList.add(newI1);
        returnList.add(newI2);
        return returnList;
    }

    public ArrayList<Individual> multiplePoint(Individual i1, Individual i2, ArrayList<Integer> points){
        // TODO: Pensar como ir "alternando" con n puntos
        /*
        Update: creo que lo resolvi. Cambias el orden de inserción por cada punto que este en points.
         */
        Individual newI1 = new Individual();
        Individual newI2 = new Individual();
        int change = 0;
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
            newI1.setValueAtIdx(i, p < 0.5? i1.getValAtIdx(i):i2.getValAtIdx(i));
            newI2.setValueAtIdx(i, p < 0.5? i2.getValAtIdx(i):i1.getValAtIdx(i));
        }
        ArrayList<Individual> returnList = new ArrayList<>();
        returnList.add(newI1);
        returnList.add(newI2);
        return returnList;
    }


}
