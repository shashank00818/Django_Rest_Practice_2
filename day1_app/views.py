from django.shortcuts import render
from day1_app.models import Friends
from day1_app.serializers import Friends_serializer
from django.http import JsonResponse
# Create your views here.
def Friend_detail(request,pk):
    frn=Friends.objects.get(id=pk)
    serializer=Friends_serializer(frn)
    return JsonResponse(serializer.data)

def Friend_list(request):
    frn=Friends.objects.all()
    serializer=Friends_serializer(frn,many=True)
    return JsonResponse(serializer.data,safe=False)