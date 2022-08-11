from django.contrib import admin
from .models import *


class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'Day_Type', 'Start_Time', 'End_Time')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Menu_File')
    fieldsets = (
        ('Info', {'fields': ('Title', 'Menu_File')}),
        ("Available Days", {
            "fields": (tuple(['Week_Day', 'Week_End']),),
        }),
        ("Weekdays time", {
            "fields": (tuple(['Week_Day_Start_Time', 'Week_Day_End_Time']),),
        }),
        ("Weekend time", {
            "fields": (tuple(['Week_End_Start_Time', 'Week_End_End_Time']),),
        }),
    )


class MenuCarouselAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info', {'fields': ('Image', 'ImageOpacity')}),
        ("Headings & Colors", {
            "fields": (tuple(['Caption_Heading', 'Color_Caption_Heading']),),
        }),

        ("Sub Headings & Colors", {
            "fields": (tuple(['Caption_subHeading', 'Color_Caption_subHeading']),),
        }),
    )


# Register your models here.
admin.site.register(MenuCarousel, MenuCarouselAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuDay, MenuDayAdmin)
