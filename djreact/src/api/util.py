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
output: [
    {
        'issueKey': key
        'severity': severity
        'msg' : message
    }
]
"""
def GetIssuesList(prokey, value):

    pload = {'componentKeys': prokey, 
            'sonarsourceSecurity': value
            }
    data = SoncloudAPICall(url2,pload)
    response = []
    #print(data)
    if type(data) == "str":
        return data
    else:
        #print(data)
        components = data['issues']
        if(len(components) != 0):
            for p in components:
                response.append({'issueKey': p['key'],
                                 'ruleKey' : p['rule'],
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
         #'textLine' :line,
         'textLine':code,
         'msg': message
         }
    ]
}
"""
def GetBugDetail(prokey):
    pload = {'componentKeys': prokey, 
                'types': 'BUG',
                'ps': 10}
    data = SoncloudAPICall(url2,pload)
    orgkey = data['organizations'][0]['key']

    response = []
    if type(data) == 'str':
        return data
    else:
        #print(data)
        components = data['issues']
        if(len(components) != 0):
            for p in components:
                ruleDesc = GetRule(orgkey,p['rule'])
                textLine = GetSourceCode(p['component'],p['line'],p['line'])[0]
                response.append({
                    'issueKey':p['key'],
                    'rule': ruleDesc,
                    'textLine': textLine,
                    'msg': p['message'],
                    'severity':p['severity']
                })
                # response.append({'issueKey': p['key'],
                #                  'rule': p['rule'],
                #                  'severity': p['severity'],
                #                  'fileKey': p['component'],
                #                  'textLine': p['line'],
                #                  'msg':p['message']
                #                  })
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
        response['htmlDesc'] =  components['mdDesc']
    return response 


"""
output:{
    #ruleKey: rule
    ruleDesc: rule
    comment: message
    details: [
        {
            componenet:
            #startline:
            #endline:
            code:
            msg:[]
        }
    ]
}
file_dict = {} # [startline, component]: [ endline, [msgs]]
"""

def GetVulnerabilityDetail(prokey, issuekey):
    pload = {'componentKeys': prokey, 
             'issues': issuekey
             }
    data = SoncloudAPICall(url2,pload)

    #get rule description
    rulekey = data['issues'][0]['rule']
    orgkey = data['organizations'][0]['key']
    rule = GetRule(orgkey,rulekey)


    comment = data['issues'][0]['message']
    response = {'ruleDesc': rule, 'comment':comment}
    detail = []
    file_dict = {} # [startline, component]: [ endline, [msgs]]
    if type(data) == 'str':
        return data
    elif data.get('errors') != None:
        return " Not Found!!!"
    else:
        #print(data)
        locations = data['issues'][0]['flows'][0]['locations']
        for location in locations:
            component = location['component']
            startline = location['textRange']['startLine']
            endline = location['textRange']['endLine']
            message = location['msg']

            key = (startline, component)
            message_list = [message]
            if key not in file_dict:
                file_dict[key] = [endline, message_list]
            else:
                file_dict[key][1] += message_list
                if file_dict[key][0] < endline:
                    file_dict[key][0] = endline
    
    for i in file_dict:
        code = GetSourceCode(i[1],i[0],file_dict[i][0])
        detail.append({
            'component': i[1],
            'msg':file_dict[i][1],
            'code':code
        })
        # flow.append({
        #     'component': i[1],
        #     'startLine': i[0],
        #     'endLine': file_dict[i][0],
        #     'msg': file_dict[i][1]
        # })


    response['detail'] = detail
    
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