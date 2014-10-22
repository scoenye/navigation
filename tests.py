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
    
    # Now that the methods return copies of the navigation items, a direct comparison
    # of the returned lists is no longer possible. Use the URL attribute instead.
    def test_alone(self):
        self.assertEqual(len(self.child4_1.children()), 0, "Children found where no children expected.")
        self.assertEqual(len(self.child4_1.siblings()), 1, "Incorrect number of siblings encountered.")
        self.assertEqual(self.child4_1.siblings()[0].url, "child4_1", "Expected self, found another.")
    
    def test_children(self):
        self.assertEqual(len(self.root.children()), 2, "Incorrect number of children detected.")
        self.assertEqual(self.root.children()[0].url, "child1_1", "Did not find child1_1 in slot 0.")
        self.assertEqual(self.root.children()[1].url, "child1_2", "Did not find child1_2 in slot 1.")
    
    def test_siblings(self):
        self.assertEqual(len(self.child2_1.siblings(self)), 2, "Incorrect number of siblings detected.")
        self.assertEqual(self.child2_1.siblings(self)[0].url, "child2_1", "Did not find child2_1 in slot 0.")
        self.assertEqual(self.child2_1.siblings(self)[1].url, "child2_2", "Did not find child2_2 in slot 1.")

    def test_elders(self):
        self.assertEqual(len(self.child3_1.elders()), 2, "Incorrect number of elders detected.")
        self.assertEqual(self.child3_1.elders()[0].url, "child1_1", "Did not find child1_1 in slot 0.")
        self.assertEqual(self.child3_1.elders()[1].url, "child1_2", "Did not find child1_2 in slot 1.")
        
        self.assertEqual(len(self.child1_1.elders()), 1, "Incorrect number of elders detected.")
        self.assertEqual(self.child1_1.elders()[0].url, None, "Unexpected URL in slot 0.")

        self.assertIsNone(self.root.elders(), "Root elders found where none expected.")
