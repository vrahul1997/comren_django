from dataclasses import field
from rest_framework import serializers
from Post_n_Publication.models import Publication, Project


class publicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
