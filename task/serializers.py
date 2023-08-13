from rest_framework import serializers
from .models import Image, PDF


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file', 'location']
        read_only_fields = ['location']


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ['id', 'file', 'location']
        read_only_fields = ['location']
