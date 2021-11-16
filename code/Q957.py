""" # description
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：



它是一个空字符串，或者

它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者

它可以被写作 (A)，其中 A 是有效字符串。



给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

 

示例 1：

输入："())"

输出：1



示例 2：

输入："((("

输出：3



示例 3：

输入："()"

输出：0



示例 4：

输入："()))(("

输出：4

 

提示：



S.length <= 1000

S 只包含 '(' 和 ')' 字符。



 


"""

""" # code demo
class Solution:

    def minAddToMakeValid(self, s: str) -> int:
"""

""" # summary

"""

_question_id = 957
_question__title = "Minimum Add to Make Parentheses Valid"
_question__title_slug = "minimum-add-to-make-parentheses-valid"
_difficulty_level = "2"
_question_url = "https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid"


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    assert method("())") == 1
    assert method("(((") == 3
    assert method("()") == 0
    assert method("()))((") == 4
    pass


class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for symbol in s:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/solution/shi-gua-hao-you-xiao-de-zui-shao-tian-jia-by-leetc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    judge(Solution, "minAddToMakeValid")
    pass
