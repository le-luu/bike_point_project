# BIKE POINT Project
<img src="https://github.com/le-luu/bike_point_project/blob/main/img/TIL%20Logo%20PDF.png" width="300" />

## Objectives
A Python project to extract the data from: https://api.tfl.gov.uk/BikePoint by Python. Then, in the data folder, it should show the output data extracting from API in JSON. In the log folder, it should show output all the logging file after running the Python script.

## Contents
[Objectives](#objectives)

[Project Structure](#project-structure)

[Explanation](#explanation)

[Instructions to Run](#instruction-to-run)

## Project Structure
```text
├── img
├── .gitignore
├── LICENSE
├── README.md
├── extract_bp_data.py
├── requirements.txt
```

## Explanation

### Step 1: Create variables

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/variables.png" />

Declare variables:
- url: the url that the project extracts from
- filename: to store the timestamp, later will assign this filename to the filepath of the data and log files.
- dir: data folder to store all the output after extracting
- logs_dir: log folder to store all logging file after running the script

### Step 2: Define logger for logging data

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/logger.png" />

- Set the logging file path in the log folder and store it in the log_filename variable
- Set the basic config for logging:
    - level = logging.INFO will capture the logging message of status INFO and higher following the hiararchy: DEBUG < INFO < WARNING < ERROR < CRITICAL
    - format: to format the content output in the log file
    - filename: specify the log output file path
- After setting the logging methods, create a logger with the function getlogger() from logging package

### Step 3: Extract the data from API and handle errors

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/while_true.png" />

Create variables: number_of_tries and count to capture the number of time that can retry extracting data. In this case, there are 3 chances to retry extracting data from API. count is set to 0, while count is still less than the max tries number (3), then:
- Send a GET request to the url with the timeout is 10 seconds
- After sending the GET request to the server, it will response the data with response code, reason. Stoe the response code in the response_code variable
- If the response code is 200 (it means OK), then
    - Make a data folder to store the output
    - Store the JSON data in response_json variable
    - Set the filepath for the output with file extension is .json
    - Then, apply error handling with try...catch. Open the the filepath just set above to write the data. Store the data as text. Print out the successful message on the screen and also write it into the logging file. Otherwise, print out the error and write to the logging file with that error.
    - Then, break the loop

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/while_false.png" />

- If the response code is greater than 499 or less than 200, it means something happened during getting the response. In this case:
    - Print out the screen the reason from the response
    - Write to the logging file with that reason
    - Wait 10 seconds to retry and add 1 to the count variable
 - In another case, print out the error and write the logging error message in the logging file and break the loop

### Step 4: Check the Output

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/output_terminal.png" />

If successfully run, it will output the terminal same as the image above.

<img src="https://github.com/le-luu/bike_point_project/blob/main/img/data_logs_folder.png" />

Then, check the data and log folder

## Instructions to run
- Install Python 3.12 or later version
- Fork and Clone this repo to local computer
- Open the Terminal on Mac or Command Prompt on Windows
- Change directory to bike_point_project
  ```
  cd <directory_after_cloning>/bike_point_project
  ```
- Install and activate the virtual environment. In the terminal, type:
  ```
  python -m venv .venv
  .venv\Scripts\activate
  ```
- Install the packages to run the Python script
  ```
  pip install requirements.txt
  ```
- Run the Python script:
  ```
  python extract_bp_data.py
  ```

