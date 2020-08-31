from django.shortcuts import render
from data.serializers import LanguageSerializer, QuotesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from data.models import Language, Quotes
from rest_framework import status
import random
# Create your views here.

class LanguageAPIView(APIView):

    def get(self, request, *args, **kwargs):
        lan_obj = Language.objects.all()
        lan_ser_obj = LanguageSerializer(lan_obj, many=True)
        return Response(lan_ser_obj.data)


class QuotesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        obj = Quotes.objects.all()
        ser_obj = QuotesSerializer(obj, many=True)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        obj = QuotesSerializer(data = request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status.HTTP_201_CREATED)
        return Response(obj.errors, status = status.HTTP_400_BAD_REQUEST)

class RandomAPI(APIView):

    def get(self, request, *args, **kwargs):
        print(request.data)
        obj = Quotes.objects.order_by('?').first()
        ser_obj = QuotesSerializer(obj, many=True)
        return Response(ser_obj.data)


class BylanguageAPI(APIView):

    def get(self, request, value, *args, **kwargs):
        v = value
        l = Language.objects.get(name=v)
        obj = Quotes.objects.get(language_id = l.id)
        ser_obj = QuotesSerializer(obj, many=True)
        return Response(ser_obj.data)


class UpdateAPI(APIView):

    def get(self, request, id, *args, **kwargs):
        quote = Quotes.objects.get(id=id)
        ser = QuotesSerializer(quote)
        return Response(ser.data)

    def put(self, request, id, *args, **kwargs):
        quote = Quotes.objects.get(id=id)
        ser = QuotesSerializer(instance = quote, data=request.data, partial = True)
        if ser.is_valid():
            update_obj = ser.save()
            ser_obj = QuotesSerializer(update_obj)
            return Response(ser_obj.data)
        return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)

