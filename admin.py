'''
Created on Oct 19, 2014

@author: sven
'''

from django.contrib import admin

from app import nav_tree

# Bolt the navigation to a subclass of ModelAdmin to reduce boilerplate
class NavigableModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, nav_item, extra_context=None):
        extra_context = extra_context or {}
        extra_context['navigation'] = nav_tree[nav_item].three_tier()
        return super(NavigableModelAdmin, self).changelist_view(request, extra_context=extra_context)
