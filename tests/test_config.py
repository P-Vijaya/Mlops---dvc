import pytest
import json
import logging
import os
import joblib
from prediction_service.prediction import form_response,api_response
import prediction_service

input_data = {
    "incorrect_range":
    {"GRE_Score": 2,
    "TOEFL_Score": 500,
    "University_Rating": 7.1,
    "SOP": 10,
    "LOR": 0,
    "CGPA": 50.6,
    "Research": 5,
    },

    "correct_range":
    {"GRE_Score": 310,
    "TOEFL_Score": 115,
    "University_Rating": 4,
    "SOP": 5,
    "LOR": 3,
    "CGPA": 8.5,
    "Research": 1,
    },

    "incorrect_col":
    {"GRE Score": 7897897,
    "TOEFL Score": 555,
    "University Rating": 99,
    "SOP": 99,
    "LOR": 12,
    "CGPA": 789,
    "Research": 75,
    },
}

TARGET_range = {
    "min": 0.0,
    "max": 1.0
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotINRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotINRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message


## pytest -v
## git add . && git commit -m"pytest example" && git push origin main
