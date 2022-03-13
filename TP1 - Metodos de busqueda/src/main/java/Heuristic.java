import java.util.Comparator;

public interface Heuristic extends Comparator<Node> {
    public int compare(Node o1, Node o2);
    public int getHValue(State s);
}
