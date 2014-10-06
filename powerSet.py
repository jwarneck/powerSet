#creates power set of the list that is entered.
# combines each subset with the list into the power set.

def powerSet(list):
	return reduce(lambda result, x: result + [subset + [x] for subset in result], list, [[]])