from graph import Graph
from graph import read_file
import unittest


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph=read_file('placeinfo_test')
        self.source_place = self.graph.get_place('Kochi')
        self.destination_place = self.graph.get_place('Elanthoor')
    def test_bfs(self):
        self.assertTrue(self.graph.check_path(self.source_place,self.destination_place))
    def test_dijkstra(self):
        self.assertEquals(self.graph.dijkstra(self.source_place,self.destination_place),125)

if __name__ == '__main__':
    unittest.main()