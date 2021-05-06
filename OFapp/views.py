from django.shortcuts import render
from rest_framework import generics
import requests, json
from rest_framework.response import Response
from requests.auth import HTTPBasicAuth
from rest_framework.decorators import api_view
from rest_framework.generics import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated



class moviesview(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        print('in list')
        baseurl = "https://demo.credy.in/api/v1/maya/movies/"
        orgdata = requests.get(baseurl,
                auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',
                'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
        # print(orgdata.json())
        # x=orgdata.json()
        # y=x
        # print("y tpe",type(y)
        # pretty_json = json.loads(orgdata.text)
        # print(pretty_json)
        # print("-----------")
       #  l=json.dumps(pretty_json, indent=2)
        print(orgdata)
        #x = json.dumps(orgdata)
        #print(x)
        return Response(orgdata)

# @api_view()
# def moviesview(request): #this movies are getting from third party api's
#     baseurl = "https://demo.credy.in/api/v1/maya/movies/"
#     orgdata = requests.get(baseurl, auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',
#                                                        'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
#     print(orgdata)
#     response = requests.get(orgdata.json())
#     return Response(orgdata.text)

class collectionuuidview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = collection_uuid_serializer
    lookup_url_kwarg = 'collectionsuuid'
    lookup_field = 'collectionsuuid'
    queryset = collections_table.objects.all()

class collectionview(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = collections_table.objects.all()
    serializer_class = collection_post_serializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = collection_serializer(queryset, many=True)
        x=serializer.data
        my_dict={"is_sucess":True,"data":{"collections":x},"favourite_genres":"moviesx"}
        z=Response(my_dict)
        return z
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,)