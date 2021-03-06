import java.util.*;

public class Selection {
    private final int GEN_SIZE = 100;
    private final int TRUNC_N = 60;
    private static final double T0 = 2.0;
    private static final double TC = 0.5;
    private static final double K = 0.005;
    private ArrayList<Double> values = new ArrayList<>();

    public ArrayList<Individual> elite(ArrayList<Individual> gen){
        Collections.sort(gen);
        gen = new ArrayList<Individual>(gen.subList(0, gen.size()/2));
        // Izq: Inclusivo, Der: Exclusivo (0-99)
        return gen;
    }

    public ArrayList<Individual> roulette(ArrayList<Individual> gen, int dim, boolean boltzmann) { 


        ArrayList<Individual> returnList = new ArrayList<>();

        if(gen.size() != values.size())
            values = calcFreqs(gen, boltzmann);

        Map<Individual, Integer> times = new HashMap<>();
        // Aca ya tengo calculados los rangos para p, así que
        // puedo iterar hasta tener GEN_SIZE elementos en returnList
        int i = 0;

        Random rand = new Random();
        double p = rand.nextDouble();

        while(returnList.size() < dim) {

            i = 0;
            while (i < values.size() - 1 && p > values.get(i)) {
                i++;
            }

            if (!times.containsKey(gen.get(i)))
                times.put(gen.get(i), 0);

            if (!returnList.contains(gen.get(i))) {
                returnList.add(gen.get(i));
            } else {
                times.put(gen.get(i), times.get(gen.get(i)) + 1);

                if (times.get(gen.get(i)) >= 20) {
                    gen.remove(i);
                    values = calcFreqs(gen, boltzmann);
                }
            }
            p = rand.nextDouble();
        }

        return returnList;
    }

    private ArrayList<Double> calcFreqs(ArrayList<Individual> gen, boolean boltzmann) {

        ArrayList<Double> values = new ArrayList<>();

        double accum_fitness = 0.0;
        double cum_freq = 0.0;
        double aux = 0.0;


        for(int i = 0; i < gen.size(); i++){
            aux = (boltzmann ? gen.get(i).getBoltzmannFitness() : 1.0/gen.get(i).getFitness());
            values.add(i, aux);// No hace falta que esten en orden, el rango solo alcanza
            accum_fitness += aux;
        }



        for(int i = 0; i < gen.size(); i++){
            aux = values.get(i)/accum_fitness;
            values.set(i, cum_freq + aux );
            cum_freq += aux;
            //System.out.println("i: " + i + " cumfreq: " + cum_freq);

        }

        return values;
    }

    
    public ArrayList<Individual> rank(ArrayList<Individual> gen){
        ArrayList<Individual> returnList = new ArrayList<>();
        ArrayList<Double> values = new ArrayList<>();
        ArrayList<Individual> rank = new ArrayList<>(gen);
        Collections.sort(rank);

        Collections.sort(rank);
        //Collections.reverse(rank);

        double accum_f1 = 0.0;
        double sum_f1 = 0.0;
        double aux;

        for (int i = 0; i < rank.size(); i++){
            aux = (gen.size()-(rank.indexOf(gen.get(i))+1))/(double)gen.size(); //El primer indice tiene que ser 1
            values.add(i, aux);
            accum_f1 += aux;
        }

        for(int i = 0; i < gen.size(); i++){
            aux = values.get(i)/accum_f1;
            values.set(i, sum_f1 + aux );
            sum_f1 += aux;
        }

        int i = 0;

        Random rand = new Random();
        double p = rand.nextDouble();

        while(returnList.size() < GEN_SIZE){
            i = 0;
            while(i < values.size()-1 && p > values.get(i))
                i++;
            if(!returnList.contains(gen.get(i))){
                returnList.add(gen.get(i));
            }
            p = rand.nextDouble();
        }



        return returnList;
    }

    public ArrayList<Individual> tournament(ArrayList<Individual> gen){
        Random rand = new Random();
        ArrayList<Individual> newGen = new ArrayList<>();
        ArrayList<Individual> competitors = new ArrayList<>();
        double u = 0;
        while(newGen.size() < GEN_SIZE){
            competitors.clear();
            //u = rand.nextDouble() * (1.0 - 0.5) + 0.5;
            u = 0.8;
            Collections.shuffle(gen);

            for(int i = 0; i < 4; i++){
                competitors.add(gen.get(i));
            }
            Individual winner1 = getWinner(competitors.get(0), competitors.get(1), u);
            Individual winner2 = getWinner(competitors.get(2), competitors.get(3), u);
            Individual finalWinner = getWinner(winner1, winner2, u);
            if(!newGen.contains(finalWinner))
                newGen.add(finalWinner);
        }
        gen = newGen;
        return gen;
    }

    private Individual getWinner(Individual i1, Individual i2, double u){
        Random rand = new Random();
        double r = rand.nextDouble();
        boolean fitter1 = i1.getFitness() > i2.getFitness();
        if(r < u){
            return fitter1? i1:i2;
        }
        else{
            return fitter1? i2:i1;
        }
    }

    public ArrayList<Individual> boltzmann(ArrayList<Individual> gen, int numGen){

        double acum = 0;



        for(Individual i : gen) {
            i.setBoltzmannFitness((Math.exp(i.getFitness()/(TC + (T0 - TC)*Math.exp(-K*numGen)))));
            acum += i.getBoltzmannFitness();
        }




        for(Individual i : gen) {
            i.setBoltzmannFitness(-1*i.getBoltzmannFitness()/acum);
            //System.out.println("i: " + i + " boltzfitness: " + i.getBoltzmannFitness());
        }



        return roulette(gen, gen.size()/2, true);
    }


    public ArrayList<Individual> truncated(ArrayList<Individual> gen){
       /*MainGenerator m = new MainGenerator();
        gen.sort(Comparator.comparingDouble(Individual::getFitness));
        Collections.reverse(gen);
        gen = new ArrayList<Individual>(gen.subList(0, (int)Math.floor(m.getGenSize()*0.6) - 1));
        Collections.shuffle(gen);
        gen = new ArrayList<Individual>(gen.subList(0, m.getGenSize()-1));
        return gen;*/

        int initialSize = gen.size();
        Collections.sort(gen);
        //System.out.println("Mejores 3 fitness pre corte: " + gen.get(0).getFitness() + "  " + gen.get(1).getFitness() + "  " + gen.get(2).getFitness());
        gen = new ArrayList<Individual>(gen.subList(0, (int) (initialSize*0.6)));
        //System.out.println("Mejores 3 fitness post corte: " + gen.get(0).getFitness() + "  " + gen.get(1).getFitness() + "  " + gen.get(2).getFitness());
        Collections.shuffle(gen);
        gen = new ArrayList<>(gen.subList(0, initialSize/2));
        return gen;
    }


}

