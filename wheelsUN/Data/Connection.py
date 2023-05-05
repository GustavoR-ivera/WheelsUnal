import sys

import psycopg2
from psycopg2 import pool


class Connection:
    #class variables
    _user='postgres'
    _password='admin'
    _host='127.0.0.1'
    _port='5432'
    _database='test_1'
    _min_connection = 1
    _max_connection = 6
    _pool = None
    # _connection = None
    # _cursor = None

    @classmethod
    def getPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._min_connection, cls._max_connection,
                                                      host = cls._host, user=cls._user,
                                                      password=cls._password, port=cls._port,
                                                      database=cls._database)
                #print('successful pool')
                return cls._pool

            except Exception as e:
                print(f'An exception has ocurred {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    # get a pool connection
    def getConnection(cls):
        connection = cls.getPool().getconn()
        #print(f'conexion exitosa {connection}')
        return connection

    @classmethod
    # free a pool connection
    def freeConnection(cls, conn):
        cls.getPool().putconn(conn)
        #print(f'free connection {conn}')

    @classmethod
    # free pool
    def closeConnections(cls):
        cls.getPool().closeall()




