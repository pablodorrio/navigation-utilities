"""Container module for the Oxts class.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import numpy as np

from .coordinate import Coordinate

EARTH_RADIUS = 6371000


class Oxts:
    """This class represents the OxTS sentence.

    Attributes:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
    """

    def __init__(self, latitude: float, longitude: float) -> None:
        """Initialize the OxTS sentence.

        Args:
            latitude (float): Latitude of the location in decimal degrees.
            longitude (float): Longitude of the location in decimal degrees.
        """
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self) -> float:
        """Get the latitude of the location in decimal degrees.

        Returns:
            float: Latitude.
        """
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """Set the latitude of the location in decimal degrees.

        Args:
            latitude (float): Latitude.
        """
        self.__latitude = latitude

    @property
    def longitude(self) -> float:
        """Get the longitude of the location in decimal degrees.

        Returns:
            float: Longitude.
        """
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """Set the longitude of the location in decimal degrees.

        Args:
            longitude (float): Longitude.
        """
        self.__longitude = longitude

    def to_coordinate(self, lat_0: float, lon_0: float) -> Coordinate:
        """Transform the latitude and longitude to a bidimensional (x, y) coordinate.

        Args:
            lat_0 (float): Latitude of the origin in decimal degrees.
            lon_0 (float): Longitude of the origin in decimal degrees.

        Returns:
            Coordinate: Bidimensional (x, y) coordinate of the location.
        """
        lat_0, lon_0, lat, lon = map(
            np.radians, [lat_0, lon_0, self.latitude, self.longitude])
        delta_lat, delta_lon = lat - lat_0, lon - lon_0

        x_coord = ((np.cos(lat_0)*np.sin(lat) - np.sin(lat_0)
                   * np.cos(lat)*np.cos(delta_lon)))
        y_coord = np.sin(delta_lon)*np.cos(lon)
        theta = np.arctan2(y_coord, x_coord)

        haversine_distance = ((2 * EARTH_RADIUS * np.arcsin(np.sqrt(np.sin(
            delta_lat / 2)**2 + np.cos(lat_0) * np.cos(lat) * np.sin(delta_lon / 2)**2))))

        x_coord, y_coord = ((haversine_distance * np.sin(theta),
                            haversine_distance * np.cos(theta)))

        return Coordinate(x_coord, y_coord)
