import sqlite3 
import datetime
import time
import sqlite3 as sql
class DB:
	def loadUser(self, uid):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'SELECT gold FROM users WHERE uid=?', (int(uid),))
			fetch = self.cur.fetchall()
			gold = fetch[0]
			self.conn.close()
			return gold
		except (sql.OperationalError, IndexError):
			gold = 0
			self.conn.close()
			return gold
	def isUserExist(self, uid):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'SELECT * FROM users WHERE uid=?', (uid,))
			fetch = self.cur.fetchall()
			if len(fetch) > 0:
				return True
			self.conn.close()
		except (sql.OperationalError, IndexError) as e:
			print(e)
			return False
	def createUser(self, uid):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS users (uid INTEGER, gold INTEGER)")
		self.conn.commit()
		var = uid, 0
		self.cur.execute("INSERT INTO users VALUES (?,?)", var)
		self.conn.commit()
		self.conn.close()
	def execute(self, datasql):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"{datasql}")
		self.conn.commit()
		self.conn.close()
	def wGoldVal(self, uid, gold):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"UPDATE users SET gold=gold+{gold} WHERE uid={uid}")
		self.conn.commit()
		self.conn.close()
	def rwGoldVal(self, uid, suid, amount):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"UPDATE users SET gold=gold-{amount} WHERE uid={uid}")
		self.cur.execute(f"UPDATE users SET gold=gold+{amount} WHERE uid={suid}")
		self.conn.commit()
		self.conn.close()
	def rGoldVal(self, uid):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'SELECT gold FROM users WHERE uid=?', (uid,))
			fetch = self.cur.fetchall()
			return fetch[0]
		except (sql.OperationalError, IndexError) as e:
			return 0
			print(e)