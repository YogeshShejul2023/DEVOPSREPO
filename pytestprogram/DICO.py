Learners = []

sumFeedback = 0

for i in range(3):

    learner = {}

    name = input("Enter the name")

    feedback = int(input("Enter the Feedback"))

    learner["name"] = name

    learner["feedback"] = feedback

    sumFeedback = sumFeedback+feedback

    Learners.append(learner)

 

 

average = sumFeedback/len(Learners)

print(average)

print(Learners)