import requests


url="https://jsonplaceholder.typicode.com/posts"
data={

    'title': 'foo',
    'body': 'bar',
    'userId': 1,

}

response=requests.post(url,data=data)
print(response)
print(response.text)