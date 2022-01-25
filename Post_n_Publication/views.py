from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Post_n_Publication.models import Publication, Project
from Post_n_Publication.serializers import publicationSerializer, projectSerializer

# Create your views here.


class publicationFetchAPI(APIView):
    """API for fetching Publication"""

    def get(self, request):
        publication = Publication.objects.all()
        serializer = publicationSerializer(publication, many=True)
        return Response(serializer.data)


class projectFetchAPI(APIView):
    """API for fetching Projects"""

    def get(self, request):
        projects = Project.objects.all()
        serializer = projectSerializer(projects, many=True)
        return Response(serializer.data)
