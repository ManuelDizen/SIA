package main;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Objects;

public class Node {
    private State state;
    private int depth;
    private int actualCost;
    private int hValue;
    private Node parent;
    private ArrayList<Node> descendants = new ArrayList<>();

    Node(State state, int depth, int actualCost){
        this.state = state;
        this.depth = depth;
        this.actualCost = actualCost;
    }

    Node(State state, int depth, int actualCost, int hValue){
        this.state = state;
        this.depth = depth;
        this.actualCost = actualCost;
        this.hValue = hValue;
    }

    public void addToDescendants(Node n){
        descendants.add(n);
    }
    //1 --> BPA, 2 --> BPP, 3 --> BPPV
    public void sortDescendantsBy(int algorithm){
        switch(algorithm){
            case 1:
                descendants.sort(new SortByBFS());
            case 2:
                descendants.sort(new SortByDFS());
        }
    }

    public State getState() {
        return state;
    }

    public int getDepth() {
        return depth;
    }

    public ArrayList<Node> getDescendants() {
        return descendants;
    }

    public int getActualCost() {
        return actualCost;
    }

    public int gethValue() {
        return hValue;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Node node = (Node) o;
        return depth == node.depth && Objects.equals(state, node.state);
    }

    @Override
    public int hashCode() {
        return Objects.hash(state, depth);
    }

    public void setParent(Node parent) {
        this.parent = parent;
    }

    public Node getParent() {
        return this.parent;
    }
}
// BPA es BFS
class SortByBFS implements Comparator<Node> {
    @Override
    public int compare(Node o1, Node o2) {
        int comp = o1.getDepth() - o2.getDepth();
        if(comp > 0){
            return -1;
        }
        else if(comp == 0){
            return comp;
        }
        return 1;
    }
}

class SortByDFS implements Comparator<Node>{
    @Override
    public int compare(Node o1, Node o2) {
        int comp = o1.getDepth() - o2.getDepth();
        if(comp < 0){
            return -1;
        }
        else if(comp == 0){
            return comp;
        }
        return 1;
    }
}
