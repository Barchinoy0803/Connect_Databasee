import pymysql

class Talaba:
    def __init__(self):
        self.connectToDataBase()
        self.createDataBase()
        self.createTable()
        self.insertIntoValues()

    def connectToDataBase(self):
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="0803",
                database="student"
            )
            self.cursor = self.db.cursor()

    def createDataBase(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS student")
        self.cursor.execute("USE student")

    def createTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS talaba")
        self.cursor.execute('''CREATE TABLE talaba(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            ism TEXT,
                            tugilgan_sana TEXT,
                            baho INT)''')

    def insertIntoValues(self):
        self.cursor.execute('''INSERT INTO talaba (ism, tugilgan_sana, baho) VALUES
                            ('Ali', '15-fevral', 4),
                            ('Vali', '10-may', 3),
                            ('Ali', '28-fevral', 5),
                            ('Olim', '22-mart', 4),
                            ('Aziza', '14-fevral', 2),
                            ('Dilshod', '11-iyun', 5),
                            ('Zokir', '4-dekabr', 1),
                            ('Shohruh', '5-fevral', 4),
                            ('Aziza', '19-aprel', 5),
                            ('Zaynab', '24-dekabr', 4)''')
        self.db.commit()

    def showStudentsTheSameNames(self):
        self.cursor.execute('''SELECT * 
                            FROM talaba 
                            WHERE ism IN (
                                SELECT ism 
                                FROM talaba 
                                GROUP BY ism 
                                HAVING COUNT(*) > 1
                            )''')
        result = self.cursor.fetchall()
        for names in result:
            print(names)

    def showStudentsByGrade(self):
        self.cursor.execute('''SELECT * FROM talaba WHERE baho=4 and tugilgan_sana LIKE "%fevral%"''')
        for student in self.cursor.fetchall():
            print(student)

    def changeId(self):
        lst = []
        self.cursor.execute('''SELECT * FROM talaba''')
        for data in self.cursor.fetchall():
            lst.append(list(data))
        print(lst)

        for i in range(1, len(lst)):
            if lst[i][0] % 2 == 0:
                even = lst[i] 
                odd = lst[i - 1]
                sql = 'UPDATE talaba SET ism=%s, tugilgan_sana=%s, baho=%s WHERE id=%s'
                self.cursor.execute(sql, (even[1], even[2], even[3], odd[0]))
                sql = 'UPDATE talaba SET ism=%s, tugilgan_sana=%s, baho=%s WHERE id=%s'
                self.cursor.execute(sql, (odd[1], odd[2], odd[3], even[0]))
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        self.db.commit()
        print(lst)

    


t = Talaba()
t.showStudentsTheSameNames() 
t.showStudentsByGrade() 
t.changeId()

