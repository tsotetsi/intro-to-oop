import unittest

from main import Bus


class TestBusClass(unittest.TestCase):
    """
    Testcase class for Bus
    """
    def setUp(self) -> None:
        self.bus = Bus(10, "Red", "Tumelo")

    def test_init_method(self):
        self.assertEqual(self.bus.color, "Red", "Color should be red")
        self.assertEqual(self.bus.driver, "Tumelo", "The driver should be Tumelo")
        self.assertEqual(self.bus.num_off_seats, 10, "The number of seats should be 10(ten)")

    def test_change_color(self):
        self.bus.change_color("Blue")
        self.assertEqual(self.bus.color, "Blue", "The should be Blue.")

    def test_number_of_bus_created(self):
        self.assertEqual(self.bus.num_bus_created, 3, "3 busses should have been created.")