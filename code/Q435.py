""" # description
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。


"""

""" # code demo
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
"""

""" # summary

"""

_question_id = 435
_question__title = "Non-overlapping Intervals"
_question__title_slug = "non-overlapping-intervals"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/non-overlapping-intervals"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    assert getattr(solution(), method)([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert getattr(solution(), method)([[1, 2], [1, 2], [1, 2]]) == 2
    assert getattr(solution(), method)([[1, 2], [2, 3]]) == 0


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return n - ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-by-leetcode-solutio-cpsb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "eraseOverlapIntervals")
