import sqlite3 
import datetime
import time
import sqlite3 as sql
class DB:
	# старый метод для получения золота; не юзай я не тестил ¯\_(ツ)_/¯
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
	# проверка на существование юзера; uid - айди нужного юзера
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
	# создание пользователя; uid - айди нужного юзера; дефолт значения: коины = 0
	def createUser(self, uid):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS users (uid INTEGER, gold INTEGER)")
		self.conn.commit()
		var = uid, 0
		self.cur.execute("INSERT INTO users VALUES (?,?)", var)
		self.conn.commit()
		self.conn.close()
	# хуйня не юзай если не знаешь sql
	def execute(self, datasql):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"{datasql}")
		self.conn.commit()
		self.conn.close()
	# замена значения коинов с прибавлением прошлого количества; uid - айди нужного юзера, amount - кол-во коинов 
	def wGoldVal(self, uid, amount):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"UPDATE users SET gold=gold+{amount} WHERE uid={uid}")
		self.conn.commit()
		self.conn.close()
	# полная замена значения коинов; uid - айди нужного юзера, amount - кол-во коинов 
	def waGoldVal(self, uid, amount):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"UPDATE users SET gold={amount} WHERE uid={uid}")
		self.conn.commit()
		self.conn.close()
	# передача коинов другому человеку; uid - айди отправителя, suid - айди получателя, amount - кол-во коинов 
	def rwGoldVal(self, uid, suid, amount):
		self.conn = sql.connect("users.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"UPDATE users SET gold=gold-{amount} WHERE uid={uid}")
		self.cur.execute(f"UPDATE users SET gold=gold+{amount} WHERE uid={suid}")
		self.conn.commit()
		self.conn.close()
	# читает кол-во коинов; uid - айди нужного юзера
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

	def duduread(self, uid):
		self.conn = sql.connect("cooldown.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'SELECT negr FROM cooldown WHERE uid=?',(uid,))
			return self.cur.fetchall()[0]
		except (sql.OperationalError,IndexError) as e:
			print(f"роялдевники тоже негры {e}")

	def duduwrite(self, uid,droonkalox):
		self.conn = sql.connect("cooldown.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'UPDATE cooldown SET negr={droonkalox} WHERE uid={uid}')
			self.conn.commit()
		except (sql.OperationalError,IndexError) as e:
			print(f"роялдевники тоже негры {e}")

	def voloski(self, uid):
		self.conn = sql.connect("cooldown.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute("CREATE TABLE IF NOT EXISTS cooldown (uid INTEGER, negr REAL)")
			self.conn.commit()
			var = uid,0.00
			self.cur.execute("INSERT INTO cooldown VALUES (?,?)",var)
			self.conn.commit()
			self.conn.close()
		except (sql.OperationalError,IndexError) as e:
			print(f"роялдевники тоже негры {e}")

	def ahahah(self, uid):
		self.conn = sql.connect("cooldown.db")
		self.cur = self.conn.cursor()
		try:
			self.cur.execute(f'SELECT * FROM cooldown WHERE uid=?',(uid,))
			fetch = self.cur.fetchall()
			if len(fetch) > 0:
				return True
			self.conn.close()
		except (sql.OperationalError,IndexError) as e:
			print(e)
			return False