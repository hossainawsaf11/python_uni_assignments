# Assignment 2 - Maintaining Bridges Infrastructure (University Course CSCA08H3)

This project focuses on analyzing real-world bridge infrastructure data in Ontario, simulating how inspectors are assigned to bridges based on priority and distance.  
It was developed as part of my coursework for CSCA08H3 at the University of Toronto Scarborough during Winter 2025.

**Grade Received: 87%**

## Project Overview

The goal of this assignment was to:
- Practice using the Function Design Recipe to plan, implement, and test functions.
- Process and transform real-world datasets from CSV files.
- Apply list methods, string processing, and loops to analyze and modify data.
- Model a bridge inspection system using calculated distances and priorities.

Key programming concepts:
- File reading and parsing
- Lists and nested data structures
- String manipulation and formatting
- Data validation and condition-based analysis
- Distance calculation using latitude and longitude
- Modular program design and helper functions

## Data Source

The dataset is based on real open data provided by the Ontario government on provincially owned bridges.  
The bridge dataset includes:
- Bridge names and highway numbers
- Geographic coordinates (latitude and longitude)
- Construction and rehabilitation years
- Span information
- Last inspection dates and Bridge Condition Indices (BCIs)

Each bridge record was cleaned, parsed, and reformatted into a structured list format for programmatic analysis.

Example formatted record:

[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, -80.275567, '1965', '2014', '2009', 4, [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012', [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]

## Tasks Completed

- **Reading CSV data** into nested lists (`read_data` function provided).
- **Formatting raw data** into clean structured lists (`format_data` function).
- **Analyzing bridge information**: average BCI, total lengths on highways, finding bridges by location, search by name.
- **Modeling inspections**: assigning bridges to inspectors based on bridge priority and geographic proximity.
- **Updating bridge records**: after inspections or rehabilitation events.

Functions developed include:
- `get_bridge`, `get_average_bci`, `get_total_length_on_hwy`
- `get_distance_between`, `get_closest_bridge`
- `get_bridges_in_radius`, `get_bridges_with_bci_below`
- `inspect_bridges`, `add_rehab`, `assign_inspectors`

All functions follow the Function Design Recipe, including proper type contracts, docstrings, and doctest examples.

## Skills Practiced

- File processing (CSV parsing)
- Working with nested lists
- String slicing and cleaning
- Mathematical calculations (distance between GPS coordinates)
- Data filtering based on conditions
- Modular function design
- Robust input validation and clean code style

## Files

- `bridge_functions.py`: Main file containing all assignment functions.
- `constants.py`: File containing index constants and priority thresholds.
- `bridge_data.csv`: Provided bridge dataset (not modified).
- `a2_checker.py`: Provided checker script to verify style and function signatures.

## Checker Information

The provided `a2_checker.py` script verifies:
- Python style guideline adherence (PEP8)
- Function signatures, parameters, and return types

Passing the checker ensures structural correctness but thorough manual testing was conducted for full functionality.

---




