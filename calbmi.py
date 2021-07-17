'''
Program to calculate BMI
BMI=Weight in KG/ square of height in meters.
1Pound(Lb)=0.453592 Kilograms(Kgs)
Author:Shaik Peeramohidin
GitHub:https://github.com/sk-pm
'''
#importing  streamlit
import streamlit as st
#title to app
st.title("Welcome - BMI Calculator")
#take weight units
weight_units=st.radio('Please Select Weight In Units:',('Kilograms(Kgs)','Pounds(lbs)'))
#weight
try:
    weight = st.number_input("Please Enter Your Weight :")
#convert weight pounds to Kgs
    if weight_units == 'Pounds(lbs)' :
        weight = weight*0.453592
    else :
        weight=weight * 1
except:
    st.text("Above field can not be blank")
#take height units
height_units = st.radio('Please Select Your Height Format: ',('Centimeters', 'Meters', 'Feets', 'Inchs'))
height = st.number_input("Please Enter Your Height :")
#convert to meters
#bmi fomula weight/(hight)^2
try:
    if(height_units == 'Centimeters'):
        height = height/100 #centimeters to meters
    elif(height_units =='Feets'):
        height = height/3.28 #feets to meters
    elif(height_units =='Inchs'):
        height = height * 0.0254
    else:
        height = height * 1
except:
    st.text("Above field can not be blank")


def calculate_bmi(h, w):
    return w / h * h
try:
    if(st.button('Calculate BMI')):

        bmi = calculate_bmi(height,weight)
        st.text(("You BMI is {}".format(bmi)))
        if(bmi < 16):
            st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi <18.5):
            st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            st.success("You are Heatlhy(Normal)")
        elif(bmi >=25 and bmi < 30):
            st.success("You are Overweight")
        elif(bmi >= 30):
            st.error("You are Extremly Overweight")
except:
    st.text("Please make sure all fields are filled")
