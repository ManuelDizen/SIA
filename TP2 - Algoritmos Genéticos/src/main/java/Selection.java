import java.util.*;

public class Selection {
    private final int GEN_SIZE = 100;
    private final int TRUNC_N = 120;

    public ArrayList<Individual> elite(ArrayList<Individual> gen){
        gen.sort(Comparator.comparingDouble(Individual::getFitness));
        //TODO: Chequear si los devuelve de menor a mayor o al reves (si no cambiar indices de subList)
        gen = new ArrayList<Individual>(gen.subList(0, GEN_SIZE)); // Izq: Inclusivo, Der: Exclusivo (0-99)
        return gen;
    }

    public ArrayList<Individual> roulette(ArrayList<Individual> gen){
        return null;
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
        int aux = -1;
        int prevIdx = -2;
        double u = 0;
        while(newGen.size() < GEN_SIZE){
            competitors.clear();
            u = rand.nextDouble() * (1.0 - 0.5) + 0.5;
            aux = -1;
            prevIdx = -2;
            for(int i = 0; i < 4; i++){
                aux = rand.nextInt() % gen.size();
                if(aux == prevIdx){
                    aux = (aux+1) == gen.size()? 0:aux+1; // "Circular"
                }
                competitors.add(gen.get(aux));
                prevIdx = aux;
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
