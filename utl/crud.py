def read(users: list[dict[str, str]])->None:
    for user in users:
     print(f'twój znajomy  {user['name']} opublikował: {user['posts']} postów')