from matplotlib import pyplot as plt
from find_correlation import find_corr_x_y
import numpy as np

high_school_grades = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
college_admission_test_score = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

plt. figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(high_school_grades, college_admission_test_score, label='data')
plt.xlabel("High School Grades")
plt.ylabel("College Admission Test Score")
plt.title("College Admission Test Score vs. High School Grades")

correlation_coefficient = find_corr_x_y(high_school_grades,
                                college_admission_test_score)
print("The correlation coefficient is {0:.4f}.".format(correlation_coefficient))

c1 = np.polyfit(high_school_grades, college_admission_test_score, 1)
x = np.arange(min(high_school_grades), max(high_school_grades)+1)
y = x*c1[0] + c1[1]

plt.plot(x, y, c='red', label='best fit line')
plt.legend(loc='best')

high_school_grades_1 = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
college_admission_test_score_1 = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

plt.subplot(1, 2, 2)
plt.scatter(high_school_grades_1, college_admission_test_score_1, marker="+",
            label='data')
plt.xlabel("High School Grades2")
plt.ylabel("College Admission Test Score2")
plt.title("College Admission Test Score vs. High School Grades2")

correlation_coefficient1 = find_corr_x_y(high_school_grades_1,
                                         college_admission_test_score_1)
print("The correlation coefficient1 is {0:.4f}.".format(
    correlation_coefficient1))

c2 = np.polyfit(high_school_grades_1, college_admission_test_score_1, 1)
x1 = np.arange(min(high_school_grades_1), max(high_school_grades_1)+1)
y1 = x1*c2[0] + c2[1]

plt.plot(x1, y1, c='purple', label='best fit line')
plt.legend()

plt.show()