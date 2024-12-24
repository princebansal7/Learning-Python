def MainProgram(f):
    def program_1():
        print("1", end=' ')
        f()
        print("2")
        return program_1


def program_2():
    print("Python", end=' ')

``