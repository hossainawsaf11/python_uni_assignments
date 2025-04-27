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



