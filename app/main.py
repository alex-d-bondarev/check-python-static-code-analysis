from datetime import date

from examples.naming import week_day_in_a_month, is_in_range


def run():
    print("Try running different ugly examples")
    week_day_in_a_month()
    is_in_range(d1=date.fromisoformat('2021-06-11'),
                d2=date.fromisoformat('2021-12-31'),
                include="second")


if __name__ == "__main__":
    run()
