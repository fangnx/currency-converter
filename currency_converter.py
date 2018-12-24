from get_rates import get_all_curr_types, get_rates, calculate_float
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("base", type=str, help="Type of currency converted from")
parser.add_argument("target", type=str, help="Type of currency converted to")
parser.add_argument("amount", type=float, help="Amount")


def handle_curr_type(type):
    curr_type_list = get_all_curr_types()
    return type in map(lambda x: x[0], curr_type_list)


def to_full_name(str):
    if len(str) > 3:
        return str
    for t in get_all_curr_types():
        if t[0] == str:
            return t[1]


def to_short_name(str):
    if len(str) == 3:
        return str
    for t in get_all_curr_types():
        if t[1] == str:
            return t[0]


def convert_real_time(base_curr, target_curr, amt):
    all_rates = get_rates(base_curr)
    target_rate = all_rates.get(to_full_name(target_curr))

    return calculate_float(target_rate, amt)


if __name__ == '__main__':

    args = parser.parse_args()
    if not handle_curr_type(args.base.upper()):
        print("Base currency type" + args.base.upper() + " is not supported.")
        exit()
    if not handle_curr_type(args.target.upper()):
        print("Target currency type" + args.base.upper() + " is not supported.")
        exit()

    out = convert_real_time(args.base.upper(), args.target.upper(), args.amount)
    print(out)
