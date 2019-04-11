class Calculator:
	def __init__(self):
		self.add_count = 0
		self.sub_count = 0
		self.mul_count = 0
		self.div_count = 0

	def add(self, num1, num2):
		self.add_count += 1

		return num1 + num2

	def sub(self, num1, num2):
		self.sub_count += 1

		return num1 - num2

	def mul(self, num1, num2):
		self.mul_count += 1

		return num1 * num2

	def div(self, num1, num2):
		self.div_count += 1
		return num1 / num2

	def show_count(self):
		print("덧셈 : %s" % self.add_count)
		print("뺄셈 : %s" % self.sub_count)
		print("곱셈 : %s" % self.mul_count)
		print("나눗셈 : %s" % self.div_count)

cal = Calculator()

print(cal.add(1, 1))
print(cal.add(2, 2))
print(cal.add(3, 3))

print(cal.sub(2, 1))
print(cal.sub(3, 1))

print(cal.mul(2, 2))

cal.show_count()
