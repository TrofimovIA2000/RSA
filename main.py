from random import randrange


def miller_rabin(n, k=10):
	if n == 1:
		return True
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True


def generator():

	result = False

	while not result:

		numb = randrange(10, 100)
		result = miller_rabin(numb)

		if result:
			return numb


class Addressee:
	p1 = 0
	p2 = 0
	n = 0
	Fi = 0
	e = 0
	D = 0
	message = 0

	def nCount(self):
		self.n = self.p1 * self.p2
		print('n:', self.n)

	def FiCount(self):
		self.Fi = (self.p1 - 1) * (self.p2 - 1)
		print('Fi', self.Fi)

	def dCount(self):
		self.D = 2

		while not (self.D * self.e) % self.Fi == 1:
			self.D += 1

		print('D:', self.D)

	def decoding(self):
		self.message = self.message ** self.D % self.n
		print('Сообщение Боба, расшифрованное Алисой:', self.message)


class Sender:

	message = 0
	n = 0
	e = 0
	encMessage = 0

	def encryption(self):
		self.encMessage = self.message ** self.e % self.n
		print('Зашифрованное сообщение:', self.encMessage)


Alice = Addressee()
Bob = Sender()

Alice.p1, Alice.p2, Alice.e, Bob.message = generator(), generator(), 17, 89

print('p1:', Alice.p1, '\n', 'p2:', Alice.p2, '\n', 'e:', Alice.e,  sep='')

Alice.nCount()
Alice.FiCount()
Alice.dCount()

Bob.e = Alice.e
Bob.n = Alice.n

print('Сообщение Боба:', Bob.message)
Bob.encryption()
Alice.message = Bob.encMessage

Alice.decoding()