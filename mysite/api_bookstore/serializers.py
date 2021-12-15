from rest_framework import serializers
from .models import Author, Book
import django.contrib.auth.models   #modelo de usuarios de django

class userSerializer(serializers.ModelSerializer):

    class Meta:
        # modelo de datos de django
        model = django.contrib.auth.models.User
        fields = ('username', 'email', )

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # modelo de datos que va a serializar/deserializar
        model = Author
        # campos del modelo de datos que va a serializar/deserializar
        fields = ('name', 'created_date')

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # modelo de datos que va a serializar/deserializar
        model = Book
        # campos del modelo de datos que va a serializar/deserializar
        fields = ('title', 'description', 'author', 'added_by')