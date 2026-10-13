# Membership Management CLI App

A lightweight, object-oriented command-line interface (CLI) application built in Python for managing membership records efficiently. Designed with a focus on clean architecture, input validation, and user experience.

## Features

- **Object-Oriented Design**: Utilizes Python classes (`Members`) and methods to encapsulate member data and behavior.
- **Robust Input Validation**: Implements strict checks (such as `.isdigit()` validation) to prevent runtime crashes caused by invalid user inputs.
- **Flexible Search System**: Allows searching records dynamically by ID, Name, or Status with clear feedback loops.
- **Smart Defaults**: Automatically handles optional fields, assigning default values (e.g., `"inactive"`) when input is skipped.
- **Cross-Platform UX**: Features automated screen clearing (`cls`/`clear`) and controlled pauses for a smooth terminal experience.

## Built With

- **Python 3** (Standard Library: `time`, `os`)

## How to Run

1. Ensure Python 3 is installed on your machine.
2. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/membership-management-cli.git](https://github.com/YOUR_USERNAME/membership-management-cli.git)