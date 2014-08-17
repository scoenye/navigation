'''
@author: Sven Coenye

Copyright (C) 2014  Sven Coenye

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/
'''
import unittest
from navigation import tier

# Create your tests here.
class TieredNavigationTest(unittest.TestCase):
    def test_alone(self):
        item = tier.TieredNavigation()
        self.assertListEqual(item.children(), [], "Children found where no children expected.")
        self.assertIsNone(item.siblings(), "Siblings found where no siblings expected.")
    
    def test_children(self):
        item = tier.TieredNavigation()
        child1 = tier.TieredNavigation(item)
        child2 = tier.TieredNavigation(item)
        self.assertListEqual(item.children(), [child1, child2], "Mismatch in children list.")
        self.assertIsNone(item.siblings(), "Siblings found where no siblings expected.")
    
    def test_siblings(self):
        root = tier.TieredNavigation()
        item = tier.TieredNavigation(root)
        sibling1 = tier.TieredNavigation(root)
        sibling2 = tier.TieredNavigation(root)
        self.assertListEqual(item.children(), [], "Children found where no children expected.")
        self.assertListEqual(item.siblings(), [item, sibling1, sibling2], "Mismatch in children list.")