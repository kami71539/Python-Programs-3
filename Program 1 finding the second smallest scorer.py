# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:04:48 2019

@author: Kamran Hashmi
"""

if __name__ == '__main__':
    student_and_score=[]
    for _ in range(int(input())):
        students=[]
        for j in range(1):
            name = input()
            score = float(input())
            students.append(name)
            students.append(score)
        student_and_score.append(students)
    student_and_score_copy=student_and_score[:]
    length_of_list=len(student_and_score_copy)
    students_score=[]
    for i in range(length_of_list):
        score=student_and_score_copy[i][1]
        students_score.append(score)
    students_score.sort()
    students_score_copy=students_score[:]
    smallest_score=students_score[0]
    length_of_students_score=len(students_score)
    for i in range(length_of_students_score-1):
        if students_score[1]!=students_score[i]:
            break
        if students_score[1]==students_score[i]:
            students_score[1],students_score[i+1]=students_score[i+1],students_score[1]
    second_smallest_score=students_score[1]
    students_score.remove(second_smallest_score)
    copy=False
    ans=[]
    for i in students_score:
        if second_smallest_score==i:
            copy=True
    for i in student_and_score_copy:    
        if i[1]==second_smallest_score:
            ans.append(i[0])
    ans.sort()
    for i in ans:
        print(i)