# Workout Planner
## Video = https://youtu.be/zy-m9FfWiow 

The **Workout Planner** is a command-line program that generates personalized workout plans for users based on their goals and experience levels. It also enables users to find local gyms through the **Google Maps API** and record their finished workouts for reuse.

This project aims to upgrade the workout session by providing **personalized exercise suggestions**, **calorie burn estimates**, and a **structured workout logbook**. Additionally, the software includes a simple **user login system**, making the experience personal and secure.

## Project Structure

### **1. `project.py` (Main Program)**
- **User authentication**: Users create an account with a username and password to ensure personalization.
- **Google Maps API integration**: Users input their location (city or ZIP code) to find nearby gyms.
- **Workout recommendations**: The program suggests a set of exercises based on the user’s goal and experience level.
- **Workout logging**: Users can save completed workouts for tracking their progress.

### **2. `test_project.py` (Unit Tests)**
- **`test_get_workout()`**: Ensures that different workout goals return appropriate exercises.
- **`test_calculate_calories_burned()`**: Validates the accuracy of the calorie-burning estimation.
- **`test_log_workout()`**: Confirms that workouts are being correctly saved to the log file.

### **3. `requirements.txt` (Dependencies)**
This file lists the necessary Python packages that need to be installed before running the project. The main dependency is `requests`, which is used for making API calls to Google Maps.

### **4. `workout_log.json` (Workout Log File)**
- The exercise name
- Duration in minutes
- Date and time (optional for future improvements)

## Design Decisions

### **1. Choosing a CLI-based approach**
Initially, the idea was to build a **Flask web application**, but a CLI format was chosen due to its simplicity and accessibility. The goal was to focus on core functionality first before expanding to a web-based version.

### **2. Implementing User Authentication**
While workout planners don't typically require authentication, adding a **username and password system** helps personalize user data and secure workout logs. This choice ensures that each user has their own workout history.

### **3. Integrating Google Maps API for Gym Locator**
Finding a gym near the user’s location was considered an essential feature. We integrated the **Google Maps Places API** to provide **real-time results** based on user input.

- **Challenge:** The API key needed to be securely stored.
- **Solution:** The key was moved to an environment variable (`GOOGLE_MAPS_API_KEY`) rather than being hardcoded.

### **4. Choosing JSON for Workout Logging**
Instead of using a database, workout logs are stored in a **JSON file** for simplicity. In future versions, this could be migrated to **SQLite** or **Firebase** for better scalability.

## Features and Future Improvements

### ✅ **Current Features**
- Secure **User Authentication** (Username & Password)
- **Personalized Workouts** (Strength, Weight Loss, Endurance)
- **Nearby Gym Locator** using Google Maps API
- **Calorie Estimation** based on exercise and duration
- **Workout Logging** in JSON format

### 🚀 **Planned Enhancements**
- **Web Interface (Flask or Django)** for a better user experience
- **Enhanced Authentication** with password encryption
- **Automated Email Reminders** for scheduled workouts
- **AI-based Workout Recommendations** based on past logs
- **Database Integration** for better scalability

## Installation and Usage
### **Prerequisites**
Ensure you have Python installed. Then, install the required dependencies using:
```bash
pip install -r requirements.txt
```

### **Running the Program**
Execute the script by running:
```bash
python project.py
```

### **Testing the Program**
Run the test suite with:
```bash
pytest test_project.py
```

## Academic Integrity

This project was constructed with standard Python libraries, external API calls, and the `requests` library. The **Google Maps API** was utilized for getting gym locations, and all respective API calls are well-documented in the code. Any tools, libraries, or sources leveraged were referenced in the code comments to uphold academic integrity standards> Using Chat.gpt, youtube tutorials and CS50 duck to assist us in our questions and errors.


The **Workout Planner** is a feature-rich CLI-based program designed to assist users in reaching their desired fitness levels through well-structured workout plans and tracking. With the integration of **Google Maps API**, it provides users with real-time gym locations to further optimize their workout sessions. Although the present version is CLI-based, subsequent versions will aim to make the program more interactive, scalable, and user-friendly.


