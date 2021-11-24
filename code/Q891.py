""" # description
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 





示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]

输出：39

解释：

转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]

0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

 

提示：



1 <= A.length <= 20

1 <= A[0].length <= 20

A[i][j] 是 0 或 1




"""

""" # code demo
class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
"""

""" # summary

"""

_question_id = 891
_question__title = "Score After Flipping Matrix"
_question__title_slug = "score-after-flipping-matrix"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/score-after-flipping-matrix"

from typing import List


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
    print(f"Test ok.")
    pass


class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = m * (1 << (n - 1))

        for j in range(1, n):
            n_ones = 0
            for i in range(m):
                if grid[i][0]:
                    n_ones += grid[i][j]
                else:
                    n_ones += 1 - grid[i][j]
            k = max(n_ones, m - n_ones)
            ret += k * (1 << n - j - 1)
        return ret


if __name__ == "__main__":
    judge(Solution, "matrixScore")
    pass
