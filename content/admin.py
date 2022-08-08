from django.contrib import admin
from .models import *


class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'Day_Type', 'Start_Time', 'End_Time')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Menu_File')


class CarouselAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Info', {'fields': (
            'Image', 'ImageOpacity')}),
        ("Headings & Colors", {
            "fields": (tuple(['Caption_Heading', 'Color_Caption_Heading']),),
        }),

        ("Sub Headings & Colors", {
            "fields": (tuple(['Caption_subHeading', 'Color_Caption_subHeading']),),
        }),
    )


class TimingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Weekdays_Start_Time', 'Weekdays_End_Time', 'WeekEndTime_Start_Time', 'WeekEndTime_End_Time')

    fieldsets = (
        ("Week days Timings", {
            "fields": (tuple(['Weekdays_Start_Time', 'Weekdays_End_Time']),),
        }),

        ("Weekend Timings", {
            "fields": (tuple(['WeekEndTime_Start_Time', 'WeekEndTime_End_Time']),),
        }),
    )


admin.site.register(Timing, TimingAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(SocialMedia)
admin.site.register(MenuDay, MenuDayAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(InstagramPost)
admin.site.register(ContactUs)
admin.site.register(BrandLogo)
admin.site.register(AboutUs)
admin.site.register(HomePageImage)
