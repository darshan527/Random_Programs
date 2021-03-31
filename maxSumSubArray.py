def maxSumSubArray(arr):
    temp_arr = []
    final_arr = []
    best_sum = 0
    temp_sum = 0

    for i in arr:
        temp_sum += i
        temp_arr.append(i)
        if temp_sum < 0:
            temp_sum = 0
            temp_arr = []
        best_sum = max(best_sum, temp_sum)
        if best_sum == temp_sum:
            final_arr = temp_arr[:]
    print(best_sum, final_arr)


if __name__ == "__main__":
    maxSumSubArray(
        list(map(int, input("Please enter the Space seperated integers").split())))
    # maxSumSubArray([1, 2, -5, -4, 1, 6])
