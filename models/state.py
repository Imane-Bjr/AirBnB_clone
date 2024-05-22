#!/usr/bin/python3
"""
This file is for declaring
and defining our State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class represents our State entity.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize our State instance."""
        super().__init__(*args, **kwargs)
        if "name" in kwargs:
            self.name = kwargs["name"]
        else:
            self.name = ""
