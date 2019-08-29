class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance
class Ave(Singleton):
	nombre = ""
		
a = Ave()
b = Ave()
 
a.nombre = "Juan"
b.nombre = "Mr. Nobody"
print (a.nombre, b.nombre)
