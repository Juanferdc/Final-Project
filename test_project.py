import pytest
import json
from project import get_workout, calculate_calories_burned, log_workout

def test_get_workout():
    expected_output = {
        "Push-ups": 10,
        "Squats": 12,
        "Dumbbell Press": 8
    }
    assert get_workout("strength", "beginner") == expected_output
    
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
