"""Container module for NMEA($GNGGA) data format class.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

from .coordinate import Coordinate
from .nmea import Nmea, NmeaError
from .oxts import Oxts
from .utils.time import Time


class Gngga(Nmea):
    """This class represents a NMEA($GNGGA) sentence.

    Attributes:
        latitude (str): Latitude of the location.
        longitude (str): Longitude of the location.
        time (TIme): Time of the location.
    """

    def __init__(self, sentence: str) -> None:
        """Initialize the NMEA($GNGGA) sentence.

        Args:
            sentence (str): NMEA($GNGGA) sentence.

        Raises:
            NmeaError: If the sentence is not a NMEA($GNGGA) sentence.
        """

        if sentence.strip().split(",")[0] != "$GNGGA":
            raise NmeaError("Error: invalid $GNGGA sentence.")
        else:
            self.sentence = sentence.strip()

        latitude = self.__parse_latitude()
        longitude = self.__parse_longitude()
        time = self.__parse_time()

        super().__init__(latitude, longitude, time)

    def to_oxts(self) -> Oxts:
        """Transform the latitude and longitude from NMEA ($GNGGA)
        to decimal degrees.

        Returns:
            Oxts: OxTS sentence with the latitude and longitude in decimal degrees.
        """

        lat_deg = int(super().latitude[:2])  # Degrees
        lat_min = float(super().latitude[2:-1])  # Minutes

        lon_deg = int(super().longitude[:3])  # Degrees
        lon_min = float(super().longitude[3:-1])  # Minutes

        lat_dec = lat_deg + (lat_min / 60)
        lon_dec = lon_deg + (lon_min / 60)

        if super().latitude[-1] == "S":  # North or south
            lat_dec *= -1
        if super().longitude[-1] == "W":  # East or west
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

    def __parse_latitude(self) -> str:
        """Parse the latitude from the NMEA($GNGGA) sentence.

        NMEA ($GNGGA) latitude format: "DDMM.MMMMMMMC"
            Example: "4217.8161502N"

        Returns:
            str: Latitude of the location.
        """
        if self.sentence.split(",")[2] == "" or self.sentence.split(",")[3] == "":
            latitude = None
        else:
            latitude = self.sentence.split(",")[2] + self.sentence.split(",")[3]

        return latitude

    def __parse_longitude(self) -> str:
        """Parse the longitude from the NMEA($GNGGA) sentence.

        NMEA ($GNGGA) longitude format: "DDDMM.MMMMMMM"
            Example: "00748.0032395W"

        Returns:
            str: Longitude of the location.
        """
        if self.sentence.split(",")[4] == "" or self.sentence.split(",")[5] == "":
            longitude = None
        else:
            longitude = self.sentence.split(",")[4] + self.sentence.split(",")[5]

        return longitude

    def __parse_time(self) -> Time:
        """Parse the time from the NMEA($GNGGA) sentence.

        Returns:
            Time: Time of the location.
        """
        if self.sentence.split(",")[1] == "":
            time = None
        else:
            not_parsed_time = self.sentence.split(",")[1]

            hours = int(not_parsed_time[:2])
            mins = int(not_parsed_time[2:4])
            secs = int(not_parsed_time[4:6])
            msecs = int(not_parsed_time[7:])

            time = Time(hours, mins, secs, msecs)

        return time

    def __str__(self) -> str:
        """Get the string representation of the NMEA($GNGGA) sentence.

        Returns:
            str: String representation of the NMEA($GNGGA) sentence.
        """
        return f"{super().__str__()}"
