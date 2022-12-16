import unittest
from fpl import Fixtures


class TestFixtures(unittest.TestCase):
    def test_entry(self):
        fixtures = Fixtures().fetch(event=4194)


if __name__ == '__main__':
    unittest.main()