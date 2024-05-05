from snippets.models import Snippet
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = "__all__"
        read_only_fields = ("created_by",)

    title = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # Assign the current user, which should be set in the serializer's context
        user = self.context["request"].user
        snippet = Snippet.objects.create(created_by=user, **validated_data)
        return snippet

    def validate_title(self, value):
        """
        Check that the Snippet post is about World.
        """
        if "世界" not in value.lower() and "world" not in value.lower():
            raise serializers.ValidationError("Snippet post is not about World")
        return value
