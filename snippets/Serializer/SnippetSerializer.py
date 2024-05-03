from snippets.models import Snippet
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ["code", "title", "description"]  # すべてのフィールドを含める

    title = serializers.CharField(max_length=100)

    def validate_title(self, value):
        """
        Check that the Snippet post is about World.
        """
        if "世界" not in value.lower() and "world" not in value.lower():
            raise serializers.ValidationError("Snippet post is not about World")
        return value
