import java.util.Random;

public class Mutation {
    private final double MUTATION_P = 0.01;
    private final double MAX_DISTURBANCE = 5;


    public Individual mutate(Individual ind){
        Random r = new Random();
        double p = r.nextDouble();
        if(p < MUTATION_P){
            int idx = Math.abs(r.nextInt()%11); // Altero valor random en mutación

            // Elijo un indice random del individuo, lo altero hasta MAX_DISTURBANCE, y el
            // signo de la perturbación lo define un nuevo valor aleatorio.

            // Es decir, la perturbación es completamente azarosa, y no sabemos que posición va a afectar,
            // ni que valor va a sumar o restar

            ind.setValueAtIdx(idx, ind.getValAtIdx(idx) +
                    r.nextDouble()*MAX_DISTURBANCE* (r.nextDouble() < 0.5? -1:1) );
        }
        return ind;
    }
}
