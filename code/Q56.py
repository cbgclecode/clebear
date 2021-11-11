""" # description
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
 
示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 
提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


"""
from clebear.core.compare import io_map_same_element_equal

""" # code demo
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
"""

""" # summary

"""

_question_id = 56
_question__title = "Merge Intervals"
_question__title_slug = "merge-intervals"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/merge-intervals"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    io_equal = io_map_same_element_equal

    assert io_equal(method([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
    assert io_equal(method([[1, 4], [4, 5]]), [[1, 5]])


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()
        start, end = intervals[0]
        for i in intervals:
            if i[0] > end:
                ret.append([start, end])
                start = i[0]
            end = max(end, i[1])
        ret.append([start, end])
        return ret


if __name__ == "__main__":
    judge(Solution, "merge")
    pass


