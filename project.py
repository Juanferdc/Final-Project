import json
import requests
import os

def main():
    print("Welcome to the Workout Planner!")
    
    # Authentication
    username = input("Create a username: ").strip()
    password = input("Create a password: ").strip()
    print("Account created successfully! Please log in.")
    
    while True:
        login_username = input("Enter your username: ").strip()
        login_password = input("Enter your password: ").strip()
        
        if login_username == username and login_password == password:
            print("Login successful!")
            break
        else:
            print("Invalid credentials, please try again.")
    
    # Get user location
    while True:
        location = input("Enter your location (city or ZIP code) to find a nearby gym: ").strip()
        if find_nearby_gym(location):
            break
        else:
            print("No gyms found. Try entering a different location.")

    # Workout plan
    goal = input("Enter your fitness goal (strength, weight_loss, endurance): ").strip().lower()
    experience_level = input("Enter your experience level (beginner, intermediate, advanced): ").strip().lower()
    workout = get_workout(goal, experience_level)
    
    print("\nSuggested Workout:")
    for exercise, reps in workout.items():
        print(f"- {exercise}: {reps} reps")
    
    # Log workout
    log_choice = input("\nDo you want to log a workout? (yes/no): ").strip().lower()
    if log_choice == "yes":
        exercise = input("Enter the exercise name: ").strip()
        duration = int(input("Enter duration in minutes: "))
        log_workout(exercise, duration)
        print("Workout logged successfully!")

def find_nearby_gym(location):
    """Fetch nearby gyms using Google Maps API"""
    api_key = "AIzaSyCu2Fh06a3jhG6QFFzgzqKuqb4Pd8YudTo"
    if not api_key:
        print("Error: Google Maps API key not found. Set it as an environment variable.")
        return False
    
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=gyms+in+{location}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        gyms = response.json().get("results", [])
        if gyms:
            print("\nHere are some gyms near you:")
            for gym in gyms[:5]:  # Show top 5 results
                print(f"- {gym['name']} (Address: {gym.get('formatted_address', 'No address available')})")
            return True
    else:
        print(f"Error fetching data from Google Maps API: {response.status_code}")
    
    return False

def get_workout(goal, experience_level):
    """Returns workout plan based on user goal and experience level"""
    workouts = {
        "strength": {
            "beginner": {"Push-ups": 10, "Squats": 12, "Dumbbell Press": 8},
            "intermediate": {"Bench Press": 8, "Deadlifts": 6, "Pull-ups": 10},
            "advanced": {"Snatch": 5, "Clean and Jerk": 5, "Front Squat": 8}
        },
        "weight_loss": {
            "beginner": {"Jumping Jacks": 20, "Burpees": 15, "Jump Rope": 30},
            "intermediate": {"Running": 15, "Cycling": 20, "Rowing": 10},
            "advanced": {"HIIT Circuits": 5, "Sled Push": 3, "Battle Ropes": 10}
        },
        "endurance": {
            "beginner": {"Walking": 20, "Light Jogging": 15, "Swimming": 10},
            "intermediate": {"Running": 20, "Rowing": 15, "Jump Rope": 25},
            "advanced": {"Marathon Training": 60, "Triathlon Training": 90, "Cycling Long Distance": 120}
        }
    }
    return workouts.get(goal, {}).get(experience_level, {"No workouts available for given input.": "N/A"})

def calculate_calories_burned(exercise, duration):
    """Calculates calories burned based on exercise and duration"""
    calorie_chart = {
        "Push-ups": 7,
        "Squats": 8,
        "Dumbbell Press": 6,
        "Jumping Jacks": 10,
        "Burpees": 12,
        "Jump Rope": 13,
        "Running": 11,
        "Cycling": 9,
        "Rowing": 10,
    }
    return calorie_chart.get(exercise, 5) * duration

def log_workout(exercise, duration):
    """Logs workout data to a JSON file"""
    log_entry = {"exercise": exercise, "duration": duration}
    try:
        with open("workout_log.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(log_entry)
    with open("workout_log.json", "w") as file:
        json.dump(data, file, indent=4)
    
if __name__ == "__main__":
    main()