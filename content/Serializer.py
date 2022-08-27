from rest_framework import serializers
from .models import *


class SocialMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'


class TimingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields = '__all__'


class ContactedUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactedUs
        fields = '__all__'


class InstagramPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = InstagramPost
        fields = '__all__'

        def get_Post_Image(self, BookTableCover):
            try:
                request = self.context.get('request')
                if BookTableCover.PaperFile:
                    Post_Image = InstagramPost.Post_Image.url
                    return request.build_absolute_uri(Post_Image)
            except NameError:
                print(NameError)


class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class BrandLogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandLogo
        fields = '__all__'

    def get_Img(self, BrandLogo):
        try:
            request = self.context.get('request')
            if BrandLogo.Logo:
                Logo = BrandLogo.Logo.url
                return request.build_absolute_uri(Logo)
        except NameError:
            print(NameError)


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

    def get_CoverImage(self, AboutUs):
        try:
            request = self.context.get('request')
            if AboutUs.CoverImage:
                CoverImage = AboutUs.CoverImage.Url
                return request.build_absolute_uri(CoverImage)
        except NameError:
            print(NameError)


class HomePageImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomePageImage
        fields = '__all__'

        def get_Img(self, BookTableCover):
            try:
                request = self.context.get('request')
                if BookTableCover.PaperFile:
                    Img = HomePageImage.Img.url
                    return request.build_absolute_uri(Img)
            except NameError:
                print(NameError)


class AddressDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'


class ContactUsPageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUsPage
        fields = '__all__'

        def get_Image(self, ContactUsPage):
            try:
                request = self.context.get('request')
                if ContactUsPage.Image:
                    Image = ContactUsPage.Image.url
                    return request.build_absolute_uri(Image)
            except NameError:
                print(NameError)
