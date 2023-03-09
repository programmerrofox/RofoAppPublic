import mysql.connector

class ConnectData():
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",password='xyz.1234',database='rofo_db')
        self.c = self.db.cursor()

    def insert_data(self,un,pw):
        n= un
        p= pw
        self.c.execute("""insert into users_tb (Id,User_Name,Password)values(%s,%s,%s)""", (0,n, p))
        #self.c.execute("""delete from users_tb""")

        self.db.commit()
        print('Done')

        #self.c.execute('select * from city where id = 5')
        #for row in self.c:
            #print(f'row={row}')