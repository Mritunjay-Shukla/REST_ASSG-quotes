from rest_framework import serializers
from data.models import Language, Quotes




class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'



class QuotesSerializer(serializers.ModelSerializer):
    
    #content = serializers.SerializerMethodField()
    language = LanguageSerializer()
    class Meta:
        model = Quotes
        fields = '__all__'
        depth = 1

    #def get_content(self, obj): 
     #   return obj.content[:3]

     
