from time import sleep
import os


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

    for _ in range(cycles):
        print("-" * 65)
        print(
            f"Work Time: {work_time} seconds 💻 | Rest Time: {rest_time} seconds 💤| Cycle: {_ + 1} 🔁"
        )
        print("-" * 65)
        print("Currently working... 💻")
        print(f"Time remaining: {countdown_timer(work_time)}")
        os.system("clear")
        print("-" * 65)
        print("Time to rest! 💤")
        print(f"Time remaining: {countdown_timer(rest_time)}")
        os.system("clear")

    print("\033[1;32mCongratulations! You have completed your job! 🎉\033[0m")


def countdown_timer(seconds):
    while seconds:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
        sleep(1)
        seconds -= 1


def spawn_pomodoro():
    print("-" * 65)
    work_time = int(input("Working time in seconds: "))
    rest_time = int(input("Resting time in seconds: "))
    cycles = int(input("How many cycles should we do?: "))

    pomodoro_timer(work_time, rest_time, cycles)


def main():
    spawn_pomodoro()


if __name__ == "__main__":
    main()
