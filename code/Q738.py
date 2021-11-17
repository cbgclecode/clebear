""" # description
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10

输出: 9



示例 2:

输入: N = 1234

输出: 1234



示例 3:

输入: N = 332

输出: 299



说明: N 是在 [0, 10^9] 范围内的一个整数。


"""

""" # code demo
class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
"""

""" # summary

"""

_question_id = 738
_question__title = "Monotone Increasing Digits"
_question__title_slug = "monotone-increasing-digits"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/monotone-increasing-digits"


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method(10) == 9
    assert method(1234) == 1234
    assert method(332) == 299
    print("Test ok.")
    pass


class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
        strN = list(str(n))
        i = 1
        len_str = len(strN)
        while i < len_str and strN[i - 1] <= strN[i]:
            i += 1
        if i < len_str:
            while i > 0 and strN[i - 1] > strN[i]:
                strN[i - 1] = str(int(strN[i - 1]) - 1)
                i -= 1
            i += 1
            while i < len_str:
                strN[i] = "9"
                i += 1
        return int("".join(strN))


if __name__ == "__main__":
    judge(Solution, "monotoneIncreasingDigits")
    pass
