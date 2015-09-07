
def strip_all_white_space(text):
	white_spaces = ["\n", "\t", "\r"]
	for white_space in white_spaces:
		text =text.replace(white_space, " ")
	return text