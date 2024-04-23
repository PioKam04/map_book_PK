lista_stasia:list=["piter","piter",]
print(lista_stasia)


def add_user(lista:list)->None:
    user_name=input("podaj imie  ")
    user_surname=input("podaj nazwisko ")
    user_posts=input("podaj ile postów ")
    lista.append({"name," : user_name, "surname": user_surname,"posts": user_posts})
    add_user(lista_stasia)

    print(lista_stasia)
