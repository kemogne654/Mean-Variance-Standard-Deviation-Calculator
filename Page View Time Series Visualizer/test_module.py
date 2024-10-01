import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_draw_line_plot(self):
       
        self.assertIsNone(draw_line_plot())  

    def test_draw_bar_plot(self):
        # Test for the bar plot function
        self.assertIsNone(draw_bar_plot())  

    def test_draw_box_plot(self):
       
        self.assertIsNone(draw_box_plot())  

if __name__ == "__main__":
    unittest.main()
