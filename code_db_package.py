import sqlite3

class Database2:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY ,Package text, Package_Facility text, Package_Cost text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, package, package_facility, package_cost):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?)",
                         ( package, package_facility, package_cost))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, package, package_facility, package_cost):
        self.cur.execute("UPDATE parts SET package = ?, package_facility = ?, package_cost = ? WHERE id = ?",
                         ( package, package_facility, package_cost, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database2('package1.db')
# db.insert("Gold","Cardic","25")
# db.insert("Silver","Workout","26")
# db.insert("Diamond","Cardic + Machines","24")
# db.insert("Platinum","Cardic + Machines + Supplements","26")
