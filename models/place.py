#!/usr/bin/python3
"""
This file is for declaring
and defining our Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class represents our Place entity.

    The Attributes we'll be using:

        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): List of amenity IDs associated with the place.

    Return:
        None
    """

    def __init__(self, *args, **kwargs):
        """we will Initialize our Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
