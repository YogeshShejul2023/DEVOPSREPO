names = []
feedbacks = []
sumFeedback = 0

for i in range(5):
    name = input("Enter the name: ")
    
    # Ensure the feedback is a valid number
    while True:
        try:
            feedback = int(input("Enter the Feedback (1-5): "))
            if 1 <= feedback <= 5:
                break
            else:
                print("Feedback must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    names.append(name)
    feedbacks.append(feedback)
    sumFeedback += feedback

average = sumFeedback / len(names)

print("\nAverage Feedback:", average)
print("Learner Names:", names)
print("Feedbacks:", feedbacks)
