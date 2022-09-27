"""
input: "([{}])*"

"""
def check_sym(open_sym, closing_sym):
	for opening, closing in zip("[({", "])}"):
		if open_sym == opening and closing_sym == closing:
			return True
	return False


character = "(){}[]"
inp = list(input())

brackets = [el for el in inp if el in character]

stack_brackets = type('stack', (list,), {'push':list.append})()

for i, el in enumerate(brackets):
	if not stack_brackets:
		stack_brackets.push(el)
	elif check_sym(stack_brackets[-1], el):
		stack_brackets.pop()
	else:
		stack_brackets.push(el)

print(not stack_brackets)
