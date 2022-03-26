import java.util.Random;

public class Individual {
    private final int IND_SIZE = 11;
    private Double[] values = new Double[IND_SIZE];
    private int fitness;

    //TODO: Mover samples a archivo de config
    private final int SAMPLE_SIZE = 3;
    private final Double[] out = {0.0,1.0,1.0};
    private final Double[][] in = {{4.4793, -4.0765, -4.0765},
            {-4.1793, -4.9218, 1.7664}, {-3.9429, -0.7689, 4.8830}};

    public Individual(){
        Random rand = new Random();
        for(int j = 0; j < IND_SIZE; j++){
            values[j] = rand.nextDouble()*100; // calculo valor de rand entre 0 y 100
            if(rand.nextDouble() < 0.5){
                values[j] = values[j] * -1; // 50-50 que sea negativo
            }
        }
        this.fitness = fitness();
    }

    public double fitness(){
        double sum = 0;
        for(int i = 0; i < SAMPLE_SIZE; i++){
            sum += Math.pow(out[i] - function(i), 2);
        }
        return sum;
    }

    public double function(int u){
        double sum = 0;
        for(int j = 1; j <= 2; j++){
            double sum2 = 0;
            for(int k = 1; k <= 3; k++){
                sum2 += values[(j*3) + (k-1)] * in[u][k] - values[(j*3)];
            }
            sum += values[j] * logistic(sum2) - values[0];
        }
        return logistic(sum);
    }

    public double logistic(double x){
        return Math.exp(x)/(1+Math.exp(x));
    }
}
