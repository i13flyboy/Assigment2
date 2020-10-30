"""
Name:Kyle Kunz
Date:10/10/2020
Brief Project Description:this is a program that allows you to add places you want ot travel to
and mark off places that you have visited.
GitHub URL: https://github.com/i13flyboy/Assigment2
"""
# Create your main program in this file, using the TravelTrackerApp class
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from place_collection import PlaceCollection
from place import Place


__author__ = 'Kyle Kunz'

sort_dictionary ={'Priority': 'priority', 'Visited': 'is_visited', 'Country': 'country'}
VISITED_COLOUR = (1, 0.5, 1, 1)
NOT_VISITED_COLOUR = (0, 1, 1, 0.7)
BLANK_STRING = ""


class TravelTrackerApp(App):
    """
    main program
    """
    current_place = StringProperty()
    list_codes = ListProperty
    program_status_bar = StringProperty()
    visited_status_message = StringProperty()

    def __init__(self, **kwargs):
        """
        makes the main app
        """
        super().__init__(**kwargs)
        self.place_collections = PlaceCollection()
        self.place = Place
        self.place_collections.load_places("places.csv")
        self.list_codes = sort_dictionary

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Travel Tracker APP"
        self.root = Builder.load_file('app.kv')
        self.list_codes = sorted(sort_dictionary.keys())
        self.root.ids.select_day.text = self.list_codes[2]
        self.dynamic_places()
        return self.root

    def change_status(self, list_code):
        self.root.ids.output_label = sort_dictionary[list_code]
        self.place_collections.sort(sort_dictionary[list_code])

    def dynamic_places(self):
        index = 1
        for place in self.place_collections.places:
            temp_button = Button(text=str(place), id=str(index))
            temp_button.place = place
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.box_list.add_widget(temp_button)
            index = index + 1
        return

    def press_entry(self, instance):
        """
        updates the entry
        """
        instance.place.is_visited = True
        self.root.ids.status_visited.text = "You visited " + instance.place.country
        self.root.ids.box_list.clear_widgets()
        self.dynamic_places()

    def on_stop(self):
        self.place_collections.save_places("places.csv")
        print("Bye")

    def create_widget(self):
        """
        makes all the place buttons
        """
        self.update_visited_status_bar()
        for index, place in enumerate(self.place_collections.places):
            visited_status = BLANK_STRING
            if place.is_visited:
                colour = VISITED_COLOUR
                visited_status = "visited"
            else:
                colour = NOT_VISITED_COLOUR
            temp_button = Button(
                text=str("{} {} {} ({})".format(place.city, place.country, place.priority, visited_status)),
                id=str(index), background_color=colour)
            temp_button.bind(on_release=self.handle__button_press)
            self.root.ids.box_list.add_widget(temp_button)

    def handle__button_press(self, instance):
        """
        handle pressing buttons
        """
        index_number = int(instance.id)
        if self.place_collections.places[index_number].is_visited:
            self.place_collections.places[index_number].place_is_visited()
            place_is_not_visited = self.place_collections.places[index_number]
            self.update_program_status_bar("You need to visit {}".format(place_is_not_visited))
        else:
            self.place_collections.places[index_number].place_is_visited()
            place_is_visited = self.place_collections.places[index_number]
            self.update_program_status_bar("You visited {}".format(place_is_visited))
        self.root.ids.box_list.clear_widgets()
        self.sort_places(self.root.ids.select_day.text)

    def add_new_place(self):
        """
        adds new place to the place collection
        """
        # Get the text from the text inputs
        new_place = self.root.ids.new_place.text
        new_country = self.root.ids.new_country.text
        new_priority = self.root.ids.new_priority.text

        if new_place == BLANK_STRING or new_country == BLANK_STRING or new_priority == BLANK_STRING:
            self.update_program_status_bar("All fields must be completed")
        else:
            try:
                new_priority = int(new_priority)
                if new_priority < 0:
                    self.update_program_status_bar("Please enter a number >= 0")
                    self.update_program_status_bar("Please enter a number <= 0")
                else:
                    self.root.ids.new_place.text = BLANK_STRING
                    self.root.ids.new_country.text = BLANK_STRING
                    self.root.ids.new_priority.text = BLANK_STRING
                    self.place_collections.add_place(
                        Place(new_place, new_country, new_priority))
                    self.sort_places(self.root.ids.select_day.text)
                    self.update_program_status_bar(
                        "{} {} from {} Added".format(new_place, new_country, new_priority))
            except ValueError:
                self.update_program_status_bar("Please enter a valid number")
            except TypeError:
                self.update_program_status_bar("Please enter a valid number")

    def update_visited_status_bar(self):
        """
        updates on how many places have been visited
        """
        self.visited_status_message = "To visited: {}. visited: {}".format(self.place_collections.get_number_not_visited
                                                                           (),
                                                                           self.place_collections.get_number_visited())

    def update_program_status_bar(self, instance):
        """
        updates when ever a function passes through
        """
        self.program_status_bar = "{}".format(instance)

    def sort_places(self, text):
        """
        sort the current places
        """
        text = text.lower()  # Call lower because it needs to be a capital in the spinner but lower case for sort
        if text == "visited":
            text = "is_visited"
        self.place_collections.sort(text)
        self.root.ids.box_list.clear_widgets()
        self.create_widget()

    def handle_clear(self):
        """
        Clear the new place inputs and the status bar
        """
        self.root.ids.new_place.text = BLANK_STRING
        self.root.ids.new_country.text = BLANK_STRING
        self.root.ids.new_priority.text = BLANK_STRING
        self.update_program_status_bar(BLANK_STRING)


"""
Run main
"""
if __name__ == '__main__':
    TravelTrackerApp().run()
