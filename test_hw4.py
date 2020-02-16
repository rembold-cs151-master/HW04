# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os
import random
import math

import Prob2

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW4.pdf') == True


class Test_Prob2:
    ep = 0.001

    def f(self,x,A):
        return (x-1)**A - A*math.cos(x/A)

    def df(self,x,A):
        return A*(x-1)**(A-1) + math.sin(x/A)

    def report(self,g,A):
        return f"\nProgram fails to get needed accuracy with a guess of {g}\n" + \
                    f"and a provided value of {A} for A.\n "

    def test_guess_1(self):
        student = Prob2.eqn_solver(1)
        assert abs(self.f(student,2)) < self.ep, self.report(1,None)

    def test_guess_1_2(self):
        student = Prob2.eqn_solver(1,2)
        assert abs(self.f(student,2)) < self.ep, self.report(1,2)

    def test_guess_2_3(self):
        student = Prob2.eqn_solver(2,3)
        assert abs(self.f(student,3)) < self.ep, self.report(2,3)

    def test_guess_n2_3(self):
        student = Prob2.eqn_solver(-2,3)
        assert abs(self.f(student,3)) < self.ep, self.report(-2,3)

    def test_guess_100_4(self):
        student = Prob2.eqn_solver(100,4)
        assert abs(self.f(student,4)) < self.ep, self.report(100,4)

    def test_guess_n100_4(self):
        student = Prob2.eqn_solver(-100,4)
        assert abs(self.f(student,4)) < self.ep, self.report(-100,4)


class Test_Prob3:
    def test_used_while_loop(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert filestr.count('def') >= 5, '\nIt does not look like you defined enough new object functions? You should have at least 3 in addition to the functions I already had defined for you.'
