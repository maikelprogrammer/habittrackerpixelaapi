#a habit tracker using pixela api

import requests
from datetime import datetime

PIXELA_END_POINT="https://pixe.la/v1/users"

TOKEN="yourowntoken"# A token string used to authenticate as a user to be created. The tokenstring is hashed and saved.Validation rule: [ -~]{8,128}
USER_NAME="yourname"#User name for this service.Validation rule: [a-z][a-z0-9-]{1,32}
GRAPH_ID="graph1"

pixela_parameters={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#response=requests.post(url=PIXELA_END_POINT,json=pixela_parameters)
#print(response.text)

GRAPH_END_POINT=f"{PIXELA_END_POINT}/{USER_NAME}/graphs"
graph_parameters={
    "id":GRAPH_ID,
    "name":"coding graph",
    "unit":"hrs",
    "type":"int",
    "color":"momiji",
}
headers_parameters={
    "X-USER-TOKEN":TOKEN,
}

#response=requests.post(GRAPH_END_POINT,json=graph_parameters,headers=headers_parameters)
#print(response.text)

POST_VALUE_END_POINT=f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}"

today=datetime.now()


parameters={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many hours did you code today? : "),
}

response=requests.post(POST_VALUE_END_POINT,json=parameters,headers=headers_parameters)
print(response.text)

#update the pixela
#UPDATE_END_POINT=f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#parameters_in={
    #"quantity":"5"
#}
#response=requests.put(UPDATE_END_POINT,json=parameters_in,headers=headers_parameters)
#print(response.text)

#delete the pixela
#DELETE_END_POINT=f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response=requests.delete(DELETE_END_POINT,headers=headers_parameters)
#print(response.text)