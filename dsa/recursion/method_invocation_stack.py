def main():
    bar()
    print("i ma main")


def bar():
    dowork()
    print("i am bar")


def dowork():
    dowork()
    print("i am do work")


def domore():
    main()
    print("i am domore")


domore()
