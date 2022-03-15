import unittest
from bestTimeToTradeStock import maxProfit

class TestStock(unittest.TestCase):
    def test_maxProfit(self):
        assert maxProfit([0, 1]) == 1
    
def main():
    unittest.main()

if __name__ == "__main__":
    main()