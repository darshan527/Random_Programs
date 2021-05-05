n = int(input())
if (n % 5) == 0 and (n % 11) == 0:
    print("BOTH")
elif (n % 5) == 0 or (n % 11) == 0:
    print("ONE")
else:
    print("NONE")