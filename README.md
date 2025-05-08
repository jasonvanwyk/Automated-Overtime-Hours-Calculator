# Automated Overtime Hours Calculator

A Python application designed to automate the monthly summation of employee overtime hours from multiple CSV files. It categorizes overtime as "Sunday" or "Public Holiday" based on filenames and generates a single summary CSV file.

**Developed by Precept Systems (Pty) Ltd**  
Contact: 083 288 9052 | info@precept.co.za | www.precept.co.za

## Features

- Processes multiple CSV files containing overtime data
- Validates file naming conventions and CSV structure
- Normalizes employee identifiers for consistent aggregation
- Handles non-numeric hour values gracefully
- Generates a consolidated monthly summary in CSV format

## Requirements

### For Running the Executable (Windows)
- Windows 7/8/10/11
- No additional requirements (Python not needed)

### For Development
- Python 3.11.x or higher
- Dependencies listed in requirements.txt

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

## Installation

### Windows Installation (Recommended for End Users)

1. Download the latest release from the [Releases page](https://github.com/jasonvanwyk/Automated-Overtime-Hours-Calculator/releases)
2. Extract the ZIP file to a location of your choice
3. Run the `install_windows.bat` file and follow the on-screen instructions
4. A shortcut will be created on your desktop

### Manual Installation (For Developers)

1. Clone the repository:
   ```
   git clone https://github.com/jasonvanwyk/Automated-Overtime-Hours-Calculator.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Using the Windows Application

1. Double-click the "Automated Overtime Calculator" shortcut on your desktop
2. Follow the on-screen instructions

### Using the Python Script

1. **Prepare your CSV files**:
   - Use the `template_overtime_sheet.csv` format
   - Required headers: "Employee Identifier", "Hours Worked"

2. **Name your CSV files correctly**:
   - For Sunday overtime: `YYYY-MM-DD-Sunday.csv` (e.g., `2025-05-05-Sunday.csv`)
   - For Public Holiday overtime: `YYYY-MM-DD-Holiday.csv` (e.g., `2025-05-01-Holiday.csv`)

3. **Place all CSV files in a single folder**
   - IMPORTANT: Only place files you want processed in this folder
   - Any CSV file with the correct naming convention will be processed

4. **Run the script**:
   ```
   python src/automated_overtime_calculator.py
   ```

5. **When prompted, provide the path to your folder containing the CSV files**
   - Type '/q' to exit the program if needed

6. **Check the output**:
   - The application will generate `Monthly_Overtime_Totals.csv` in the `output/` directory
   - A log file with processing details will also be generated
   - The output file contains columns: "Employee Identifier", "Sunday Hours", "Public Holiday Hours"
   - Each run will overwrite the existing output file if it exists

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

## Building the Windows Executable

To build the Windows executable yourself:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Generate the icon (optional, if you want to customize):
   ```
   python create_icon.py
   ```

3. Build the executable:
   ```
   pyinstaller automated_overtime_calculator.spec
   ```

4. The executable will be created in the `dist` directory

## Testing

For testing purposes, example input files are provided in the `data/input_examples/` directory.

## Features

- **User-friendly interface** with clear instructions
- **Input validation** for folder paths and CSV files
- **File processing** with proper naming convention validation
- **Data validation** with employee ID normalization and hours validation
- **Aggregation** of overtime hours by type (Sunday and Public Holiday)
- **Output generation** in CSV format
- **Comprehensive error handling** with detailed feedback
- **Summary statistics** showing total employees and hours
- **Log file generation** with timestamp for record-keeping
