import java.util.ArrayList;
import java.util.List;

public class Place {
    String name;
    List<Place> neighborList;

    Place(){
        neighborList = new ArrayList<Place>();
    }

    public List<Place> getNeighborList() {
        return neighborList;
    }

    public void setNeighborList(List<Place> neighborList) {
        this.neighborList = neighborList;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void addNeighbor(Place place){
        neighborList.add(place);
    }

}
