from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .util import GetProjectList, GetProjectFacets, GetIssuesList, GetSourceCode,GetBugDetail, GetRule, GetVulnerabilityDetail



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

"""
output: [
    {
        val: xss
        count: 3
        issues : [
            {
            issueKey,
            ruleKey,
            severity,
            msg
            }
        ]
    }
]
"""
def ProjectVulnerabilityFacet(request,*args,**kwargs):
    para = kwargs['prokey']
    response = GetProjectFacets(para,'sonarsourceSecurity')
    status = "is_ok"
    #print(response)
    data = []
    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    else:
        for p in response.keys():
            if(p != 'others'):
                issue = GetIssuesList(para,p)
                data.append({'val': p ,
                             'count' : response[p],
                            'issues': issue})
    #print(data)
    return render(request, "viewvulnerability.html",context={'data': data},status = 200)



"""
output: [
       {'issueKey': p['key'],
        //'rule': p['rule'],
        'severity': p['severity'],
        //'fileKey': p['component'],
        'textLine': code,
        'msg':p['message']
        'rule': {
            'key' : rulekey,
            'title': name,
            'htmlDesc': htmlDesc
            }
        }
]
"""

def ProjectBugsList(request,*args, **kwargs):
    param1 = kwargs['org']
    param2 = kwargs['prokey']
    response = GetBugDetail(param2)
    status = "is_ok"

    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    elif len(response) == 0:
        status = "No Bugs!!! Great!!!"
    else:
        status = 200
        # for p in response:
        #     rulekey = p['rule']
        #     filename = p['fileKey']
        #     textline = p['textLine']
        #     rule = GetRule(param1,rulekey)
        #     p['rule'] = rule
        #     code = GetSourceCode(filename, textline, textline)[0]
        #     p['textLine'] = code


    #response = {'data': response, 'status':status}
    return render(request, "viewbugs.html",context={'data': response},status = 200)

"""
output: 
"""

def ProjectVulnerability(request,*args, **kwargs):
    param1 = kwargs['prokey']
    param2 = kwargs['issuekey']

    response = GetVulnerabilityDetail(param1,param2)
    # print(param1)
    # print(param2)

    return render(request, "addquestion.html",context={'data': response},status = 200)





