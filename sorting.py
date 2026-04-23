import random
import matplotlib.pyplot as plt
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
random.seed(42)
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
#n = n/2
#1 +
def selection_sort(values):
    seznam = values.copy()
    delka = len(values) #1
    for pozice_ukl in range(delka):#n
        pozice_min = pozice_ukl #n
        for pozice_prohl in range(pozice_min + 1, delka): #n/2
            if seznam[pozice_min] > seznam[pozice_prohl]: #n/2
                pozice_min = pozice_prohl  #n/2   0
        seznam[pozice_ukl], seznam[pozice_min] = seznam[pozice_min], seznam[pozice_ukl] #n
    return seznam



def bubble_sort(numbers):
    bubliki = numbers.copy()
    dylka = len(numbers)
    plt.ion()
    plt.show()
    for ukl in range(dylka):
        for hled in range(0, dylka - ukl -1):
            if bubliki[hled] > bubliki[hled + 1]:
                bubliki[hled], bubliki[hled + 1] = bubliki[hled + 1], bubliki[hled]
            index_highlight1 = hled
            index_highlight2 = hled + 1
            colors = ["steelblue"] * dylka
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(dylka), bubliki, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return bubliki




def main():
    seznamek = [5,3,8,4,2]
    serazeno = selection_sort(seznamek)

    nahodne = random_numbers(20)
    serazeno_nah = selection_sort(nahodne)

if __name__ == "__main__":
    test = random_numbers(10)
    bubble_sort(test)


