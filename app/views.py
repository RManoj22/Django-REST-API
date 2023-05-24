from django.shortcuts import redirect
from rest_framework.views import APIView
from . serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework import status
from . models import Info
from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics

# class List_and_Create(generics.ListCreateAPIView):
#     permission_classes=(IsAuthenticated,)
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer

# class Retrieve_and_Delete(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer



class InfoAPI(APIView):
    serializer_class = InfoSerializer
    # permission_classes=(IsAuthenticated,)
 
    def get (self,request,id=None):
        if id:
            queryset = Info.objects.get(id=id)
            serializer = InfoSerializer(queryset)
            return Response(serializer.data)
        else:
            queryset = Info.objects.all()
            serializer = InfoSerializer(queryset,many=True)
            return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = InfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        deeds = Info.objects.get(id=id)
        data=request.data
        serializer = InfoSerializer(data=data,instance=deeds)
        if serializer.is_valid():
            serializer.save()
            return Response({'Updated successfully'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        deeds = Info.objects.filter(id=id)
        deeds.delete()
        return Response({'Deleted'})    


# class InfoView(viewsets.ModelViewSet):
#     queryset = Info.objects.all()
#     serializer_class = InfoSerializer