# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import Prob1
import Prob2


class Test_Prob1:
    def test_PartA_returns_list_of_desired_length(self):
        imaxes = [10, 26, 8]
        for i in imaxes:
            student = Prob1.create_histogram_array(i,[1,2,3])
            assert len(student) == i, f"You are not returning a list of the proper length. An imax of {i} is giving a list of length {len(student)}."

    def test_PartA_returns_correct_counts(self):
        data = [
            (10,[3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]),
            (2, [1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1]),
            (20,[i % 20 for i in range(56)]),
            (10,[8,8,8,8,8,8,8]),
        ]
        sols = [
            [0,2,1,2,1,4,1,1,1,3],
            [11,11],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
            [0,0,0,0,0,0,0,0,7,0],
        ]
        for i,o in zip(data, sols):
            student = Prob1.create_histogram_array(*i)
            assert student == o, f"Your histograms do not match. create_histogram_array{i} should give {o} but is instead giving {student}."

    def test_PartA_counts_consistant_with_input(self):
        data = [
            (10,[3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]),
            (2, [1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1]),
            (20,[i % 20 for i in range(56)]),
            (10,[8,8,8,8,8,8,8]),
        ]
        for i in data:
            student = Prob1.create_histogram_array(*i)
            assert sum(student) == len(i[1]), "The sum of all the elements in your histogram array should be equal to the original number of elements in the data list!"

    def test_PartB_returns_nothing(self):
        h = [2,4,6,8,1,3,7,2,9,4]
        student = Prob1.print_histogram(h)
        assert student is None, "print_histogram should only print, not return anything!"

    def test_PartB_lines_start_with_digit(self, capsys):
        h = [2,4,6,8,1,3,7,2,9,4]
        Prob1.print_histogram(h)
        captured = capsys.readouterr().out.splitlines()
        for i,line in enumerate(captured):
            assert line[0].isdigit(), "Each line of your printout should start with a number!"
            assert line[0] == str(i), "Your numbering pattern should start at 0 and count up!"

    def test_PartB_line_have_cor_num_stars(self, capsys):
        h = [2,4,6,8,1,3,7,2,9,4]
        Prob1.print_histogram(h)
        captured = capsys.readouterr().out.splitlines()
        for i,(line,c) in enumerate(zip(captured, h)):
            assert line.count('*') == c, f"For a histogram array of {h}, you should have {h[i]} stars in the {i}th line, but you seem to have only {line.count('*')}."

class Test_Prob2:
    def test_returns_boolean(self):
        sq2 = [[8,1,6],[3,5,7],[4,9,2]]
        assert isinstance(Prob2.is_magic_square(sq2), bool), "You should be returning a boolean, and you are not?"

    def test_correct_squares(self):
        sq1 = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
        sq2 = [[8,1,6],[3,5,7],[4,9,2]]
        sq3 = [[1,23,16,4,21],[15,14,7,18,11],[24,17,13,9,2],[20,8,19,12,6],[5,3,10,22,25]]
        sq4 = [[18,11,16],[13,15,17],[14,19,12]]
        for sq in [sq1, sq2, sq3, sq4]:
            assert Prob2.is_magic_square(sq), f"The square {sq} is a magic square but your function says it is not!"

    def test_incorrect_squares(self):
        sq1 = [[1,2,3],[4,5,6],[7,8,9]]
        sq2 = [[8,1,6,10],[3,5,7,11],[4,9,2,12]]
        sq3 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        for sq in [sq1, sq2, sq3]:
            assert not Prob2.is_magic_square(sq), f"The square {sq} is not a magic square but your function says it is!"
