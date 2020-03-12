import shelve

FILENAME = 'DBSHELVE'


def create_user(id_, login, password):
    with shelve.open(FILENAME) as users:
        users[str(id_)] = {1: 2}


def get_user(id_):
    with shelve.open(FILENAME) as users:
        return users.get(str(id_))


create_user(12345, 123, 13)
print(get_user(12345))
