from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np



# تحميل النموذج والمقياس
model = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')

# إنشاء تطبيق FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Tuwaiq Academy"}

# تعريف Pydantic model للتحقق من صحة البيانات المدخلة
class InputFeatures(BaseModel):
    appearance: int
    minutes_played: int
    award: int
    highest_value: int

# معالجة البيانات المدخلة
def preprocessing(input_features: InputFeatures):
    # تحويل المدخلات إلى مصفوفة numpy (التي يمكن تمريرها إلى النموذج)
    input_data = np.array([[
        input_features.appearance,
        input_features.minutes_played,
        input_features.award,
        input_features.highest_value
    ]])
    
    # استخدام المقياس لتحويل البيانات (تقييس القيم)
    input_data_scaled = scaler.transform(input_data)
    return input_data_scaled

@app.post("/predict")
def predict(input_features: InputFeatures):
    # تجهيز البيانات المدخلة عبر الـ preprocessing
    processed_data = preprocessing(input_features)
    
    # إجراء التنبؤ باستخدام النموذج
    prediction = model.predict(processed_data)
    
    # إرجاع التنبؤ
    return {"prediction": prediction[0]}  # إرجاع التنبؤ كـ JSON

