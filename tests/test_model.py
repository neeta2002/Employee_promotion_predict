import joblib

def test_employee_promotion_prediction():
    model = joblib.load("model/model.pkl")
    prediction = model.predict([[8]])
    assert prediction[0] == 1