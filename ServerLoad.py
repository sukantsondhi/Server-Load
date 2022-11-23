
import math


A = [1,2,3,4,5,6,7,8,9,10]

def solution(A):

    sum = 0
    for i in range(0, len(A)):
        sum = sum + A[i]

    newSum = sum/2

    top = math.ceil(newSum)
    print(f"Load on Server1: {top}")

    bottom = math.floor(newSum)
    print(f"Load on Server2: {bottom}")

    diff = top - bottom
    print("Difference between the Server Loads:")

    return diff

print(solution(A))
