import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count=0
    sorted=False
    while sorted is not True:
    	sorted=True
    	for i in range(n-1):
        	if(a[i]>a[i+1]):
        		p=a[i]
        		a[i]=a[i+1]
        		a[i+1]=p
        		count+=1
        		sorted=False
    print("Array is sorted in ",count," sawps")
    print("First Element: ",a[0])
    print("Last Element: ",a[n-1])
           


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

