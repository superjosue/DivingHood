class DicPrint():

	def __init__(self,Dict):
		import pprint
		pprint.PrettyPrinter(indent=4)
		self.p = pprint.pprint(Dict)
