import requests


url="https://api.yelp.com/v3/businesses/search"
api_key="ZQf5IBsDDtS59VXmc6knYTobMOkyk4DNwrb6ZIaIcasxMjLau9faF5_fHG9CKxNNAr7sPLWmGyU2bBSYhHkKn_26latBY7nqylEKixDS-Cbab9iWYLFAusYg8eBfYnYx"

headers={
    "Authorization":"Bearer "+api_key
}

params={
    "location":"NYC",
    "term":'Barber'
}
response=requests.get(url,headers=headers,params=params)
businesses=response.json()["businesses"]
print(businesses)
for business in businesses:
    print(business["name"])