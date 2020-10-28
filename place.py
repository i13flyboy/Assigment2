class Place:
    def __init__(self, city="", country="", priority=0, is_visited=False):
        self.city = city
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        if self.is_visited == True:
            visit_status = "Visited"
        else:
            visit_status = ""
        return "City {} Country {} with priority of ({}) status {}".format(self.city, self.country, self.priority,
                                                                           visit_status)

    #def __repr__(self):
        #if self.is_visited == True:
            #visit_status = "Visited"
        #else:
            #visit_status = ""
        #return "City {} Country {} with priority of ({}) status {}".format(self.city, self.country, self.priority,
                                                                           #visit_status)

    def get_place_name(self):
        return self.city

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
        return self.is_visited

    pass
