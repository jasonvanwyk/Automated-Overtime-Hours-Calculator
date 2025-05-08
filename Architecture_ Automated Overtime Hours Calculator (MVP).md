# **Architecture: Automated Overtime Hours Calculator (MVP)**

## **1\. Introduction**

This document outlines the technical architecture for the Minimum Viable Product (MVP) of the "Automated Overtime Hours Calculator." The system is a Python script designed to automate the monthly summation of employee overtime hours from multiple CSV files. It categorizes overtime as "Sunday" or "Public Holiday" based on filenames and generates a single summary CSV file. This document provides a lean overview suitable for a simple script with a 1-day development target, focusing on clarity for development and future understanding.

## **2\. System Overview**

The Automated Overtime Hours Calculator is a standalone Python script executed via a Command Line Interface (CLI). It processes CSV files from a user-specified input folder. Each input CSV adheres to a strict naming convention (YYYY-MM-DD-Sunday.csv or YYYY-MM-DD-Holiday.csv) and internal template (template\_overtime\_sheet.csv). The script sums hours for each employee, categorized by overtime type, and outputs a consolidated CSV report. User interaction is handled through CLI prompts and feedback messages.

## **3\. Key Functional Requirements Affecting Architecture**

The architecture directly supports the following core functional requirements (derived from PRD):

* **Input Processing:**  
  * Accept a user-specified input folder path via CLI.  
  * Process multiple CSV files within that folder.  
* **Input Validation (Strict):**  
  * Filenames must match YYYY-MM-DD-Sunday.csv or YYYY-MM-DD-Holiday.csv.  
  * CSV content must match template\_overtime\_sheet.csv headers: "Employee Identifier", "Hours Worked".  
* **Data Parsing & Summation:**  
  * Parse 'Employee Identifier' and 'Hours Worked' from valid CSVs.  
  * Normalize 'Employee Identifier' (trim whitespace, case-insensitive matching).  
  * Validate 'Hours Worked' (treat non-numeric as 0.0, log/report).  
  * Sum "Sunday Hours" and "Public Holiday Hours" separately for each unique employee.  
* **Output Generation:**  
  * Generate a single output CSV file (e.g., Monthly\_Overtime\_Totals.csv).  
  * Output columns: "Employee Identifier", "Sunday Hours", "Public Holiday Hours".  
* **User Interface (CLI):**  
  * Provide clear instructions for usage, file preparation, and input.  
  * Display processing feedback and clear error messages.  
* **Error Handling:**  
  * Handle issues like: input folder not found, no valid files, incorrect filenames, non-compliant CSV structures, non-numeric hours. Report and skip/handle gracefully.

## **4\. Technology Stack**

* **Programming Language:** Python  
  * **Specific Version:** 3.11.x (e.g., latest stable 3.11.9)  
  * **Rationale:** Modern, stable, widely available, and supports all necessary standard libraries.  
* **Core Standard Libraries (Bundled with Python 3.11.x):**  
  * **pathlib module:** For object-oriented file system path operations (directory scanning, path construction).  
  * **csv module:** For CSV file parsing (reading inputs) and generation (writing output).  
  * **collections.defaultdict:** For efficient summation of overtime hours per employee.  
  * **Built-in string methods:** For filename parsing and 'Employee Identifier' normalization.  
* **Development & Execution Environment:**  
  * **Operating System:** Windows (target user environment).  
  * **Runtime:** Python 3.11.x interpreter.  
* **Exclusions (MVP):** No external/third-party libraries, no databases, no web frameworks.

## **5\. Core Script Structure / Components (Logical Functions)**

The script (automated\_overtime\_calculator.py) will be structured procedurally, with functionality broken down into distinct Python functions to enhance readability and maintainability. Standard Python coding conventions (PEP 8\) will be followed.

* **main()**: Orchestrates the entire process:  
  * Calls functions to display welcome messages and instructions.  
  * Prompts for and validates the input folder path.  
  * Initiates file discovery and processing.  
  * Triggers data summation.  
  * Initiates output file generation.  
  * Displays completion or error messages.  
* **display\_instructions()**: Prints usage guidelines to the CLI.  
* **get\_input\_folder\_path()**: Prompts user for the input folder path and performs basic validation (e.g., path exists, is a directory).  
* **process\_files\_in\_folder(folder\_path)**:  
  * Iterates through files in folder\_path.  
  * Validates filenames against the YYYY-MM-DD-Type.csv convention.  
  * For each valid file, calls parse\_csv\_file() to extract data.  
  * Collects all valid records or updates totals directly.  
* **parse\_csv\_file(file\_path, overtime\_type)**:  
  * Reads the given CSV file.  
  * Validates headers ("Employee Identifier", "Hours Worked").  
  * For each row:  
    * Parses and normalizes 'Employee Identifier' (strip whitespace, convert to consistent case for case-insensitivity).  
    * Parses and validates 'Hours Worked' (convert to float, treat non-numeric as 0.0 and report).  
    * Returns a list of (employee\_id, hours\_worked, overtime\_type) tuples or similar structure.  
* **sum\_overtime\_hours(records)**:  
  * Takes the list of all processed records.  
  * Uses a collections.defaultdict(lambda: {'Sunday Hours': 0.0, 'Public Holiday Hours': 0.0}) to sum hours for each employee, categorized by overtime\_type.  
  * Returns the dictionary of summed totals.  
* **generate\_output\_csv(employee\_totals, output\_path)**:  
  * Takes the summed employee totals.  
  * Writes the data to Monthly\_Overtime\_Totals.csv in the specified output\_path (e.g., current working directory or a user-defined path if enhanced later).  
  * Includes headers: "Employee Identifier", "Sunday Hours", "Public Holiday Hours".  
* **Helper functions** for error reporting, string normalization, etc., as needed. Type hints will be used for function signatures to improve clarity.

## **6\. Data Flow Overview**

1. **User Interaction (CLI)**: Script starts, displays instructions. User provides input folder path.  
2. **Input Validation**: Script validates the folder path.  
3. **File Discovery & Filtering**: Script scans the input folder, identifies potential CSV files, and validates filenames. Invalid files are reported and skipped.  
4. **CSV Parsing & Validation**: For each validly named CSV:  
   * Headers are validated. If invalid, file is reported and skipped.  
   * Rows are read. 'Employee Identifier' is normalized. 'Hours Worked' is validated (non-numeric becomes 0.0 and is reported).  
5. **Data Summation**: Validated and parsed records (employee ID, hours, type) are collected. A dictionary (e.g., defaultdict) stores the running totals of "Sunday Hours" and "Public Holiday Hours" for each unique (normalized) employee ID.  
6. **Output Generation**: The final summed data is written to Monthly\_Overtime\_Totals.csv.  
7. **Feedback**: User is informed of completion and output file location, or any critical errors.

graph TD  
    Start((Start Script)) \--\> CLI\_Instruct\[Display Instructions & Get Input Path\];  
    CLI\_Instruct \-- Input Folder Path \--\> ValidatePath{Validate Path?};  
    ValidatePath \-- Valid \--\> ScanFolder\[Scan Input Folder for CSVs\];  
    ValidatePath \-- Invalid \--\> CLI\_Error\_Path\[Report Path Error & End\];  
    ScanFolder \--\> LoopFiles{For Each File};  
    LoopFiles \-- File \--\> ValidateFilename{Validate Filename?};  
    ValidateFilename \-- Invalid \--\> CLI\_Error\_File\[Report File Error & Skip\];  
    ValidateFilename \-- Valid \--\> ParseCSV\[Parse CSV & Validate Headers/Rows\];  
    CLI\_Error\_File \--\> LoopFiles;  
    ParseCSV \-- Invalid Row/Header \--\> CLI\_Error\_Row\[Report Row/Header Error & Skip Row/File\];  
    CLI\_Error\_Row \--\> LoopFiles;  
    ParseCSV \-- Valid Data Records \--\> SumData\[Sum Hours per Employee \- Sunday/Holiday\];  
    SumData \--\> LoopFiles;  
    LoopFiles \-- All Files Processed \--\> GenerateOutput\[Generate Output CSV\];  
    GenerateOutput \--\> CLI\_Complete\[Report Completion & Output Path\];  
    CLI\_Complete \--\> End((End Script));

## **7\. Input/Output Specifications**

* **Command-Line Execution**:  
  * python src/automated\_overtime\_calculator.py (from project root).  
  * No command-line arguments for MVP; input path is prompted.  
* **Input Folder**: User-specified path containing overtime CSVs.  
* **Input CSV Files (template\_overtime\_sheet.csv structure):**  
  * **Naming**: YYYY-MM-DD-Sunday.csv or YYYY-MM-DD-Holiday.csv.  
  * **Encoding**: UTF-8 recommended.  
  * **Headers (Row 1\)**: Employee Identifier, Hours Worked  
  * **Data Types**:  
    * Employee Identifier: String (normalized: trimmed, case-insensitive).  
    * Hours Worked: Numeric (float/int). Non-numeric treated as 0.0 (with user notification).  
  * **Template Location**: data/template\_overtime\_sheet.csv.  
* **Output CSV File (Monthly\_Overtime\_Totals.csv):**  
  * **Filename**: Monthly\_Overtime\_Totals.csv (default, saved in current working directory or other communicated location).  
  * **Encoding**: UTF-8.  
  * **Headers (Row 1\)**: Employee Identifier, Sunday Hours, Public Holiday Hours  
  * **Data Content**: One row per unique employee with their total summed Sunday and Public Holiday hours (float).

## **8\. Error Handling Approach (Summary)**

The script will provide clear, user-friendly error messages and warnings via the CLI.

* **Input Folder Issues**: If the path is not found or not a directory, an error is reported, and the script terminates.  
* **No Valid Files**: If no CSVs matching the naming convention are found, this is reported.  
* **Filename Errors**: Files not matching YYYY-MM-DD-Type.csv are reported and skipped.  
* **CSV Structure Errors**: Files not matching template\_overtime\_sheet.csv (e.g., wrong headers) are reported and skipped.  
* **Data Errors**: Non-numeric 'Hours Worked' are treated as 0.0, reported for the specific record/file, and processing continues.  
* General I/O: Standard try-except blocks will handle file read/write issues.  
  The goal is to be robust, continue processing valid data where possible, and guide the user to fix input issues.

## **9\. Project File Structure (Summary)**

A simple structure will be used:

automated-overtime-calculator/  
├── docs/  
│   └── architecture.md         \# This document  
├── data/  
│   ├── input\_examples/         \# Example input CSVs for testing  
│   │   └── ...  
│   └── template\_overtime\_sheet.csv \# Deliverable template  
├── output/                     \# Default for generated output (git-ignored)  
│   └── Monthly\_Overtime\_Totals.csv \# Example output  
├── src/  
│   └── automated\_overtime\_calculator.py \# The Python script  
├── tests/                      \# For future automated tests  
│   └── test\_calculator.py      \# Placeholder  
├── .gitignore  
└── README.md                   \# User guide: setup, run, file prep

The main script is src/automated\_overtime\_calculator.py. The template\_overtime\_sheet.csv is in data/.

## **10\. Testing Strategy (MVP Focus \- Manual)**

Given the 1-day MVP timeframe, testing will be primarily manual, focusing on verifying core functionality and error handling as per the PRD.

* **Key Scenarios**:  
  * Processing correctly formatted and named input files with valid data.  
  * Handling files with incorrect naming conventions (skipped, reported).  
  * Handling CSVs not adhering to the template (skipped, reported).  
  * Handling CSVs with non-numeric 'Hours Worked' values (hours treated as 0, reported).  
  * Handling variations in 'Employee Identifier' (leading/trailing spaces, case differences – ensuring correct summation).  
  * Handling empty input folder or input folder not found.  
  * Handling input folder with no valid CSVs.  
* **Method**:  
  * Create diverse sample CSV files in data/input\_examples/.  
  * Execute the script with these samples.  
  * Manually verify CLI output (instructions, feedback, errors).  
  * Manually verify the content of the generated Monthly\_Overtime\_Totals.csv against expected results (e.g., by manual calculation or comparison with a known-good output).  
* **Performance**: Observe processing time for a typical month's data (30-60 CSVs) to ensure it's within a few minutes.  
* **Usability**: Ensure CLI instructions are clear and actionable for the Payroll Administrator.

## **11\. Change Log**

| Date | Version | Description | Author |
| :---- | :---- | :---- | :---- |
| 2025-05-08 | 1.0 | Initial consolidated architecture document for MVP. | Architect Agent |

