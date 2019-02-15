from rest_framework import generics
from .models import Userdetails
from .serializers import Userdetailsserializer

# Create your views here.

class UserRequest(generics.ListCreateAPIView):
    queryset = Userdetails.objects.all()
    serializer_class = Userdetailsserializer

class UserRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userdetails.objects.all()
    serializer_class = Userdetailsserializer