# test_web3xeno.py
"""
Tests for Web3Xeno module.
"""

import unittest
from web3xeno import Web3Xeno

class TestWeb3Xeno(unittest.TestCase):
    """Test cases for Web3Xeno class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Xeno()
        self.assertIsInstance(instance, Web3Xeno)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Xeno()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
