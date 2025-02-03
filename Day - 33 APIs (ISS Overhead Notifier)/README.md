# Day 33 - APIs and ISS Overhead Notifier

This project is part of the **100 Days of Code** challenge. It integrates an external API to notify users when the **International Space Station (ISS)** is overhead. The project involves working with APIs, handling environment variables, and implementing notifications based on the ISS’s location.

## How It Works

1. **API Integration**:
   - The project communicates with the [Open Notify API](http://open-notify.org/), which provides real-time data on the ISS's position.
   - The program fetches the current location of the ISS, including its latitude and longitude.

2. **User Location**:
   - The user inputs their **latitude** and **longitude** when prompted, which represents their current location on Earth.
   - Alternatively, the program can use **environment variables** to retrieve user data such as location, providing flexibility and security in fetching sensitive information.

3. **Overhead Detection**:
   - The program continuously checks if the ISS is overhead by comparing its coordinates to the user's coordinates.
   - If the ISS’s position is within a specified range of the user’s location, the program triggers a notification.

4. **Notification**:
   - When the ISS is overhead, the program sends a simple notification to the user, either by printing a message to the console or using system notifications (this can be enhanced using libraries like `plyer`).

## How It Was Made

### Technologies Used

- **Python**: The core language used for the project.
- **Requests**: The `requests` library is used to interact with the Open Notify API and fetch the ISS’s location.
- **Environment Variables**: `os.environ.get()` is used to retrieve sensitive data like the user's location from environment variables, ensuring that they are not hard-coded in the script for security reasons.
- **Time Management**: The script uses the `time` module to periodically check the ISS’s position at regular intervals.

### Key Components

1. **Fetching ISS Location**:
   - The program makes a request to the Open Notify API to get the current position of the ISS.
   - The returned data is parsed to extract the latitude and longitude of the ISS.

2. **Comparing Locations**:
   - The user’s inputted location (latitude and longitude) is compared with the ISS’s coordinates.
   - If the ISS is within a defined proximity to the user's location, it is considered overhead.

3. **Sending Notifications**:
   - A simple notification is displayed in the console to alert the user when the ISS is overhead.
   - Future versions could incorporate system-level notifications using libraries such as `plyer` or email notifications.

4. **Environment Variable Handling**:
   - Using `os.environ.get()`, the program retrieves environment variables for sensitive information (e.g., location or configuration) instead of hardcoding them directly into the script.
   - This allows for easier and more secure deployment in different environments.

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of working with APIs and environment variables.

### Steps to Install

1. **Clone the Repository**:
   Clone the project to your local machine:

   ```bash
   git clone https://github.com/rahulparmar-202/100-Days-of-Code---The-Complete-Python/tree/master/Day%20-%2033%20APIs%20(ISS%20Overhead%20Notifier)
