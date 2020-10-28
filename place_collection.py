from place import Place
from operator import attrgetter


class PlaceCollection:
    """
    Create the list of places
    """
    def __init__(self):
        self.places = []

    def __str__(self):
        """
        String function
        """
        return "{}".format(self.places)

    def add_place(self, place):
        """
        Add the new place to the Place list
        """
        self.places.append(place)

    def load_places(self, filename="places.csv"):
        """
        load the places
        """
        with open(filename) as input_file:
            for line in input_file:
                line2 = line.strip()
                parts = line2.split(",")
                place = Place(parts[0], parts[1], int(parts[2]))
                if parts[3] == 'n':
                    place.is_visited = False
                else:
                    place.is_visited =True
                self.add_place(Place(parts[0], parts[1], int(parts[2])))
            input_file.close()
        for place in self.places:
            print(place)
        print(self.places)

    def get_number_visited(self):
        """
        get the number of visited places
        """
        places_visited_counter = 0
        for place in self.places:
            if place.is_visited is True:
                places_visited_counter += 1
        return places_visited_counter

    def get_number_not_visited(self):
        """
        get the number of not visited places
        """
        places_not_visited_counter = 0
        for place in self.places:
            if not place.is_watched:
                places_not_visited_counter += 1
        return places_not_visited_counter

    def save_places(self, filename="places.csv"):
        """
        Save the places
        """
        exported_file = open(filename, 'w')
        self.sort("place")
        visited_places = []
        for place in self.places:
            visited_symbol = 'n'
            if place.is_visited is True:
                visited_symbol = "V"
            visited_places.append("{},{},{}".format(place.city, place.country, place.priority, visited_symbol))
            visited_places.append("\n")
            exported_file.writelines(visited_places)
        exported_file.close()

    def sort(self, attr="priority"):
        self.places.sort(key=attrgetter(attr, "priority"))
