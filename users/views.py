from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import NewUser
import pandas as pd
from .ID3algorithm import build_decision_tree, classify_instance
from .cleandata import cleandata
# from .outlookprediction import build_decision_tree, classify_instance

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        queryset = NewUser.objects.all()
        print('hey ashim')
        serializer = CustomUserSerializer(queryset,many=True)
        print(serializer)
        if serializer:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class PredictionRead(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        test_instance = request.data
        
        # df = pd.read_csv(r'F:\\HeartDiseasePrediction\\users\\tenis.csv')
        # print(df.keys()[-1])
        # decision_tree = build_decision_tree(df)
        
        
        data = pd.read_csv(r'F:\\HeartDiseasePrediction\\users\\Heart_Disease_Prediction.csv')
        df = cleandata(data)
        print(df)
        decision_tree = build_decision_tree(df)
        print(decision_tree,test_instance)
        prediction = classify_instance(test_instance, decision_tree)
        # print ('decision is',prediction)
        
        return Response({"prediction ":prediction})


# class PredictionRead(APIView):
#     permission_classes = [AllowAny]
#     def post(self,request):
#         test_instance = request.data
#         df = pd.read_csv(r'F:\\HeartDiseasePrediction\\users\\tenis.csv')
#         decision_tree = build_decision_tree(df)
#         prediction = classify_instance(test_instance, decision_tree)
#         print ('decision is',prediction)
        
#         return Response({"message":prediction,"tree":decision_tree})