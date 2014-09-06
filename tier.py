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

class TieredNavigation:
    '''
    n-Tiered navigation building block
    '''
    
    def __init__(self, name, url, parent=None):
        self.name = name
        self.url = url
        self.parent = parent
        self.offspring = []
        
        if (parent):
            parent.add_child(self)
        
    def add_child(self, new_child):
        '''
        Add children to this item
        '''
        self.offspring.append(new_child)
    
    def children(self):
        '''
        Retrieve the descendent items
        '''
        return self.offspring
        
    def siblings(self):
        '''
        Retrieve the sibling items
        '''
        if (self.parent):
            return self.parent.children()
        else:
            return [self]       # Give 1st level children at least one elder.
    
    def elders(self):
        '''
        Return the parent and its siblings
        '''
        if (self.parent):
            return self.parent.siblings()
        else:
            return None
