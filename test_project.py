import pytest
import json
from project import get_workout, calculate_calories_burned, log_workout

def test_get_workout():
    assert get_workout("strength", "beginner") == ["Push-ups", "Squats", "Dumbbell Press"]
    assert get_workout("weight_loss", "advanced") == ["HIIT Circuits", "Sled Push", "Battle Ropes"]
    assert get_workout("invalid_goal", "beginner") == ["No workouts available for given input."]

def test_calculate_calories_burned():
    assert calculate_calories_burned("Push-ups", 10) == 70
    assert calculate_calories_burned("Jump Rope", 5) == 65
    assert calculate_calories_burned("Unknown Exercise", 10) == 50

def test_log_workout(tmp_path):
    log_file = tmp_path / "workout_log.json"
    log_workout("Push-ups", 10)
    with open("workout_log.json", "r") as file:
        data = json.load(file)
    assert {"exercise": "Push-ups", "duration": 10} in data
