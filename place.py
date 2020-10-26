class Place:
    def __init__(self, name="", country="", priority=0, is_visited=True, not_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited
        self.not_visited = not_visited

    def __str__(self):
        if self.is_visited:
            visit_status = "Visited"
        else:
            visit_status = ""
        return "Name {} Country {} with priority {} status {}".format(self.name, self.country, self.priority,
                                                                      visit_status)

    def __repr__(self):
        return "Name {} Country {} with priority {} status {}".format(self.name, self.country, self.priority,)

    def get_place_name(self):
        return self.name

    def get_country(self):
        return self.country

    def get_priority(self):
        return self.priority

    def place_is_visited(self):
        """
        Mark the current place as visited
        """
        return self.is_visited

    def place_is_not_visited(self):
        """
        Mark the current place as visited
        """
        return self.not_visited
    pass
