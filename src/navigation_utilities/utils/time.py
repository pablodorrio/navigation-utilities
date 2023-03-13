"""This module contains the Time class."""


class Time:
    """This class represents a time in the format hh:mm:ss.
    
    Attributes:
        hours (int): Hours.
        minutes (int): Minutes.
        seconds (int): Seconds.
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        """Initialize the time sentence.

        Args:
            hours (int): Hours.
            minutes (int): Minutes.
            seconds (int): Seconds.
        """
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self) -> int:
        """Get the hours of the time.

        Returns:
            int: Hours."""
        return self.__hours

    @hours.setter
    def hours(self, hours: int) -> None:
        """Set the hours of the time.

        Args:
            hours (int): Hours.
        """
        self.__hours = hours

    @property
    def minutes(self) -> int:
        """Get the minutes of the time.

        Returns:
            int: Minutes.
        """
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int) -> None:
        """Set the minutes of the time.

        Args:
            minutes (int): Minutes.
        """
        self.__minutes = minutes

    @property
    def seconds(self) -> int:
        """Get the seconds of the time.

        Returns:
            int: Seconds.
        ."""
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int) -> None:
        """Set the seconds of the time.

        Args:
            seconds (int): Seconds.
        """
        self.__seconds = seconds

    def __str__(self) -> str:
        """Get the time representation of time in the format "hh:mm:ss".

        Returns:
            str: String representation of time.
        """
        return f"{self.__hours}:{self.__minutes}:{self.__seconds}"
