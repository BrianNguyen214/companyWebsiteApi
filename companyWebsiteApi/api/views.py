#generic

from rest_framework import generics
from .serializers import MemberSerializer
from boardMembers.models import Member
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def MembersManip(request):
    if request.method == 'GET':
        data = Member.objects.all()
        theMembers = []
        for member in data:
            theMembers.append({member.Name, member.Position, member.Description, member.PictureLink)})
            
        return JsonResponse({"These are the board members": theMembers})

    if request.method == 'POST':
        body = request.body
        dict = json.loads(str(request.body).encode('utf-8'))
        newName = dict['Name']
        newPosition = dict['Position']
        newDescription = dict['Description']
        newPicture = dict['PictureLink']
        newMember = Member(Name = newName, Position = newPosition, Description = newDescription, PictureLink = newPicture)
        newMember.save()
        print newMember.Name
        print newMember.Position
        return JsonResponse({"Result":"A new member was successfully added"})
