A,B,C,D = map(int,[num for num in input()])

if A+B+C+D == 7:
    print("%s+%s+%s+%s=7" %(A,B,C,D))
elif A-B+C+D == 7:
    print("%s-%s+%s+%s=7" %(A,B,C,D))
elif A+B-C+D == 7:
    print("%s+%s-%s+%s=7" %(A,B,C,D))
elif A+B+C-D == 7:
    print("%s+%s+%s-%s=7" %(A,B,C,D))
elif A-B-C+D == 7:
    print("%s-%s-%s+%s=7" %(A,B,C,D))
elif A-B+C-D == 7:
    print("%s-%s+%s-%s=7" %(A,B,C,D))
elif A+B-C-D == 7:
    print("%s+%s-%s-%s=7" %(A,B,C,D))
elif A-B-C-D == 7:
    print("%s-%s-%s-%s=7" %(A,B,C,D))
else:
    print("No solution found.")
