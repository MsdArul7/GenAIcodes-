#wrire a code a tuples to give a score to 5 students and print them
scores = ()
for i in range(5):
    score = int(input(f"Enter the score for student {i + 1}: "))
    scores += (score,)
print("Scores of the students:", scores)
