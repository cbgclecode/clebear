""" # description
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:



num 的长度小于 10002 且 ≥ k。

num 不会包含任何前导零。



示例 1 :



输入: num = "1432219", k = 3

输出: "1219"

解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。



示例 2 :



输入: num = "10200", k = 1

输出: "200"

解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。



示例 3 :



输入: num = "10", k = 2

输出: "0"

解释: 从原数字移除所有的数字，剩余为空就是0。




"""

""" # code demo
class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
"""

""" # summary

"""

_question_id = 402
_question__title = "Remove K Digits"
_question__title_slug = "remove-k-digits"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/remove-k-digits"


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method(num="1432219", k=3) == "1219"
    assert method(num="10200", k=1) == "200"
    assert method(num="10", k=2) == "0"
    print(f"Test ok.")
    pass


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/remove-k-digits/solution/yi-diao-kwei-shu-zi-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "removeKdigits")
    pass
