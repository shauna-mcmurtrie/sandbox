from airflow import models, settings
from sys import argv


def set_connection(conn_id, conn_dict):

    conn = models.Connection()
    conn.conn_id = conn_id
    conn.conn_type = conn_dict[conn_id]['CONN_TYPE']
    conn.host = conn_dict[conn_id]['HOST']
    conn.password = conn_dict[conn_id]['PASSWORD']
    conn.port = conn_dict[conn_id]['PORT']
    conn.set_extra( "{{\"SSLMODE\": \"{0}\"}}".format(conn_dict[conn_id]['SSLMODE']))

    session = settings.Session()
    session.add(conn)
    session.commit()
    session.close()


if __name__ == '__main__':

    conn_dict=eval(argv[1])

    set_connection('rouge_one', conn_dict)
#    for conn in conn_dict:
#        set_connection(conn, conn_dict)
    exit()