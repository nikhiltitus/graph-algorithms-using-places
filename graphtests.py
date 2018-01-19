from graph import Graph
from graph import read_file
import unittest


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph=read_file('placeinfo_test')
        self.source_place = self.graph.get_place('Kochi')
        self.destination_place = self.graph.get_place('Elanthoor')
        self.disconnected_destination_place=self.graph.get_place('Boston')
    def test_bfs(self):
        self.assertTrue(self.graph.check_path(self.source_place,self.destination_place))
        self.assertFalse(self.graph.check_path(self.source_place,self.disconnected_destination_place))
    def test_dijkstra(self):
        self.assertEqual(self.graph.dijkstra(self.source_place,self.destination_place),125)
        self.assertFalse(self.graph.dijkstra(self.source_place,self.disconnected_destination_place))

if __name__ == '__main__':
    unittest.main()