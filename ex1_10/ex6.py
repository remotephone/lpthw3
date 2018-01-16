# assign 10 to the variable
types_of_people = 10
# assign X to the statement and f format it as an f-string.
x = f"There are {types_of_people} types of people."

# assign to variables and create a statement and assign it to y.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print them both.
print(x)
print(y)

# print them as f-strings and inside quotes
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "isn't that joke so funy?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
