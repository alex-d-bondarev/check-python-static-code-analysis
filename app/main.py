from datetime import date

from examples.simple_calculator import calc
from examples.naming import week_day_in_a_month, is_in_range


def run():
    print("Try running different ugly examples")
    week_day_in_a_month()
    is_in_range(d1=date.fromisoformat('2021-06-11'),
                d2=date.fromisoformat('2021-12-31'),
                include="second")
    calc("1 + 2 + 3 + 4 - 5 - 6 + 7 - 8", True)


if __name__ == "__main__":
    run()
