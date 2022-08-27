class ListTree:
	"""
	Подмешиваемый класс, который возвращает в __ str__ результат обхода целого
	дерева классов и атрибуты всех его объектов, начиная с self и выше;
	запускается print () и str() и возвращает сформированную строку;
	использует схему именования атрибутов _ X, чтобы избежать конфликтов
	имен в клиентах; явно рекурсивно обращается к суперклассам,
	для ясности применяет str.format().
	"""

	def __strnames(self, obj, indent):
		spaces = " " * (indent + 1)
		result = ""
		for attr in sorted(obj.__dict__):
			if attr.startswitch("__") and attr.endswitch("__"):
				result += spaces + "{0}\n".format(attr)
			else:
				result += spaces + "{0}={1}\n".format(attr, getattr(obj, attr))
		return result
	def __listclass(self, aClass, indent):
		dots = "." * indent
		if aClass in self.visited:
			return "\n{0}<Class {1}:, adress {2}: {see above}>\n".format(
				dots,
				aClass,__name__,
				id(aClass)
				)
	def __str__(self):
		self.__visited = {}
		here = self.__attrnames(self, 0)
		above = self.__listclass(self.__class__, 4)
		return "<Instance of {0}, adress {1}:\n{2}{3}>".format(
			self.__class__.__name__,
			id(self),
			here, above
			)

