from models.data import users
from utl.crud import read

if __name__ == "__main__":
    print(f"witaj {users[0]["name"]}")

    read(users)