def searchRange(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return[0, 0]

    for i in range(len(nums)):
        lp = i
        rp = len(nums) - 1 - i

        if nums[rp] == target:
            n_right = rp
            while (nums[rp] == target):
                rp -= 1
                if rp < 0:
                    break
            return [rp + 1, n_right]
        elif nums[lp] == target:
            n_left = lp
            while (nums[lp] == target):
                lp += 1
                if lp > len(nums) - 1:
                    break
            return [n_left, lp - 1]

    return [-1, -1]

if __name__ == '__main__':
    nums = [2,2]
    target = 2
    print(searchRange(nums, target))
        