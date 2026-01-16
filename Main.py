# Get the name of user
Fname = input("What is your name ? "'\n')
# Clean up the input
Fname = Fname.lower().title().strip()

def ScoreCalc():
    # Get a list of the scores
    scores = []
    for i in range(2):
        # Get 2 scores from the user
        score = float(input(f"What percentage did you get on Mini Project {i+1} ?"'\n'))
        # Added to the list
        scores.append(score)
        # If more scores needed, would be much more efficient
    avg = (scores[0]*0.4) + (scores[1]*0.6)
    avg = round(avg)
    return(avg)
# Get the average score to be used in the get_grade() function
score = ScoreCalc()

def get_grade(score):
    # Score is passed through as a parameter
    if score < 40:
        classification = "Fail"
    elif score < 50:
        classification = "Third"
    elif score < 60:
        classification = "Lower Second"
    elif score < 70:
        classification = "Upper Second"
    else:
        classification = "First Class"
    # Return the classification to be outputed at the end
    return classification

# Gets the classification from the get_grade() function
classification = get_grade(score)

print(f"Student : {Fname} | Final Score : {score} | Result : {classification}")