import threading


def run_again():
    threading.Timer(5.0, run_again).start()
    print("Run! Run! Run!")


run_again()
