from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .util import GetProjectList, GetProjectFacets, GetIssuesList, GetSourceCode,GetBugDetail



# Create your views here.
## e.g. /hello, /main, end point for a url

class QuestionView(generics.ListAPIView): #CreateAPIView - to post
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer




def ProjectView(request, *args,**kwargs):
    return render(request, "viewprojects.html",context={},status = 200)

"""
output:{
    data :
        [ 
            {
            'name': name,
            'projectKey' : project_key,
            'types' : {
                        'bug' : count,
                        'code smell' : count,
                        'vulnerability' : count,
                        }
            },
        ]
}

data = {[]}
"""
def ProjectList(request, *args,**kwargs):
    print(1)
    para = kwargs['org']
    response = GetProjectList(para)['data']
    status = "is_ok"
    data = []
    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    elif len(response) == 0:
        status = "No Project Imported"
    else:
        for p in response:
            pkey = p['projectKey']
            types = GetProjectFacets(pkey,'types')
            p['types'] = types
            data.append(p)
    #response = {'data': data, 'status':status}
    #return JsonResponse(data = response)
    return render(request, "viewprojects.html",context={'data': data},status = 200)





def ProjectVulnerabilityFacet(request,*args,**kwargs):

    response = GetProjectFacets(args,'sonarsourceSecurity')
    status = "is_ok"
    data = {}
    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    else:
        data = response
    response = {'data': data, 'status':status}
    return JsonResponse(data = response)


def ProjectBugsList(request,*args, **kwargs):
    # print(2)
    # print(kwargs['prokey'])
    param = kwargs['prokey']
    response = GetBugDetail(param)
    status = "is_ok"

    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    elif len(response) == 0:
        status = "No Bugs!!! Great!!!"
    else:
        for p in response:
            filename = p['fileKey']
            textline = p['textLine']
            code = GetSourceCode(filename, textline, textline)[0]
            p['textLine'] = code

    #response = {'data': response, 'status':status}
    return render(request, "viewbugs.html",context={'data': response},status = 200)


def ProjectVulnerabilityList(request,*args, **kwargs):
    response = GetIssuesList(args[0],args[1])
    status = "is_ok"
    data = {}
    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    elif len(response) == 0:
        status = "No Vulnerable Issues about " + args[1] + "!!! Great!!!"
    else:
        data = response
    response = {'data': data, 'status':status}
    return JsonResponse(data = response)

###def VulnerabilityDetail(request,*args,**kwargs):




