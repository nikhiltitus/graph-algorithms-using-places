from collections import deque
import sys
import argparse

class Place:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, place, distance):
        self.neighbors[place] = distance


class Graph:
    def __init__(self):
        self.place_map = {}

    def add_place(self, name):
        place = Place(name)
        self.place_map[place.name] = place
        return place

    def get_place(self, name):
        if name in self.place_map:
            return self.place_map[name]
        else:
            return False
    '''BFS Implementation'''
    def check_path(self, source, destination):
        visited_places = set()
        queue = deque()
        queue.append(source)
        while queue:
            place = queue.popleft()
            visited_places.add(place)
            for neighbor in place.neighbors:
                if neighbor == destination:
                    return True
                elif neighbor not in visited_places:
                    queue.append(neighbor)
        return False
    def min_distance(self,distance_map):
        min_distance=sys.maxsize
        min_place=None
        for place,distance in distance_map.items():
            if distance<min_distance:
                min_distance=distance
                min_place=place
        return min_place

    def dijkstra(self,source,destination):
        visited_places=set()
        distance_map = {source.name:0}
        current=source.name
        current_distance=None
        while destination.name not in visited_places and current is not None:
            current_place = self.place_map[current]
            for place,distance in current_place.neighbors.items():
                if place.name not in visited_places:
                    new_distance=distance_map[current]+int(distance)
                    distance_map[place.name]=min(distance_map.get(place.name,sys.maxsize),new_distance)
            visited_places.add(current)
            current_distance=distance_map[current]
            distance_map.pop(current,None)
            current=self.min_distance(distance_map)
        if destination.name in visited_places:
            return current_distance
        else:
            return False


def read_file(file_name):
    graph = Graph()
    with open(file_name) as f:
        content = f.readlines()
        for line in content:
            source, destination, distance = line.split(',')
            source_place = graph.get_place(source)
            destination_place = graph.get_place(destination)
            if not source_place:
                source_place = graph.add_place(source)
            if not destination_place:
                destination_place = graph.add_place(destination)
            source_place.add_neighbor(destination_place, distance)
            destination_place.add_neighbor(source_place, distance)
    return graph


def main():
    parser = argparse.ArgumentParser(description='Check if path exist and get distance')
    parser.add_argument('source', metavar='source', type=str,help='source string')
    parser.add_argument('destination', metavar='destination', type=str, help='destination string')
    parser.add_argument('fileLocation',nargs='?', metavar='fileLocation', type=str, help='destination string',default='placeinfo')
    args = parser.parse_args()
    graph = read_file(args.fileLocation)
    source=args.source
    destination=args.destination
    print('Does a path exist: '+str(graph.check_path(graph.get_place(source), graph.get_place(destination))))
    print('Distance between source and destination: '+str(graph.dijkstra(graph.get_place(source),graph.get_place(destination))))

if __name__ == "__main__":
    main()
