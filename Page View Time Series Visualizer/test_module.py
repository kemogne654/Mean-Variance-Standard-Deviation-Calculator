import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_draw_line_plot(self):
        # Test for the line plot function
        self.assertIsNone(draw_line_plot())  # or add specific checks for the figure if needed

    def test_draw_bar_plot(self):
        # Test for the bar plot function
        self.assertIsNone(draw_bar_plot())  # or add specific checks for the figure if needed

    def test_draw_box_plot(self):
        # Test for the box plot function
        self.assertIsNone(draw_box_plot())  # or add specific checks for the figure if needed

if __name__ == "__main__":
    unittest.main()
