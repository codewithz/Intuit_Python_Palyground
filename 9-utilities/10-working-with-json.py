import json
from pathlib import Path

movies=[
    {"id":1,"title":"Movie 1","year":1990},
    {"id":2,"title":"Movie 2","year":2000},
    {"id":3,"title":"Movie 3","year":2003},
    {"id":4,"title":"Movie 4","year":2011},
    {"id":5,"title":"Movie 5","year":2015}

]

data=json.dumps(movies)
print(data)

Path("movies.json").write_text(data)