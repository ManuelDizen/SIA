import java.util.ArrayList;

public class MainGenerator {
    private static final int GEN_SIZE = 100;
    private static int MAX_GENS = 10;
    private static final long MAX_TIME = 10 * 60 * 1000; // 10 minutes
    private static final double EPSILON = -0.0000000001;
    private static final int FITNESS_CONTENT_MAX = 10;

    private static long INITIAL_T;
    private static ArrayList<Individual> gen = new ArrayList<>();
    private static ArrayList<Individual> firstGen = new ArrayList<>();

    private static void initialPopulation() {
        gen.clear();
        for (int i = 0; i < GEN_SIZE; i++) {
            gen.add(new Individual());
        }
    }


    private static void algorithm(SelectionMethod sel, ReproductionMethod rep) {
        long executionTime = INITIAL_T;
        int gens = 0;
        int bestFitnessAcum = 0;
        double prevFitness = -1;
        Selection s = new Selection();
        Reproduction r = new Reproduction();
        Mutation m = new Mutation();
        ArrayList<Individual> parents = new ArrayList<>();
        ArrayList<Individual> children = new ArrayList<>();

        // && (executionTime - INITIAL_T < MAX_TIME)
        // && currentBestFitness(gen) < EPSILON && (bestFitnessAcum < FITNESS_CONTENT_MAX)
        while(gens < MAX_GENS){
            //TODO: Agregar condición con desviación estandar
            ArrayList<Individual> newGen = new ArrayList<>();
            while(newGen.size() < GEN_SIZE) {
                parents = s.roulette(gen, 2, false);
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
            switch (sel) {
                case ELITE:
                    gen = s.elite(gen);
                    break;
                case ROULETTE:
                    gen = s.roulette(gen, GEN_SIZE, false);
                    break;
                case RANK:
                    gen = s.rank(gen);
                    break;
                case TOURNAMENT:
                    gen = s.tournament(gen);
                    break;
                case BOLTZMANN:
                    gen = s.boltzmann(gen, gens);
                    break;
                case TRUNCATED:
                    gen = s.truncated(gen);
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
            executionTime += (System.currentTimeMillis() - executionTime);
            if(bestFitnessAcum == 0 || prevFitness == currentBestFitness(gen)){
                bestFitnessAcum++;
            }
            else{
                bestFitnessAcum = 0;
            }
        }

    }

    static double currentBestFitness(ArrayList<Individual> gen){
        double max = 1;
        for(Individual i : gen){
            if(max == 1 || max < i.getFitness()){
                max = i.getFitness();
            }
        }
        return max;
    }



    public static void main(String[] args) {

        /* Para leer un config desde un jar (no chequeado pero fue lo que encontre en internet):

        InputStream inputStream = Main.class.getResourceAsStream(path);
        InputStreamReader inputReader = new InputStreamReader(inputStream);
         */

        INITIAL_T = System.currentTimeMillis();
        initialPopulation();
        algorithm(SelectionMethod.ELITE, ReproductionMethod.SINGLEPOINT, 0.5);
        System.out.println("Individuo: " );
        String[] array = {"W0", "W1", "W2", "w11", "w12", "w13", "w21", "w22", "w23", "w01", "w02"};
        Individual j = getBestIndividual(gen);
        for(int i = 0; i < j.getIndSize(); i++){
            System.out.println(array[i] + ": " + j.getValAtIdx(i));
        }
        System.out.println("Fitness de mejor individuo: " + currentBestFitness(gen));
    }

    static Individual getBestIndividual(ArrayList<Individual> gen){
        Individual max  = null;
        for(Individual i : gen){
            if(max == null || max.getFitness() < i.getFitness()){
                max = i;
            }
        }
        return max;
    }
}
