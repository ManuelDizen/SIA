//resolver por BPA y BPP
/* usamos una cola de estados, en el cual vamos guardando cada estado generado para comparar
 * despues iteramos con un for arrancando del nodo inicial, preguntando qué acciones se pueden hacer sobre él
 * se ejecutan todas las acciones válidas, generando nuevos estados, chequeando que no sean repetidos y generando nodos
 * también se tiene que chequear si ganaste */

import java.util.Comparator;
import java.util.LinkedList;
import java.util.function.Function;

public class SearchMethods {


    private State firstState = new State(COMPLETE_TOWER, EMPTY_TOWER, EMPTY_TOWER);
    private Node firstNode;
    private static final long EMPTY_TOWER = 8;
    private static final long COMPLETE_TOWER = 87654321;
    private static final int MAX_DEPTH = 10;
    private LinkedList<Node> tree = new LinkedList<>();
    private LinkedList<Node> leaves = new LinkedList<>();
    private LinkedList<Node> explored = new LinkedList<>();

    private State objectiveState = new State(EMPTY_TOWER, EMPTY_TOWER, COMPLETE_TOWER);

    private Node setFirstNode() {
        firstNode = new Node(firstState, 0, 0);
        firstNode.setParent(null);
        return firstNode;
    }


    public returnNode SearchUninformed(Node firstNode, State firstState, Method method){

        tree.add(firstNode);
        leaves.add(firstNode);

        int currentDepth = 0;

        while (!leaves.isEmpty()) {
            Node current = leaves.getFirst();
            leaves.remove(current);
            if (!explored.contains(current))
                explored.add(current);
            if(current.getState().equals(objectiveState)) {
                return printObjective(current);
            }
            /*Evaluar nodos que se guardan en leaves*/
            LinkedList<State> possible = checkPossibleDescendants(current.getState(), method, current);
            //possible son los estados posibles, hay que crear un nodo por cada estado posible.
            //tree.addAll(possible);
            //leaves.addAll(possible);

            for(State s : possible){
                Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
                current.addToDescendants(aux);
                aux.setParent(current);
                tree.add(aux);
                leaves.add(aux);
            }

            switch (method){
                case BPA:
                    leaves.sort((o1, o2) -> o1.getDepth() - o2.getDepth());
                case BPP:
                    leaves.sort((o1, o2) -> o2.getDepth() - o1.getDepth());
                case BPPV:
                    leaves = sortByBPPL(leaves, MAX_DEPTH);
            }
            currentDepth = current.getDepth();

        }
        /*TODO: Aca falta que, si es BPPV, se actualize el depth y arranque de vuelta a buscar.
        */

        System.out.printf("No se encontraron soluciones despues de evaluar %d niveles.%n", currentDepth);
        return new returnNode(explored.size(), leaves.size(), -1, -1, false, null);
    }

    public returnNode LocalHeuristicSearch (LinkedList<Node> succesors){
        while (!succesors.isEmpty()){
            Node current = succesors.getFirst();
            if(current.getState().equals(objectiveState)) {
                return printObjective(current);
            }
            LinkedList<State> possible = checkPossibleDescendants(current.getState(), Method.LOCAL, current);
            //possible son los estados posibles, hay que crear un nodo por cada estado posible.
            //tree.addAll(possible);
            //leaves.addAll(possible);

            for(State s : possible){
                Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
                current.addToDescendants(aux);
                aux.setParent(current);
                tree.add(aux);
                leaves.add(aux);
            }
            LocalHeuristicSearch(leaves);
            succesors.remove(current);
        }
        return null;
    }

    public returnNode GlobalHeuristicSearch (Node firstNode, Heuristic heuristic){
        tree.add(firstNode);
        leaves.add(firstNode);
        while (!leaves.isEmpty()){
            Node current = leaves.getFirst();
            if(current.getState().equals(objectiveState)) {
                return printObjective(current);
            }
            LinkedList<State> possible = checkPossibleDescendants(current.getState(), Method.GLOBAL, current);
            for(State s : possible){
                Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
                current.addToDescendants(aux);
                aux.setParent(current);
                tree.add(aux);
                leaves.add(aux);
            }
            leaves.sort(new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    return heuristic.getValue(o1.getState()) - heuristic.getValue(o2.getState());
                }
            });
        }
        return null;
    }

    public returnNode AStar (Node firstNode, Heuristic heuristic){
        tree.add(firstNode);
        leaves.add(firstNode);
        while (!leaves.isEmpty()){
            Node current = leaves.getFirst();
            if(current.getState().equals(objectiveState)) {
                return printObjective(current);
            }
            LinkedList<State> possible = checkPossibleDescendants(current.getState(), Method.GLOBAL, current);
            for(State s : possible){
                Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
                current.addToDescendants(aux);
                aux.setParent(current);
                tree.add(aux);
                leaves.add(aux);
            }
            leaves.sort(new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    return (o1.getActualCost() + heuristic.getValue(o1.getState())) - (o2.getActualCost() + heuristic.getValue(o2.getState()));
                }
            });
        }
        return null;
    }

    private LinkedList<State> checkPossibleDescendants(State current, Method alg, Node currentN) {

        LinkedList<State> toReturn = new LinkedList<>();
        State newState1;
        State newState2;

        if(isInitialState(current)){
            newState1 = new State(remove(COMPLETE_TOWER), 1, EMPTY_TOWER);
            newState2 = new State(remove(COMPLETE_TOWER), EMPTY_TOWER, 1);
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
                newState2 = new State(peekFirst, add(peekSecond, peekThird), remove(peekThird));
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

        int currentDepth = currentN.getDepth();
        boolean isBPPV = alg.equals(Method.BPPV);
        for(Node n : explored){
            for(State s : toReturn){
                if(s.equals(n.getState())){
                    if(isBPPV){
                        if(currentDepth + 1 >= n.getDepth()){
                            toReturn.remove(s);
                        }
                    }
                    else{
                        toReturn.remove(s);
                    }
                }
            }
        }
        /*
            NEcesito: COnseguir estados de nodos. Comparar esos estados de nodos con
            mis candidatos. Si metodo es BPPV, comparar profundidad. Si es < profundidad del
            nodo explorado, lo encolo igual (porque la solución se puede llegar a encontrar en
            una menor prof). Si es >= remuevo.
            Si es BPA o BPPV, remuevo directamente.
         */

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

    private LinkedList<Node> sortByBPPL(LinkedList<Node> list, int height){
        LinkedList<Node> aux = new LinkedList<>();
        for (Node node : list){
            if (node.getDepth() <= height)
                aux.add(node);
        }
        return aux;
    }


    private State getFirstState(){
        return this.firstState;
    }

    private returnNode printObjective (Node node){
        Node aux = node.getParent();
        StringBuilder s = new StringBuilder(node.getState().toString());
        int i = 0;
        while (aux != null) {
            s.insert(0, aux.getState().toString() + " --> ");
            aux = aux.getParent();
            if (i++ % 4 == 0) {
                s.insert(0, "\n");
            }
        }
        System.out.println("Estados desde inicial a objetivo: \n");
        System.out.println(s);
        return new returnNode(explored.size(), leaves.size(), node.getDepth(),
                node.getDepth(), true, s.toString());
    }


    public void main(String[] args) {
        long initialTime = System.currentTimeMillis();
        System.out.println("hola\n");

        State s = getFirstState();
        Node i = setFirstNode();

        returnNode n = SearchUninformed(i, s, Method.BPA);

        long endingTime = System.currentTimeMillis();
        long totalTime = (endingTime - initialTime)/1000;
        StringBuilder str = new StringBuilder();
        str.append("Resultados: \n").append("Tiempo de ejecución: "). append(totalTime).append("\n");
        str.append("Encontro solución: ").append(n.getResult()).append("\n");
        if(n.getResult()) {
            str.append("Solución: ").append(n.getSolution()).append("\n");
            str.append("Costo de solución: ").append(n.getCost()).append("\n");
            str.append("Profundidad de solución: ").append(n.getDepth()).append("\n");
        }
        str.append("Nodos expandidos: ").append(n.getExpandedNodes()).append("\n");
        str.append("Nodos frontera: ").append(n.getFrontierNodes()).append("\n");
        System.out.println(str);
    }



    public static class returnNode{
        private final int expandedNodes;
        private final int frontierNodes;
        private final int cost;
        private final int depth;
        private final boolean result;
        private final String solution;

        public returnNode(int expandedNodes, int frontierNodes, int cost, int depth,
        boolean result, String solution){
            this.expandedNodes = expandedNodes;
            this.frontierNodes = frontierNodes;
            this.cost = cost;
            this.depth = depth;
            this.result = result;
            this.solution = solution;
        }

        public int getExpandedNodes() {
            return expandedNodes;
        }

        public int getFrontierNodes() {
            return frontierNodes;
        }

        public int getCost() {
            return cost;
        }

        public int getDepth() {
            return depth;
        }

        public boolean getResult() {
            return result;
        }

        public String getSolution() {
            return solution;
        }
    }

}
