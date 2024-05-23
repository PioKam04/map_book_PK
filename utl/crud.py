def read(users: list[dict[str, str]])->None:
    for user in users:
     print(f'twój znajomy  {user['name']} opublikował: {user['posts']} postów')

def search(users: list[dict[str, str]])->None:
   user_name=input("kogo szukasz: ")
    for user in users:
       if user["name"] == user_name:
        print(f'znaleziono użytkownika{user}