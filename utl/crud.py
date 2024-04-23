def read(users: list[dict[str, str]])->None:
    for user in users:
     print(f'twój znajomy  {user['name']} opublikował: {user['posts']} postów')

def add_user(lista:list)->None:
    user_name=input("podaj imie  ")
    user_surname=input("podaj nazwisko ")
    user_posts=input("podaj ile postów ")
    lista.append({"name," : user_name, "surname": user_surname,"posts": user_posts})
