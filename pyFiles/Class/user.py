class User:
	def __init__(self, name, password, status):
		self.name = name	
		self.password = password
		self.status = status #0 : Employee / 1 : Project owner / 2 : Admin
		self.projects = []
		self.tasks = []