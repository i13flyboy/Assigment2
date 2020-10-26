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

    def load_places(self, filename="places.csv"):
        """
        loads in the csv file called places.csv
        """
        p1 = Place
        self.add_place(p1)
        with open(filename) as input_file:
            for line in input_file:
                if line == "":
                    print("blank line here")
                else:
                    line = line.strip()
                    parts = line.split(",")
                    temp_city = Place(parts[1], int(parts[1]))
                    if parts[3] == 'n':
                        temp_city.is_visited = False
                    else:
                        temp_city.is_visited =True
                    self.add_place(Place(parts[1], int(parts[1]), temp_city))
            input_file.close()
        for place in self.places:
            print(place)
        print(self.places)

    def save_places(self, output_file):
        """
        Save the places
        """
        exported_file = open(output_file, 'w')
        self.sort("priority")
        visited_places = []
        for place in self.places:
            visited_symbol = 'n'
            if place.is_visited is True:
                visited_symbol = "V"
            visited_places.append("{},{},{}".format(place.name, place.country, place.priority, visited_symbol))
            visited_places.append("\n")
            exported_file.writelines(visited_places)
        exported_file.close()

    def sort(self, attr="priority"):
        self.places.sort(key=attrgetter(attr, "priority"))
    pass