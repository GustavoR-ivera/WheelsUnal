from datetime import datetime

from Data.PoolCursor import PoolCursor
from Data.User import User
from Data.UserDAO import UserDAO


class UserDAOImpl(UserDAO):

    def loginValidation(self, email, password):
        try:
            with PoolCursor() as cursor:
                query = f"select * from test_users " \
                        f"where email = '{email}' and password = '{password}' "
                cursor.execute(query)
                record = cursor.fetchone()
                if record:
                    return 1
                else:
                    return 0
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getUsersByStatus(self, status):
        #return a user list with the user status specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM test_users " \
                        f"WHERE user_status = '{status}' "
                cursor.execute(query)
                records = cursor.fetchall()
                print(f'records: {cursor.rowcount}')
                print(f'users: {records}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getUserById(self, user_id):
        #return a user with the user_id specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM test_users " \
                        f"WHERE user_id = '{user_id}' "
                cursor.execute(query)
                record = cursor.fetchone()
                print(f'user: {record}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def getUserByDni(self, dni_number):
        #return a user with the user dni_number specified
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * " \
                        f"FROM test_users " \
                        f"WHERE dni_number = '{dni_number}' "
                cursor.execute(query)
                record = cursor.fetchone()
                print(f'user: {record}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def insert(self, user):
        try:
            with PoolCursor() as cursor:
                query = f"insert into test_users (user_name, password, user_status, country, " \
                        f"dni_type, dni_number, email, last_login, phone_number, deleted, created_at," \
                        f"updated_at, driving_license, rol) " \
                        f"values ('{user.user_name}','{user.password}',{user.user_status}," \
                        f"'{user.country}', '{user.dni_type}', '{user.dni_number}', '{user.email}', " \
                        f"'{user.lastLogin}', '{user.phoneNumber}', {user.deleted}, '{user.created_at}'," \
                        f"'{user.updated_at}', '{user.drivingLicense}', '{user.rol}' )"
                cursor.execute(query)
                print(f'inserted records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')

    def select(self):
        try:
            with PoolCursor() as cursor:
                query = f"SELECT * FROM test_users"
                cursor.execute(query)
                records = cursor.fetchall()
                print(f'records: {cursor.rowcount}')
                print(f'users: {records}')
        except Exception as e:
            print(f'An exception has occurred: {e}')


    def delete(self, user):
        try:
            with PoolCursor() as cursor:
                query = f"update test_users " \
                        f"set deleted = 1, deleted_at = '{datetime.now()}'  " \
                        f"where user_id = {user.user_id} "
                cursor.execute(query)
                print(f'deleted records: {cursor.rowcount}')

        except Exception as e:
            print(f'An exception has occurred: {e}')

    def update(self, user):
        try:
            with PoolCursor() as cursor:
                query = f"update test_users " \
                        f"set user_id = {user.user_id}, user_name = '{user.user_name}', " \
                        f"password = '{user.password}', user_status = {user.user_status}, " \
                        f"country = '{user.country}', dni_type = '{user.dni_type}', dni_number = '{user.dni_number}' " \
                        f"where user_id = {user.user_id} "
                cursor.execute(query)
                print(f'updated records: {cursor.rowcount}')
        except Exception as e:
            print(f'An exception has occurred: {e}')


if __name__ == "__main__":
    pass
    # insert
    #user1 = User(None, "Michael Jordan", "DFRG5677gh4", 0, "Belgica", "DNI", "gt5555-0", 'loquesea2@mail.com', datetime.now(),
    #             '3223877590', 0, datetime.now(), datetime.now(), None, 'gt5555-0', 'generico')
    #userDAO = UserDAOImpl()
    # userDAO.insert(user1)
    #
    # user1 = User(58, "Gerrad Lampard", "YTfr3", 1, "Inglaterra", "TI", "65665E14")
    # userDAO = UserDAOImpl()
    # userDAO.update(user1)
    #UserDAOImpl().getUsersByStatus(True)

    # #-get user by dni number
    # userDao = UserDAOImpl()
    # userDao.getUserByDni("98595-T")

    # get user by id
    #userDao = UserDAOImpl()
    # check the user
    #userDao.getUserById(12)

    # delete user
    # check the user
    #userDao.getUserById(12)
    # then you can delete it
    #userDAO.delete(user1)

    # # get users by status
    # userDao = UserDAOImpl()
    # userDao.getUsersByStatus(0)

    # # select method
    # userDao = UserDAOImpl()
    # userDao.select()


    #print(datetime.now())