import java.util.Arrays;

public class State {

    private long towers[];

    public State(long tower1, long tower2, long tower3) {
        this.towers = new long[3];
        towers[0] = tower1;
        towers[1] = tower2;
        towers[2] = tower3;
    }

    public State(long newState[]) {
        if(newState.length == 3) {
            this.towers = Arrays.copyOf(newState, 3);
        }
    }

    public long getTower(int num) {
        if(num < 0 || num > 2)
            return -1;
        return towers[num];
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        State state = (State) o;
        return Arrays.equals(towers, state.towers);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(towers);
    }

}
