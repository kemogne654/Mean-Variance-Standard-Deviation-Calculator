import unittest
from demographic_data_analyzer import calculate_demographic_data

class DemographicDataTest(unittest.TestCase):
    def test_demographic_data(self):
        result = calculate_demographic_data(print_data=False)
        self.assertEqual(result['average_age_men'], 39.4)  # Modify as needed
        self.assertEqual(result['percentage_bachelors'], 16.4)  # Modify as needed

if __name__ == "__main__":
    unittest.main()
