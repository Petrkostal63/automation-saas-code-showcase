import unittest
from datetime import datetime, timezone
from showcase.company_directory import Company, order_promotional_directory


class CompanyDirectoryTests(unittest.TestCase):
    def test_higher_promotional_support_sorts_first(self):
        items = [
            Company("a", "Alpha", "CZ", "Tech", 25, datetime(2026, 1, 1, tzinfo=timezone.utc)),
            Company("b", "Beta", "DE", "Industry", 100, datetime(2026, 1, 2, tzinfo=timezone.utc)),
        ]
        self.assertEqual(order_promotional_directory(items)[0].company_id, "b")

    def test_equal_total_uses_earlier_time_then_id(self):
        later = Company("a", "Later", "CZ", "Tech", 50, datetime(2026, 1, 2, tzinfo=timezone.utc))
        earlier = Company("b", "Earlier", "DE", "Industry", 50, datetime(2026, 1, 1, tzinfo=timezone.utc))
        self.assertEqual(order_promotional_directory([later, earlier])[0].company_id, "b")


if __name__ == "__main__":
    unittest.main()
