"""Container module for NMEA data format classes.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

from .utils.time import Time


class Nmea:
    """This class represents a NMEA sentence.

    Attributes:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location.
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
