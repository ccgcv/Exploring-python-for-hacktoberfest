n = int(
    input("Enter the number whose Bell Number you would like to find :- ")) + 2


def bell(num):
    lst_o = [0] * num  # old list
    lst_n = [1] * num  # new list
    j, k = 0, 0

    for i in range(num):
        for j in range(i):
            if j > 0:
                lst_n[j] = lst_n[j -
                                 1] + lst_o[j -
                                            1]  # Creating the bell triangle
        lst_o = lst_n[:]  # updating the old list with the new one
        k = lst_n[0]  # Bell no
        lst_n[0] = lst_n[
            j]  # making the last varible of old list the first varible of the new list
    return k


print("The Bell Number of", n - 2, "is", bell(n))
