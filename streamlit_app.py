import streamlit as st
import pandas as pd

st.write("""
# Find the largest among the 3 given numbers (value greater than the other two)

""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    first_num = st.number_input("FIRST_NUM")
    second_num = st.number_input("SECOND_NUM")
    third_num = st.number_input("THIRD_NUM")
    

    data = {'FIRST_NUM': first_num,
            'SECOND_NUM': second_num,
            'THIRD_NUM': third_num
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Inputs')
st.table(df)

def highest(data):
    nam = -99999999999
    for column in data:
        if data[column].item() > nam:
            nam = data[column].item()
        else:
            continue
    return nam

High_num = highest(df)
st.subheader('Highest number')
st.write('The number is: ', High_num)