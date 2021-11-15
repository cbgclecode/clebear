""" # description
数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：

将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。

最开始的时候，同一位置上也可能放着两个或者更多的筹码。
返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
 
示例 1：
输入：chips = [1,2,3]
输出：1
解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。

示例 2：
输入：chips = [2,2,2,3,3]
输出：2
解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。

 
提示：

1 <= chips.length <= 100
1 <= chips[i] <= 10^9


"""

""" # code demo
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
"""

""" # summary

"""

_question_id = 1329
_question__title = "Minimum Cost to Move Chips to The Same Position"
_question__title_slug = "minimum-cost-to-move-chips-to-the-same-position"
_difficulty_level = "1"
_question_url = "https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([1, 2, 3]) == 1
    assert method([2, 2, 2, 3, 3]) == 2
    pass


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


# 作者：Athenahe126
# 链接：https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/solution/xian-li-jie-ti-yi-zai-li-jie-dai-ma-si-lu-by-athen/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "minCostToMoveChips")
    pass
