from django.contrib import admin
from .models import *


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


class ContactedUSAdmin(admin.ModelAdmin):
    list_display = ('id', 'TicketID', 'Name', 'Email', 'Subject')


class ContactUSAdmin(admin.ModelAdmin):
    list_display = ('id', 'Phone', 'Google_Maps', 'Email', 'Address')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Facebook', 'Twitter', 'Instagram')


admin.site.register(Timing, TimingAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(ContactedUs, ContactedUSAdmin)
admin.site.register(InstagramPost)
admin.site.register(ContactUs, ContactUSAdmin)
admin.site.register(BrandLogo)
admin.site.register(AboutUs)
admin.site.register(HomePageImage)
admin.site.register(ContactUsPage)
