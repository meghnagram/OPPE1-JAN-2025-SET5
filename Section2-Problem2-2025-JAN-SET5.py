

n = int(input())
score = 0
n_correct = 0
for i in range(n):
    ans_type, sol, ans = input().split()
    if ans_type == 'choice':
        if sol == ans:
            score += 3
            n_correct += 1
        else:
            score -= 1
    elif ans_type == 'range':
        a, b = map(float, sol.split('..'))
        if a <= float(ans) <= b:
            score += 3
            n_correct += 1
print(score)
print(f"{n_correct}")

# #Another Method:
# n=int(input())

# l=[]
# m=[]
# sum=0
# c=0
# r=[]

# for i in range(n):
#     l.append(input())
#     m=l[i].split()
#     if m[0]=='choice':
#         if m[1]==m[2]:
#             sum +=3
#             c +=1
#         else:
#             sum -=1
#     if m[0]== 'range':
#         r=m[1].split('..')
#         if float(r[0])<=float(m[2])<=float(r[1]):
#             sum +=3
#             c +=1
            
# print(sum)
# print(c)


# Score Objective Questions
# Given the type of question with the correct answer and the student's answer separated by space over multiple lines, find the total marks and number of correct anwers, assuming each question has three marks for a correct answer and a choice type question also has a negative one marks for an incorrect answer. range type question has no negative marks.

# The range in the range-type question is given in the format {low}..{high}.

# The choice type answer is correct if both the answer given and the student's answer are same.
# The range type answer is correct if low<=student_anser<=high.
# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# The first line contains an integer n representing the number of questions.
# The next n lines each contain the question type (choice or range), the correct answer (or range), and the student's answer.
# Output Format

# A single integer representing the total score.
# An integer representing the total number of correct answers.
# Example

# Input

# 4
# choice a b
# range 1..4 3
# choice b b
# range 1.1..4.5 5
# Output

# 5
# 2
# Explanation

# Input line	is correct	marks	total marks	n_correct
# choice a b	No	-1	-1	0
# range 1..4 3	Yes	3	2	1
# choice b b	Yes	3	5	2
# range 1.1..4.5 5	No	0	5	2
# Thus the total marks is 5 and the number of correct answers is 2.

