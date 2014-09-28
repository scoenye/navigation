'''
A tiered navigation workflow extension for the Django admin

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

import copy

class TieredNavigation:
    '''
    n-Tiered navigation building block
    '''
    
    def __init__(self, name, url, parent=None):
        self.name = name
        self.url = url
        self.parent = parent
        self.offspring = []
        self.selected = False
        
        if (parent):
            parent.add_child(self)
        
    def add_child(self, new_child):
        '''
        Add children to this item
        '''
        self.offspring.append(new_child)
    
    def children(self, selected = None):
        '''
        Retrieve the descendent items. A copy of the originals is returned so the
        selected flag can be set without interfering with other requests.
        '''
        children_copies = []
        
        for child in self.offspring:
            child_copy = copy.copy(child)
            if child == selected:
                child_copy.selected = True
            children_copies.append(child_copy)
            
        return children_copies 
        
    def siblings(self, selected = None):
        '''
        Retrieve the sibling items
        '''
        if (self.parent):
            siblings = self.parent.children(selected)
        else:
            siblings = [copy.copy(self)]    # Give 1st level children at least one elder.
            siblings[0].select = True       # Mark as the selected item as there are no others.    
        return siblings
    
    def elders(self):
        '''
        Return the parent and it's siblings
        '''
        if (self.parent):
            return self.parent.siblings(self.parent)
        else:
            return None
        
    def three_tier(self):
        '''
        Generate the three tiered navigation structure. url_name is used to 
        determine which objects will have their selected flag set.
        '''
        return [self.elders(), self.siblings(self), self.children()]
        
        

