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
    def setUp(self):
        self.root = tier.TieredNavigation("root", None)
        self.child1_1 = tier.TieredNavigation("child1_1", "child1_1", self.root)
        self.child1_2 = tier.TieredNavigation("child1_2", "child1_2", self.root)
        self.child2_1 = tier.TieredNavigation("child2_1", "child2_1", self.child1_1)
        self.child2_2 = tier.TieredNavigation("child2_2", "child2_2", self.child1_1)
        self.child3_1 = tier.TieredNavigation("child3_1", "child3_1", self.child1_2)
        self.child3_2 = tier.TieredNavigation("child3_2", "child3_2", self.child1_2)
        self.child4_1 = tier.TieredNavigation("child4_1", "child4_1", self.child3_1)
        
    def test_alone(self):
        self.assertListEqual(self.child4_1.children(), [], "Children found where no children expected.")
        self.assertListEqual(self.child4_1.siblings(), [self.child4_1], "Siblings found where no siblings expected:" + str(self.child4_1.siblings()))
    
    def test_children(self):
        self.assertListEqual(self.root.children(), [self.child1_1, self.child1_2], "Mismatch in children list.")
    
    def test_siblings(self):
        self.assertListEqual(self.child2_1.siblings(), [self.child2_1, self.child2_2], "Mismatch in children list.")
    
    def test_elders(self):
        self.assertListEqual(self.child3_1.elders(), [self.child1_1, self.child1_2], "Mismatch in elders list.")
        self.assertListEqual(self.child1_1.elders(), [self.root], "Mismatch in 1st level elders list.")
        self.assertIsNone(self.root.elders(), "Root elders found where none expected.")

