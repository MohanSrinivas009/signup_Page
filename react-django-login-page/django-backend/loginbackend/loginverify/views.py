from django.shortcuts import render
from loginverify.models import user
from loginverify.serialize import userSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request,"home.html")


# Fetch Data
class userFetch(APIView):
    def get(self,request,username):#get request
        # userObj=user.objects.all()#from user model collect the all data and assign to userObj
        userObj=user.objects.filter(username=username)
        serializeObj=userSerializer(userObj,many=True)#serialize the userObj object
        return Response(serializeObj.data)#sends serialized data

    def post(self,request,username):
        try:
            serializeObj=userSerializer(data=request.data)# gets the data from frontend with (data=request.data) and serialize into object
        except:
            return Response(username+" is inavlid")
        if serializeObj.is_valid():
            serializeObj.save()
        return Response(200)
