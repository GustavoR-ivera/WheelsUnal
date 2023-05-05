from Data.Connection import Connection


class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        #si hubo alguna excepcion entonces hacemos rollback, no se realizan cambios
        if exc_val:
            self._connection.rollback()
            print(f'An exception has occurred {exc_type}, {exc_val}, {exc_tb}')
        else:
            #sino hay inconvenientes con la transaccion entonces hacemos commit
            self._connection.commit()
            #print(f'transaction committed')

        self._cursor.close()
        Connection.freeConnection(self._connection)


if __name__ == '__main__':
    with PoolCursor() as cursor:
        print('bloque with')
        cursor.execute('selecte * from test_users')
        print(cursor.fetchall())