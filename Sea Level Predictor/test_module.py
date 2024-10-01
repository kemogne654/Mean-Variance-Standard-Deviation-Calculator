import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_draw_plot(self):
        # Test for the draw_plot function
        self.assertIsNone(draw_plot())  # Check if it runs without error

if __name__ == "__main__":
    unittest.main()
