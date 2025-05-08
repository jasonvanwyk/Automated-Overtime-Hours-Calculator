# Automated Overtime Hours Calculator

A Python script designed to automate the monthly summation of employee overtime hours from multiple CSV files. It categorizes overtime as "Sunday" or "Public Holiday" based on filenames and generates a single summary CSV file.

## Features

- Processes multiple CSV files containing overtime data
- Validates file naming conventions and CSV structure
- Normalizes employee identifiers for consistent aggregation
- Handles non-numeric hour values gracefully
- Generates a consolidated monthly summary in CSV format

## Requirements

- Python 3.11.x or higher

## Project Structure

```
automated-overtime-calculator/
├── data/
│   ├── input_examples/      # Example input CSVs for testing
│   └── template_overtime_sheet.csv # Template for input files
├── output/                  # Default location for generated output
├── src/
│   └── automated_overtime_calculator.py # The main Python script
├── tests/                   # For future automated tests
└── README.md                # This file
```

## Usage

1. **Prepare your CSV files**:
   - Use the `template_overtime_sheet.csv` format
   - Required headers: "Employee Identifier", "Hours Worked"

2. **Name your CSV files correctly**:
   - For Sunday overtime: `YYYY-MM-DD-Sunday.csv` (e.g., `2025-05-05-Sunday.csv`)
   - For Public Holiday overtime: `YYYY-MM-DD-Holiday.csv` (e.g., `2025-05-01-Holiday.csv`)

3. **Place all CSV files in a single folder**

4. **Run the script**:
   ```
   python src/automated_overtime_calculator.py
   ```

5. **When prompted, provide the path to your folder containing the CSV files**

6. **Check the output**:
   - The script will generate `Monthly_Overtime_Totals.csv` in the `output/` directory
   - The output file contains columns: "Employee Identifier", "Sunday Hours", "Public Holiday Hours"

## Example

Input files:
- `2025-05-05-Sunday.csv` - Sunday overtime for May 5, 2025
- `2025-05-12-Sunday.csv` - Sunday overtime for May 12, 2025
- `2025-05-01-Holiday.csv` - Public Holiday overtime for May 1, 2025

Output:
- `Monthly_Overtime_Totals.csv` - Contains the summed overtime hours for each employee

## Error Handling

The script provides clear error messages for:
- Invalid input folder paths
- Files with incorrect naming conventions
- Files with incorrect CSV structure
- Non-numeric hour values (treated as 0.0)

## Testing

For testing purposes, example input files are provided in the `data/input_examples/` directory.
