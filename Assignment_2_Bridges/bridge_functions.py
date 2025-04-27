"""Assignment 2: Bridges

The data used for this assignment is a subset of the data found in:
https://data.ontario.ca/dataset/bridge-conditions

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of Toronto
Scarborough. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Anya Tafliovich, Mario Badr, Tom Fairgrieve, Sadia
Sharmin, and Jacqueline Smith

"""

import csv
from copy import deepcopy
from math import sin, cos, asin, radians, sqrt, inf
from typing import TextIO

from constants import (
    ID_INDEX, NAME_INDEX, HIGHWAY_INDEX, LAT_INDEX,
    LON_INDEX, YEAR_INDEX, LAST_MAJOR_INDEX,
    LAST_MINOR_INDEX, NUM_SPANS_INDEX,
    SPAN_DETAILS_INDEX, LENGTH_INDEX,
    LAST_INSPECTED_INDEX, BCIS_INDEX, FROM_SEP, TO_SEP,
    HIGH_PRIORITY_BCI, MEDIUM_PRIORITY_BCI,
    LOW_PRIORITY_BCI, HIGH_PRIORITY_RADIUS,
    MEDIUM_PRIORITY_RADIUS, LOW_PRIORITY_RADIUS,
    EARTH_RADIUS)
EPSILON = 0.01


# We provide this function for you to use as a helper.
def read_data(csv_file: TextIO) -> list[list[str]]:
    """Read and return the contents of the open CSV file csv_file as a
    list of lists, where each inner list contains the values from one
    line of csv_file.

    Docstring examples not given since the function reads from a file.

    """

    lines = csv.reader(csv_file)
    return list(lines)[2:]


# We provide this sample data to help you set up example calls.
THREE_BRIDGES_UNCLEANED = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403', '43.167233',
     '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012', '72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531', '-80.251582',
     '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61', '04/13/2012',
     '71.5', '', '71.5', '', '68.1', '', '69', '', '69.4', '', '69.4', '',
     '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579', '1958',
     '2013', '', '1', 'Total=16  (1)=16;', '18.4', '08/28/2013', '85.1',
     '85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '', '75.1', '',
     '90.1', '']
]

THREE_BRIDGES = [
    [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567,
     '1965', '2014', '2009', 4, [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, '04/13/2012',
     [71.5, 68.1, 69.0, 69.4, 69.4, 70.3, 73.3]],
    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579,
     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013',
     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
]


# We provide the header and doctring for this function to help get you
# started.
def get_bridge(bridge_data: list[list], bridge_id: int) -> list:
    """Return the data for the bridge with id bridge_id from bridge data
    bridge_data. If there is no bridge with id bridge_id, return [].

    >>> result = get_bridge(THREE_BRIDGES, 1)
    >>> result == [
    ...    1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
    ...    -80.275567, '1965', '2014', '2009', 4,
    ...    [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
    ...    [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    True
    >>> get_bridge(THREE_BRIDGES, 42)
    []

    """

    for bridge in bridge_data:
        if bridge[ID_INDEX] == bridge_id:
            return bridge

    return []


def get_average_bci(bridge_data: list[list], bridge_id: int) -> float:
    """Return the average BCI of the bridge with matching bridge_id from
    bridge_data. If there is no bridge with matching bridge_id or there are no
    BCIs for the given bridge, return zero.

    >>> get_average_bci(THREE_BRIDGES, 1)
    70.88571428571429
    >>> get_average_bci(THREE_BRIDGES, 2)
    70.14285714285714
    """

    selected_bridge = get_bridge(bridge_data, bridge_id)

    if not selected_bridge:
        return 0.0

    bci_list = selected_bridge[BCIS_INDEX]

    if not bci_list:
        return 0.0

    return sum(bci_list) / len(bci_list)


def get_total_length_on_hwy(bridge_data: list[list], highway: str) -> float:
    """Return the total length of all bridges on the given highway.

    The function iterates through `bridge_data` and sums the lengths of all
    bridges that are located on the specified `highway`. If no bridges exist
    on that highway, the function returns 0.0.

    Preconditions:
    - `bridge_data` follows the formatted data structure.
    - `highway` is a valid string.

    >>> get_total_length_on_hwy(THREE_BRIDGES, '403')
    126.0
    >>> get_total_length_on_hwy(THREE_BRIDGES, '6')
    18.4
    """

    total_length = 0.0

    for i in bridge_data:
        if i[HIGHWAY_INDEX] == highway:
            total_length = total_length + i[LENGTH_INDEX]
    return total_length

# We provide this function for you to use as a helper.  This function
# uses the haversine function to find the distance between two
# locations. You do not need to understand why it works. You will just
# need to call this function and work with what it returns.  Based on
# https://en.wikipedia.org/wiki/Haversine_formula
# Notice how we use the built-in function abs and the constant EPSILON
# defined above to constuct example calls for the function that
# returns a float. We do not test with ==; instead, we check that the
# return value is "close enough" to the expected result.


def calculate_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined by
    (lat1, lon1) and (lat2, lon2), rounded to the nearest meter.

    >>> abs(calculate_distance(43.659777, -79.397383, 43.657129, -79.399439)
    ...     - 0.338) < EPSILON
    True
    >>> abs(calculate_distance(43.42, -79.24, 53.32, -113.30)
    ...     - 2713.226) < EPSILON
    True
    """

    lat1, lon1, lat2, lon2 = (radians(lat1), radians(lon1),
                              radians(lat2), radians(lon2))

    haversine = (sin((lat2 - lat1) / 2) ** 2
                 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2)

    return round(2 * EARTH_RADIUS * asin(sqrt(haversine)), 3)


def get_distance_between(b_1: list, b_2: list) -> float:
    """Return the distance in kilometers between two bridges b_1 and b_2,
    rounded to 3 decimal places.

    The distance is calculated using latitude and longitude values from the two
    given bridge data lists.

    >>> get_distance_between(THREE_BRIDGES[0], THREE_BRIDGES[1])
    1.968
    >>> get_distance_between(THREE_BRIDGES[0], THREE_BRIDGES[2])
    224.451
    """

    return round(
        calculate_distance(
            b_1[LAT_INDEX], b_1[LON_INDEX], b_2[LAT_INDEX], b_2[LON_INDEX]
        ),
        3
    )


def get_closest_bridge(bridge_data: list[list], bridge_id: int) -> int:
    """Return the ID of the closest bridge to the bridge
    with the given bridge_id from bridge_data.


    >>> get_closest_bridge(THREE_BRIDGES, 2)
    1
    >>> get_closest_bridge(THREE_BRIDGES, 1)
    2

    """

    smallest_distance = float('inf')

    closest_bridge = 0

    target_bridge = get_bridge(bridge_data, bridge_id)

    for i in bridge_data:
        if i[ID_INDEX] != bridge_id:
            distance = get_distance_between(target_bridge, i)

            if distance < smallest_distance:
                smallest_distance = distance
                closest_bridge = i[ID_INDEX]

    return closest_bridge


def get_bridges_in_radius(
    bridge_data: list[list], lat: float, lon: float, radius: float
) -> list[int]:
    """Return a list of IDs of all bridges that are within the given `radius`
    (in kilometers) of the given location (`lat`, `lon`) from list bridge_data.

    >>> get_bridges_in_radius(THREE_BRIDGES, 43.10, -80.15, 50)
    [1, 2]
    >>> get_bridges_in_radius(THREE_BRIDGES, 43.10, -80.15, 1000)
    [1, 2, 3]

    """

    bridges_in_range = []

    for bridge in bridge_data:
        d = calculate_distance(lat, lon, bridge[LAT_INDEX], bridge[LON_INDEX])
        if d <= radius:
            bridges_in_range.append(bridge[ID_INDEX])

    return bridges_in_range


def get_bridges_with_bci_below(
    bridge_data: list[list], bridge_ids: list[int], bci_limit: float
) -> list[int]:
    """Return a list of IDs of all bridges whose IDs are in `bridge_ids` and
    whose most recent BCI is less than or equal to `bci_limit` from bridge_data.

    >>> get_bridges_with_bci_below(THREE_BRIDGES, [1, 2], 72)
    [2]
    """

    matching_bridges = []

    for bridge_id in bridge_ids:
        bridge = get_bridge(bridge_data, bridge_id)

        if bridge and bridge[BCIS_INDEX]:
            most_recent_bci = bridge[BCIS_INDEX][0]

            if most_recent_bci <= bci_limit:
                matching_bridges.append(bridge_id)

    return matching_bridges


def get_bridges_containing(
    bridge_data: list[list], search_string: str
) -> list[int]:
    """ Return a list of IDs of all bridges from bridge_data whose names
    contain the given `search_string`.

    >>> get_bridges_containing(THREE_BRIDGES, 'underpass')
    [1, 2]
    >>> get_bridges_containing(THREE_BRIDGES, 'pass')
    [1, 2]
    >>> get_bridges_containing(THREE_BRIDGES, 'river')
    [3]
    """

    matching_bridges = []

    search_string = search_string.lower()

    for bridge in bridge_data:
        bridge_name = bridge[NAME_INDEX].lower()

        if search_string in bridge_name:
            matching_bridges.append(bridge[ID_INDEX])

    return matching_bridges


# We provide the header and doctring for this function to help get you
# started. Note the use of the built-in function deepcopy (see
# help(deepcopy)!): since this function modifies its input, we do not
# want to call it with THREE_BRIDGES, which would interfere with the
# use of THREE_BRIDGES in examples for other functions.
def inspect_bridges(bridge_data: list[list], bridge_ids: list[int], date: str,
                    bci: float) -> None:
    """Update the bridges in bridge_data with id in bridge_ids with the new
    date and bci score for a new inspection.

    >>> bridges = deepcopy(THREE_BRIDGES)
    >>> inspect_bridges(bridges, [1], '09/15/2018', 71.9)
    >>> bridges == [
    ...   [1, 'Highway 24 Underpass at Highway 403', '403',
    ...    43.167233, -80.275567, '1965', '2014', '2009', 4,
    ...    [12.0, 19.0, 21.0, 12.0], 65.0, '09/15/2018',
    ...    [71.9, 72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
    ...   [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
    ...    '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2],
    ...    61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3, 73.3]],
    ...   [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579,
    ...    '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013',
    ...    [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]]
    True

    """

    for bridge in bridge_data:
        if bridge[ID_INDEX] in bridge_ids:
            bridge[LAST_INSPECTED_INDEX] = date
            bridge[BCIS_INDEX].insert(0, bci)


def add_rehab(
    bridge_data: list[list], bridge_id: int, date: str, major_rehab: bool
) -> None:
    """
    Update the rehab year 'date' of the bridge with `bridge_id` from
    bridge_data. If `major_rehab` is True, update the major rehab year. If
    `major_rehab` is False, update the minor rehab year. If the bridge ID is
    not found, return nothing.

    >>> bridges = deepcopy(THREE_BRIDGES)
    >>> add_rehab(bridges, 1, '2023', False)
    >>> bridges[0]
    [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567,
     '1965', '2014', '2023', 4, [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012',
     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    """

    for bridge in bridge_data:
        if bridge[ID_INDEX] == bridge_id:
            if major_rehab:
                bridge[LAST_MAJOR_INDEX] = date
            else:
                bridge[LAST_MINOR_INDEX] = date


# We provide the header and doctring for this function to help get you started.
def assign_inspectors(bridge_data: list[list], inspectors: list[list[float]],
                      max_bridges: int) -> list[list[int]]:
    """Return a list of bridge IDs from bridge data bridge_data, to be
    assigned to each inspector in inspectors. inspectors is a list
    containing (latitude, longitude) pairs representing each
    inspector's location. At most max_bridges are assigned to each
    inspector, and each bridge is assigned once (to the first
    inspector that can inspect that bridge).

    See the "Assigning Inspectors" section of the handout for more details.

    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15], [42.10, -81.15]], 0)
    [[], []]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 1)
    [[1]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 2)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 3)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 1)
    [[1], [2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 2)
    [[1, 2], []]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [45.0368, -81.34]],
    ...                   2)
    [[1, 2], [3]]
    >>> assign_inspectors(THREE_BRIDGES, [[38.691, -80.85], [43.20, -80.35]],
    ...                   2)
    [[], [1, 2]]

    """

    assigned_bridges = []

    assigned_bridge_ids = []

    for inspector in inspectors:
        lat = inspector[0]
        lon = inspector[1]

        inspector_bridges = []

        for p_bci, p_rad in [
            (HIGH_PRIORITY_BCI, HIGH_PRIORITY_RADIUS),
            (MEDIUM_PRIORITY_BCI, MEDIUM_PRIORITY_RADIUS),
            (LOW_PRIORITY_BCI, LOW_PRIORITY_RADIUS)
        ]:
            if len(inspector_bridges) >= max_bridges:
                break

            n_bridge = get_bridges_in_radius(bridge_data, lat, lon, p_rad)

            v_bridge = get_bridges_with_bci_below(bridge_data, n_bridge, p_bci)

            v_bridge.sort()

            for bridge_id in v_bridge:
                if (
                    bridge_id not in assigned_bridge_ids
                    and len(inspector_bridges) < max_bridges
                ):
                    inspector_bridges.append(bridge_id)
                    assigned_bridge_ids.append(bridge_id)

        assigned_bridges.append(inspector_bridges)

    return assigned_bridges


# We provide the header and doctring for this function to help get you started.
def format_data(data: list[list[str]]) -> None:
    """Modify the uncleaned bridge data data, so that it contains proper
    bridge data, i.e., follows the format outlined in the 'Data
    formatting' section of the assignment handout.

    >>> d = deepcopy(THREE_BRIDGES_UNCLEANED)
    >>> format_data(d)
    >>> d == THREE_BRIDGES
    True

    """

    bridge_id = 1

    for bridge in data:
        bridge[ID_INDEX] = bridge_id
        bridge_id += 1

        format_location(bridge)

        if bridge[YEAR_INDEX] == '':
            bridge[YEAR_INDEX] = ''
        if bridge[LAST_MAJOR_INDEX] == '':
            bridge[LAST_MAJOR_INDEX] = ''
        if bridge[LAST_MINOR_INDEX] == '':
            bridge[LAST_MINOR_INDEX] = ''

        bridge[NUM_SPANS_INDEX] = int(bridge[NUM_SPANS_INDEX])

        format_spans(bridge)

        format_length(bridge)

        if bridge[LAST_INSPECTED_INDEX] == '':
            bridge[LAST_INSPECTED_INDEX] = ''

        format_bcis(bridge)


# This is a suggested helper function for format_data. We provide the
# header and doctring for this function to help you structure your
# solution.
def format_location(bridge_record: list) -> None:
    """Format latitude and longitude data in the bridge record bridge_record.

    >>> record = ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    >>> format_location(record)
    >>> record == ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           43.167233, -80.275567, '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    True
    """

    bridge_record[LAT_INDEX] = float(bridge_record[LAT_INDEX])
    bridge_record[LON_INDEX] = float(bridge_record[LON_INDEX])


# This is a suggested helper function for format_data. We provide the
# header and doctring for this function to help you structure your
# solution.
def format_spans(bridge_record: list) -> None:
    """Format the bridge spans data in the bridge record bridge_record.

    >>> record = ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    >>> format_spans(record)
    >>> record == ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', 4,
    ...           [12.0, 19.0, 21.0, 12.0], '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    True

    """

    bridge_record[NUM_SPANS_INDEX] = int(bridge_record[NUM_SPANS_INDEX])

    span_details = bridge_record[SPAN_DETAILS_INDEX]
    span_list = []

    spans = span_details.split(TO_SEP)
    for span in spans:
        if FROM_SEP in span:
            key, value = span.split(FROM_SEP, 1)  # Split only once
            if key.strip().isdigit():  # Ignore 'Total=' entry
                span_list.append(float(value.strip()))

    bridge_record[SPAN_DETAILS_INDEX] = span_list


# This is a suggested helper function for format_data. We provide the
# header and doctring for this function to help you structure your
# solution.
def format_length(bridge_record: list) -> None:
    """Format the bridge length data in the bridge record bridge_record.

    >>> record = ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    >>> format_length(record)
    >>> record == ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...            '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...            'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', 65.0,
    ...            '04/13/2012', '72.3', '', '72.3', '', '69.5', '', '70', '',
    ...            '70.3', '', '70.5', '', '70.7', '72.9', '']
    True

    """

    if bridge_record[LENGTH_INDEX] == '':
        bridge_record[LENGTH_INDEX] = 0.0
    else:
        bridge_record[LENGTH_INDEX] = float(bridge_record[LENGTH_INDEX])


# This is a suggested helper function for format_data. We provide the
# header and doctring for this function to help you structure your
# solution.
def format_bcis(bridge_record: list) -> None:
    """Format the bridge BCI data in the bridge record bridge_record.

    >>> record = ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           '72.3', '', '72.3', '', '69.5', '', '70', '', '70.3', '',
    ...           '70.5', '', '70.7', '72.9', '']
    >>> format_bcis(record)
    >>> record == ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403',
    ...           '43.167233', '-80.275567', '1965', '2014', '2009', '4',
    ...           'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012',
    ...           [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    True

    """

    bci_values = bridge_record[BCIS_INDEX:]

    bci_list = [float(bci) for bci in bci_values if bci.strip()]

    bridge_record[BCIS_INDEX:] = [bci_list]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # To test your code with larger lists, you can uncomment the code below to
    # read data from the provided CSV file.
    # with open('bridge_data.csv', encoding='utf-8') as bridge_data_file:
    #     BRIDGES = read_data(bridge_data_file)
    # format_data(BRIDGES)

    # For example:
    # print(get_bridge(BRIDGES, 3))
    # EXPECTED = [3, 'NORTH PARK STEET UNDERPASS', '403', 43.165918, -80.263791,
    #             '1962', '2013', '2009', 4, [12.2, 18.0, 18.0, 12.2], 60.8,
    #             '04/13/2012', [71.4, 69.9, 67.7, 68.9, 69.1, 69.9, 72.8]]
    # print('Testing get_bridge: ', get_bridge(BRIDGES, 3) == EXPECTED)
