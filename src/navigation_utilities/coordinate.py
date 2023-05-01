"""Container module for the Coordinate class.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""


class Coordinate:
    """This class represents a bidimensional coordinate.
    
    Attributes:
        x (float): x coordinate.
        y (float): y coordinate.
    """

    def __init__(self, x_coord: float, y_coord: float) -> None:
        """Initialize the coordinate.

        Args:
            x_coord (float): x coordinate.
            y_coord (float): y coordinate.
        """
        self.__x = x_coord
        self.__y = y_coord

    @property
    def x(self) -> float:
        """Get the x coordinate.

        Returns:
            float: x coordinate.
        """
        return self.__x

    @x.setter
    def x(self, x_coord: float) -> None:
        """Set the x coordinate.

        Args:
            x_coord (float): x coordinate.
        """
        self.__x = x_coord

    @property
    def y(self) -> float:
        """Get the y coordinate.

        Returns:
            float: y coordinate.
        """
        return self.__y

    @y.setter
    def y(self, y_coord: float) -> None:
        """Set the y coordinate.

        Args:
            y_coord (float): y coordinate.
        """
        self.__y = y_coord

    def __str__(self) -> str:
        """Get the string representation of the coordinate.

        Returns:
            str: String representation of the coordinate.
        """
        return f"{self.__x}, {self.__y}"
