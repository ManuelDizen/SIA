import java.util.ArrayList;
import java.util.Comparator;
import java.util.Random;
import java.util.TreeSet;

public class MainGenerator {
    private static final int GEN_SIZE = 10;
    private static ArrayList<Individual> gen = new ArrayList<>();

    private static void initialPopulation() {
        for (int i = 0; i < GEN_SIZE; i++) {
            gen.add(new Individual());
        }
    }


    private static void algorithm(SelectionMethod sel, ReproductionMethod rep, double pMutation) {
        int gens = 0;
        Selection s = new Selection();
        Reproduction r = new Reproduction();
        Mutation m = new Mutation();
        ArrayList<Individual> parents = new ArrayList<>();
        ArrayList<Individual> children = new ArrayList<>();



        while(gens < 3) {
            ArrayList<Individual> newGen = new ArrayList<>();
            while(newGen.size() < GEN_SIZE) {
                parents = s.roulette(gen, 2);
//                System.out.println("first parent: " + parents.get(0));
//                System.out.println("second parent: " + parents.get(1));
                switch(rep) {
                    case SINGLEPOINT :
                        children = r.singlePoint(parents.get(0), parents.get(1));
                        break;
                    case MULTIPLEPOINT:
                        ArrayList<Integer> pointList = new ArrayList<>();
                        pointList.add(3);
                        pointList.add(7);
                        children = r.multiplePoint(parents.get(0), parents.get(1), pointList);
                        break;
                    case UNIFORM:
                        children = r.uniform(parents.get(0), parents.get(1));
                        break;
                }
//                System.out.println("first child: " + children.get(0));
//                System.out.println("second child: " + children.get(1));
                children.set(0, m.mutate(children.get(0)));
                children.set(1, m.mutate(children.get(1)));
                newGen.addAll(children);
                //System.out.println(newGen.size());
            }
//            System.out.println("new generation!");
//            for(Individual i : newGen) {
//                System.out.println(i);
//            }
//            System.out.println("----------------------------------------------");

            gen.addAll(newGen);

//            System.out.println("combine two generations!");
//            for(Individual i : gen) {
//                System.out.println(i);
//            }
//            System.out.println("----------------------------------------------");
//
//            System.out.println("gen size: " + gen.size());
            sel = SelectionMethod.RANK;
            switch (sel) {
                case ELITE:
                    gen = s.elite(gen);
                    break;
                case ROULETTE:
                    gen = s.roulette(gen, GEN_SIZE);
                    break;
                case RANK:
                    gen = s.rank(gen);
                    break;
                case TOURNAMENT:
                    break;
                case BOLTZMANN:
                    break;
            }

//            System.out.println("gen size after selection: " + gen.size());
//
//            System.out.println("new generation! after selection");
//            for(Individual i : gen) {
//                System.out.println(i);
//            }
//            System.out.println("----------------------------------------------");
            gens++;

        }

    }



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


//        for (int i = 0; i < GEN_SIZE; i++) {
//            gen.add(new Individual());
//        }
//
//        gen.sort(Comparator.comparingDouble(Individual::getFitness));
//
//        for (Individual ind : gen) {
//            System.out.println(ind.getFitness());
//        }
//
//        System.out.println(gen.size());

        initialPopulation();
        algorithm(SelectionMethod.ELITE, ReproductionMethod.SINGLEPOINT, 0.5);

    }
}
