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
        Random r = new Random();
        Double p = r.nextDouble() * (1.0 - 0.5) + 0.5; // 0.5 - 1.0
        // ¿Si hacemos torneo entre 4 individuos, y gana 1 solo, no quedaría una población resultante
        // de P/4 cuando queremos que sea de P/2?
        return gen;
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
