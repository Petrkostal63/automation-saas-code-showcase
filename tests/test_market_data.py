import unittest
from showcase.market_data import Observation, detect_burst


class MarketDataTests(unittest.TestCase):
    def test_price_and_volume_move_triggers_alert(self):
        result = detect_burst([Observation(100, 100), Observation(100.1, 100), Observation(102, 200)])
        self.assertTrue(result.triggered)

    def test_flat_price_does_not_trigger(self):
        result = detect_burst([Observation(100, 100), Observation(100, 100), Observation(100, 500)])
        self.assertFalse(result.triggered)

    def test_invalid_prices_raise(self):
        with self.assertRaises(ValueError):
            detect_burst([Observation(100, 100), Observation(0, 50)])


if __name__ == "__main__":
    unittest.main()
