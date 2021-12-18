import streamlit as st
import joblib 
st.title('Months vs Sales Prediction')            #title for the webapp
forecast_model = joblib.load('forecast')        #load the model using joblib
ip = st.slider("Pick a number of months", 0, 24)         #user input in streamlit 
op = forecast_model.make_future_dataframe(periods = ip, freq = 'M')

# Predict the graph
predict = forecast_model.predict(op)  
fig = forecast_model.plot(predict)
st.pyplot(fig)                   
