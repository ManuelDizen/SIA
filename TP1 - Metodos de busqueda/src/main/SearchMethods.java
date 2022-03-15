package main;//resolver por BPA y BPP
/* usamos una cola de estados, en el cual vamos guardando cada estado generado para comparar
 * despues iteramos con un for arrancando del nodo inicial, preguntando qué acciones se pueden hacer sobre él
 * se ejecutan todas las acciones válidas, generando nuevos estados, chequeando que no sean repetidos y generando nodos
 * también se tiene que chequear si ganaste */

import java.io.IOException;
import java.io.InputStream;
import java.util.LinkedList;
import java.util.Properties;

public class SearchMethods {

    private State firstState = new State(COMPLETE_TOWER, EMPTY_TOWER, EMPTY_TOWER);
    private Node firstNode;
    private Heuristic h;
    private Method method;
    private boolean compareDepths;
    private int limit = MAX_DEPTH;
    private static final long EMPTY_TOWER = 8;
    private static final long COMPLETE_TOWER = 87654321;
    private static final int MAX_DEPTH = 150;
    private LinkedList<Node> tree = new LinkedList<>();
    private LinkedList<Node> leaves = new LinkedList<>();
    private LinkedList<Node> explored = new LinkedList<>();

    private State objectiveState = new State(EMPTY_TOWER, EMPTY_TOWER, COMPLETE_TOWER);

    private Node setFirstNode() {
        firstNode = new Node(firstState, 0, 0);
        firstNode.setParent(null);
        return firstNode;
    }
    public void setHeuristic(Heuristic h){
        this.h = h;
    }

    public returnNode Search (Node firstNode, State firstState, Method method){

        tree.add(firstNode);
        leaves.add(firstNode);
        explored.add(firstNode);

        int currentDepth = 0;

      if(method.equals(Method.BPPV)) {
          return searchBPPV(firstNode);
      }
      else if(method.equals(Method.LOCAL_NO_BACK)){
          return searchLocalNoBack(firstNode);
      }
      else if(method.equals(Method.LOCAL_BACK)){
          LinkedList<Node> list = new LinkedList<>();
          list.add(firstNode);
          return searchLocalWithBack(list);
      }
      else {
            while (!leaves.isEmpty()) {

                Node current = leaves.getFirst();
                leaves.remove(current);

                if(current.getState().equals(objectiveState)) {
                    Node aux = current.getParent();
                    StringBuilder s = new StringBuilder(current.getState().toString());
                    int i = 0;
                    while(aux != null){
                        s.insert(0, aux.getState().toString() + " --> ");
                        aux = aux.getParent();
                        if(i++ % 4 == 0){
                            s.insert(0, "\n");
                        }
                    }

                    return new returnNode(explored.size(), leaves.size(), current.getDepth(),
                            current.getDepth(), true, s.toString());
                }
                /*Evaluar nodos que se guardan en leaves*/
                LinkedList<State> possible = checkPossibleDescendants(current.getState(), method, current);
                //possible son los estados posibles, hay que crear un nodo por cada estado posible.
                //tree.addAll(possible);
                //leaves.addAll(possible);

                for(State s : possible){
                    Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
                    if(!explored.contains(aux)){
                        current.addToDescendants(aux);
                        aux.setParent(current);
                        tree.add(aux);
                        leaves.add(aux);
                        explored.add(aux);
                    }
                }

                switch (method){
                    case BPA:
                        leaves.sort((o1, o2) -> o1.getDepth() - o2.getDepth());
                        break;
                    case BPP:
                        leaves.sort((o1, o2) -> o2.getDepth() - o1.getDepth());
                        break;
                    case GLOBAL:
                        leaves.sort(h);
                        break;
                    case A_STAR:
                        leaves.sort((o1, o2) -> (o2.getDepth() + h.getHValue(o2.getState())) -
                                o1.getDepth() + h.getHValue(o1.getState()));
                        break;

                }
                currentDepth = current.getDepth();
            }
        }

        System.out.printf("No se encontraron soluciones despues de evaluar %d niveles.%n", currentDepth);
        return new returnNode(explored.size(), leaves.size(), -1, -1, false, null);
    }

    private returnNode searchLocalWithBack(LinkedList<Node> list) {
        while(!list.isEmpty()){
            Node n = list.getFirst();
            explored.add(n);
            if(n.getState().equals(objectiveState)){
                return generateReturnNode(n);
            }
            LinkedList<State> possible = checkPossibleDescendants(n.getState(), method, n);
            for(State s : possible){
                Node aux = new Node(s, n.getDepth() + 1, n.getDepth() + 1);
                if(!explored.contains(aux)){
                    n.addToDescendants(aux);
                    aux.setParent(n);
                    tree.add(aux);
                    leaves.add(aux);
                    explored.add(aux);
                }
            }
            leaves.sort((o1, o2) -> h.getHValue(o1.getState()) - h.getHValue(o2.getState()));
            returnNode toRet = searchLocalWithBack(leaves);
            list.remove(n);
            if (toRet.result)
                return toRet;
        }
        return new returnNode(explored.size(), leaves.size(), -1, -1, false, "No solution");
    }

    private returnNode searchLocalNoBack(Node current) {
        if (current == null){
            return new returnNode(explored.size(), leaves.size(), -1, -1, false, "No solution");
        }
        if(current.getState().equals(objectiveState)){
            return generateReturnNode(current);
        }
        LinkedList<State> possible = checkPossibleDescendants(current.getState(), method, current);
        for(State s : possible){
            Node aux = new Node(s, current.getDepth() + 1, current.getDepth() + 1);
            if(!explored.contains(aux)){
                current.addToDescendants(aux);
                aux.setParent(current);
                tree.add(aux);
                leaves.add(aux);
                explored.add(aux);
            }
        }
        leaves.sort((o1, o2) -> h.getHValue(o1.getState()) - h.getHValue(o2.getState()));
        if (leaves.isEmpty())
            return searchLocalNoBack(null);
        return searchLocalNoBack(leaves.getFirst());
    }

    private returnNode generateReturnNode(Node current) {
        Node aux = current.getParent();
        StringBuilder s = new StringBuilder();
        s.insert(0, current.getState().toString());
        int i = 0;
        while(aux != null){
            s.insert(0, aux.getState().toString() + " --> ");
            aux = aux.getParent();
            if(i++ % 4 == 0){
                s.insert(0, "\n");
            }
        }
        return new returnNode(explored.size(), leaves.size(), current.getDepth(),
                current.getDepth(), true, s.toString());
    }

    private LinkedList<State> getDescendants(State current, int hasOne, int lower) {
        long[] newState1, newState2, newState3;
        newState1 = new long[3];
        newState2 = new long[3];
        newState3 = new long[3];
        int other = 3 - hasOne - lower;


        long hasOneNum = current.getTower(hasOne);
        long lowerNum = current.getTower(lower);
        long otherNum = current.getTower(other);

        newState1[hasOne] = remove(hasOneNum);
        newState1[lower] = add(lowerNum, hasOneNum);
        newState1[other] = otherNum;

        newState2[hasOne] = remove(hasOneNum);
        newState2[lower] = lowerNum;
        newState2[other] = add(otherNum, hasOneNum);

        newState3[hasOne] = hasOneNum;
        newState3[lower] = (lowerNum == otherNum ? lowerNum : remove(lowerNum));
        newState3[other] = (lowerNum == otherNum ? lowerNum : add(otherNum, lowerNum));

        LinkedList<State> toReturn = new LinkedList<>();

        toReturn.add(new State(newState1));
        toReturn.add(new State(newState2));
        toReturn.add(new State(newState3));
        return toReturn;
    }

    private LinkedList<State> checkPossibleDescendants(State current, Method alg, Node currentN) {

        long peekFirst = current.getTower(0) % 10;
        long peekSecond = current.getTower(1) % 10;
        long peekThird = current.getTower(2) % 10;

        LinkedList<State> toReturn = new LinkedList<>();

        if (peekFirst == 1) {
            if (peekSecond < peekThird)
                toReturn =  getDescendants(current,0, 1);
            else
                toReturn = getDescendants(current, 0, 2);
        } else if (peekSecond == 1) {
            if (peekFirst < peekThird)
                toReturn = getDescendants(current,1, 0);
            else
                toReturn = getDescendants(current,1, 2);
        } else {
            if (peekFirst < peekSecond)
                toReturn = getDescendants(current,2, 0);
            else
                toReturn = getDescendants(current,2, 1);
        }

        return toReturn;
    }

    private long add(long n, long disc) {
        return (n * 10) + (disc%10);
    }

    private long remove(long n) {
        return (n - (n%10))/10;
    }

    private returnNode searchBPPV(Node firstNode){
        for (int i = limit; i < MAX_DEPTH; i++){
            leaves = new LinkedList<>();
            leaves.add(firstNode);
            tree = new LinkedList<>();
            explored = new LinkedList<>();
            returnNode aux = searchBPPVRecInc(i);
            if (aux != null)
                return aux;
            System.out.println("No se encontro solucion en " + i + " niveles.");
        }
        for (int i = limit; i >= 0; i--){
            leaves = new LinkedList<>();
            leaves.add(firstNode);
            tree = new LinkedList<>();
            explored = new LinkedList<>();
            tree = new LinkedList<>();
            returnNode aux = searchBPPVRecDec(i);
            if (aux != null)
                return aux;
            System.out.println("No se encontro solucion en " + i + " niveles.");
        }
        return new returnNode(explored.size(), leaves.size(), -1, -1, false, "No solution");
    }

    private returnNode searchBPPVRecInc (int depth){
        if (leaves.isEmpty())
            return null;
        Node first = leaves.getFirst();
        if (first.getState().equals(objectiveState) && first.getDepth() == depth)
            return printObjective(first);
        if (first.getDepth() > depth)
            return null;
        LinkedList<State> possible = checkPossibleDescendants(first.getState(), method, first);
        for(State s : possible){
            Node aux = new Node(s, first.getDepth() + 1, first.getDepth() + 1);
            if(!explored.contains(aux)){
                first.addToDescendants(aux);
                aux.setParent(first);
                tree.add(aux);
                leaves.add(aux);
                explored.add(aux);
            }
        }
        leaves.remove(first);
        leaves.sort((o1, o2) -> o1.getDepth() - o2.getDepth());
        return searchBPPVRecInc(depth);
    }

    private returnNode searchBPPVRecDec (int depth){
        if (leaves.isEmpty())
            return null;
        Node first = leaves.getFirst();
        if (first.getState().equals(objectiveState) && first.getDepth() == depth)
            return printObjective(first);
        if (first.getDepth() > depth)
            return null;
        LinkedList<State> possible = checkPossibleDescendants(first.getState(), method, first);
        for(State s : possible){
            Node aux = new Node(s, first.getDepth() + 1, first.getDepth() + 1);
            if(!explored.contains(aux)){
                first.addToDescendants(aux);
                aux.setParent(first);
                tree.add(aux);
                leaves.add(aux);
                explored.add(aux);
            }
        }
        leaves.remove(first);
        leaves.sort((o1, o2) -> o1.getDepth() - o2.getDepth());
        return searchBPPVRecDec(depth);
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
        return new returnNode(explored.size(), leaves.size(), node.getDepth(),
                node.getDepth(), true, s.toString());
    }


    public static void main(String[] args) throws IOException {
        long initialTime = System.currentTimeMillis();
        SearchMethods search = new SearchMethods();

        Properties prop = new Properties();
        String propFileName = "config.properties";

        InputStream inputStream = SearchMethods.class.getClassLoader().getResourceAsStream(propFileName);
        if (inputStream == null){
            System.out.println("Error leyendo el archivo de configuración");
            return;
        }
        prop.load(inputStream);

        String methodStr = prop.getProperty("method");
        String heuristicStr = prop.getProperty("heuristic");
        String BPPVDepthStr = prop.getProperty("BPPVDepth");
        inputStream.close();

        Method method;
        switch (methodStr){
            case "BPA": method = Method.BPA; break;
            case "BPP": method = Method.BPP; break;
            case "BPPV": method = Method.BPPV; break;
            case "LOCAL_NO_BACK": method = Method.LOCAL_NO_BACK; break;
            case "LOCAL_BACK": method = Method.LOCAL_BACK; break;
            case "GLOBAL": method = Method.GLOBAL; break;
            case "A_STAR": method = Method.A_STAR; break;
            default: System.out.println("Método inválido"); return;
        }
        search.setMethod(method);
        if (method.equals(Method.LOCAL_BACK) || method.equals(Method.LOCAL_NO_BACK) || method.equals(Method.GLOBAL) || method.equals(Method.A_STAR)) {
            Heuristic heuristic;
            switch (heuristicStr) {
                case "1":
                    heuristic = new Heuristic1();
                    break;
                case "2":
                    heuristic = new Heuristic2();
                    break;
                case "3":
                    heuristic = new Heuristic3();
                    break;
                default:
                    System.out.println("Heurística inválida");
                    return;
            }
            search.setHeuristic(heuristic);
        }
        else if (method.equals(Method.BPPV))
            search.setDepth(Integer.parseInt(BPPVDepthStr));

        State s = search.getFirstState();
        Node i = search.setFirstNode();

        returnNode n = search.Search(i, s, method);

        long endingTime = System.currentTimeMillis();
        long totalTime = (endingTime - initialTime);
        StringBuilder str = new StringBuilder();
        str.append("Resultados: \n").append("Tiempo de ejecución (ms): "). append(totalTime).append("\n");
        str.append("Encontró solución: ").append(n.getResult()).append("\n");
        if(n.getResult()) {
            str.append("Solución: ").append(n.getSolution()).append("\n");
            str.append("Costo de solución: ").append(n.getCost()).append("\n");
            str.append("Profundidad de solución: ").append(n.getDepth()).append("\n");
        }
        str.append("Nodos expandidos: ").append(n.getExpandedNodes()).append("\n");
        str.append("Nodos frontera: ").append(n.getFrontierNodes()).append("\n");
        System.out.println(str);
    }

    private void setMethod(Method method) {
        this.method = method;
    }

    private void setDepth (int depth){
        this.limit = depth;
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
