import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MainGenerator {
    private static final int GEN_SIZE = 100;
    private static int MAX_GENS = 500;
    private static long MAX_TIME = 1;
    private static double EPSILON = -0.01;
    private static final int FITNESS_CONTENT_MAX = 10;
    private static int gensN;

    private static long INITIAL_T;
    private static ArrayList<Individual> gen;
    private static ArrayList<Individual> firstGen = new ArrayList<>();

    private static ArrayList<Individual> initialPopulation() {
        gen = new ArrayList<>();
        for (int i = 0; i < GEN_SIZE; i++) {
            gen.add(new Individual());
        }
        return gen;
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

        // gens < MAX_GENS && (executionTime - INITIAL_T < MAX_TIME)
        // && currentBestFitness(gen) < EPSILON && (bestFitnessAcum < FITNESS_CONTENT_MAX)
        while((executionTime - INITIAL_T < MAX_TIME || gens < MAX_GENS || currentBestFitness(gen) < EPSILON) && (bestFitnessAcum < FITNESS_CONTENT_MAX)){
            //TODO: Agregar condición con desviación estandar
            ArrayList<Individual> newGen = new ArrayList<>();
            while(newGen.size() < GEN_SIZE) {
                parents = s.roulette(gen, 2, false);
                switch(rep) {
                    case SINGLEPOINT :
                        children = r.singlePoint(parents.get(0), parents.get(1));
                        break;
                    case MULTIPLEPOINT:
                    
                        children = r.multiplePoint(parents.get(0), parents.get(1));
                        break;
                    case UNIFORM:
                        children = r.uniform(parents.get(0), parents.get(1));
                        break;
                }
                children.set(0, m.mutate(children.get(0)));
                children.set(1, m.mutate(children.get(1)));
                newGen.addAll(children);
            }

            gen.addAll(newGen);

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
                default:
                    break;
            }

            gens++;
            executionTime += (System.currentTimeMillis() - executionTime);
            if(bestFitnessAcum == 0 || prevFitness == currentBestFitness(gen)){
                bestFitnessAcum++;
            }
            else{
                bestFitnessAcum = 0;
            }
        }
        gensN = gens;

    }

    /* https://www.programiz.com/java-programming/examples/standard-deviation */
    public static double calculateSD(ArrayList<Individual> gen)
    {
        double sum = 0.0, standardDeviation = 0.0;
        int length = gen.size();

        for(Individual ind : gen) {
            sum += ind.getFitness();
        }

        double mean = sum/length;

        for(Individual ind: gen) {
            standardDeviation += Math.pow(ind.getFitness() - mean, 2);
        }

        return Math.sqrt(standardDeviation/length);
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

        ArrayList<Individual> initialGen = new ArrayList<>(initialPopulation());
        String[] array = {"W0", "W1", "W2", "w11", "w12", "w13", "w21", "w22", "w23", "w01", "w02"};
        //int[] genLimit = {10,20,30,40,50,100,200,500,1000, 2000};
        int[] genLimit = {MAX_GENS};
        int[] secsLimit = {1, 5, 10, 15, 20, 30, 60};
        double[] fitnessLimit = {0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001};
        for(SelectionMethod s : SelectionMethod.values()) {
            System.out.println("Resultados con método " + s + " :");

            for (int i : genLimit) {
                    gen.removeAll(gen);
                    gen.addAll(initialGen);
                    MAX_GENS = i;
                    algorithm(s, ReproductionMethod.SINGLEPOINT);

                    StringBuilder sb = new StringBuilder();
                    Individual bestInd = getBestIndividual(gen);
                    for(int k = 0 ; k < gen.get(0).getIndSize(); k++){
                        sb.append(array[k] + ": " +  bestInd.getValAtIdx(k) + " ");
                    }
                    System.out.println(sb);
                    System.out.println("N max de gens: " + i + "  Mejor fitness: " + getBestIndividual(gen).getFitness());
            }
            System.out.println();

            int auxiMax = MAX_GENS;
            for(double d: fitnessLimit){
                MAX_GENS = 0;
                gen.removeAll(gen);
                gen.addAll(initialGen);
                EPSILON = -1*d;
                algorithm(s, ReproductionMethod.SINGLEPOINT);
                System.out.println("Gens necesarias para alcanzar cota " + EPSILON + ": " + gensN);
            }
            System.out.println();
            MAX_GENS = auxiMax;
            for(int sec: secsLimit){
                INITIAL_T = System.currentTimeMillis();
                gen.removeAll(gen);
                gen.addAll(initialGen);
                MAX_TIME = sec*1000;
                algorithm(s, ReproductionMethod.SINGLEPOINT);
                System.out.println("Mejor fitness en " + sec + " segundos: " + getBestIndividual(gen).getFitness());
            }
            System.out.println();

            System.out.println("\n##################\n");

        }

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

    public int getGenSize() {
        return GEN_SIZE;
    }
}
