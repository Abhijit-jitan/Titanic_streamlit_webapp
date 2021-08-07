import pandas as pd
import streamlit as st
import pickle
import numpy as np
model=pickle.load(open(r"titanic_v0.pkl",'rb'))

## Main Function
def main():
    st.title("Titanic Survival Prediction")
    st.image(r"titanic_sinking.jpg", caption="Sinking of 'RMS Titanic' : 15 April 1912 in North Atlantic Ocean",use_column_width=True)
    st.write("""## Would you have survived From Titanic Disaster?""")

    ## Side Bar Configurations
    st.sidebar.header("More Details:")
    st.sidebar.markdown("[For More facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")
    st.sidebar.markdown("[and here](https://titanicfacts.net/titanic-survivors/)")
    st.title("-----          Check Your Survival Chances          -----")

    ## Framing UI Structure
    age = st.slider("Enter Age :", 1, 75, 30)

    fare = st.slider("Fare (in 1912 $) :", 15, 500, 40)

    SibSp = st.selectbox("How many Siblings or spouses are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8])

    Parch = st.selectbox("How many Parents or children are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8])

    sex = st.selectbox("Select Gender:", ["male","female"])
    if (sex == "male"):
        Sex=0
    else:
        Sex=1

    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])

    boarded_location = st.selectbox("Boarded Location:", ["Cherbourg","Queenstown","Southampton"])
    Embarked_C,Embarked_Q,Embarked_S=0,0,0
    if boarded_location == "Queenstown":
        Embarked_Q=1
    elif boarded_location == "Southampton":
        Embarked_S=1
    else:
        Embarked_C=1

    ## Getting & Framing Data
    data={"Age":age,"Fare":fare,"SibSp":SibSp,"Parch":Parch,"Sex":Sex,"Pclass":Pclass,"Embarked_Q":Embarked_Q,"Embarked_S":Embarked_S,"Embarked_C":Embarked_C}

    df=pd.DataFrame(data,index=[0])
    return df

data=main()

## Prediction:
if st.button("Predict"):
    result = model.predict(data)
    proba=model.predict_proba(data)
    #st.success('The output is {}'.format(result))

    if result[0] == 1:
        st.write("congratulation !!!.... **You probably would have made it!**")
        st.image(r"lifeboat.jfif")
        st.write("Survival Probability Chances : 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("Better Luck Next time !!!!...**you're probably Ended up like 'Jack'**")
        st.image(r"Rip.jfif")
        st.write("Survival Probability Chances : 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))

## Working Button:
if st.button("Working"):
    st.write("""# How's prediction Working :- Insider Survival Facts and Tips: 
             - Only about `32%` of passengers survived In this Accident\n
             - Ticket price:
                    1st-class: $150-$435 ; 2nd-class: $60 ; 3rd-class: $15-$40\n
             - About Family Factor:
                If You Boarded with atleast one family member `51%` Survival rate
               """)
    st.image(r"gr.PNG")

## Author Info.
if st.button("Author"):
    st.write("## @ Abhijit")
    st.write("### Built with Streamlit")