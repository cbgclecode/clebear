""" # description
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：



输入：nums = [-2,1,-3,4,-1,2,1,-5,4]

输出：6

解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。



示例 2：



输入：nums = [1]

输出：1



示例 3：



输入：nums = [0]

输出：0



示例 4：



输入：nums = [-1]

输出：-1



示例 5：



输入：nums = [-100000]

输出：-100000



 

提示：



1 <= nums.length <= 3 * 104

-105 <= nums[i] <= 105



 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


"""

""" # code demo
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
"""

""" # summary

"""

_question_id = 53
_question__title = "Maximum Subarray"
_question__title_slug = "maximum-subarray"
_difficulty_level = "1"
_question_url = "https://leetcode-cn.com/problems/maximum-subarray"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert method([1]) == 1
    assert method([0]) == 0
    assert method([-1]) == -1
    assert method([-100000]) == -100000
    pass


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 类似寻找最大最小值的题目,初始值一定要定义成理论上的最小最大值
        result = float("-inf")
        numsSize = len(nums)
        sum = 0
        for i in range(numsSize):
            sum += nums[i]
            result = max(result, sum)
            # 如果sum < 0,重新开始找子序串
            if (sum < 0):
                sum = 0

        return result


# 作者：gu-xx-qi
# 链接：https://leetcode-cn.com/problems/maximum-subarray/solution/si-wei-dao-tu-zheng-li-3chong-fang-fa-ch-zxih/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "maxSubArray")
    pass
