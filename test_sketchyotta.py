# test_sketchyotta.py
"""
Tests for SketchYotta module.
"""

import unittest
from sketchyotta import SketchYotta

class TestSketchYotta(unittest.TestCase):
    """Test cases for SketchYotta class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchYotta()
        self.assertIsInstance(instance, SketchYotta)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchYotta()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
