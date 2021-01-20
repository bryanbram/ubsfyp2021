import requests
from django.shortcuts import render, redirect
import re



url1 = "https://sonarcloud.io/api/components/search"
url2 = "https://sonarcloud.io/api/issues/search"
url3 = "https://sonarcloud.io/api/rules/show"
url4 = "https://sonarcloud.io/api/sources/show"


"""
output:{
    data : [ 
            {
                'name': projectname,
                'projectKey': key
                },
        ]
} 

"""

def GetProjectList(orgkey): 
    pload={'organization' : orgkey,
             'qualifiers' : 'TRK'}

    data = SoncloudAPICall(url1, pload)
    #print(data)
    response = []
    #print(data)
    if type(data) == 'str':
        return data
    else:
        #print(data)
        components = data['components']
        if(len(components) != 0):
            for p in components:
                response.append({'name': p['name'],
                                 'projectKey': p['key']})
    return {'data': response}


"""
output: {
    data: {
        val : count
    }
}
"""
def GetProjectFacets(prokey,facet):
    pload = {'componentKeys': prokey,
             'facets': facet}

    data = SoncloudAPICall(url2, pload)
    response = {}
    if type(data) == 'str':
        return data
    else:
        components = data['facets'][0]['values']
        if(len(components) != 0):
            for p in components:
                 response[p['val']] = p['count'] 
    return response


"""
output: {
    data: [
        {'issueKey': key,
         'severity': severity,
         'msg':pmessage
         }
    ]
}
"""
def GetIssuesList(prokey, type):

    pload = {'componentKeys': prokey, 
            'sonarsourceSecurity': type
            }
    data = SoncloudAPICall(url2,pload)
    response = []
    if type(data) == 'str':
        return data
    else:
        #print(data)
        components = data['issues']
        if(len(components) != 0):
            for p in components:
                response.append({'issueKey': p['key'],
                                 'severity': p['severity'],
                                 'msg':p['message']
                                 })
    return response


    


"""
output: {
    data: [
        {'issueKey': key,
         'rule' : rule,
         'fileKey' : componment,
         'severity' : severity,
         'textLine' :line,
         'msg': message
         }
    ]
}
"""
def GetBugDetail(prokey):
    pload = {'componentKeys': prokey, 
                'types': 'BUG',
                'ps': 5}
    data = SoncloudAPICall(url2,pload)
    response = []
    if type(data) == 'str':
        return data
    else:
        #print(data)
        components = data['issues']
        if(len(components) != 0):
            for p in components:
                response.append({'issueKey': p['key'],
                                 'rule': p['rule'],
                                 'severity': p['severity'],
                                 'fileKey': p['component'],
                                 'textLine': p['line'],
                                 'msg':p['message']
                                 })
    return response




def GetSourceCode(filekey, startline,endline):
    pload = {'key': filekey, 
             'from': startline,
             'to': endline
             }
    data = SoncloudAPICall(url4,pload)
    response = []
    if type(data) == 'str':
        return data
    elif data.get('errors') != None:
        return "File Not Found!!!"
    else:
        #print(data)
        components = data['sources']
        for x in components:
            l = re.sub('<.*?>', '', x[1])
            l1 = re.sub('&lt;', '<', l)
            l2 = re.sub('&gt;', '>', l1)
            response.append(l2)
    return response 



"""
output: {
    data: 
        {'key': key,
         'name' : name,
         'htmlDesc' : htmlDesc,
         }
}
"""

def GetRule(orgkey, rulekey):
    pload = {'key': rulekey, 
             'organization': orgkey
             }
    data = SoncloudAPICall(url3,pload)
    response = {}
    if type(data) == 'str':
        return data
    elif data.get('errors') != None:
        return "Rule Not Found!!!"
    else:
        #print(data)
        components = data['rule']
        response['key'] = components['key']
        response['name'] = components['name']
        response['htmlDesc'] =  components['htmlDesc']
    return response         



def SoncloudAPICall(key, pload):
    
    url = key
    headers = {}
    response = requests.get(url, headers=headers, params= pload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    # Must have been a 200 status code
    json_obj = response.json()
    return json_obj