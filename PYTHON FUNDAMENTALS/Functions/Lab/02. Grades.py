def grade_in_word(grade_num):
    if 2.00 <= grade_num <= 2.99:
        return "Fail"
    elif 3 <= grade_num <= 3.49:
        return "Poor"
    elif 3.5 <= grade_num <= 4.49:
        return "Good"
    elif 4.5 <= grade_num <= 5.49:
        return "Very Good"
    elif 5.5 <= grade_num <= 6:
        return "Excellent"

grade_data = float(input())

result = grade_in_word(grade_data)
print(result)
