#99 Bottles of Beer
def bottles(n):
	bottles = n
	for i in range(n+1):
		if bottles == 1:
			print(bottles, "bottle of beer on the wall,", bottles,"bottle of beer.")
			print("Take one down and pass it around,", bottles, "bottle of beer on the wall.")
			print()
			bottles-=1
		elif bottles == 0:
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print("Go to the store and buy some more,", n,"bottles of beer on the wall.")

		else:
			print(bottles, "bottles of beer on the wall,", bottles,"bottles of beer.")
			print("Take one down and pass it around,", bottles, "bottles of beer on the wall.")
			print()
			bottles -= 1
	