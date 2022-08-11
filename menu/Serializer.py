from rest_framework import serializers
from .models import *


class MenuDaySerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuDay
        fields = '__all__'


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def get_Menu_File(self, Menu):
        try:
            request = self.context.get('request')
            if Menu.Menu_File:
                Menu_File = Menu.Menu_File.url
                return request.build_absolute_uri(Menu_File)
        except NameError:
            print(NameError)


class MenuCarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuCarousel
        fields = '__all__'

    def get_Image(self, MenuCarousel):
        try:
            request = self.context.get('request')
            if MenuCarousel.Image:
                Image = MenuCarousel.Image.url
                return request.build_absolute_uri(Image)
        except NameError:
            print(NameError)
