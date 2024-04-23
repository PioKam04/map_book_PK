users:list[dict[str, str]] = [
    {"name": "stas","surname": "Grzymski","posts": 1},
    {"name":"Kacper","surname": "Macioch","posts": 2},
    {"name":"michal","surname": "Krzywinski","posts": 3},
    {"name":"tymon","surname": "Leszczyc","posts": 3},
    {"name":"michal","surname": "Lembryk","posts": 5},
]
print(f"witaj {users[0]["name"]}")

def read(users: list[dict[str, str]])->None:
    for user in users:
     print(f'twój znajomy  {user['name']} opublikował: {user['posts']} postów')

read(users)