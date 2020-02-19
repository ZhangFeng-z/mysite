
class A:
	def d(self):
		print("heleo")
	c=0

	class B():
		def d(self):
			print("这是内类")

if __name__ == '__main__':
	b=A()
	e=b.B()
	print(b.d())

	