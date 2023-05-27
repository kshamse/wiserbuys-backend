from rest_framework import serializers
from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        user = self.context['request'].user
        return user == obj.profile.owner

    class Meta:
        model = Experience
        fields = [
            'id', 'profile', 'created_at', 'updated_at', 'title', 'company',
            'location', 'date_from', 'date_to', 'is_current', 'description',
            'recommendations', 'is_owner'
        ]
