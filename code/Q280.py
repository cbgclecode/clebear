""" # description
给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。

示例:

输入: nums = [3,5,2,1,6,4]

输出: 一个可能的解答是 [3,5,1,6,2,4]


"""

''' # code demo
class Solution:

    def wiggleSort(self, nums: List[int]) -> None:

        """

        Do not return anything, modify nums in-place instead.

        """
'''

""" # summary

"""

_question_id = 280
_question__title = "Wiggle Sort"
_question__title_slug = "wiggle-sort"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/wiggle-sort"

from typing import List

# todo: 写测试程序

def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)

    pass


class Solution:

    def wiggleSort(self, nums: List[int]) -> None:

        """

        Do not return anything, modify nums in-place instead.

        """
        n = len(nums)
        for i in range(n - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


# 作者：Hanxin_Hanxin
# 链接：https://leetcode-cn.com/problems/wiggle-sort/solution/c-python3-cong-zuo-wang-you-yi-ci-bian-l-gcqi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "wiggleSort")
    pass
