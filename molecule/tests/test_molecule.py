"""
Unit and regression test for the molecule package.
"""

# Import package, test suite, and other packages as needed
import molecule
import pytest
import sys

def test_molecule_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecule" in sys.modules
