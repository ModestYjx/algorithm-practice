import copy


class Solution:

    def quickSort(self, nums, left, right, key):
        pivotElement = nums[key]
        while left < right:
            while right > 0 and nums[right] > pivotElement:
                right = right - 1

            while left < len(nums) - 1 and nums[left] <= pivotElement:
                left = left + 1
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp

            key = right
            pivotElement = nums[key]
            self.quickSort(copy.deepcopy(nums), left, key, left)
            self.quickSort(copy.deepcopy(nums), key, right, key)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     len_of_nums = len(nums)
    #     nums = [1, 2, 3]
    #     self.quickSort(nums, 0, len_of_nums - 1, 0)


def main():
    solution = Solution()
    nums = [6, 4, 1, 2, 3]
    nums = list(nums)
    len_of_nums = len(nums)
    # python中不存在所谓的传值调用, 一切传递的都是对象的引用, 也可以认为是传址。 python list 传值不传址
    # c,c++与python的不同就体现出来了
    solution.quickSort(copy.deepcopy(nums), 0, len_of_nums - 1, 0)
    print(nums[0])


if __name__ == '__main__':
    main()
