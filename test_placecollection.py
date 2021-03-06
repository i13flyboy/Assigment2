"""(Incomplete) Tests for PlaceCollection class."""
from place import Place
from place_collection import PlaceCollection


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places is True  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    open('places.csv')
    print(place_collection)
    assert not place_collection.places is True  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("\nTest sorting - place:")
    place_collection.sort("priority")
    for place_collection in place_collection.places:
        print(place_collection)


run_tests()
