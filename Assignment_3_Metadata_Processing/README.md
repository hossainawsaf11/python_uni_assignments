# Assignment 3 - Working with Metadata from arxiv.org (University Course CSCA08H3)

**Grade Received: 88%**

This project focuses on reading structured metadata files, organizing scholarly article data, and building Python data structures to model articles, authors, and their relationships.  
It was developed as part of my coursework for CSCA08H3 at the University of Toronto Scarborough during Winter 2025.

## Project Overview

The goal of this assignment was to:
- Process structured metadata from academic articles.
- Extract and organize data into dictionaries and nested data structures.
- Analyze metadata to suggest collaborations, find prolific authors, and manage article information.
- Apply modular function design with clean, testable Python code.

Key programming concepts:
- File reading and parsing
- Working with nested dictionaries and lists
- String processing and data cleaning
- Sorting and filtering based on conditions
- Writing robust helper functions
- Unit testing

## Data Source

The metadata simulates records from **arxiv.org**, containing:
- Article IDs
- Titles
- Creation and modification dates
- Lists of authors
- Abstracts

Example article stored:
```python
{
    'identifier': '008',
    'title': 'Intro to CS is the best course ever',
    'created': '2023-09-01',
    'modified': None,
    'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
    'abstract': 'We present clear evidence that Introduction to\nComputer Science is the best course.'
}
```


## Tasks Completed

- **Reading metadata files** and building structured dictionaries (`read_arxiv_file`).
- **Modeling articles and authors**: creating structured records with IDs, titles, authors, dates, and abstracts.
- **Analyzing metadata**:
  - Finding coauthors (`get_coauthors`)
  - Identifying prolific authors (`get_most_published_authors`)
  - Suggesting new collaboration opportunities (`suggest_collaborators`)
- **Filtering metadata**:
  - Keeping only articles authored by prolific researchers (`keep_prolific_authors`)
- **Testing**:
  - Creating a complete unittest suite (`test_get_most_published_authors.py`) to verify correctness.

Each function was written using clean modular design, following the Function Design Recipe with clear contracts and doctests where applicable.

## Skills Practiced

- File parsing and line-by-line reading
- Building and managing complex nested dictionaries and tuples
- String processing and data validation
- Data transformation and organization
- Writing robust modular Python functions
- Writing unit tests using `unittest`
- Following clean code practices (PEP8 style guidelines)

## Files

- `arxiv_functions.py`: Main file containing all assignment functions.
- `constants.py`: File containing predefined constants used across modules.
- `test_get_most_published_authors.py`: Unit test file for verifying author-based functions.
- `example_data.txt` and `data.txt`: Provided sample metadata files for testing and development.
- `a3_checker.py`: Provided checker script to validate function headers, return types, and PEP8 compliance.

## Checker Information

The provided `a3_checker.py` script was used to ensure:
- All functions match required signatures and types
- Python coding style guidelines (PEP8) are fully followed

Passing the checker verifies structural and style correctness; functional correctness was achieved through careful manual testing and automated unit tests.

---

