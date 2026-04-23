class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

# grades = StudentsGrades([10,25,60,55,99])
# print(grades.scores)
# results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

# print(results.count())          # 9
# print(results.get_by_index(2))  # 91
# print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        elif score >= 50:
            return 'E'
        else:
            return 'F'

    def find(self, hledany):
        seznamek = []
        delcicka = len(self.scores)
        for i in range(delcicka):
            if self.scores[i] == hledany:
                seznamek.append(i)
        return seznamek


if __name__ == '__main__':
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

