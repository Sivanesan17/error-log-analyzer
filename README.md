# Error Log Analyzer

This Python script reads a log file, counts the number of lines containing the word `ERROR`, and prints:

- Total number of ERROR lines

## Features

- Reads log files line by line
- Detects lines containing `ERROR`
- Displays error count

## Requirements

- Python 3.x

## Usage

1. Place your log file in the project directory.

2. Run the script:

```bash
python3 log_error_counter.py
```

3. Example:

```python
count_errors("system.log")
```

## Example Output

```text
Total ERROR lines: 12

ERROR lines:
ERROR: Database connection failed
ERROR: Invalid user credentials
ERROR: Timeout occurred
ERROR: File not found
ERROR: Server unavailable
```
