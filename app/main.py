from datetime import datetime, timedelta, date


# Have a fun with this one. Thank you uncle Bob for this example
def is_in_range(d1, d2, include):
    print("Who cares about readable if statements?")
    d = date.today()
    r = False
    if (include == "both"):
        r = d1 <= d and d <= d2
    if (include == "first"):
        r = d1 <= d and d < d2
    if (include == "second"):
        r = d1 < d and d <= d2
    else:
        r = d1 < d and d < d2
    print(f"Function result is {r}. Enjoy :)")


# will this be + 31 days or the same day, but next month?
def week_day_in_a_month():
    print("Who cares about readable variable names?")
    t = datetime.today()
    d = timedelta(days=31)
    n = t + d
    print(f'A week day in a month is "{n.strftime("%A")}"')


def run():
    print("Try running different ugly examples")
    week_day_in_a_month()
    is_in_range(d1=date.fromisoformat('2021-06-11'),
                d2=date.fromisoformat('2021-12-31'),
                include="second")


if __name__ == "__main__":
    run()
