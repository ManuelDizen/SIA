import java.util.ArrayList;
import java.util.Random;

public class MainGenerator {
    private static final int GEN_SIZE = 100;

    public static void main(String[] args) {
        // X = (W0, W1, W2, w11, w12, w13, w21, w22, w23, w01, w02)
        /*Double[][] generation = new Double[GEN_SIZE][IND_SIZE];
        Random rand = new Random();
        for(int i = 0; i < GEN_SIZE; i++){
            for(int j = 0; j < IND_SIZE; j++){
                generation[i][j] = rand.nextDouble()*100; // calculo valor de rand entre 0 y 100
                if(rand.nextDouble() < 0.5){
                    generation[i][j] = generation[i][j] * -1; // 50-50 que sea negativo
                }
            }
        }*/

        /* Para leer un config desde un jar (no chequeado pero fue lo que encontre en internet):

        InputStream inputStream = Main.class.getResourceAsStream(path);
        InputStreamReader inputReader = new InputStreamReader(inputStream);
         */

        ArrayList<Individual> gen = new ArrayList<>();
        for(int i = 0; i < GEN_SIZE; i++){
            gen.add(new Individual());
        }



    }
}
