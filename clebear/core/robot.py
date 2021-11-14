import json
import os
import re
import io
import inspect
import time

import tqdm
import glob
import pandas as pd
from clebear.configs import cfg
from clebear.core.utils import load_module


def judge(solution=None, method=None, io_equal=None):
    method = getattr(solution(), method)
    pass


class Question(object):

    def __init__(self):
        self.question_id = None
        self.question__title = None
        self.question__title_slug = None
        self.difficulty_level = None
        self.question_url = None

        self.py_description = '""" # description\n\n"""'
        self.code_demo = ''
        self.py_summary = '""" # summary\n\n"""'
        self.imports = list()
        self.if_main_str = f'\n\nif __name__=="__main__":\n    pass'

    def load_from_py(self, path):
        with open(path, 'r', encoding="utf8") as f:
            data = f.read()

        self.py_description = re.findall(r'"""\s#\sdescription.*?"""', data, re.DOTALL)[0].strip() + "\n"

        self.code_demo = re.findall(r'"""\s#\scode\sdemo(.*?)"""', data, re.DOTALL)[0].strip() + "\n"

        self.py_summary = re.findall(r'"""\s*#\s*summary.*?"""', data, re.DOTALL)[0]
        module = load_module(path)

        self.question_id = getattr(module, "_question_id", "")
        self.question__title = getattr(module, "_question__title", "")
        self.question__title = getattr(module, "_question__title_slug", "")
        self.difficulty_level = getattr(module, "_difficulty_level", "")
        self.question_url = getattr(module, "_question_url", "")

        self.imports += re.findall(r'[\n]import.*', data)
        self.imports += re.findall(r'from.*', data)

        # re.findall(r'(class\sSolution.*:.*\n)[a-zA-Z]', data, re.DOTALL)

        self.if_main_str = re.findall(r'[\n]if\s__name__.*', data, re.DOTALL)[0].strip() + "\n"

    def dump2py(self, path, add_judge=False):
        st = ""
        st += self.py_description
        st += "\n\n"
        st += f'""" # code demo\n{self.code_demo}\n"""\n'
        st += "\n"
        st += self.py_summary
        st += "\n\n"
        st += f'_question_id={self.question_id}\n'
        st += f'_question__title="{self.question__title}"\n'
        st += f'_question__title_slug="{self.question__title_slug}"\n'
        st += f'_difficulty_level="{self.difficulty_level}"\n'
        st += f'_question_url="{self.question_url}"'
        st += "\n\n"
        if self.code_demo:
            if "List" in str(self.code_demo):
                self.imports.append("from typing import List")
        for i in self.imports:
            st += f'{i}\n'

        if add_judge:
            st += f"\n{inspect.getsource(judge)}\n"

        st += f'{self.code_demo}        \n        pass' if self.code_demo and isinstance(self.code_demo, str) else ""

        st += "\n"
        st += self.if_main_str

        with open(path, "w", encoding="utf8") as f:
            f.write(st)

    def load_from_json(self, path):
        pass

    def dump2json(self, path):
        pass

    def load_from_dict(self, data):
        """
        {
            "stat": {
                "question_id": 115,
                "question__title": "Distinct Subsequences",
                "question__title_slug": "distinct-subsequences",
                "question__hide": false,
                "total_acs": 63560,
                "total_submitted": 121829,
                "total_column_articles": 695,
                "frontend_question_id": "115",
                "is_new_question": false
            },
            "status": null,
            "difficulty": {
                "level": 3
            },
            "paid_only": false,
            "is_favor": false,
            "frequency": 0,
            "progress": 0
        }
        """
        self.question_id = data["stat"]["question_id"]
        self.question__title = data["stat"]["question__title"]
        self.question__title_slug = data["stat"]["question__title_slug"]
        self.difficulty_level = data["difficulty"]["level"]
        self.question_url = "https://leetcode-cn.com/problems/" + data["stat"]["question__title_slug"]

        df = pd.read_csv(cfg.PATH_ALL_CSV)
        if any(df.question_id == self.question_id):
            d = df[df.question_id == self.question_id].iloc[0]
            self.py_description = f'""" # description\n{d.translatedContent}\n"""'
            self.code_demo = d.codeSnippets_python3

    def __repr__(self):
        return ''

    @staticmethod
    def create_py(query, save=None):
        """
        :query: question_id or question__title_slug
        """
        with open(cfg.PATH_PROBLEMS_JSON, "r") as f:
            data = json.load(f)

        for d in data["stat_status_pairs"]:
            if (d["stat"]["question_id"] == query
                    or str(d["stat"]["question__title_slug"]) == query):
                que = Question()
                que.load_from_dict(d)
                if save is None:
                    save = os.path.join(cfg.PATH_CODE, f"Q{d['stat']['question_id']}.py")
                    assert not os.path.exists(save), f"exists file: {save}"

                    que.dump2py(save, add_judge=True)
                    return True
                elif save:
                    que.dump2py(save, add_judge=True)
                    return True
                else:
                    return que
        return False

    @staticmethod
    def copy_py(query):
        if isinstance(query, int):
            query = f"Q{query}"
        with open(cfg.PATH_PROBLEMS_JSON, "r") as f:
            data = json.load(f)
        code_list = glob.glob(os.path.join(cfg.PATH_CODE, "**.py"), recursive=True)
        code_list_str = ""
        code_list_str = "".join([os.path.basename(os.path.splitext(p)[0]) for p in code_list])
        path = None
        question_id = None
        if query in code_list_str:
            path = os.path.join(cfg.PATH_CODE, f"{query}.py")
            question_id = query.lstrip("Q")
            question_id = int(question_id) if question_id.isdigit() else question_id
        else:
            for d in data["stat_status_pairs"]:
                if ((d["stat"]["question_id"] == query
                     or str(d["stat"]["question__title_slug"]) == query)
                        and f"Q{d['stat']['question_id']}" in code_list_str
                ):
                    path = os.path.join(cfg.PATH_CODE, f"Q{d['stat']['question_id']}.py")
                    question_id = d['stat']['question_id']
        if path:
            return Question.copy_py_path(path, question_id=question_id)

        return False

    @staticmethod
    def copy_py_path(path, question_id=None):
        if question_id is None:
            question_id = os.path.basename(os.path.splitext(path)[0])
        que = Question()
        que.load_from_py(path)
        que.imports.append(f'from clebear.core.utils import load_module')
        que.imports.append(f'\njudge=load_module(f"{path}").judge\n')
        que.dump2py(os.path.join(cfg.PATH_CODE_PRACTICE,
                                 f"P{question_id}-{time.strftime('%Y%m%d-%H%M%S')}.py"))
        return True


if __name__ == '__main__123':
    data = {
        "stat": {
            "question_id": 115,
            "question__title": "Distinct Subsequences",
            "question__title_slug": "distinct-subsequences",
            "question__hide": False,
            "total_acs": 63560,
            "total_submitted": 121829,
            "total_column_articles": 695,
            "frontend_question_id": "115",
            "is_new_question": False
        },
        "status": False,
        "difficulty": {
            "level": 3
        },
        "paid_only": False,
        "is_favor": False,
        "frequency": 0,
        "progress": 0
    }
    a = Question()
    a.load_from_dict(data)
    a.dump2py("./demo-dict2py.py")

if __name__ == '__main__123':
    a = Question()
    a.load_from_py(
        r"D:\Prog\hello_group\ccode\ccode\code\sort02.py"
    )
    a.dump2py(r"D:\Prog\hello_group\ccode\gTest\tt02.py")

if __name__ == '__main__as':
    # Question.create_py(123, r"D:\Prog\hello_group\ccode\gTest\tt03.py")
    # Question.create_py(123)

    with tqdm.tqdm(range(2000)[:15]) as pbar:
        for i in pbar:
            pbar.set_description_str("hello")
            pbar.set_postfix_str(f"id={i}")
            if Question.create_py(i):
                pass
            else:
                print(f"False: id={i}")

if __name__ == '__main__':
    # print(Question.create_py(15))
    # print(Question.copy_py(15))

    # print(Question.create_py("3sum"))
    # print(Question.copy_py("3sum"))

    print(Question.create_py(2))
    print(Question.copy_py(1))
"""
# 增加一个新的code文件，
Question.create_py(1)
Question.create_py("two-sum")

# 增加一个新的练习文件  
Question.copy_py(query)

# 直接使用code名称转到code-practice
Question.copy_py("QM01")

"""
