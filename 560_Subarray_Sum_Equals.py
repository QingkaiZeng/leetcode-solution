def subarraySum(nums, k: int):
    sum2count = {0:1}
    sum_all = 0
    result = 0
    for i in range(0, len(nums)):
        sum_all += nums[i]
        if sum_all - k in sum2count:
            result += sum2count[sum_all - k]
        if sum_all not in sum2count:
            sum2count[sum_all] = 1
        else:
            sum2count[sum_all] += 1
    print(sum2count)
    # result = 0
    # for key, value in sum2count.items():
    #     if k-key in sum2count:
    #         print(key, k, value)
    #         result += value
    print(result)
    return result

subarraySum([1,1,1],2)