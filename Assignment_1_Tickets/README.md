# Assignment 1 - Airplane Tickets Project (University Course CSCA08H3)

This project simulates managing airplane tickets based on a custom ticket string format, using Python functions built through the Function Design Recipe approach.  
It was developed as part of my coursework for CSCA08H3 at the University of Toronto Scarborough during Winter 2025.

**Grade Received: 98%**

## Project Overview

The goal of this assignment was to:
- Practice planning, implementing, and testing functions using Python 3.
- Handle string manipulation, date validation (including leap years), and ticket information extraction.
- Use constants for readable and flexible code.
- Write clean code following Python style guidelines and docstring documentation standards.

Key concepts used:
- Variables, numeric types, strings, conditionals
- Functions with proper contracts, examples, and doctests
- No use of print/input statements (pure functions only)

## Ticket Structure

Each ticket is a string containing:
- **Date** (year, month, day)
- **Departure and Arrival Airports**
- **Seat Row and Seat Letter**
- **Frequent Flyer Number (optional)**

Functions validate ticket format, extract fields (like date, seat, frequent flyer number), check validity, and determine seat types (window, aisle, middle).

Example Ticket:  
`20231221YYZYEG25F4442`  
(Dec 21, 2023, YYZ ➔ YEG, Row 25 Seat F, Frequent Flyer 4442)

## Files

- `tickets.py`: Core file to complete. Contains partial starter code for functions handling ticket information.
- `constants.py`: Provided constants like YR, MON, DEP, ARR, etc., to be used throughout the program.
- `checker_generic.py`: Helper utility for checking multiple assignments (provided).
- `a1_checker.py`: Python script to check style compliance and function signatures.

## Skills Practiced

- String slicing and indexing
- Conditional logic
- Data validation (dates, frequent flyer numbers, airport codes)
- Modular programming
- Testing with doctests
- Working with constants for flexible coding

## Checker Information

The provided `a1_checker.py` script checks:
- Python coding style (PEP8 compliance)
- Correct function signatures
- Proper return types

Passing the checker does **NOT** guarantee correctness — additional internal tests were used after submission.

---


