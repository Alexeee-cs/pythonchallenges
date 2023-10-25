a_score = 0
b_score = 0
c_score = 0
#Round 1
a_question_1 = input("Give me one question: ")
a_answer_1 = input("Give me the answer for the question: ")

print("Player A asks:",a_question_1)
b_response_1 = input("Answer this question: ")
if b_response_1 == a_answer_1:
    b_score = b_score +1
#Round 2
b_question_1 = input("Give me one question: ")
b_answer_1 = input("Give me the answer for the question: ")

print("Player B asks:",b_question_1)
c_response_1 = input("Answer this question: ")
if c_response_1 == b_answer_1:
    c_score = c_score +1
#Round 3
c_question_1 = input("Give me one question: ")
c_answer_1 = input("Give me the answer for the question: ")

print("Player C asks:",c_question_1)
a_response_1 = input("Answer this question: ")
if a_response_1 == c_answer_1:
    a_score = a_score +1

print("player A scores:",a_score)
print("player B scores:",b_score)
print("player C scores:",c_score)
