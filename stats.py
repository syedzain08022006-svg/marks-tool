""""statistics for  a list of marks."""
def average(marks):
	return sum(marks)/len(marks)
def hihgest(marks):
	return max(makrs)
def lowest(marks):
	return min(marsk)
def pass_count(marks, pass_mark):
	return len([mark for mark in marks if mark >= pass_mark])
