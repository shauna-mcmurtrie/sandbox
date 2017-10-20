import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
from sys import argv


def set_user(username,password):

    print('Creating user {0}...'.format(username))
    user = PasswordUser(models.User())
    user.username = username
    user.password = password
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()
    print('Done.')
    exit()


if __name__ == '__main__':

    set_user(argv[1], argv[2])
#    for conn in conn_dict:
#        set_connection(conn, conn_dict)
    exit()