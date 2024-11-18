import streamlit as st
import requests

# إعداد واجهة المستخدم
st.title("Player Price Prediction")

appearance = st.number_input("Appearance", min_value=0)
minutes_played = st.number_input("Minutes Played", min_value=0)
award = st.number_input("Award", min_value=0)
highest_value = st.number_input("Highest Value", min_value=0)

# زر التنبؤ
if st.button("Predict Price"):
    # URL الخاص بـ FastAPI
    url = "https://lab7-app-2.onrender.com"  # تأكد من أنه صحيح عند اختبار محلياً
    
    # البيانات المرسلة
    data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "award": award,
        "highest_value": highest_value
    }

    print(f"Sending data: {data}")  # طباعة البيانات المرسلة إلى API

    with st.spinner("Predicting..."):
        try:
            # إرسال البيانات إلى FastAPI
            response = requests.post(url, json=data)
            response.raise_for_status()  # تحقق من حالة الاستجابة
            
            # التنبؤ المرسل من FastAPI
            prediction = response.json()
            print(f"Received response: {prediction}")  # طباعة الاستجابة الواردة
            st.write(f"Estimated Price: {prediction['prediction']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error while requesting prediction from the API: {str(e)}")
            st.write(f"Details: {e}")

