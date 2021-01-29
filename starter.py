#!/usr/bin/env python3


"""
 Python app that does 7 - boom up to user specified int, 
 made for devops experts class 7 hw as a throw-away starter python
 file to upload to github.

 because this py file IS NOT the main thing for the HW assignment,
 PEP8 guidelines may not be, uh, implemented. Sorry!

                                                
        2021© whitehawk2
        no rights reserved™
"""

def main():
    limiter = 0
    while True:
        try:
            limiter = int(input('enter int as limit to 7 boom upto:\n->\t'))
            if limiter > 0:
                break

            else:
                print('negetive ints made positive by the power of sunlight')
                limiter *= -1
                break

        except TypeError:
            print('not a valid input! try again thx\n\n')
            continue

        except ValueError:
            print('not a valid input! try again thx\n\n')
            continue

    b_list = ["BOOM" if x % 7 == 0 or str(x).count("7") > 0 else x
        for x in range(1, limiter +1 )]

    print(*b_list, sep=", ")


if __name__ == '__main__':
    main()

