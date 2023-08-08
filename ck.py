import random
from guess import a

jawaban = random.randint(1,10)
print(jawaban)
tebakan = int(input('tebak angka 1 s.d 10 '))

if a(tebakan, jawaban ) :
	print("jwban km bnr")
else :
	print("jwbn km slh")