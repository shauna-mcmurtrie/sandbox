import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())
user.username = 'airflow'
user.password = 'airflow123'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
