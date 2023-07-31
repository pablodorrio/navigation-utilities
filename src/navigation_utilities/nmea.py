"""Container module for NMEA data format classes.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

from .coordinate import Coordinate
from .oxts import Oxts
from .utils.time import Time


class Nmea:
    """This class represents a NMEA sentence.

    Attributes:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location.
        time (Time): Time of the location.
    """

    def __init__(self, latitude: str, longitude: str, time: Time) -> None:
        """Initialize the NMEA sentence.

        Args:
            latitude (str): Latitude of the location.
            longitude (str): Longitude of the location.
        """
        self.__latitude = latitude
        self.__longitude = longitude
        self.__time = time

    @property
    def latitude(self) -> str:
        """Get the latitude of the location.

        Returns:
            str: Latitude of the location.
        """
        return self.__latitude

    @property
    def longitude(self) -> str:
        """Get the longitude of the location.

        Returns:
            str: Longitude of the location.
        """
        return self.__longitude

    @property
    def time(self) -> Time:
        """Get the time of the location.

        Returns:
            Time: Time of the location.
        """
        return self.__time
    
    def to_oxts(self) -> Oxts:
        """Transform the latitude and longitude from NMEA ($GNGGA)
        to decimal degrees.

        Returns:
            Oxts: OxTS sentence with the latitude and longitude in decimal degrees.
        """

        lat_deg = int(self.latitude[:2])  # Degrees
        lat_min = float(self.latitude[2:-1])  # Minutes

        lon_deg = int(self.longitude[:3])  # Degrees
        lon_min = float(self.longitude[3:-1])  # Minutes

        lat_dec = lat_deg + (lat_min / 60)
        lon_dec = lon_deg + (lon_min / 60)

        if self.latitude[-1] == "S":  # North or south
            lat_dec *= -1
        if self.longitude[-1] == "W":  # East or west
            lon_dec *= -1

        return Oxts(lat_dec, lon_dec)

    def to_coordinate(self, lat_0: float, lon_0: float) -> Coordinate:
        """Transform the latitude and longitude from NMEA($GNGGA)
        to a bidimensional (x, y) coordinate.

        Args:
            lat_0 (float): Latitude of the origin in decimal degrees.
            lon_0 (float): Longitude of the origin in decimal degrees.

        Returns:
            Coordinate: Bidimensional (x, y) coordinate of the location.
        """
        oxts = self.to_oxts()
        return oxts.to_coordinate(lat_0, lon_0)

    def __str__(self) -> str:
        """Get the string representation of the NMEA sentence.

        Returns:
            str: String representation of the NMEA sentence.
        """
        return f"Latitude: {self.__latitude}, Longitude: {self.__longitude}, Time: {self.__time}"


class NmeaError(Exception):
    """Exception raised for errors in the NMEA sentence.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str) -> None:
        """Initialize the NmeaError exception.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)
