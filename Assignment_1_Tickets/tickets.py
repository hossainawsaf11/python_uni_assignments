"""CSCA08 Fall 2023 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2023 Jacqueline Smith and Anya Tafliovich.

"""

from constants import (YR, MON, DAY, DEP, ARR, ROW, SEAT, FFN,
                       WINDOW, AISLE, MIDDLE, SA, SB, SC, SD, SE, SF)

# We provide this function solution as an example of correct
# documentation, as well as a function that uses other functions as
# helpers.


def get_date(ticket: str) -> str:
    """Return the date of ticket 'ticket' in YYYYMMDD format.

    Precondition: 'ticket' is in valid format

    >>> get_date('20230915YYZYEG12F')
    '20230915'
    >>> get_date('20240915YYZYEG12F1236')
    '20240915'
    """

    return get_year(ticket) + get_month(ticket) + get_day(ticket)

# We provide this function solution as an example of correct
# documentation, as well as a function that uses constants.


def get_year(ticket: str) -> str:
    """Return the year of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_year('20230915YYZYEG12F')
    '2023'
    >>> get_year('20240915YYZYEG12F1236')
    '2024'
    """

    return ticket[YR:YR + 4]

# We provide the docstring for this function to help you get started.


def get_month(ticket: str) -> str:
    """Return the month of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_month('20230915YYZYEG12F')
    '09'
    >>> get_month('20241215YYZYEG12F1236')
    '12'
    """

    return ticket[MON: MON + 2]


def get_day(ticket: str) -> str:
    """Return the day of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_day('20230915YYZYEG12F')
    '15'
    >>> get_day('20241215YYZYEG12F1236')
    '15'
    """

    return ticket[DAY: DAY + 2]


def get_departure(ticket: str) -> str:
    """Return the departure airport initials of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_departure('20230915YYZYEG12F')
    'YYZ'
    >>> get_departure('20241215ZYZYEG12F1236')
    'ZYZ'
    """

    return ticket[DEP: DEP + 3]


def get_arrival(ticket: str) -> str:
    """Return the arrival airport initials of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_arrival('20230915YYZYEG12F')
    'YEG'
    >>> get_arrival('20241215ZYZYEG12F1236')
    'YEG'
    """

    return ticket[ARR: ARR + 3]


def get_row(ticket: str) -> int:
    """Return the row number of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_row('20230915YYZYEG12F')
    12
    >>> get_row('20241215ZYZYEG12F1236')
    12
    """

    return int(ticket[ROW: ROW + 2])


def get_seat(ticket: str) -> str:
    """Return the seat allocation letter of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_seat('20230915YYZYEG12F')
    'F'
    >>> get_seat('20241215ZYZYEG12F1236')
    'F'
    """

    return ticket[SEAT: SEAT + 1]


def get_ffn(ticket: str) -> str:
    """Return the ffn number of ticket 'ticket' if passenger has it,
    else return empty string.

    Precondition: 'ticket' is in valid format

    >>> get_ffn('20230915YYZYEG12F')
    ''
    >>> get_ffn('20241215ZYZYEG12F1236')
    '1236'
    """

    return ticket[FFN: FFN + 4]


def is_valid_seat(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if ticket 'ticket' has a valid seat. That
    is, if the seat row is between 'first_row' and 'last_row',
    inclusive, and the seat is SA, SB, SC, SD, SE, or SF.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_seat('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_seat('20230915YYZYEG42F1236', 1, 30)
    False
    >>> is_valid_seat('20230915YYZYEG21Q1236', 1, 30)
    False

    """

    row = int(get_row(ticket))

    seat = get_seat(ticket)

    if last_row >= row >= first_row:
        if seat in (SA, SB, SC, SD, SE, SF):
            return True
    return False


def is_valid_ffn(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' has a valid ffn number.
    The ffn number must consist of four digits, where the sum of the first
    three digits modulo 10 equals the fourth digit. If the passenger doesn't
    have an ffn, return True.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_ffn('20230915YYZYEG12F')
    True
    >>> is_valid_ffn('20230915YYZYEG12F1236')
    True
    >>> is_valid_ffn('20230915YYZYEG12F1237')
    False

    """

    ffn = ticket[FFN: FFN + 4]

    if ffn == '':
        return True

    if len(ffn) != 4 or not ffn.isdigit():
        return False

    digit1 = int(ffn[0])
    digit2 = int(ffn[1])
    digit3 = int(ffn[2])
    digit4 = int(ffn[3])

    sum_of_three_digits = digit1 + digit2 + digit3

    check_sum = sum_of_three_digits % 10

    return digit4 == check_sum


def is_valid_date(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' shows a valid date.
    Month must be between 1 and 12, year must be greater than 0, and the day
    must be valid for that month and year (taking leap years into account).

    Precondition: 'ticket' is in valid format.

    >>> is_valid_date('20230915YYZYEG12F1236')
    True
    >>> is_valid_date('20010229YYZYEG42F1236')
    False
    >>> is_valid_date('20010931YYZYEG42F1236')
    False

    """

    year = int(get_year(ticket))
    month = int(get_month(ticket))
    if year <= 0 or not 1 <= month <= 12:
        return False

    day = int(get_day(ticket))

    if month == 2:
        max_day = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:
        max_day = 31

    return 1 <= day <= max_day


def is_valid_ticket_format(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format:

    - year is 4 digits
    - months is 2 digits
    - day is 2 digits
    - departure is 3 letters
    - arrival is 3 letters
    - row is 2 digits
    - seat is a characters
    - frequent flyer number is either empty or 4 digits, and
      it is the last record in 'ticket'

    >>> is_valid_ticket_format('20241020YYZYEG12C1236')
    True
    >>> is_valid_ticket_format('20241020YYZYEG12C12361236')
    False
    >>> is_valid_ticket_format('ABC41020YYZYEG12C1236')
    False
    """

    return (FFN == 17
            and (len(ticket) == 17
                 or len(ticket) == 21 and ticket[FFN:FFN + 4].isdigit())
            and ticket[YR:YR + 4].isdigit()
            and ticket[MON:MON + 2].isdigit()
            and ticket[DAY:DAY + 2].isdigit()
            and ticket[DEP:DEP + 3].isalpha()
            and ticket[ARR:ARR + 3].isalpha()
            and ticket[ROW:ROW + 2].isdigit()
            and ticket[SEAT].isalpha())


def is_valid_ticket(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format and
    all of the ticket information on this ticket is valid. The parameter
    'first_row' is the first valid row number, and 'last_row' is the last
    valid row number on the plane.

    >>> is_valid_ticket('20241020YYZYEG12C1236', 1, 50)
    True
    >>> is_valid_ticket('20241020YYZYEG12C', 1, 50)
    True
    >>> is_valid_ticket('20240230YYZYEG12C1236', 1, 50)
    False
    """

    if not is_valid_ticket_format(ticket):
        return False

    if not is_valid_date(ticket):
        return False

    departure = get_departure(ticket)
    arrival = get_arrival(ticket)

    if departure == arrival:
        return False

    return is_valid_seat(ticket, first_row, last_row) and is_valid_ffn(ticket)


def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if either departure or arrival airport on
    ticket 'ticket' is the same as 'airport'.

    Precondition: 'ticket' is a valid ticket.

    >>> visits_airport('20230915YYZYEG12F1236', 'YEG')
    True
    >>> visits_airport('20230915YEGYYZ12F1236', 'YEG')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'YVR')
    False

    """

    arrival = get_arrival(ticket)
    departure = get_departure(ticket)

    if arrival == airport or departure == airport:
        return True
    return False


def connecting(ticket1: str, ticket2: str) -> bool:
    """Return true if and only if the flights represented by ticket1 and
    ticket2 are connecting.That is, the arrival airport of ticket1 is the same
    as the departure airport of ticket2, and the flights are on the same date.

    Precondition: Both ticket1 and ticket2 are valid tickets.

    >>> connecting('20230915YYZYEG12F1236', '20230915YEGXYZ12F1236')
    True
    >>> connecting('20230915YYZYEG12F1236', '20230916YEGYYZ12F1236')
    False
    >>> connecting('20230915YYZYEG12F1236', '20230915YZZZYY12F1236')
    False
    """

    arrival1 = get_arrival(ticket1)
    departure2 = get_departure(ticket2)

    date1 = get_date(ticket1)
    date2 = get_date(ticket2)

    return (date1 == date2) and (arrival1 == departure2)


def adjacent(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats in tickets 'ticket1' and
    'ticket2' are adjacent (next to each other). Seats across an aisle
    are not considered to be adjacent, that means seat C and D are not
    adjacent.

    Precondition: 'ticket1' and 'ticket2' are valid tickets.

    >>> adjacent('20230915YYZYEG12D1236', '20230915YYZYEG12E1236')
    True
    >>> adjacent('20230915YYZYEG12B1236', '20230915YYZYEG12A1236')
    True
    >>> adjacent('20230915YYZYEG12C1236', '20230915YYZYEG12D1236')
    False
    >>> adjacent('20230915YYZYEG12A1236', '20230915YYZYEG11B1236')
    False
    """
    row1 = get_row(ticket1)
    row2 = get_row(ticket2)

    if row1 != row2:
        return False

    seat1 = get_seat(ticket1)
    seat2 = get_seat(ticket2)

    if seat1 in SA:
        return seat2 in [SB]
    if seat1 in SB:
        return seat2 in [SA, SC]
    if seat1 in SC:
        return seat2 in [SB]
    if seat1 in SD:
        return seat2 in [SE]
    if seat1 in SE:
        return seat2 in [SD, SF]
    if seat1 in SF:
        return seat2 in [SE]

    return False


def behind(ticket1: str, ticket2: str) -> bool:
    """Return true if and only if ticket 1 'ticket1' is exactly behind
    ticket 2 'ticket2' or ticket 2 'ticket2' is exactly behind ticket 1
    'ticket1'.

    Precondition: 'ticket1' and 'ticket2' are valid tickets.

    >>> behind('20230915YYZYEG12D1236', '20230915YYZYEG11D1236')
    True
    >>> behind('20230915YYZYEG15D1236', '20230915YYZYEG16D1236')
    True
    >>> behind('20230915YYZYEG12D1236', '20230915YYZYEG10D1236')
    False
    >>> behind('20230915YYZYEG12D1236', '20230915YYZYEG11C1236')
    False
    """

    row1 = get_row(ticket1)
    row2 = get_row(ticket2)

    if row1 == row2:
        return False

    seat1 = get_seat(ticket1)
    seat2 = get_seat(ticket2)

    if seat1 != seat2 or abs(row1 - row2) != 1:
        return False

    return True


# We provide the docstring for this function to help you get started.


def get_seat_type(ticket: str) -> str:
    """Return WINDOW, AISLE, or MIDDLE depending on the type of seat in
    ticket 'ticket'.

    Precondition: 'ticket' is a valid ticket.

    >>> get_seat_type('20230915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20230915YYZYEG08B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12C1236')
    'aisle'

    """

    seat = get_seat(ticket)



    if seat in [SA, SF]:
        return WINDOW
    if seat in [SB, SE]:
        return MIDDLE
    if seat in [SC, SD]:
        return AISLE
    return ''

last_word = 'If you have time, double check your answers before you leave! :)'

#[::-1][:-1]:

if __name__ == '__main__':
    import doctest
    doctest.testmod()
