from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, Http404
from rest_framework import generics, status
from .models import Question, Option
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .util import GetProjectList, GetProjectFacets, GetIssuesList, GetSourceCode,GetBugDetail, GetRule, GetVulnerabilityDetail
from .form import QuestionForm,OptionForm
from django.contrib import messages

# Create your views here.
## e.g. /hello, /main, end point for a url

# class QuestionView(generics.ListAPIView): #CreateAPIView - to post
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer




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
    if not request.user.is_staff :
        return redirect('/admin/')
    para = kwargs['org']
    response = GetProjectList(para)['data']
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
    if not request.user.is_staff :
        return redirect('/admin/')
    para = kwargs['prokey']
    response = GetProjectFacets(para,'sonarsourceSecurity')
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
    if not request.user.is_staff :
        return redirect('/admin/')
    param2 = kwargs['prokey']
    response = GetBugDetail(param2)

    if type(response) == 'str':
        status = "Error: Unable to connect to Sonarcloud!!!!!!!"
    elif len(response) == 0:
        status = "No Bugs!!! Great!!!"
    else:
        status = 200
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
    questionform = QuestionForm()
    optionform = OptionForm()
    if not request.user.is_staff :
        return redirect('/admin/')
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_form = OptionForm(request.POST)
        if questionform.is_valid:
            question_form.save()
            instance = question_form.save(commit=False)
        if option_form.is_valid():
            options = option_form.cleaned_data
            Option(question=instance, option_text=options['option_1'], explanation= options['explanation_1'], is_correct=options['is_correct_1']).save()
            Option(question=instance, option_text=options['option_2'], explanation= options['explanation_2'], is_correct=options['is_correct_2']).save()
            Option(question=instance, option_text=options['option_3'], explanation= options['explanation_3'], is_correct=options['is_correct_3']).save()
            #print(optionform.cleaned_data)
        messages.success(request, "Successfully Created")
    return render(request, "addquestion.html",context={'data': response, 'Questionform': questionform , 'Optionform':optionform},status = 200)



