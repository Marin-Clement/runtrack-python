def round_grade(grade):
    if grade <= 40:
        return grade
    else:
        grade_s = [int(a) for a in str(grade)]
        if grade_s[1] in range(3, 5):
            grade_s[1] = 5
            return int(''.join(map(str, [grade_s[0], grade_s[1]])))
        elif grade_s[1] in range(8, 10):
            grade_s[1] = 0
            grade_s[0] += 1
            return int(''.join(map(str, [grade_s[0], grade_s[1]])))
        else:
            return grade


print(round_grade(42))
print(round_grade(43))
print(round_grade(44))
print(round_grade(47))
print(round_grade(48))
print(round_grade(49))