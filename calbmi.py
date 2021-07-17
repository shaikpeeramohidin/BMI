#import streamlit
import streamlit as st
#title to app
st.title("Welcome : BMI Calculator")
#take input
weight = st.number_input("Please Enter your weight (in KGs)")
#take height
status = st.radio('Please select your height format: ',('cms', 'meters', 'feet'))
#compare status value
#bmi fomula weight/(hight)^2
if(status == 'cms'):
    height = st.number_input('Centermeters')
    try:
        bmi=weight/((height/100)**2)
    except:
        st.text("Enter some value of height")
elif(status =='meters'):
    height = st.number_input('Meters')
    try:
        bmi=weight/(height**2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    try:
        #1mt=3.28
        bmi=weight/(((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):
 try:
    #print bmi index
    st.text("Your BMI Index is {}".format(bmi))
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >=16 and bmi <18.5):
        st.warning("Ypu are Under weight")
    elif(bmi >=18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi > 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.error("Extremly Overweight")
 except:
    st.text("Please enter the values.")
st.text("----------By Peeramohidin")
