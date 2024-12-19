# Vısual

![Screenshot_2024-12-19-19-31-34-984_com termux-edit~2](https://github.com/user-attachments/assets/3bb63a80-001b-4547-ae2b-ea6f29e048c5)


# Instagram Master Analyzer

Instagram Master Analyzer is a Python tool designed to analyze Instagram users' followers and followees. This tool helps users identify people who are not following them back. It uses the `instaloader` library to gather Instagram data and saves the analysis results in `.txt` or `.csv` formats.

## Features

- **Analyze your followers and followees:** Easily identify users who do not follow you back.
- **Start and end user filtering:** You can specify a range of users to analyze.
- **Output formats:** Save the results in `.txt` or `.csv` format.
- **API limit handling:** The script includes wait times to avoid hitting Instagram's API limits.

## Installation

To use this tool, you need to have Python 3.x installed along with the necessary libraries.

### 1. Install Python

You can download and install Python from the official [Python website](https://www.python.org/downloads/).

### 2. Install Required Libraries

To install the required libraries, run the following command:

```
pip install instaloader
```
## Usage

1. Clone the Repository

You can clone the repository from GitHub:

```
git clone https://github.com/archescyber/instagram-master-analyzer.git
```
```
cd instagram-master-analyzer
```

2. Run the Script

Once you have installed the dependencies, you can run the script using the following command:

`python master.py <your_username> <your_password> [--start_user <start_username>] [--end_user <end_username>] [--file_format <txt/csv>] [--sleep_time <seconds>]`

## Arguments:

`your_username: Your Instagram username.`

`your_password: Your Instagram password.`

`--start_user: The username to start analyzing (optional).`

`--end_user: The username to end analyzing (optional).`

`--file_format: The format to save the results (txt or csv). Default is txt.`

`--sleep_time: Time to wait (in seconds) to avoid hitting Instagram API limits. Default is 10 seconds.`


**Example:**

`python master.py your_username your_password --start_user start_username --end_user end_username --file_format csv --sleep_time 15`

Output:

The tool will analyze the followers and followees, and then save the list of users who do not follow you back in the specified file format (txt or csv). You will see a message indicating where the results are saved.

Contributing:

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.



## Disclaimer

This tool is for educational purposes only. Use it responsibly and ensure you comply with Instagram's Terms of Service.

This README provides a general overview of the project, installation instructions, usage, and other essential information for users and contributors.
