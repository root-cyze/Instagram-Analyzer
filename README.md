# Instagram Follower Analyzer

## Description

This project is a Python-based tool that helps you find users on Instagram whom you follow, but they do not follow you back. It utilizes Instagram's API to fetch and compare your followers and following lists.

## Features

- Fetches your list of followers and following on Instagram.
- Compares the two lists to identify users who don't follow you back.
- User-friendly output displaying the results.
- Handles Instagram API limits and provides guidance on managing API calls effectively.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/archescyber/Instagram-Follower-Analyzer
   ```

2. Install the required dependencies.

3. Set up your Instagram API credentials:
   - Create an Instagram developer account and register your app.
   - Get your **Access Token** and **Client ID**.
   - Store these credentials in a `.env` file in the root directory.

## Usage

1. Run the script:

   ```
   cd Instagram-Follower-Analyzer
   ```
   ```
   python main.py
   ```

3. Enter your Instagram username when prompted.

4. The script will output a list of users that you follow but do not follow you back.

## API Rate Limits

Instagram API has certain rate limits you need to be aware of:

- **Basic Instagram API Rate Limits:**
  - **200 GET requests per hour** for user-related data (such as followers, following).

  Be cautious with frequent API requests as exceeding the limit can result in temporary suspension of API access. It’s recommended to add delays between API calls or use batch requests to stay within the limit.

- If your app frequently exceeds rate limits, you may consider:
  - Caching API responses locally.
  - Spreading requests over a longer time frame.
  - Upgrading your API access if necessary.

## Contribution

Feel free to contribute to the project by submitting issues or pull requests. All contributions are welcome!   

