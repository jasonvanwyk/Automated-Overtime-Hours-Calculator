#!/usr/bin/env python3
"""
Automated Overtime Hours Calculator

This script automates the monthly summation of employee overtime hours from multiple CSV files.
It categorizes overtime as "Sunday" or "Public Holiday" based on filenames and generates
a single summary CSV file.
"""

import csv
import datetime
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union


def display_instructions() -> None:
    """Display welcome message and usage instructions."""
    print("\n===== AUTOMATED OVERTIME HOURS CALCULATOR =====\n")
    print("Welcome to the Automated Overtime Hours Calculator!")
    print("This script processes overtime data from CSV files and generates a monthly summary.\n")
    
    print("Developed by Precept Systems (Pty) Ltd")
    print("Contact: 083 288 9052 | info@precept.co.za | www.precept.co.za\n")
    
    print("INSTRUCTIONS:")
    print("1. Prepare your CSV files using the template_overtime_sheet.csv format")
    print("   - Required headers: \"Employee Identifier\", \"Hours Worked\"")
    print("   - Template location: data/template_overtime_sheet.csv\n")
    
    print("2. Name your CSV files using the following convention:")
    print("   - For Sunday overtime: YYYY-MM-DD-Sunday.csv (e.g., 2025-05-05-Sunday.csv)")
    print("   - For Public Holiday overtime: YYYY-MM-DD-Holiday.csv (e.g., 2025-05-01-Holiday.csv)\n")
    
    print("3. Place all your CSV files in a single folder")
    print("   - IMPORTANT: Only place files you want processed in this folder")
    print("   - Any CSV file with the correct naming convention will be processed\n")
    
    print("4. When prompted, provide the full path to this folder")
    print("   - Example: /home/user/overtime_data\n")
    
    print("NOTE: Each run of this program will overwrite the existing output file")
    print("(output/Monthly_Overtime_Totals.csv) if it exists.\n")


def get_input_folder_path() -> Optional[Path]:
    """
    Prompt user for input folder path and validate it.
    
    Returns:
        Path object if valid, None if invalid or exit requested
    """
    print("Please enter the path to the folder containing your overtime CSV files:")
    print("(Type '/q' to exit the program)")
    folder_path_str = input("> ").strip()
    
    # Check if user wants to exit
    if folder_path_str.lower() == '/q':
        print("Exiting program as requested.")
        return None
    
    folder_path = Path(folder_path_str)
    
    if not folder_path.exists():
        print(f"Error: Input folder not found at '{folder_path_str}'. Please check the path and try again.")
        return None
    
    if not folder_path.is_dir():
        print(f"Error: '{folder_path_str}' is not a valid directory. Please provide a folder path.")
        return None
    
    return folder_path


def parse_csv_file(file_path: Path, overtime_type: str) -> Tuple[List[Tuple[str, float, str]], List[str]]:
    """
    Parse a CSV file and extract employee data.
    
    Args:
        file_path: Path to the CSV file
        overtime_type: Type of overtime ("Sunday" or "Public Holiday")
        
    Returns:
        Tuple containing:
            - List of tuples containing (employee_id, hours_worked, overtime_type)
            - List of issues encountered during parsing
    """
    records = []
    issues = []
    
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Read and validate headers
            try:
                headers = next(csv_reader)
            except StopIteration:
                issue = f"File is empty"
                print(f"Warning: File '{file_path.name}' is empty. Skipping.")
                issues.append(issue)
                return records, issues
            
            # Strip BOM character if present
            if len(headers) > 0 and headers[0].startswith('\ufeff'):
                headers[0] = headers[0].replace('\ufeff', '')
                
            if headers != ["Employee Identifier", "Hours Worked"]:
                issue = f"Invalid headers: Found '{','.join(headers)}' instead of 'Employee Identifier,Hours Worked'"
                print(f"Error: File '{file_path.name}' does not have the required headers.")
                print(f"Expected: 'Employee Identifier,Hours Worked'")
                print(f"Found: '{','.join(headers)}'")
                print(f"Skipping file '{file_path.name}'.")
                issues.append(issue)
                return records, issues
            
            # Process data rows
            for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 because row 1 is headers
                if len(row) < 2:
                    issue = f"Row {row_num}: Insufficient data"
                    print(f"Warning: Row {row_num} in '{file_path.name}' has insufficient data. Skipping row.")
                    issues.append(issue)
                    continue
                
                # Normalize employee identifier (trim whitespace, convert to uppercase)
                employee_id = row[0].strip().upper()
                
                # Validate and convert hours worked
                hours_str = row[1].strip()
                try:
                    hours_worked = float(hours_str)
                except ValueError:
                    issue = f"Row {row_num}: Invalid hours value '{hours_str}' for employee '{employee_id}' - treating as 0.0"
                    print(f"Warning: Invalid hours value '{hours_str}' for employee '{employee_id}' in file '{file_path.name}', row {row_num}.")
                    print(f"Treating as 0.0 hours and continuing.")
                    issues.append(issue)
                    hours_worked = 0.0
                
                records.append((employee_id, hours_worked, overtime_type))
    
    except Exception as e:
        error_msg = str(e)
        issue = f"Error processing file: {error_msg}"
        print(f"Error processing file '{file_path.name}': {error_msg}")
        issues.append(issue)
    
    return records, issues


def process_files_in_folder(folder_path: Path) -> Tuple[List[Tuple[str, float, str]], Dict[str, List[str]], Dict[str, List[str]]]:
    """
    Process all valid CSV files in the given folder.
    
    Args:
        folder_path: Path to the folder containing CSV files
        
    Returns:
        Tuple containing:
            - List of all valid records from all processed files
            - Dictionary of skipped files with reasons
            - Dictionary of files with skipped/adjusted entries
    """
    all_records = []
    skipped_files = {}
    files_with_issues = {}
    
    # Find all CSV files in the folder
    csv_files = list(folder_path.glob("*.csv"))
    print(f"Found {len(csv_files)} potential CSV files in '{folder_path}'.")
    
    valid_files_count = 0
    
    # Process each CSV file
    for file_path in csv_files:
        # Validate filename
        filename_pattern = r"^\d{4}-\d{2}-\d{2}-(Sunday|Holiday|sunday|holiday)\.csv$"
        if not re.match(filename_pattern, file_path.name, re.IGNORECASE):
            reason = "Does not match the required naming convention"
            print(f"Skipping file '{file_path.name}' - {reason}.")
            print(f"Expected format: YYYY-MM-DD-Sunday.csv or YYYY-MM-DD-Holiday.csv")
            skipped_files[file_path.name] = reason
            continue
        
        # Extract overtime type from filename
        overtime_type = "Sunday Hours" if "sunday" in file_path.name.lower() else "Public Holiday Hours"
        
        # Parse the file
        print(f"Processing file: {file_path.name}")
        records, issues = parse_csv_file(file_path, overtime_type)
        
        if issues:
            files_with_issues[file_path.name] = issues
        
        if records:
            valid_files_count += 1
            all_records.extend(records)
        elif not issues:  # If no records and no issues reported, it's an empty file with valid headers
            files_with_issues[file_path.name] = ["File contains no data records"]
    
    print(f"Successfully processed {valid_files_count} valid files.")
    
    if valid_files_count == 0:
        print("No valid files were found to process. Please check your input files and try again.")
    
    return all_records, skipped_files, files_with_issues


def sum_overtime_hours(records: List[Tuple[str, float, str]]) -> Dict[str, Dict[str, float]]:
    """
    Sum overtime hours for each employee, categorized by overtime type.
    
    Args:
        records: List of (employee_id, hours_worked, overtime_type) tuples
        
    Returns:
        Dictionary mapping employee IDs to their summed overtime hours by type
    """
    employee_totals = defaultdict(lambda: {"Sunday Hours": 0.0, "Public Holiday Hours": 0.0})
    
    for employee_id, hours_worked, overtime_type in records:
        employee_totals[employee_id][overtime_type] += hours_worked
    
    return employee_totals


def generate_log_file(skipped_files: Dict[str, str], files_with_issues: Dict[str, List[str]], 
                  employee_totals: Dict[str, Dict[str, float]], output_dir: Path) -> Path:
    """
    Generate a log file with details about skipped files and issues.
    
    Args:
        skipped_files: Dictionary of skipped files with reasons
        files_with_issues: Dictionary of files with issues
        employee_totals: Dictionary mapping employee IDs to their overtime hours
        output_dir: Directory where the log file will be saved
        
    Returns:
        Path to the generated log file
    """
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create log filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = output_dir / f"processing_log_{timestamp}.txt"
    
    try:
        with open(log_path, 'w', encoding='utf-8') as log_file:
            log_file.write("===== AUTOMATED OVERTIME HOURS CALCULATOR - PROCESSING LOG =====\n\n")
            log_file.write(f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Add summary statistics
            total_employees = len(employee_totals)
            total_sunday_hours = sum(hours["Sunday Hours"] for hours in employee_totals.values())
            total_holiday_hours = sum(hours["Public Holiday Hours"] for hours in employee_totals.values())
            
            log_file.write(f"SUMMARY STATISTICS:\n")
            log_file.write(f"  - Total Employees: {total_employees}\n")
            log_file.write(f"  - Total Sunday Hours: {total_sunday_hours:.1f}\n")
            log_file.write(f"  - Total Public Holiday Hours: {total_holiday_hours:.1f}\n")
            log_file.write(f"  - Total Overtime Hours: {total_sunday_hours + total_holiday_hours:.1f}\n\n")
            
            # Log skipped files
            if skipped_files:
                log_file.write(f"Files skipped ({len(skipped_files)}):\n\n")
                for filename, reason in skipped_files.items():
                    log_file.write(f"  - {filename}: {reason}\n")
                log_file.write("\n")
            else:
                log_file.write("No files were skipped.\n\n")
            
            # Log files with issues
            if files_with_issues:
                log_file.write(f"Files with issues ({len(files_with_issues)}):\n\n")
                for filename, issues_list in files_with_issues.items():
                    log_file.write(f"  - {filename}:\n")
                    for issue in issues_list:
                        log_file.write(f"      * {issue}\n")
                log_file.write("\n")
            else:
                log_file.write("No issues were encountered during processing.\n\n")
            
            log_file.write("===== END OF LOG =====\n")
        
        return log_path
    
    except Exception as e:
        print(f"Error generating log file: {str(e)}")
        return None


def generate_output_csv(employee_totals: Dict[str, Dict[str, float]], output_path: Path) -> None:
    """
    Generate the output CSV file with summed overtime hours.
    
    Args:
        employee_totals: Dictionary mapping employee IDs to their overtime hours
        output_path: Path where the output file will be saved
    """
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write headers
            csv_writer.writerow(["Employee Identifier", "Sunday Hours", "Public Holiday Hours"])
            
            # Write data rows
            for employee_id, hours in employee_totals.items():
                csv_writer.writerow([
                    employee_id,
                    hours["Sunday Hours"],
                    hours["Public Holiday Hours"]
                ])
        
        print(f"Output successfully generated: {output_path.absolute()}")
    
    except Exception as e:
        print(f"Error generating output file: {str(e)}")


def main() -> None:
    """Main function to orchestrate the entire process."""
    # Track start time for performance reporting
    start_time = __import__('time').time()
    # Display welcome message and instructions
    display_instructions()
    
    # Get input folder path
    folder_path = get_input_folder_path()
    if folder_path is None:
        print("\nProgram terminated.")
        sys.exit(0)
    
    # Process files in the folder
    print(f"\nProcessing files from folder: {folder_path}")
    records, skipped_files, files_with_issues = process_files_in_folder(folder_path)
    
    # If no valid records were found, exit
    if not records:
        print("No valid records found. Output file will not be generated.")
        sys.exit(1)
    
    # Sum overtime hours
    print(f"\nCalculating overtime totals for {len(set(record[0] for record in records))} employees...")
    employee_totals = sum_overtime_hours(records)
    
    # Create output directory path
    output_dir = Path("output")
    
    # Generate output file
    output_path = output_dir / "Monthly_Overtime_Totals.csv"
    
    # Check if output file already exists
    if output_path.exists():
        print(f"\nNote: Existing output file will be overwritten.")
    
    print(f"Generating output file...")
    generate_output_csv(employee_totals, output_path)
    
    # Generate log file
    log_path = generate_log_file(skipped_files, files_with_issues, employee_totals, output_dir)
    
    # Print summary report
    print("\n===== PROCESSING SUMMARY =====\n")
    
    # Add summary statistics
    total_employees = len(employee_totals)
    total_sunday_hours = sum(hours["Sunday Hours"] for hours in employee_totals.values())
    total_holiday_hours = sum(hours["Public Holiday Hours"] for hours in employee_totals.values())
    
    print(f"SUMMARY STATISTICS:\n")
    print(f"  - Total Employees: {total_employees}")
    print(f"  - Total Sunday Hours: {total_sunday_hours:.1f}")
    print(f"  - Total Public Holiday Hours: {total_holiday_hours:.1f}")
    print(f"  - Total Overtime Hours: {total_sunday_hours + total_holiday_hours:.1f}\n")
    
    # Report on skipped files
    if skipped_files:
        print(f"Files skipped ({len(skipped_files)}):\n")
        for filename, reason in skipped_files.items():
            print(f"  - {filename}: {reason}")
        print()
    else:
        print("No files were skipped.\n")
    
    # Report on files with issues
    if files_with_issues:
        print(f"Files with issues ({len(files_with_issues)}):\n")
        for filename, issues_list in files_with_issues.items():
            print(f"  - {filename}:")
            for issue in issues_list:
                print(f"      * {issue}")
        print()
    else:
        print("No issues were encountered during processing.\n")
    
    print("Processing complete!")
    print(f"Output file: {output_path.absolute()}")
    if log_path:
        print(f"Log file: {log_path.absolute()}")


if __name__ == "__main__":
    main()
