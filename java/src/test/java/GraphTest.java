import org.junit.Assert;
import org.junit.Before;
import org.testng.annotations.Test;

public class GraphTest {
    private Graph graph;

    @Before
    @Test(groups={"checkpath-test"})
    //Set up with place 1 connected to 2 and 3. place 4 connected to 3.
    public void setUp(){
        graph=new Graph();
        Place place1 = graph.addPlace("1"),place2=graph.addPlace("2"),place3=graph.addPlace("3"),place4=graph.addPlace("4");
        graph.addPlace("5");
        place1.addNeighbor(place2);place1.addNeighbor(place3);
        place3.addNeighbor(place4);
    }
    @Test(groups={"checkpath-test"})
    public void testCheckPath(){
        System.out.println("Running testcheckpath");
        Assert.assertTrue(graph.checkPath("1","4"));
        Assert.assertFalse(graph.checkPath("1","5"));
    }
}
