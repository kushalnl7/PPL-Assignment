# 1.  Solve the puzzle with a Python program : A man is walking down the village road with a tiger, a goat and a bundle of grass.
# Soon he arrives at the river bank where there is one tiny boat that can carry him and another animal or grass at a time.
# Here is the problem: Left alone, the tiger will eat the goat. And similarly, the goat will eat the grass bundle.
# How is he going to take all three across the river safely?

bank_a = {"tiger", "goat", "grass"}
bank_b = set()
current_bank = 'a'
illegal1 = {"tiger", "goat"}
illegal2 = {"goat", "grass"}
#last = str()
while len(bank_a) > 0 :
	if current_bank == 'a' :
		if len(bank_a) == 3 :
			x = bank_a.pop()
			if (bank_a != illegal1) and (bank_a != illegal2) :
				print(x.capitalize() + " taken from bank A to bank B.")
				bank_b.add(x)
				current_bank = 'b'
			else :
				bank_a.add(x)
		else :
			x = bank_a.pop()
			print(x.capitalize() + " taken from bank A to bank B.")
			bank_b.add(x)
			current_bank = 'b'
	else :
		if (bank_b != illegal1) and (bank_b != illegal2) :
			print("Farmer returns alone.")
		else :
			x = bank_b.pop()
			print(x.capitalize() + " taken from bank B to bank A.")
			bank_a.add(x)
		current_bank = 'a'
