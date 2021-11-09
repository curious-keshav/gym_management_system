
import sqlite3

class Database1:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY ,Name text, Phone_No INTEGER, joining text,BMI INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, phone_no, joining, bmi):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         ( name, phone_no, joining, bmi))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, phone_no, joining, bmi):
        self.cur.execute("UPDATE parts SET name = ?, phone_no = ?, joining = ?, bmi = ? WHERE id = ?",
                         (name, phone_no, joining, bmi, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database1('customer1.db')
# db.insert("Keshav",7973068960,"7 November",25)
# db.insert("Rahul",7973063410,"2 October",26)
# db.insert("Harsh",7426263410,"4 August",24)
# db.insert("Tushar",3242063410,"12 October",26)

# for i in range(32):
#     db.remove(i)
