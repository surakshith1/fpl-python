import unittest
from fpl import EntryHistory


class TestEntryHistory(unittest.TestCase):
    def test_entry_history(self):
        # Create an instance of the Entry class
        entry_history = EntryHistory().fetch(59865)

        # Assert that the id attribute is equal to 59865
        self.assertTrue(len(entry_history.past) > 0)


if __name__ == '__main__':
    unittest.main()
