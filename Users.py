from Models.Base import *
from Models.Reports import Reports


class Users(Base):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    login = CharField(max_length=8)
    password = CharField()
    role = CharField()

if __name__ == "__main__":

    connect().create_tables([Users,Reports])
