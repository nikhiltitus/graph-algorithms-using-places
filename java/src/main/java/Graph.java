import exceptions.PlaceNotFoundException;

import java.util.*;

public class Graph {

    Map <String,Place> placeMap;

    Graph(){

        placeMap = new HashMap<String, Place>();
    }

    public Place addPlace(String name){
        Place place = new Place();
        place.setName(name);
        placeMap.put(name,place);
        return place;
    }

    public Place getPlace(String name)throws PlaceNotFoundException{
        if (placeMap.containsKey(name)){
            return placeMap.get(name);
        }
        else{
            throw new PlaceNotFoundException(name);
        }
    }
    //BFS implementation to see if a route exists
    public boolean checkPath(String source,String destination){
        HashSet<Place> placeSet = new HashSet<Place>();
        Place sourcePlace=placeMap.get(source);
        Place destinationPlace=placeMap.get(destination);
        Queue traversalQueue=new LinkedList();
        traversalQueue.add(sourcePlace);
        while (!traversalQueue.isEmpty()){
            Place place = (Place) traversalQueue.remove();
            placeSet.add(place);
            if (place == destinationPlace)
                return true;
            for (Place neighbor:place.getNeighborList()){
                if (!placeSet.contains(neighbor)){
                    traversalQueue.add(neighbor);
                }
            }
        }
        return false;
    }
}
