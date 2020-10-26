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
        loads in the csv file called places.csv
        """
        place = open(filename, "r")
        place.readlines()
        for line in place:
            if line == "":
                print("blank line here")
            else:
                line = line.strip()
                place = line.split(",")
                visited_symbol = False
                if place[3] == 'w':
                    visited_symbol = True
                self.add_place(Place(place[0], int(place[1]), place[2], visited_symbol))
        place.close()

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
        self.sort("priority")
        visited_places = []
        for place in self.places:
            visited_symbol = 'n'
            if place.is_visited is True:
                visited_symbol = "V"
            visited_places.append("{},{},{}".format(place.place, place.country, place.priority, visited_symbol))
            visited_places.append("\n")
            exported_file.writelines(visited_places)
        exported_file.close()

    def sort(self, key):
        self.places.sort(key=attrgetter(key, "place"))
    pass