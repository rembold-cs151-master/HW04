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
import Prob3

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
    def test_status1(self):
        student = Prob3.generate_status('fish','ih')
        actual = '_i_h'
        assert student == actual, 'Incorrect status line returned'

    def test_status2(self):
        student = Prob3.generate_status('zebra','ebr')
        actual = '_ebr_'
        assert student == actual, 'Incorrect status line returned'

    def test_remain_guesses1(self):
        student = Prob3.remaining_guesses(7, 'a', 'abc')
        actual = 7
        assert student == actual, 'Remaining guesses should have remained constant'

    def test_remain_guesses2(self):
        student = Prob3.remaining_guesses(7, 'd', 'abc')
        actual = 6
        assert student == actual, 'Remaining guesses should have remained gone down'

    def test_game_won_fish(self):
        inputs = ['f','i','s','h']
        with mock.patch('builtins.input', side_effect=inputs):
            student = Prob3.play('fish')
            actual = 'Win'
            assert student == actual, "Play doesn't return 'Win' when it should"

    def test_game_won_aardvark(self):
        inputs = ['j','a','d','v','r','k']
        with mock.patch('builtins.input', side_effect=inputs):
            student = Prob3.play('aardvark')
            actual = 'Win'
            assert student == actual, "Play doesn't return 'Win' when it should"

    def test_game_lost_pirate(self):
        inputs = ['z','o','i','u','s','n','l','b','q','m','k']
        with mock.patch('builtins.input', side_effect=inputs):
            student = Prob3.play('pirate')
            actual = 'Lose'
            assert student == actual, "Play doesn't return 'Lose' when it should"

    def test_game_lost_rock(self):
        inputs = ['z','o','i','u','s','n','l','b','q','m','k','j']
        with mock.patch('builtins.input', side_effect=inputs):
            student = Prob3.play('rock')
            actual = 'Lose'
            assert student == actual, "Play doesn't return 'Lose' when it should"

    def test_game_lost_stupid_rock(self):
        inputs = ['a']*10
        with mock.patch('builtins.input', side_effect=inputs):
            student = Prob3.play('rock')
            actual = 'Lose'
            assert student == actual, "Repeated bad guesses do not result in 'Lose' when it should"
