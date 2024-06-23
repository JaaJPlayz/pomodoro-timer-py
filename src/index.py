from time import sleep


def pomodoro_timer(work_time, rest_time, cycles) -> None:
    """
    Simple pomodoro timer.

    :param work_time: working time in seconds
    :param rest_time: resting time in seconds
    :param cycles: number of cycles

    :type work_time: int
    :type rest_time: int
    :type cycles: int

    :return: None
    """

    if work_time is None or rest_time is None:
        raise ValueError("Either working time or sleeping time not provided!")

    if cycles is None or cycles < 1:
        raise ValueError(
            "The amount of cycles must \
            be provided and be 1 or more!"
        )

    if work_time < 1 or rest_time < 1:
        raise ValueError(
            """Working time and sleeping time should 
            have the value of 1 or bigger!"""
        )

    iter = 0
    while True:
        if iter == 0:
            print("-" * 50)
            print("\033[1;32mStarting working time! 💻\033[m")

        sleep(work_time)
        print("\033[1;35mWorking time over! Time to rest! 💤\033[m")
        print("-" * 50)

        if iter + 1 == cycles:
            print("\033[1;36mSessions over. Good Job! 👍\033[m")
            break

        sleep(rest_time)
        print("\033[1;31mResting time over! Time to work! 💻\033[m")

        iter += 1


def main():
    print("-" * 50)
    work_time = int(input("Working time in seconds: "))
    rest_time = int(input("Resting time in seconds: "))
    cycles = int(input("How many cycles should we do?: "))

    pomodoro_timer(work_time, rest_time, cycles)


if __name__ == "__main__":
    main()
