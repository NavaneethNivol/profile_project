from rest_framework import serializers
from .models import Userdetails


class Userdetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = ('first_name','last_name','about_me','email_id','phone_number',)

        