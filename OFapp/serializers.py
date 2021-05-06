from rest_framework import serializers
from .models import *

class collection_uuid_serializer(serializers.ModelSerializer):
    class Meta:
        model = collections_table
        fields = '__all__'
        depth = 1

class movie_serializer(serializers.ModelSerializer):
    class Meta:
        model = movies_table
        fields = '__all__'


class collection_serializer(serializers.ModelSerializer):
    class Meta:
        model = collections_table
        fields=('title','collectionsuuid','description')
    def to_representation(self, instance):
        data=super(collection_serializer,self).to_representation(instance)
        print("data is ",data)
        data.update({"hi":"abhi"})
        return data

class collection_post_serializer(serializers.ModelSerializer):
    movies=movie_serializer(many=True,required=False)
    uuidfield=serializers.SerializerMethodField('uuidmethod')
    class Meta:
        model=collections_table
        fields=('title','description','movies','uuidfield')

    def create(self, validated_data):
        print('validated data in ser',validated_data)
        movie_validated_data = validated_data.pop('movies')
        collection =collections_table.objects.create(**validated_data)
        for eachmovie in movie_validated_data:
            print(eachmovie['moviesuuid'])
            s=movies_table(moviesuuid=eachmovie['moviesuuid'],title=eachmovie['title'],
                           description=eachmovie['description'],generes=eachmovie['generes'])
            s.save()
            collection.movies.add(s)
        print('collection is',collection)
        self.abhi=collection
        return collection
    def uuidmethod(self,collections_table):
        return collections_table.collectionsuuid


