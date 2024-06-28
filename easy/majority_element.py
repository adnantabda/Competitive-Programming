# num = [3, 2, 3]
# frequency = [0 for i in range(0, len(num) + 1)]
# print(frequency)


def majority(nums):
    frequency_ = [0 for i in range(0, max(nums) + 1)]
    for i in nums:
        frequency_[i] = frequency_[i] + 1

    return frequency_.index(max(frequency_))


def majority2(nums):
    list_ = []
    for i in nums:
        fre = nums.count(i)
        list_.append(fre)
    maximum = max(list_)
    index_ = list_.index(maximum)
    return nums[index_]


def majorityElement(self, nums) -> int:
    list_ = [nums.count(i) for i in nums]
    index_ = list_.index(max(list_))
    return nums[index_]

def majority3(nums):
    dict = {}
    for i in nums:
        if i in dict:
            pass
        else:
            dict[f"{i}"] = 0
    for i in nums:
        if f"{i}" in dict.keys():
            dict[f"{i}"] = dict[f"{i}"] + 1
    item = []
    frequency = []
    for k, v in dict.items():
        item.append(int(k))
        frequency.append(v)

    return item[frequency.index(max(frequency))]


nums_ = [3, 2, 3]
print(majority3(nums_))


