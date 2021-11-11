""" # description
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。
 

示例 1：

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
示例 2：

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4

示例 3：

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2

示例 4：

输入：points = [[1,2]]
输出：1

示例 5：

输入：points = [[2,3],[2,3]]
输出：1

 
提示：

0 <= points.length <= 104
points[i].length == 2
-231 <= xstart end <= 231 - 1


"""

""" # code demo
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
"""

""" # summary

"""

_question_id = 452
_question__title = "Minimum Number of Arrows to Burst Balloons"
_question__title_slug = "minimum-number-of-arrows-to-burst-balloons"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert method([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert method([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert method([[1, 2]]) == 1
    assert method([[2, 3], [2, 3]]) == 1
    print(f"Test ok")


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/yong-zui-shao-shu-liang-de-jian-yin-bao-qi-qiu-1-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "findMinArrowShots")
    pass
