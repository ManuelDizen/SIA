//resolver por BPA y BPP
/* usamos una cola de estados, en el cual vamos guardando cada estado generado para comparar
 * despues iteramos con un for arrancando del nodo inicial, preguntando qué acciones se pueden hacer sobre él
 * se ejecutan todas las acciones válidas, generando nuevos estados, chequeando que no sean repetidos y generando nodos
 * también se tiene que chequear si ganaste */

import sun.awt.image.ImageWatched;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class SearchMethods {


    private State firstState;
    private Node firstNode;
    private static final long EMPTY_TOWER = 8;
    private static final long COMPLETE_TOWER = 87654321;
    private static final int MAX_DEPTH = 10;
    private LinkedList<Node> tree = new LinkedList<>();
    private LinkedList<Node> leaves = new LinkedList<>();
    private LinkedList<Node> explored = new LinkedList<>();

    private State objectiveState = new State(EMPTY_TOWER, EMPTY_TOWER, COMPLETE_TOWER);

    private void setFirstState() {
        firstState = new State(COMPLETE_TOWER, EMPTY_TOWER, EMPTY_TOWER);
        firstNode = new Node(firstState, 0, 0);
    }


    public LinkedList Search (Node firstNode, State firstState, Methods method){

        tree.add(firstNode);
        leaves.add(firstNode);

        while (!leaves.isEmpty()) {
            Node current = leaves.getFirst();
            leaves.remove(current);
            if (!explored.contains(current))
                explored.add(current);
            if(current.getState().equals(objectiveState))
                return tree;
            /*Evaluar nodos que se guardan en leaves*/
            LinkedList<State> possible = checkPossibleDescendants(current.getState());
            tree.addAll(possible);
            leaves.addAll(possible);

            switch (method){
                case BPA:
                    leaves.sort((o1, o2) -> o1.getDepth() - o2.getDepth());
                case BPP:
                    leaves.sort((o1, o2) -> o2.getDepth() - o1.getDepth());
                case BPPV:
                    leaves = sortBPPV(leaves);
            }


        }

        return null;
    }

    private LinkedList<State> checkPossibleDescendants(State current) {

        LinkedList<State> toReturn = new LinkedList<>();
        State newState1;
        State newState2;

        if(isInitialState(current)){
            newState1 = new State(COMPLETE_TOWER/10, 1, EMPTY_TOWER);
            newState2 = new State(COMPLETE_TOWER/10, EMPTY_TOWER, 1);
            toReturn.add(newState1);
            toReturn.add(newState2);
            return toReturn;
        }

        /*


        long peekFirst = current.getTower(0);
        long peekSecond = current.getTower(1);
        long peekThird = current.getTower(2);

        State newState1, newState2, newState3;

        if(peekFirst%10 == 1) {
            newState1 = new State(peekFirst/10, peekSecond*10+1, peekThird);
            newState2 = new State(peekFirst/10, peekSecond, peekThird*10+1);

            if(peekSecond%10 < peekThird%10) {
                newState3 = new State(peekFirst, peekSecond/10, peekThird*10+(peekSecond%10));
            } else {
                newState3 = new State(peekFirst, peekSecond*10+(peekThird%10), peekThird/10);
            }
        }


         */

        long peekFirst = current.getTower(0);
        long peekSecond = current.getTower(1);
        long peekThird = current.getTower(2);

        int hasOne;

        if(peekFirst == 1){
            hasOne = 0;
        }
        else if(peekSecond == 1){
            hasOne = 1;
        }
        else{
            hasOne = 2;
        }

        State newState3;
        // Not in initial state --> Procedo a revisar
        if(peekFirst < peekSecond){ // 1 < 2
            if(peekFirst < peekThird){ // 1 < 2 and 1 < 3
                // En primer palo, esta el mas chico
                newState1 = new State(remove(peekFirst), add(peekSecond, peekFirst), peekThird);
                newState2 = new State(remove(peekFirst), peekSecond, add(peekThird, peekFirst));
                if(peekSecond < peekThird){ // 1 < 2 and 1 < 3 and 2 < 3 ==> 1 < 2 < 3
                    newState3 = new State(peekFirst, remove(peekSecond), add(peekThird, peekSecond));
                }
                else{ // 1 < 3 < 2
                    newState3 = new State(peekFirst, add(peekSecond, peekThird), remove(peekThird));
                }
            }
            else{ // 1 < 2 y 1 >= 3  ==>  3 < 1 < 2
                newState1 = new State(remove(peekFirst), add(peekSecond, peekFirst), peekThird);
                newState2 = new State(peekFirst, add(peekSecond, peekThird), peekThird);
                newState3 = new State(add(peekFirst, peekThird), peekSecond, remove(peekThird));
            }
        }
        else{ // 1 > 2
            if(peekFirst > peekThird){ // 1 > 2 and 1 > 3
                newState1 = new State(add(peekFirst, peekThird), peekSecond, remove(peekThird));
                newState2 = new State(add(peekFirst, peekThird), remove(peekSecond), peekThird);
                if(peekSecond > peekThird){ // 3 < 2 < 1
                    newState3 = new State(peekFirst, add(peekSecond, peekThird), remove(peekThird));
                }
                else{ // 1 > 3 and 2 < 3 and 1 > 2 ==> 2 < 3 < 1
                    newState3 = new State(peekFirst, remove(peekSecond), add(peekThird, peekSecond));
                }
            }
            else{ // 1 > 2 and 3 > 1 ==> 2 < 1 < 3
                newState1 = new State(add(peekFirst, peekSecond), remove(peekSecond), peekThird);
                newState2 = new State(peekFirst, remove(peekSecond), add(peekThird, peekSecond));
                newState3 = new State(remove(peekFirst), peekSecond, add(peekThird, peekFirst));
            }
        }
        toReturn.add(newState1);
        toReturn.add(newState2);
        toReturn.add(newState3);

        /* Chequear que nodos estan en explorados */
        for(State s : toReturn){
            if(explored.contains(s)){
                toReturn.remove(s);
            }
        }

        return toReturn;
    }

    private long add(long n, long disc) {
        return (n * 10) + (disc%10);
    }

    private long remove(long n) {
        return (n - (n%10))/10;
    }

    private boolean isInitialState(State current) {
        return current.getTower(0) == COMPLETE_TOWER && current.getTower(1) == EMPTY_TOWER
                && current.getTower(2) == EMPTY_TOWER;
    }

    private LinkedList<Node> sortByBPPV(LinkedList<Node> list){
        LinkedList<Node> aux = new LinkedList<>();
        int currentDepth = MAX_DEPTH;
        for (Node node : list){
            if < (node.getDepth())
        }
        return aux;
    }

}
