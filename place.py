class Place:
    def __init__(self, name="", country="", priority=0, is_visited=True):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        if self.is_visited == True:
            visit_status = "visited"
        else:
            visit_status = ""
        return "{} ({}) {} {}".format(self.name, self.priority, self.country, visit_status)

    def __repr__(self):
        return "{} ({}) {} {}".format(self.name, self.country, self.priority, self.is_visited)

    def place_is_visited(self):
        """
        Mark the current place as visited
        """
        self.is_visited =True

    def place_is_not_visited(self):
        """
        Mark the current place as visited
        """
        self.is_visited = False
    pass