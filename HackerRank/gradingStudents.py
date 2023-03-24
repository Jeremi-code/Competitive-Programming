from typing import List
def gradingStudents (grades:List)->List:
    list=[100,95,90,85,80,75,70,65,60,55,50,45,40]
    for i in range (len(grades)):
        for j in range(len(list)):
            if list[j]>grades[i] and list[j]-grades[i]<=2:
                grades[i]=list[j]
                break
    return grades
