import unittest
from menstruration_app import UserAccount
from datetime import  datetime

class MyTestCase(unittest.TestCase):
    def test_my_constructor(self):
        userAccount = UserAccount("Ada", 25, 28, 5, "2025-04-01")
        self.assertEqual(userAccount.name, "Ada")
        self.assertEqual(userAccount.age, 25)
        self.assertEqual(userAccount.cycle_length, 28)
        self.assertEqual(userAccount.period_length, 5)
        self.assertEqual(userAccount.last_period_date.strftime("%Y-%m-%d"), "2025-04-01")
    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            UserAccount("", 25, 28, 5, "2025-04-01")
    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            UserAccount("Ada", 9, 28, 5, "2025-04-01")

    def test_invalid_cycle_length(self):
        with self.assertRaises(ValueError):
            UserAccount("Ada", 25, 15, 5, "2025-04-01")

    def test_invalid_period_length(self):
        with self.assertRaises(ValueError):
            UserAccount("Ada", 25, 28, 2, "2025-04-01")
    def test_invalid_last_period_date(self):
        with self.assertRaises(ValueError):
            UserAccount("Ada", 25, 28, 5, "01-04-2025")
    def test_the_next_period_date(self):
        userAccount = UserAccount("Ada", 25, 28, 3, "2025-04-01")
        expected_date = datetime(2025,4,29)
        self.assertEqual(userAccount.get_next_period_day(), expected_date)

    def test_safe_and_unsafe_days(self):
        userAccount = UserAccount("Ada", 25, 28, 3, "2025-04-01")
        safe_and_unsafe_days = userAccount.get_safe_and_unsafe_days()

        self.assertEqual(safe_and_unsafe_days, ["unsafe days start's"], "2025-04-10")
        self.assertEqual(safe_and_unsafe_days,["Ovulation_day"], "2025-04-15")
        self.assertEqual(safe_and_unsafe_days,["unsafe days end's"], "2025-04-16")



if __name__ == '__main__':
    unittest.main()
