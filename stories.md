### Story ID: US1.1
Epic ID: EPIC001
Title: As a Payroll Administrator, I want the script to process all CSV files from a specified input folder so that all my overtime data for the month is included.
Objective: To ensure the script can accept a user-defined folder path and identify all files within it for subsequent processing.
Background/Context:
This story initiates the core file processing capability. The script needs to interact with the file system to locate and access input files. [cite: 140]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py` for functions like `get_input_folder_path()` and the initial part of `process_files_in_folder()`. [cite: 24, 28, 29, 71]
* Relevant PRD Sections: User Story 1.1[cite: 140], Acceptance Criteria 1.1.1-1.1.3. [cite: 141, 142, 143]
* The script will prompt the user for the input folder path. [cite: 9, 26, 28, 102, 141]
* It will then iterate through all files in the specified folder. [cite: 29, 103, 142]

Acceptance Criteria (AC):
* **AC 1.1.1:**
    * Given the script is executed
    * When the user is prompted for an input folder
    * Then the script successfully accepts a valid folder path provided by the user. [cite: 141]
* **AC 1.1.2:**
    * Given a valid input folder path is provided
    * When the script processes the folder
    * Then it iterates through all entries (files and subdirectories) within that specified folder. [cite: 142]
* **AC 1.1.3:**
    * Given the script is iterating through files in the input folder
    * When it encounters a file with a ".csv" extension
    * Then the script correctly identifies it as a CSV file for potential processing. [cite: 143]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Implement `get_input_folder_path()` function in `src/automated_overtime_calculator.py`: [cite: 28]
    * [ ] Prompt user to enter the path to an input folder. [cite: 26, 141]
    * [ ] Read the path provided by the user.
    * [ ] Perform basic validation (path exists, is a directory) as per ArchDoc Sec 5. [cite: 28, 63]
    * [ ] Return the validated folder path.
* [ ] Implement initial part of `process_files_in_folder(folder_path)` function in `src/automated_overtime_calculator.py`: [cite: 29]
    * [ ] Accept `folder_path` as an argument.
    * [ ] Use `pathlib` to iterate through all files in `folder_path`. [cite: 18, 29]
    * [ ] For each file, check if it has a ".csv" extension. [cite: 143]
* [ ] Add function calls within `main()` in `src/automated_overtime_calculator.py`: [cite: 25]
    * [ ] Call `get_input_folder_path()` to get the folder path from the user. [cite: 26]
    * [ ] Pass the obtained path to `process_files_in_folder()`. [cite: 26]
* [ ] Create unit tests for `get_input_folder_path()` in `tests/test_calculator.py` (Placeholder, as MVP testing is manual [cite: 71, 72]):
    * [ ] Test with a valid directory path.
    * [ ] Test with an invalid/non-existent path.
    * [ ] Test with a path that is a file, not a directory.
* [ ] Create unit tests for the file iteration part of `process_files_in_folder()` in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with a folder containing multiple CSV files.
    * [ ] Test with a folder containing no CSV files.
    * [ ] Test with a folder containing mixed file types.
    * [ ] Test with an empty folder.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Developer to create sample folders and files for testing these scenarios locally as per ArchDoc Sec 10. [cite: 77]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72] (Unit Tests via PyTest if automated, target framework for future).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script successfully prompts for and reads files from a directory, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US1.2
Epic ID: EPIC001
Title: As a Payroll Administrator, I want the script to only process CSV files that match the required naming convention (YYYY-MM-DD-Sunday.csv or YYYY-MM-DD-Holiday.csv) so that overtime is correctly categorized.
Objective: To implement strict filename validation to ensure only correctly named CSV files are processed and to categorize them by overtime type (Sunday/Holiday). [cite: 144]
Background/Context:
This story focuses on filtering and categorizing input files based on a strict naming convention. This is crucial for correct overtime type assignment. [cite: 3, 6, 85, 105, 144]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py`, specifically within the `process_files_in_folder()` function. [cite: 24, 29, 71]
* Filename Convention: `YYYY-MM-DD-Sunday.csv` or `YYYY-MM-DD-Holiday.csv`. [cite: 6, 10, 57, 105, 114, 144, 163]
* Relevant PRD Sections: User Story 1.2[cite: 144], Acceptance Criteria 1.2.1-1.2.3. [cite: 145, 146, 147]
* The script needs to parse the filename to determine the overtime type. [cite: 106, 145]

Acceptance Criteria (AC):
* **AC 1.2.1:**
    * Given a CSV file with a name matching "YYYY-MM-DD-Sunday.csv" or "YYYY-MM-DD-Holiday.csv"
    * When the script validates the filename
    * Then the script correctly identifies the overtime type as "Sunday" or "Public Holiday" respectively. [cite: 145]
* **AC 1.2.2:**
    * Given a file that does not match the required naming convention (e.g., "report.csv", "2023-13-01-Sunday.csv", "2023-12-31-Weekend.csv")
    * When the script validates the filename
    * Then the file is skipped, and a message is logged/displayed to the user indicating the filename error and that the file was skipped. [cite: 16, 65, 118, 146, 179]
* **AC 1.2.3:**
    * Given a CSV file with a correctly formatted name (e.g., "2024-03-10-Sunday.csv")
    * When the script validates the filename
    * Then the script successfully extracts the date components (YYYY, MM, DD) from the filename (though not explicitly used for MVP aggregation, this is for future potential). [cite: 147]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Enhance `process_files_in_folder(folder_path)` function in `src/automated_overtime_calculator.py`: [cite: 29]
    * [ ] For each identified CSV file:
        * [ ] Implement logic to parse the filename (e.g., using string methods or regex). [cite: 21]
        * [ ] Validate if the filename strictly matches `YYYY-MM-DD-Sunday.csv` or `YYYY-MM-DD-Holiday.csv` convention. [cite: 10, 29]
        * [ ] If valid, extract the overtime type ("Sunday" or "Public Holiday"). [cite: 145]
        * [ ] If valid, extract date components (YYYY, MM, DD). [cite: 147]
        * [ ] If invalid, print/log an error message to the console specifying the filename and reason for skipping. [cite: 15, 62, 65, 118, 146, 179]
        * [ ] Skip processing for invalid filenames.
* [ ] Create unit tests for filename validation logic within `process_files_in_folder()` in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with correctly named "Sunday" file (e.g., "2023-12-31-Sunday.csv").
    * [ ] Test with correctly named "Holiday" file (e.g., "2024-01-01-Holiday.csv").
    * [ ] Test with incorrect date format (e.g., "2023-31-12-Sunday.csv").
    * [ ] Test with incorrect type suffix (e.g., "2023-12-31-Sonday.csv").
    * [ ] Test with missing parts (e.g., "2023-12-Sunday.csv").
    * [ ] Test with extra parts (e.g., "2023-12-31-Sunday-Extra.csv").
    * [ ] Test with non-CSV extension but matching name pattern.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Developer to create sample files with various correct and incorrect names for testing as per ArchDoc Sec 10. [cite: 73, 77]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 73] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script correctly categorizes or skips files based on naming convention, appropriate messages are displayed, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US1.3
Epic ID: EPIC001
Title: As a Payroll Administrator, I want the script to read data only from CSV files that follow the template_overtime_sheet.csv (headers: Employee Identifier, Hours Worked) so that data is interpreted correctly.
Objective: To ensure that the script validates the structure of CSV files against a defined template, specifically checking for correct headers, and parses the required data fields. [cite: 148]
Background/Context:
This story deals with the integrity of the data within the CSV files. The script must ensure that CSV files adhere to the expected structure to prevent errors during data parsing and aggregation. [cite: 11, 104, 148]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py`, implementing the `parse_csv_file(file_path, overtime_type)` function. [cite: 24, 30, 31, 71]
* CSV Template: `template_overtime_sheet.csv` with headers "Employee Identifier", "Hours Worked". [cite: 6, 11, 58, 59, 72, 104, 113, 129, 148, 162, 180, 193]
* Relevant PRD Sections: User Story 1.3[cite: 148], Acceptance Criteria 1.3.1-1.3.3. [cite: 149, 150, 151]
* The `csv` module should be used for parsing. [cite: 19]

Acceptance Criteria (AC):
* **AC 1.3.1:**
    * Given a CSV file that has passed filename validation
    * When the script attempts to parse the file
    * Then it correctly checks if the first row (headers) contains exactly "Employee Identifier" and "Hours Worked". [cite: 11, 42, 119, 149]
* **AC 1.3.2:**
    * Given a CSV file with incorrect or missing headers (e.g., "Emp ID", "Hrs" or only "Employee Identifier")
    * When the script attempts to parse the file
    * Then the file is skipped, and a message is logged/displayed to the user indicating the header mismatch and that the file was skipped. [cite: 16, 43, 66, 119, 150, 180]
* **AC 1.3.3:**
    * Given a CSV file with correct headers
    * When the script parses the data rows
    * Then it successfully extracts the values for 'Employee Identifier' and 'Hours Worked' from each data row. [cite: 12, 31, 107, 151]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Implement `parse_csv_file(file_path, overtime_type)` function in `src/automated_overtime_calculator.py`: [cite: 31]
    * [ ] Accept `file_path` and `overtime_type` as arguments.
    * [ ] Open and read the CSV file using the `csv` module. [cite: 19, 31]
    * [ ] Read the header row.
    * [ ] Validate headers: must be "Employee Identifier" and "Hours Worked". [cite: 11, 31, 42, 149]
    * [ ] If headers are incorrect, print/log an error message (specifying filename and issue) and return an indicator of failure (e.g., empty list or specific error status). [cite: 15, 43, 66, 119, 150, 180]
    * [ ] If headers are correct, iterate through subsequent rows: [cite: 32]
        * [ ] Parse 'Employee Identifier' (String). [cite: 12, 151]
        * [ ] Parse 'Hours Worked' (String, to be validated as numeric later). [cite: 12, 151]
        * [ ] Store these as structured data (e.g., list of tuples/dictionaries). [cite: 34]
    * [ ] Return the list of parsed records (e.g., `[(employee_id, hours_str, overtime_type), ...]`). [cite: 34]
* [ ] Modify `process_files_in_folder(folder_path)` in `src/automated_overtime_calculator.py`: [cite: 29]
    * [ ] For each validly named file, call `parse_csv_file()`. [cite: 30]
    * [ ] Collect all valid records from all successfully parsed files. [cite: 30, 45]
* [ ] Create unit tests for `parse_csv_file()` in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with a CSV matching the template perfectly.
    * [ ] Test with a CSV missing "Employee Identifier" header.
    * [ ] Test with a CSV missing "Hours Worked" header.
    * [ ] Test with a CSV having extra headers.
    * [ ] Test with a CSV having headers in the wrong order.
    * [ ] Test with an empty CSV file (only headers).
    * [ ] Test with a CSV file that has no headers but has data.
    * [ ] Test with a CSV file that is completely empty.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Developer to create `data/template_overtime_sheet.csv`. [cite: 59, 72, 129]
* MANUAL STEP: Developer to create sample CSV files with various correct/incorrect header structures for testing as per ArchDoc Sec 10. [cite: 74, 77]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 74] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script correctly validates CSV headers, parses data from valid files, skips invalid files with appropriate messages, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US1.4
Epic ID: EPIC001
Title: As a Payroll Administrator, I want the script to accurately sum all "Sunday Hours" for each employee from all relevant Sunday CSV files.
Objective: To implement logic that correctly aggregates "Sunday Hours" for each unique employee, handling data variations and non-numeric hour values gracefully. [cite: 152]
Background/Context:
This story focuses on the core calculation logic for Sunday overtime. It involves normalizing employee identifiers for accurate grouping and validating hour values. [cite: 13, 108, 152]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py`, implementing data normalization within `parse_csv_file()` and aggregation within `sum_overtime_hours()`. [cite: 24, 32, 33, 34, 71]
* Data Handling: 'Employee Identifier' normalization (trim whitespace, case-insensitive). [cite: 12, 32, 58, 75, 154] 'Hours Worked' validation (non-numeric as 0.0, log/report). [cite: 13, 33, 44, 59, 67, 74, 120, 155, 181]
* Relevant PRD Sections: User Story 1.4[cite: 152], Acceptance Criteria 1.4.1-1.4.3. [cite: 153, 154, 155]
* `collections.defaultdict` is recommended for summation. [cite: 20, 35, 46]

Acceptance Criteria (AC):
* **AC 1.4.1:**
    * Given multiple "*-Sunday.csv" files containing valid data for various employees
    * When the script processes these files
    * Then it correctly sums all 'Hours Worked' for each unique Employee Identifier from these Sunday files. [cite: 153]
* **AC 1.4.2:**
    * Given Employee Identifiers with variations such as leading/trailing spaces (e.g., " EMP001 ", "EMP001") or different cases (e.g., "emp001", "EMP001")
    * When the script aggregates hours
    * Then it treats these variations as the same employee and sums their hours correctly under a single normalized identifier. [cite: 12, 32, 75, 135, 154, 158]
* **AC 1.4.3:**
    * Given a record in a Sunday CSV file has a non-numeric value for 'Hours Worked' (e.g., "N/A", "five")
    * When the script processes this record
    * Then it treats these hours as 0.0 for summation, logs/displays a message indicating the specific record/file and the invalid data, and continues processing other valid records and files. [cite: 13, 33, 44, 67, 74, 120, 155, 181]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Enhance `parse_csv_file(file_path, overtime_type)` function in `src/automated_overtime_calculator.py`: [cite: 31]
    * [ ] For each parsed 'Employee Identifier':
        * [ ] Normalize it: trim leading/trailing whitespace. [cite: 12, 32, 154]
        * [ ] Normalize it: convert to a consistent case (e.g., uppercase) for case-insensitive matching. [cite: 12, 32, 154]
    * [ ] For each parsed 'Hours Worked' string:
        * [ ] Attempt to convert to a float. [cite: 33]
        * [ ] If conversion fails (non-numeric), set hours to 0.0 for that record. [cite: 13, 33, 44, 67, 155]
        * [ ] Print/log a warning message to the console, including filename, row number (if possible), employee identifier, and the invalid hours value. [cite: 13, 15, 33, 44, 67, 120, 155, 181]
    * [ ] Ensure the returned records contain the normalized employee ID and validated (float) hours.
* [ ] Implement `sum_overtime_hours(records)` function in `src/automated_overtime_calculator.py`: [cite: 34]
    * [ ] Accept the list of all processed records `[(employee_id, hours_worked_float, overtime_type), ...]`.
    * [ ] Initialize `collections.defaultdict(lambda: {'Sunday Hours': 0.0, 'Public Holiday Hours': 0.0})`. [cite: 20, 35, 46]
    * [ ] Iterate through the records:
        * [ ] If `overtime_type` is "Sunday", add `hours_worked_float` to `employee_totals[employee_id]['Sunday Hours']`. [cite: 35, 108, 153]
    * [ ] Return the `employee_totals` dictionary. [cite: 36]
* [ ] Modify `main()` to call `sum_overtime_hours()` with the collected records. [cite: 26]
* [ ] Create unit tests for 'Employee Identifier' normalization in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with leading spaces, trailing spaces, mixed case.
* [ ] Create unit tests for 'Hours Worked' validation in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with valid integer, valid float, "0", "0.0".
    * [ ] Test with non-numeric strings ("abc", "N/A"), negative numbers (clarify handling, assume 0.0 if not specified).
    * [ ] Test with empty string for hours.
* [ ] Create unit tests for `sum_overtime_hours()` for Sunday hours in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with single employee, single Sunday record.
    * [ ] Test with single employee, multiple Sunday records.
    * [ ] Test with multiple employees, multiple Sunday records each.
    * [ ] Test with records having 0.0 hours.
    * [ ] Test with only Holiday records (Sunday hours should be 0).
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Developer to create sample Sunday CSVs with varied Employee Identifiers and Hours Worked data for testing, including non-numeric values, as per ArchDoc Sec 10. [cite: 74, 75, 77]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 74, 75] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script correctly aggregates Sunday hours, handles data variations and errors gracefully with appropriate messages, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US1.5
Epic ID: EPIC001
Title: As a Payroll Administrator, I want the script to accurately sum all "Public Holiday Hours" for each employee from all relevant Holiday CSV files.
Objective: To implement logic that correctly aggregates "Public Holiday Hours" for each unique employee, handling data variations and non-numeric hour values gracefully, mirroring the Sunday hours functionality. [cite: 156]
Background/Context:
This story is parallel to US1.4 but focuses on "Public Holiday" overtime. It leverages the same normalization and validation logic. [cite: 109, 156]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py`, primarily enhancing the `sum_overtime_hours()` function. Normalization and validation logic from US1.4 in `parse_csv_file()` is reused. [cite: 24, 32, 33, 34, 71]
* Data Handling: 'Employee Identifier' normalization (trim whitespace, case-insensitive) already covered. [cite: 12, 32, 58, 75, 158] 'Hours Worked' validation (non-numeric as 0.0, log/report) already covered. [cite: 13, 33, 44, 59, 67, 74, 120, 159]
* Relevant PRD Sections: User Story 1.5[cite: 156], Acceptance Criteria 1.5.1-1.5.3. [cite: 157, 158, 159]
* `collections.defaultdict` is used for summation. [cite: 20, 35, 46]

Acceptance Criteria (AC):
* **AC 1.5.1:**
    * Given multiple "*-Holiday.csv" files containing valid data for various employees
    * When the script processes these files
    * Then it correctly sums all 'Hours Worked' for each unique Employee Identifier from these Holiday files. [cite: 157]
* **AC 1.5.2:**
    * Given Employee Identifiers with variations such as leading/trailing spaces or different cases in Holiday files
    * When the script aggregates hours
    * Then it treats these variations as the same employee and sums their Public Holiday hours correctly under a single normalized identifier. [cite: 12, 32, 75, 135, 158]
* **AC 1.5.3:**
    * Given a record in a Holiday CSV file has a non-numeric value for 'Hours Worked'
    * When the script processes this record
    * Then it treats these hours as 0.0 for summation, logs/displays a message, and continues processing. [cite: 13, 33, 44, 67, 74, 120, 159, 181]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Ensure `parse_csv_file(file_path, overtime_type)` already handles normalization and 'Hours Worked' validation as per US1.4. No new changes should be needed here for this story if US1.4 is complete.
* [ ] Enhance `sum_overtime_hours(records)` function in `src/automated_overtime_calculator.py`: [cite: 34]
    * [ ] (Ensure defaultdict is initialized as `lambda: {'Sunday Hours': 0.0, 'Public Holiday Hours': 0.0}`) [cite: 35]
    * [ ] Iterate through the records:
        * [ ] If `overtime_type` is "Public Holiday" (or "Holiday" based on parsing), add `hours_worked_float` to `employee_totals[employee_id]['Public Holiday Hours']`. [cite: 35, 109, 157]
* [ ] Create unit tests for `sum_overtime_hours()` for Public Holiday hours in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with single employee, single Holiday record.
    * [ ] Test with single employee, multiple Holiday records.
    * [ ] Test with multiple employees, multiple Holiday records each.
    * [ ] Test with only Sunday records (Holiday hours should be 0).
    * [ ] Test with mixed Sunday and Holiday records for the same employee.
    * [ ] Test with records already handled by US1.4 for normalization and validation of Employee ID and Hours.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Developer to create sample Holiday CSVs with varied Employee Identifiers and Hours Worked data for testing, including non-numeric values, as per ArchDoc Sec 10. [cite: 74, 75, 77]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 74, 75] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script correctly aggregates Public Holiday hours, handles data variations and errors gracefully with appropriate messages, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US2.1
Epic ID: EPIC002
Title: As a Payroll Administrator, when I run the script, I want to see a clear welcome message and instructions so I know how to use it correctly.
Objective: To provide the user with essential information on script usage, input file preparation (template and naming), and input folder specification via the CLI. [cite: 160]
Background/Context:
This story focuses on the user interface aspect, ensuring the Payroll Administrator understands how to prepare data and run the script. Clear instructions are paramount for usability. [cite: 8, 15, 80, 97, 113, 114, 115, 125, 126, 129, 130, 160, 199]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Target Path: `src/automated_overtime_calculator.py`, implementing a `display_instructions()` function and calling it from `main()`. [cite: 24, 25, 27, 71]
* Relevant PRD Sections: User Story 2.1[cite: 160], Acceptance Criteria 2.1.1-2.1.5. [cite: 161, 162, 163, 164, 165]
* Instructions must cover:
    * Welcome message. [cite: 161]
    * Use of `template_overtime_sheet.csv`. [cite: 113, 162]
    * Filename convention: `YYYY-MM-DD-Sunday.csv` / `YYYY-MM-DD-Holiday.csv`. [cite: 114, 163]
    * Input folder preparation. [cite: 114, 164]
    * How to provide the input folder path. [cite: 114, 165]

Acceptance Criteria (AC):
* **AC 2.1.1:**
    * Given the script is executed
    * When it starts
    * Then a welcoming message is displayed to the user on the CLI. [cite: 161]
* **AC 2.1.2:**
    * Given the script is executed
    * When instructions are displayed
    * Then the instructions clearly state the requirement to use the `template_overtime_sheet.csv` for input files, specifying its headers ("Employee Identifier", "Hours Worked"). [cite: 113, 162]
* **AC 2.1.3:**
    * Given the script is executed
    * When instructions are displayed
    * Then the instructions clearly display the exact required file naming conventions: `YYYY-MM-DD-Sunday.csv` and `YYYY-MM-DD-Holiday.csv`. [cite: 114, 163]
* **AC 2.1.4:**
    * Given the script is executed
    * When instructions are displayed
    * Then the instructions clearly explain how to prepare an input folder containing these correctly named and formatted CSV files. [cite: 114, 164]
* **AC 2.1.5:**
    * Given the script is executed
    * When instructions are displayed
    * Then the script clearly explains how the user will be prompted to provide the path to this input folder. [cite: 114, 165]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25]

Subtask Checklist:
* [ ] Implement `display_instructions()` function in `src/automated_overtime_calculator.py`: [cite: 27]
    * [ ] Print a welcome message (e.g., "Welcome to the Automated Overtime Hours Calculator!"). [cite: 161]
    * [ ] Print instructions about `template_overtime_sheet.csv`: [cite: 113, 162]
        * Required headers: "Employee Identifier", "Hours Worked".
        * Location of template: `data/template_overtime_sheet.csv`. [cite: 59, 72]
    * [ ] Print instructions about file naming convention: `YYYY-MM-DD-Sunday.csv` and `YYYY-MM-DD-Holiday.csv`. [cite: 114, 163]
    * [ ] Print instructions on preparing the input folder (placing files there). [cite: 114, 164]
    * [ ] Print instructions on how the script will ask for the input folder path. [cite: 114, 165]
* [ ] Call `display_instructions()` at the beginning of the `main()` function in `src/automated_overtime_calculator.py`. [cite: 25]
* [ ] Create unit tests for `display_instructions()` in `tests/test_calculator.py` (Placeholder, may involve capturing stdout):
    * [ ] Verify that all key instruction points (welcome, template, naming, folder prep, path input) are present in the output.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Review the displayed instructions for clarity and completeness from a Payroll Administrator's perspective as per ArchDoc Sec 10. [cite: 80, 126]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 80] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, clear and comprehensive instructions are displayed on script startup, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US2.2
Epic ID: EPIC002
Title: As a Payroll Administrator, I want to receive feedback during the script's operation so I know it's working and when it's finished.
Objective: To provide the user with status updates during processing and a clear confirmation message upon completion, including the output file details. [cite: 166]
Background/Context:
This story is about keeping the user informed during script execution. Feedback messages improve user experience by indicating progress and confirming successful completion or issues. [cite: 8, 15, 115, 130, 166]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Target Path: `src/automated_overtime_calculator.py`, within `main()`, `process_files_in_folder()`, and at the end of script execution. [cite: 24, 25, 29, 71]
* Relevant PRD Sections: User Story 2.2[cite: 166], Acceptance Criteria 2.2.1-2.2.3. [cite: 167, 168, 169]

Acceptance Criteria (AC):
* **AC 2.2.1:**
    * Given the script has received a valid input folder path
    * When it starts processing files
    * Then a message is displayed indicating the number of files it is attempting to process and from which folder (e.g., "Processing X files from [folder path]..."). [cite: 115, 167]
* **AC 2.2.2:**
    * Given the script has successfully processed all valid files and generated the output
    * When it completes
    * Then a success message is displayed, including the name and path of the generated output file (e.g., "Processing complete. Output saved to output/Monthly_Overtime_Totals.csv"). [cite: 15, 48, 115, 168]
* **AC 2.2.3:**
    * Given the input folder contains no files matching the naming convention (after iterating through all files)
    * When the file processing stage finishes
    * Then a clear message is displayed to the user stating that no valid files were found to process. [cite: 16, 64, 117, 169]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25]

Subtask Checklist:
* [ ] In `process_files_in_folder()` in `src/automated_overtime_calculator.py`:
    * [ ] Before iterating through files, print a message like "Attempting to process files from [folder_path]...". A more precise count can be added after an initial scan or by processing a list of found files.
    * [ ] Alternative for AC 2.2.1: After identifying potential CSVs and before filtering by name, display "Found N potential CSV files to analyze...". Then, during filtering, messages for skipped files are already covered.
* [ ] In `main()` function in `src/automated_overtime_calculator.py`:
    * [ ] After `process_files_in_folder()` returns the list of files it found and attempted to process:
        * [ ] Display a message like "Processing X identified files...". [cite: 115, 167] (This can be refined based on when the count of "to be processed" files is known).
    * [ ] After successful output generation by `generate_output_csv()`:
        * [ ] Print a success message indicating completion and the full path to `Monthly_Overtime_Totals.csv`. [cite: 15, 48, 115, 168] (e.g., using `os.path.abspath()` for the output file path if it's relative). Default output location is `output/Monthly_Overtime_Totals.csv`. [cite: 60, 70]
    * [ ] If, after `process_files_in_folder()`, the list of records to sum is empty and no errors were reported that terminated the script (meaning no valid files were found or all files were skipped due to naming/structure):
        * [ ] Print a message indicating that no valid files were found or no data could be processed. [cite: 64, 117, 169] (This may need careful logic to distinguish from other error states).
* [ ] Create unit tests for feedback messages (Placeholder, may involve capturing stdout):
    * [ ] Test scenario where files are processed, verify completion message.
    * [ ] Test scenario where no valid files are found, verify "no valid files" message.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Run script with various scenarios (files present, no valid files) to check feedback clarity as per ArchDoc Sec 10. [cite: 73, 76, 77, 78]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 78] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, user receives appropriate feedback during processing and on completion/failure, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US3.1
Epic ID: EPIC003
Title: As a Payroll Administrator, I want the script to generate a single CSV output file named Monthly_Overtime_Totals.csv containing the aggregated overtime hours.
Objective: To ensure the script produces a correctly formatted CSV output file with the aggregated Sunday and Public Holiday hours for every employee found in the input files. [cite: 170]
Background/Context:
This story covers the final output of the script. The generated CSV must conform to specific header and data requirements. [cite: 7, 14, 47, 90, 96, 110, 111, 112, 170, 192]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Type hints should be used for function signatures as per ArchDoc Sec 5. [cite: 39]
* Target Path: `src/automated_overtime_calculator.py`, implementing `generate_output_csv(employee_totals, output_path)`. [cite: 24, 26, 36, 37, 71]
* Output File: `Monthly_Overtime_Totals.csv` in the `output/` directory (or current working directory if `output/` doesn't exist or isn't specified for MVP). [cite: 14, 37, 60, 70, 110, 172]
* Output Headers: "Employee Identifier", "Sunday Hours", "Public Holiday Hours". [cite: 14, 38, 61, 96, 111, 173]
* Relevant PRD Sections: User Story 3.1[cite: 170], Acceptance Criteria 3.1.1-3.1.5. [cite: 171, 172, 173, 174, 175]
* The `csv` module should be used for writing the output. [cite: 19]

Acceptance Criteria (AC):
* **AC 3.1.1:**
    * Given valid input files have been processed and data aggregated successfully
    * When the script is instructed to generate output
    * Then a CSV file is created in the specified output location. [cite: 171]
* **AC 3.1.2:**
    * Given the output CSV file is generated
    * When its name is checked
    * Then the file is named `Monthly_Overtime_Totals.csv`. [cite: 60, 172] (Path: `output/Monthly_Overtime_Totals.csv` [cite: 70])
* **AC 3.1.3:**
    * Given the output CSV file is generated
    * When its header row is inspected
    * Then the headers are exactly "Employee Identifier", "Sunday Hours", "Public Holiday Hours" in that order. [cite: 14, 38, 61, 111, 173]
* **AC 3.1.4:**
    * Given multiple employees had overtime hours in the input files
    * When the output CSV is inspected
    * Then it includes a distinct row for every unique employee who had hours recorded in any of the valid input files. [cite: 112, 174]
* **AC 3.1.5:**
    * Given an employee has aggregated Sunday and/or Public Holiday hours
    * When their row in the output CSV is inspected
    * Then the "Sunday Hours" and "Public Holiday Hours" columns correctly reflect the summed totals (as floats) for that employee. [cite: 61, 175]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25, 39]

Subtask Checklist:
* [ ] Implement `generate_output_csv(employee_totals, output_path_str)` function in `src/automated_overtime_calculator.py`: [cite: 36]
    * [ ] Accept `employee_totals` dictionary and `output_path_str` (e.g., "output/Monthly_Overtime_Totals.csv") as arguments.
    * [ ] Ensure the output directory (e.g., `output/`) exists. If not, create it (or decide MVP will write to current dir). ArchDoc Sec 7 implies `output/` is the default. [cite: 70] For MVP, writing to current working directory or a predefined `output/` folder is fine. Let's assume `output/` and create if not exists.
    * [ ] Construct the full output file path using `pathlib`. [cite: 18]
    * [ ] Open the file for writing using the `csv` module. [cite: 19, 37]
    * [ ] Write the header row: "Employee Identifier", "Sunday Hours", "Public Holiday Hours". [cite: 38, 61, 173]
    * [ ] Iterate through the `employee_totals` dictionary:
        * [ ] For each employee, write a row with their normalized Employee Identifier, total Sunday Hours, and total Public Holiday Hours. [cite: 37, 61, 174, 175]
        * [ ] Ensure hours are formatted as numbers (floats).
* [ ] In `main()` function in `src/automated_overtime_calculator.py`: [cite: 25]
    * [ ] Define the output file path (e.g., `output/Monthly_Overtime_Totals.csv`). [cite: 70]
    * [ ] Call `generate_output_csv()` with the summed totals and the output path. [cite: 26]
* [ ] Add `output/` directory to `.gitignore` if it doesn't exist already. (ArchDoc implies it's git-ignored [cite: 70]).
* [ ] Create unit tests for `generate_output_csv()` in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with typical `employee_totals` data, verify file creation and content (headers, data rows, correct values).
    * [ ] Test with empty `employee_totals` (should create file with only headers).
    * [ ] Test values are correctly formatted as numbers.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Verify the generated `Monthly_Overtime_Totals.csv` against manually calculated totals for test datasets as per ArchDoc Sec 10. [cite: 73, 78, 136]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 73, 78, 136] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script generates `Monthly_Overtime_Totals.csv` in the correct format and location with accurate data, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US3.2
Epic ID: EPIC003
Title: As a Payroll Administrator, if I provide an incorrect input folder path, I want the script to inform me of the error so I can correct it.
Objective: To implement robust error handling for invalid input folder paths, providing clear messages to the user and terminating gracefully. [cite: 176]
Background/Context:
This story addresses a critical error condition at the start of script execution. The user must be clearly informed if the provided input path is unusable. [cite: 16, 28, 63, 98, 116, 176]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Target Path: `src/automated_overtime_calculator.py`, within the `get_input_folder_path()` function or immediately after its call in `main()`. [cite: 24, 25, 28, 71]
* Relevant PRD Sections: User Story 3.2[cite: 176], Acceptance Criteria 3.2.1. [cite: 177]
* Error handling should be user-friendly. [cite: 62]

Acceptance Criteria (AC):
* **AC 3.2.1:**
    * Given the user provides an input folder path that does not exist, or is a file instead of a directory
    * When the script validates this path
    * Then a clear error message is displayed (e.g., "Error: Input folder not found at [path]. Please check the path and try again." or "Error: [path] is not a directory.") and the script terminates gracefully. [cite: 15, 28, 41, 63, 116, 177]
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25]

Subtask Checklist:
* [ ] Enhance `get_input_folder_path()` function in `src/automated_overtime_calculator.py`: [cite: 28]
    * [ ] After getting path input from the user:
        * [ ] Use `pathlib.Path` to check if the path exists. [cite: 18]
        * [ ] If not, print an error message like "Error: Input folder not found at [path]. Please check the path and try again." [cite: 177]
        * [ ] Use `pathlib.Path.is_dir()` to check if it's a directory. [cite: 18]
        * [ ] If it exists but is not a directory, print an error message like "Error: [path] is not a valid directory. Please provide a folder path."
        * [ ] In case of error, the function should indicate failure (e.g., return `None` or raise an exception to be caught in `main`). For MVP, returning `None` and checking in `main` is simpler.
* [ ] Modify `main()` function in `src/automated_overtime_calculator.py`: [cite: 25]
    * [ ] After calling `get_input_folder_path()`:
        * [ ] Check if the returned path is valid (not `None`).
        * [ ] If invalid (e.g., `None`), gracefully terminate the script (e.g., `sys.exit()` or simply return from `main`).
* [ ] Create unit tests for `get_input_folder_path()` for error conditions in `tests/test_calculator.py` (Placeholder):
    * [ ] Test with a non-existent path.
    * [ ] Test with a path that points to an existing file (not a directory).
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Test by running the script and providing invalid folder paths (non-existent, path to a file) to verify error messages and graceful termination as per ArchDoc Sec 10. [cite: 76, 78]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 76, 78] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script handles invalid input folder paths correctly with clear error messages and graceful termination, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---
Story ID: US3.3
Epic ID: EPIC003
Title: As a Payroll Administrator, if my input files are not named correctly or are not in the correct CSV format, I want the script to notify me about these specific files so I can fix them.
Objective: To ensure the script provides specific error messages for files that fail validation (naming convention or CSV structure/headers) and skips them, allowing other valid files to be processed. [cite: 178]
Background/Context:
This story combines error reporting for previously defined validation steps (US1.2 for filenames, US1.3 for CSV structure). The key is that these errors should not halt the entire process if other valid files exist. [cite: 16, 17, 65, 66, 98, 118, 119, 120, 178]
* Adhere to project coding standards defined in ArchDoc Sec 5 (PEP 8). [cite: 25]
* Target Path: `src/automated_overtime_calculator.py`, within `process_files_in_folder()` and `parse_csv_file()`. [cite: 24, 29, 31, 71]
* Relevant PRD Sections: User Story 3.3[cite: 178], Acceptance Criteria 3.3.1-3.3.3. [cite: 179, 180, 181]
* This also includes handling non-numeric 'Hours Worked' by reporting and treating as zero (already covered in US1.4/US1.5 logic but reiterated here for error messaging visibility). [cite: 13, 33, 44, 59, 67, 74, 120, 155, 159, 181]

Acceptance Criteria (AC):
* **AC 3.3.1:**
    * Given an input folder contains files with names not conforming to `YYYY-MM-DD-Sunday.csv` or `YYYY-MM-DD-Holiday.csv`
    * When the script processes the folder
    * Then a message is logged/displayed for each non-conforming file, indicating the filename and that it's being skipped, and these files are not processed further. [cite: 15, 65, 118, 146, 179] (Covered by US1.2)
* **AC 3.3.2:**
    * Given a CSV file (that passed filename validation) does not have the required headers ("Employee Identifier", "Hours Worked")
    * When the script attempts to parse this file
    * Then a message is logged/displayed for this file, indicating the filename and the header issue, and this file is skipped. [cite: 15, 43, 66, 119, 150, 180] (Covered by US1.3)
* **AC 3.3.3:**
    * Given a record within an otherwise valid CSV file has a non-numeric value for 'Hours Worked'
    * When the script processes this record
    * Then a message is logged/displayed (including filename, ideally row identifier, and the problematic value), the hours for this specific record are treated as zero, and processing continues for other records/files. [cite: 13, 15, 33, 44, 67, 120, 155, 159, 181] (Covered by US1.4/US1.5)
* **AC (Implied):** Adherence to referenced general coding/documentation standards. [cite: 25]

Subtask Checklist:
* [ ] Ensure `process_files_in_folder()` correctly implements logging/displaying messages for skipping files due to incorrect naming conventions (as per US1.2). [cite: 29, 65, 179]
* [ ] Ensure `parse_csv_file()` correctly implements logging/displaying messages for skipping files due to incorrect CSV headers (as per US1.3). [cite: 31, 66, 180]
* [ ] Ensure `parse_csv_file()` correctly implements logging/displaying messages for records where 'Hours Worked' is non-numeric and is treated as zero (as per US1.4/US1.5). [cite: 31, 33, 67, 181]
* [ ] Review all error/warning messages for clarity, ensuring they include specific filenames and, where possible, context (like row number for data errors). [cite: 15, 62]
* [ ] Create comprehensive unit tests for error reporting scenarios in `tests/test_calculator.py` (Placeholder, may involve capturing stdout/stderr):
    * [ ] Test with a mix of valid files, files with bad names, files with bad headers, and files with bad data rows. Verify that correct error messages are produced for each invalid case and that valid data is still processed.
* [ ] Add comments as per documentation standards. [cite: 124]
* MANUAL STEP: Create a diverse set of input CSVs in `data/input_examples/` that trigger each error condition (bad name, bad header, non-numeric hours) and run the script to verify all error messages are clear, specific, and that the script continues to process other valid files/data, as per ArchDoc Sec 10. [cite: 73, 74, 77, 78]

Testing Requirements:
* Test Types: Manual testing for MVP. [cite: 72, 73, 74, 78] (Unit Tests via PyTest if automated).
* Code Coverage: N/A for MVP (Target >= 85% if unit tests were implemented).
* Definition of Done: All ACs met, script provides clear, specific notifications for files/records skipped due to validation errors, continues processing valid data, and all specified manual tests passing.

Story Wrap Up (To be filled in AFTER agent execution):
* Agent Model Used: <Agent Model Name/Version>
* Agent Credit or Cost: <Cost/Credits Consumed>
* Date/Time Completed: <Timestamp>
* Commit Hash: <Git Commit Hash of resulting code>
* Change Log:

---