import os

__all__ = [
    "io_map_equal_normal",
]


def io_map_equal_normal(inputs, output) -> bool:
    return inputs == output


def io_map_same_element_equal(inputs, output) -> bool:
    if len(inputs) != len(output):
        return False
    for i in inputs:
        if i in output:
            output.remove(i)
        else:
            return False
    return True
