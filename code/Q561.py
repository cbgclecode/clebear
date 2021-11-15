""" # description
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
返回该 最大总和 。
 
示例 1：

输入：nums = [1,4,3,2]
输出：4
解释：所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4
示例 2：

输入：nums = [6,2,6,5,1,2]
输出：9
解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9

 
提示：

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104


"""

""" # code demo
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
"""

""" # summary

"""

_question_id = 561
_question__title = "Array Partition I"
_question__title_slug = "array-partition-i"
_difficulty_level = "1"
_question_url = "https://leetcode-cn.com/problems/array-partition-i"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([1, 4, 3, 2]) == 4
    assert method([6, 2, 6, 5, 1, 2]) == 9
    pass


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# 作者：MGA_Bronya
# 链接：https://leetcode-cn.com/problems/array-partition-i/solution/561-shu-zu-chai-fen-i-jian-dan-tan-xin-b-zl6f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    judge(Solution, "arrayPairSum")
    pass
