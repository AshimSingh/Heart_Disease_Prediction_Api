from rest_framework.decorators import api_view
from rest_framework.response import Response
from prediction.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status


class QuestionDetail(APIView):
    def get(self,request):
        question = Question.objects.all()
        serializer =  QuestionSerializer(question,many=True)
        return JsonResponse(serializer.data, safe=False)
    def post(self,request):
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        print(serializer,'this is serial')
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse('Cannot post data ', safe=False)
        
class ChoiceDetail(APIView):
    def get(self,request):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# def getRoutes(request):
#     if request.method == 'GET':
#         question = Question.objects.all()
#         serializer = QusetionSerializer(question,many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = QusetionSerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#         return JsonResponse(serializer.data, safe=False)

# @api_view(['POST'])
# def getRoutes(request):
#     serializer = QusetionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)