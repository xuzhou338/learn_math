from unittest import TestCase, main
from roll_die_possibility import find_prob


class TestFind_prob(TestCase):
    def test_less_than_6_1(self):
        p = find_prob(1, 6)
        self.assertEqual(p, 1)

    def test_less_than_6_2(self):
        p = find_prob(5, 1)
        self.assertEqual(p, 1/3)

    def test_greater_than_6(self):
        p = find_prob(10, 5)
        self.assertLess(p, 1)

if __name__ == '__main__':
    main()
