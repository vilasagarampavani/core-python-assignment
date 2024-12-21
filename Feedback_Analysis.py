def feedback_analysis(ratings):
    if not ratings:
        return "No ratings available to calculate feedback"
    total_positive = sum(1 for rating in ratings if rating >= 4)

    if total_positive == 0:
        return 0.0

    percentage = (total_positive / len(ratings)) * 100
    return percentage

input_ratings = input("Enter ratings : ")
input_ratings = input_ratings.strip("[]")
ratings = list(map(int, input_ratings.split(',')))
print(f"Positive Feedback: {feedback_analysis(ratings)}%")
