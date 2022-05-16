from polynomial_supscript import smap, trans
from itertools import zip_longest
from collections import deque


class Polynomial:
    """Custom Made Polynomial Class that allows you to view polynomials as you would at any school.
Only supports addition and subtraction of polynomials for now."""

    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"{self.__class__.__name__}{self.args}"

    def __str__(self):
        str_list = []
        range_list = [x[0] for x in enumerate(self.args)]
        for coeff, deg in enumerate(list(reversed(range_list))):
            if deg == 0 and self.args[coeff] > 0:
                str_list.append(f" + {self.args[coeff]}")
            elif deg == 0 and self.args[coeff] < 0:
                str_list.append(f" - {self.args[coeff]}")
            elif deg == 1 and self.args[coeff] > 0:
                str_list.append(f" + {self.args[coeff]}x")
            elif deg == 1 and self.args[coeff] < 0:
                str_list.append(f" - {self.args[coeff]}x")
            elif coeff == 0 and self.args[coeff] == 1:
                str_list.append(f"x{smap[str(deg)].translate(trans)}")
            elif coeff == 0 and self.args[coeff] == - 1:
                str_list.append(f" - x{smap[str(deg)].translate(trans)}")
            elif coeff == 0 and self.args[coeff] > 0:
                str_list.append(f"{self.args[coeff]}x{smap[str(deg)].translate(trans)}")
            elif coeff == 0 and self.args[coeff] < 0:
                str_list.append(f"-{self.args[coeff]}x{smap[str(deg)].translate(trans)}")
            elif deg > 0 and self.args[coeff] > 0:
                str_list.append(f" + {self.args[coeff]}x{smap[str(deg)].translate(trans)}")
            elif deg > 0 and self.args[coeff] < 0:
                str_list.append(f" - {self.args[coeff]}x{smap[str(deg)].translate(trans)}")

        return ''.join(str_list)

    def __add__(self, other):
        if type(other) is (int or float):
            self.args = list(self.args)
            self.args[-1] = self.args[-1] + other
            return Polynomial(*self.args)

        if isinstance(other, Polynomial):
            shift_to_self = False
            shift_to_other = False
            new_list = []
            if self.args > other.args:
                self.shift_factor = len(self.args) - len(other.args)
                shift_to_other = True
            else:
                self.shift_factor = len(other.args) - len(self.args)
                shift_to_self = True
            zippy = zip_longest(self.args, other.args, fillvalue=0)
            self_arg = zip(*zippy)
            self_arg = list(self_arg)
            other_arg = list(self_arg[1])
            self_arg = list(self_arg[0])
            if shift_to_other:
                other_arg = deque(other_arg)
                other_arg.rotate(self.shift_factor)
                other_arg = list(other_arg)
            elif shift_to_self:
                self_arg = deque(self_arg)
                self_arg.rotate(self.shift_factor)
                self_arg = list(self_arg)

            for a, b in zip_longest(self_arg, other_arg, fillvalue=0):
                new_list.append(a + b)
            return Polynomial(*new_list)

    def __sub__(self, other):
        if type(other) is int:
            self.args = list(self.args)
            self.args[-1] = self.args[-1] - other
            return Polynomial(*self.args)
        shift_to_self = False
        shift_to_other = False
        new_list = []
        if self.args > other.args:
            self.shift_factor = len(self.args) - len(other.args)
            shift_to_other = True
        else:
            self.shift_factor = len(other.args) - len(self.args)
            shift_to_self = True
        zippy = zip_longest(self.args, other.args, fillvalue=0)
        self_arg = zip(*zippy)
        self_arg = list(self_arg)
        other_arg = list(self_arg[1])
        self_arg = list(self_arg[0])
        if shift_to_other:
            other_arg = deque(other_arg)
            other_arg.rotate(self.shift_factor)
            other_arg = list(other_arg)
        elif shift_to_self:
            self_arg = deque(self_arg)
            self_arg.rotate(self.shift_factor)
            self_arg = list(self_arg)

        for a, b in zip_longest(self_arg, other_arg, fillvalue=0):
            new_list.append(a - b)
        return Polynomial(*new_list)

    def __mul__(self, other):
        if type(other) is (int or float):
            int_mul = []
            list_args = list(self.args)
            print(list_args)
            for x in list_args:
                int_mul.append(x * other)
            return Polynomial(*int_mul)
        return "Bruh"







