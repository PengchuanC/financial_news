from rest_framework import serializers

from news.models import News


class NewSerializer(serializers.Serializer):
    infopubldate = serializers.DateField()
    infopubltime = serializers.CharField(max_length=8)
    media = serializers.CharField(max_length=50)
    newscategory = serializers.CharField(max_length=200)
    infotitle = serializers.CharField(max_length=200)
    infoshorttitle = serializers.CharField(max_length=200)
    abstract = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField(max_length=200)
    linkaddress = serializers.CharField(max_length=300)
    category = serializers.CharField(max_length=50)
    infolevel = serializers.IntegerField()