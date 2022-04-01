from rest_framework import serializers
from rest_framework.serializers import Serializer
from home.models import Contact
from home.api.serializers import ContactSerializer
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer