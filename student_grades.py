class StudentsGrades:
    from sorting import bubble_sort
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

    def get_sorted(self):
        scores = self.scores.copy()
        dylka = len(self.scores)
        for ukl in range(dylka):
            for hled in range(0, dylka - ukl - 1):
                if scores[hled] > scores[hled + 1]:
                    scores[hled], scores[hled + 1] = scores[hled + 1], scores[hled]
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print((f"Test psalo {results.count()} studentu."))
    for i, score in enumerate(results.scores):
        grade = results.get_grade(i)
        print(f"Student {i}: {score} points - {grade}")
    print(f"Studenti s plym: {results.find(100)}")
    print(f"Serazene vysledy: {results.get_sorted()}")

if __name__ == '__main__':
    main()
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
