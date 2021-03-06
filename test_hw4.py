# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
import os

from Prob2 import to_obenglobish
from Prob3 import encrypt

class Test_Prob2:
    def test_returns_string(self):
        student = to_obenglobish("english")
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_easy_vowels(self):
        words = ["english", "fish", "panda"]
        sols = ["obenglobish", "fobish", "pobandoba"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_repeat_vowels(self):
        words = ["gooiest", "fruit", "books"]
        sols = ["gobooiest", "frobuit", "bobooks"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_ending_ees(self):
        words = ["amaze", "apple", "eerie"]
        sols = ["obamobaze", "obapple", "obeerobie"]
        for w,s in zip(words, sols):
            student = to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

class Test_Prob3:
    KEY = "pyfgcrlaoeuidhtnsqjkxbmwvz"
    def test_returns_string(self):
        student = encrypt("english", self.KEY)
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_basic_substitutions(self):
        msgs = ["hello", "fishsticks", "papaya"]
        sols = ["aciit", "rojajkofuj", "npnpvp"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} but should have been {s}."

    def test_non_alphabetic_characters(self):
        msgs = ["hello!", "fishsticks and food", "I'm here now!"]
        sols = ["aciit!", "rojajkofuj phg rttg", "O'd acqc htm!"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} but should have been {s}."

    def test_capitalization(self):
        msgs = ["Hello!", "Fishsticks and FooD", "I'm here NOW!"]
        sols = ["Aciit!", "Rojajkofuj phg RttG", "O'd acqc HTM!"]
        for w,s in zip(msgs, sols):
            student = encrypt(w, self.KEY)
            assert student == s, f"{w} encrypted to {student} but should have been {s}."
