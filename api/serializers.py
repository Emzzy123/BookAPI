from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    is_recent = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'created_at', 'days_since_created', 'is_recent']

    def get_days_since_created(self, object):
        return (datetime.now().date() - object.created_at.date()).days
    
    def get_is_recent(self, obj):
        return self.get_days_since_created(obj) < 30
    