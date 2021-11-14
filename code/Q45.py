""" # description
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
 
示例 1:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:

输入: [2,3,0,1,4]
输出: 2

 
提示:

1 <= nums.length <= 1000
0 <= nums[i] <= 105


"""

""" # code demo
class Solution:
    def jump(self, nums: List[int]) -> int:
"""

""" # summary

"""

_question_id = 45
_question__title = "Jump Game II"
_question__title_slug = "jump-game-ii"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/jump-game-ii"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([2, 3, 1, 1, 4]) == 2
    assert method([2, 3, 0, 1, 4]) == 2


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "jump")
    pass
