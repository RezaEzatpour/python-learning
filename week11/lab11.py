from mysql.connector import MySQLConnection, Error

from configparser import ConfigParser


def readDbConfig(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(r'E:\_learning\Python\assignments\lab11\week11\config.ini')

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(
            '{0} not found in the {1} file'.format(section, filename))

    return db


def insertGrade(lastName, firstName, province, grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql = '''INSERT INTO grades (FName, LName, Province, Grade) VALUES(%s, %s, %s, %s)'''
        val = (firstName, lastName, province, grade)
        cursor.execute(sql, val)
        conn.commit()
        cursor.execute('SELECT * FROM grades')
        row = cursor.fetchone()
        print('<table border="1">')
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def deleteGrade(lastName, firstName, province, grade):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql = '''DELETE FROM grades WHERE(%s = FName and %s = LName and %s = Province and %s = Grade)'''
        val = (firstName, lastName, province, grade)
        cursor.execute(sql, val)
        conn.commit()
        cursor.execute('SELECT * FROM grades')
        row = cursor.fetchone()
        print('<table border="1">')
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def displayGrade(lastName, firstName, province):
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql = '''SELECT * FROM grades WHERE(FName LIKE %s and LName LIKE %s and Province LIKE %s)'''
        val = (firstName, lastName, province)
        cursor.execute(sql, val)
        conn.commit()
        row = cursor.fetchone()
        print('<table border="1">')
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

# def displayGrade(lastName, firstName, province):
#     try:
#         dbconfig = readDbConfig()
#         conn = MySQLConnection(**dbconfig)
#         cursor = conn.cursor()
#         sql = "SELECT * FROM grades WHERE FName = %s " 
#         val = str(firstName)
#         cursor.execute(sql)
#         conn.commit()
#         box = []
#         row = cursor.fetchone()
#         box.append = row
#         sql = """SELECT * FROM grades WHERE LName like '%s'"""
#         val = str(lastName)
#         cursor.execute(sql, val)
#         conn.commit()
#         row = cursor.fetchone()
#         box.append = row
#         sql = """SELECT * FROM grades WHERE Province like '%s'"""
#         val = str(province)
#         cursor.execute(sql, val)
#         conn.commit()
#         row = cursor.fetchone()
#         box.append = row
#         return box

#     except Error as e:
#         print(e)

#     finally:
#         cursor.close()
#         conn.close()



if __name__ == '__main__':
    while True:
        try:
            choice = int(input("""
                How do you whant to proceed (0. to exit):
                
                1. Enter a garde
                2. Display a garde
                3. Delete a grade
                0. Exit
                
            """))
            if choice == 0:
                break
            f = str(input('please enter First name =>  '))
            l = str(input('please enter Last name =>  '))
            p = str(input('please enter Province =>  '))
            if choice == 1: 
                g = str(input('please enter The Grade =>  '))
                insertGrade(l, f, p, g)
            elif choice == 2:
                g = displayGrade(l, f, p)
                print('<table border="1">')
                i = []
                while i in g:
                    print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(i[0], i[1], i[2], i[3]))
                print("</table>")
            elif choice == 3:
                g = str(input('please enter The Grade =>  '))
                deleteGrade(l, f, p, g)
            elif choice == 0: break
        
        except:
            print('Try a valid number!!')
