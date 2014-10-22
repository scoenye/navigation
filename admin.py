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

from django.contrib import admin

from app import nav_tree

# Bolt the navigation to a subclass of ModelAdmin to reduce boilerplate
class NavigableModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, nav_item, extra_context=None):
        extra_context = extra_context or {}
        extra_context['navigation'] = nav_tree[nav_item].three_tier()
        return super(NavigableModelAdmin, self).changelist_view(request, extra_context=extra_context)