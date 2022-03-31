import java.util.*;

public class Selection {
    private final int GEN_SIZE = 10;
    private final int TRUNC_N = 120;

    public ArrayList<Individual> elite(ArrayList<Individual> gen){
        gen.sort(Comparator.comparingDouble(Individual::getFitness));
        Collections.reverse(gen);
        //TODO: Chequear si los devuelve de menor a mayor o al reves (si no cambiar indices de subList)
        gen = new ArrayList<Individual>(gen.subList(0, GEN_SIZE));
        // Izq: Inclusivo, Der: Exclusivo (0-99)
        return gen;
    }

    public ArrayList<Individual> roulette(ArrayList<Individual> gen, int dim){
        /*
        Aca hay un tema, y es que nuestra función de fitness devuelve valores negativos.
        Esto lo hacemos xq en realidad nuestra función de fitness es la de error,
        la cual nosotros sabemos que, cuanto mas chica sea, "mejor" es. Al ser un requerimiento
        que le "mejor" fitness sea el numero mas grande, se multiplican todos los valores por -1,
        dejando así el orden invertido, y el numero mas chico paso a ser el mas grande.

        Pero esto presenta un problema al usar metodos de selección, dado que
        para hacer las probabilidades relativas, uno hace f(i) / suma de todas las f(i),
        y en ese caso es favorable para los individuos de peor fitness.

        Por ello, intentaré hacerlo con probabilidades relativas sobre 1/f(i).
        De esta manera, quedarán los valores mas cercanos a 0 con mejor probabilidad.

        TODO: En cuanto a código, es SUPER Optimizable. Yo estoy medio tosco pero
        guardar los "rangos" entre individuos es innecesario, se puede ir comparando con el rand.

         */
        double accum_fitness = 0.0;
        double cum_freq = 0.0;
        double aux = 0.0;

        ArrayList<Individual> returnList = new ArrayList<>();
        ArrayList<Double> values = new ArrayList<>();

        for(int i = 0; i < gen.size(); i++){
            aux = 1.0/gen.get(i).getFitness();
            values.add(i, aux);// No hace falta que esten en orden, el rango solo alcanza
            accum_fitness += aux;
        }

        for(int i = 0; i < gen.size(); i++){
            aux = values.get(i)/accum_fitness;
            values.set(i, cum_freq + aux );
            cum_freq += aux;
            //System.out.println("cum freq " + i + ": " + cum_freq);
        }


        // Aca ya tengo calculados los rangos para p, así que
        // puedo iterar hasta tener GEN_SIZE elementos en returnList
        int i = 0;

        Random rand = new Random();
        double p = rand.nextDouble();

        while(returnList.size() < dim){
            //System.out.println("p:" + p);
            //System.out.println("size:" + returnList.size());
            i = 0;
            while(i<values.size()-1 && p > values.get(i)){
                i++;
            }
            //System.out.println("i:" + i);
            //System.out.println("fitness: " + (values.get(i)-values.get(i-1)));
            if(!returnList.contains(gen.get(i))){
                returnList.add(gen.get(i));
            }
            p = rand.nextDouble();
        }
        return returnList;
    }

    public ArrayList<Individual> rank(ArrayList<Individual> gen){
        return null;
    }

    public ArrayList<Individual> tournament(ArrayList<Individual> gen){
        Random rand = new Random();
        // 0.5 - 1.0
        /*¿Si hacemos torneo entre 4 individuos, y gana 1 solo, no quedaría una población resultante
          de P/4 cuando queremos que sea de P/2?

        Update: Solución parcial (aunque sujeta a discusión).
        Vale hacer que los individuos puedan ser tomados como competidores con reemplazo,
        pero hay que chequear que haya una población final de P
        */
        ArrayList<Individual> newGen = new ArrayList<>();
        ArrayList<Individual> competitors = new ArrayList<>();
        double u = 0;
        while(newGen.size() < GEN_SIZE){
            competitors.clear();
            u = rand.nextDouble() * (1.0 - 0.5) + 0.5;
            Collections.shuffle(gen);
            /*
            Para randomziar selección de individuos, hago shuffle a toda la generación
            (no es relevante su orden en este caso) y tomo los primeros 4. Todos tienen la
            misma chance de ser escogidos, y en cada iteración uno esperaría 4 individuos distintos.
             */
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

    public ArrayList<Individual> boltzmann(ArrayList<Individual> gen){
        return null;
    }

    public ArrayList<Individual> truncated(ArrayList<Individual> gen){
        gen.sort(Comparator.comparingDouble(Individual::getFitness));
        gen = new ArrayList<Individual>(gen.subList(0, TRUNC_N - 1));
        Collections.shuffle(gen);
        gen = new ArrayList<Individual>(gen.subList(0, GEN_SIZE));
        //TODO: Mismo de arriba, ver como reordena el comparingDouble
        return gen;
    }


}

