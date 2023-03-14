"""Container module for NMEA data format classes.

Author:
    Pablo Dorrio Vazquez
"""

from .oxts import Oxts
from .utils.coordinate import Coordinate
from .utils.time import Time


class Nmea:
    """This class represents a NMEA sentence.

    Attributes:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location.
    """

    def __init__(self, latitude: str, longitude: str) -> None:
        """Initialize the NMEA sentence.

        Args:
            latitude (str): Latitude of the location.
            longitude (str): Longitude of the location.
        """
        self.__latitude = latitude
        self.__longitude = longitude

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

    def __str__(self) -> str:
        """Get the string representation of the NMEA sentence.

        Returns:
            str: String representation of the NMEA sentence.
        """
        return f"{self.__latitude}, {self.__longitude}"


class Gpgga(Nmea):
    """This class represents a NMEA(GPGGA) sentence.
    
    Attributes:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location.
        time (Time): Time of the location.
    """

    def __init__(self, latitude: str, longitude: str, time: Time) -> None:
        """Initialize the NMEA(GPGGA) sentence.

        Args:
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
            time (Time): Time of the location.

        NMEA (GPGGA) latitude format: "DDMM.MMMMMMMC"
        NMEA (GPGGA) longitude format: "DDDMM.MMMMMMM"

        Example:    latitude = "4217.8161502N"
                    longitude = "00748.0032395W"
        """
        super().__init__(latitude, longitude)
        self.__time = time

    def to_oxts(self) -> Oxts:
        """Transform the latitude and longitude from NMEA (GPGGA)
        to decimal degrees.

        Returns:
            OxTS: OXTS sentence whit the latitude and longitude in decimal degrees.
        """

        lat_dir = super().latitude[-1]  # North or south
        lat_deg = int(super().latitude[:2])  # Degrees
        lat_min = float(super().latitude[2:-1])  # Minutes

        lon_dir = super().longitude[-1]  # East or west
        lon_deg = int(super().longitude[:3])  # Degrees
        lon_min = float(super().longitude[3:-1])  # Minutes

        lat_dec = lat_deg + (lat_min / 60)
        lon_dec = lon_deg + (lon_min / 60)

        if lat_dir == 'S':
            lat_dec *= -1
        if lon_dir == 'W':
            lon_dec *= -1

        return Oxts(lat_dec, lon_dec)

    def to_coordinate(self, lat_0: float, lon_0: float) -> Coordinate:
        """Transform the latitude and longitude from NMEA (GPGGA)
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
        """Get the string representation of the NMEA(GPGGA) sentence.

        Returns:
            str: String representation of the NMEA(GPGGA) sentence.
        """
        return f"{self.__time}, {super().__str__()}"
