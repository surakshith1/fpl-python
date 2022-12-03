import unittest
from fpl import PlayerEntry


class TestEntry(unittest.TestCase):
    def test_entry(self):
        # Create an instance of the Entry class
        entry = PlayerEntry().fetch(59865)

        # Assert that the id attribute is equal to 59865
        self.assertEqual(entry.id, 59865)

        # Assert that the name attribute is equal to "ETH"
        self.assertEqual(entry.name, "ETH")


if __name__ == '__main__':
    unittest.main()
