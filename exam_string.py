key = "ABCDAC"
answers = "ABXDA"

correct = 0
wrong = 0
unanswered = 0
score = 0

for i in range(len(key)):
    if i < len(answers):
        ans = answers[i]
    else:
        ans = ""

    if ans == "":
        unanswered += 1
    elif ans == key[i]:
        correct += 1
        score += 2
    else:
        wrong += 1
        score -= 0.5

print("Correct:", correct)
print("Wrong:", wrong)
print("Unanswered:", unanswered)
print("Final Score:", score)