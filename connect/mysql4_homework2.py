import pymysql

class Drug:
    def __init__(self):
        self.connectToDataBase()
        self.createDataBase()
        self.createTable()
        self.insertIntoValues()

    def connectToDataBase(self):
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="0803"
            )
            self.cursor = self.db.cursor()
       
    def createDataBase(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS medicine")
        self.cursor.execute("USE medicine") 

    def createTable(self):
        self.cursor.execute('DROP TABLE IF EXISTS drugs')
        self.cursor.execute('''CREATE TABLE drugs(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            drugName text,
                            drugCompany text,
                            drugDateTime text,
                            drugCountry text,
                            drugPrice int)''')
        
    def insertIntoValues(self):
        self.cursor.execute('''INSERT INTO drugs(drugName, drugCompany, drugDateTime, drugCountry,drugPrice) VALUES
                            ('Paracetamol', 'HealthCorp', '2024-03-15', 'Uzbekistan', 450),
                            ('Ibuprofen', 'PharmaPlus', '2024-04-10', 'Russia', 300),
                            ('Aspirin', 'MedLife', '2023-05-05', 'Germany', 210),
                            ('Amoxicillin', 'BioHealth', '2023-07-20', 'USA', 150),
                            ('Ciprofloxacin tablet', 'GlobalMeds', '2024-02-25', 'Germany', 320),
                            ('Azithromycin', 'HealthCorp', '2024-09-17', 'Uzbekistan', 500),
                            ('Loratadine', 'PharmaPlus', '2024-03-12', 'France', 430),
                            ('Cetirizine', 'HealthWell', '2024-11-28', 'Uzbekistan', 250),
                            ('Metformin', 'WellnessLife', '2023-04-08', 'USA', 275),
                            ('Pantoprazole', 'BioHealth', '2023-05-21', 'Russia', 220),
                            ('Omeprazole', 'GlobalMeds', '2024-06-05', 'France', 340),
                            ('Salbutamol', 'AirwayMeds', '2024-10-29', 'Uzbekistan', 210),
                            ('Insulin 400', 'HealthCorp', '2024-12-15', 'Germany', 550),
                            ('Losartan', 'BioHealth', '2024-03-22', 'Germany', 405),
                            ('Glipizide', 'DiabetesMeds', '2023-05-30', 'USA', 450)
                            ''')
        self.db.commit()
    def firstQuery(self):
        self.cursor.execute('''SELECT drugName, drugCompany, drugPrice FROM drugs 
                            WHERE drugPrice BETWEEN 200 and 500
                            ORDER BY drugCompany DESC''') 
        for drug in self.cursor.fetchall():
            drug = list(drug)
            data = drug[0].split(" ") 
            if len(data) == 1:
                print(f"{drug[0]}, {drug[1]}, {drug[2]}")

    def secondQuery(self):
        self.cursor.execute('SELECT * FROM drugs ORDER BY drugCompany')
        for data in self.cursor.fetchall():
            data = list(data)
            date = data[3].split("-")
            if  date[1] == '03' or date[1] == '04' or date[1] == '05':
                print(f"{data[1]}, {data[2]}, {data[3]}, {data[4]}")


d = Drug()
d.firstQuery()
d.secondQuery()               