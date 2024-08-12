#import the libraries

import math
import numpy as np
import pickle
import streamlit as st
import emoji
import folium
from streamlit_folium import st_folium
from PIL import Image


#SET PAGE WIDE
st.set_page_config(page_title='IPL_Score_Predictor',layout="centered")


filename = 'ml_model.pkl'
model = pickle.load(open(filename,'rb'))


st.markdown('<h1 style="color:#FFFF00"> IPL Fourth Umpire Pre Innings</h1>', unsafe_allow_html=True)
st.image('https://bestmediainfo.com/public/uploads/2018/05/Cricket-Live-and-Extraaa-Innings_8.jpg',width=600)
# SELECT THE BATTING TEAM

batting_team= st.selectbox('Select the Batting Team-🏏',('Royal Challengers Bangalore', 'Delhi Capitals','Punjab Kings','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Chennai Super Kings','Sunrisers Hyderabad','Gujarat Titans', 'Lucknow Super Giants'))

prediction_array = []
  # Batting Team
if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif batting_team == 'Punjab Kings':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif batting_team == 'Gujarat Titans':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif batting_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]


#SELECT BOWLING TEAM
# bt = 

# b1, b2 = st.columns(2)

bowling_team = st.selectbox('Select the Bowling Team-🥎',('Chennai Super Kings', 'Delhi Capitals','Punjab Kings','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad','Gujarat Titans', 'Lucknow Super Giants'))
if bowling_team==batting_team:
    st.error('Bowling and Batting teams should be different')

# Bowling Team
    
if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Capitals':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif bowling_team == 'Punjab Kings':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif bowling_team == 'Gujarat Titans':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif bowling_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]

st.markdown("---")

aa, bb, cc = st.columns(3)

# adding logos of teams 
width = 200
hight = 200
with bb:
    # st.subheader(")
    ma = '<h3 style="colour:#00FF00"> Match Between </h3>'
    st.markdown('<h3 style="color:#FFFF00"> Match Between</h3>', unsafe_allow_html=True)
    # st.markdown('<h3 style="colour:#00FF00"> Match Between </h3>', unsafe_allow_html=True)
    
col6,colvs, col7 = st.columns(3)
if batting_team == 'Chennai Super Kings':
    with col6:
        st.image("Logos/Chennai_Super_Kings_Logo.png", width=width)
elif batting_team == 'Delhi Capitals':
    with col6:
        st.image("Logos/Delhi_Capitals.png", width=180)
elif batting_team == 'Punjab Kings':
    # batting_team = 'Delhi Daredevils' 
    with col6:
        st.image("Logos/Punjab_Kings_Logo.png", width=140)
elif batting_team == 'Kolkata Knight Riders':
    with col6:
        st.image("Logos/Kolkata_Knight_Riders_Logo.png", width=115)
elif batting_team == 'Mumbai Indians':
    with col6:
        st.image("Logos/mumbai_indians.png", width=210)
elif batting_team == 'Rajasthan Royals':
    with col6:
        st.image("Logos/Rajasthan_Royals_Logo.png", width=190)
elif batting_team =='Royal Challengers Bangalore':
    with col6:
        st.image("Logos/rcb-logo-new.png", width=120)
elif batting_team == 'Sunrisers Hyderabad':
    with col6:
        st.image("Logos/sunrisers_hydrabad.png", width=width)
elif batting_team == 'Gujarat Titans':
    with col6:
        st.image("Logos/Gujarat_Titans_Logo.png", width=200)
elif batting_team == 'Lucknow Super Giants':
    with col6:
        st.image("Logos/Lucknow_Super_Giants_IPL_Logo.png", width=220)

with colvs:
    st.image("Logos/vs.png", width=150)
if bowling_team == 'Chennai Super Kings':
    with col7:
        st.image("Logos/Chennai_Super_Kings_Logo.png", width=width)
elif bowling_team == 'Delhi Capitals':
    with col7:
        st.image("Logos/Delhi_Capitals.png", width=180)
elif bowling_team == 'Punjab Kings':
    with col7:
        st.image("Logos/Punjab_Kings_Logo.png", width=140)
elif bowling_team == 'Kolkata Knight Riders':
    with col7:
        st.image("Logos/Kolkata_Knight_Riders_Logo.png", width=115)
elif bowling_team == 'Mumbai Indians':
    with col7:
        st.image("Logos/mumbai_indians.png", width=210)
elif bowling_team == 'Rajasthan Royals':
    with col7:
        st.image("Logos/Rajasthan_Royals_Logo.png", width=190)
elif bowling_team == 'Royal Challengers Bangalore':
    with col7:
        st.image("Logos/rcb-logo-new.png", width=120)
elif bowling_team == 'Sunrisers Hyderabad':
    with col7:
        st.image("Logos/sunrisers_hydrabad.png", width=width)
elif bowling_team == 'Gujarat Titans':
    with col7:
        st.image("Logos/Gujarat_Titans_Logo.png", width=200)
elif bowling_team == 'Lucknow Super Giants':
    with col7:
        st.image("Logos/Lucknow_Super_Giants_IPL_Logo.png", width=220)

st.markdown("---")



d=['M. Chinnaswamy Stadium, Bangalore','Wankhede Stadium, Mumbai','Arun Jaitley Stadium, Delhi','Mohali Stadium, Mohali','Sawai Mansingh Stadium, Jaipur','Eden Gardens, Kolkata','Narendra Modi Stadium, Ahmedabad','Ekana Sports City, Lucknow','Rajiv Gandhi International Cricket Stadium, Hyderabad','M. A. Chidambaram Stadium, Chennai']
d.sort()
venue=st.selectbox('Select the venue-',('M. Chinnaswamy Stadium, Bangalore','Wankhede Stadium, Mumbai','Arun Jaitley Stadium, Delhi','Mohali Stadium, Mohali','Sawai Mansingh Stadium, Jaipur','Eden Gardens, Kolkata','Narendra Modi Stadium, Ahmedabad','Ekana Sports City, Lucknow','Rajiv Gandhi International Cricket Stadium, Hyderabad','M. A. Chidambaram Stadium, Chennai'))


a, b, c, d = st.columns(4)

#Enter the Current Ongoing Over
with a:
    overs = st.number_input('Enter the Current Over',min_value=5.0,max_value=19.5,value=5.0,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with d:
#Enter Current Run
    runs = st.number_input('Enter the Current runs',min_value=0,max_value=354,step=1,format='%i')

ab, bc , ca = st.columns(3)

with bc:
    st.write("Current Run Rate: ", round((runs/overs),2))
    

#Wickets Taken till now
wickets =st.slider('Enter Wickets fallen till now',0,9, 1)
wickets=int(wickets)

col3, col4,col5= st.columns(3)

with col3:
#Runs in last 4 over
    runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs',min_value=0,max_value=runs,step=1,format='%i')

with col4:
#Wickets in last 4 over
    wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs',min_value=0,max_value=wickets,step=1,format='%i')

#Get all the data for predicting

prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)

with col5:
    temp= st.selectbox('Select the Weather condition ',('Overcast','Sunny','Rainy','Humid'))


st.markdown("---")  

my_prediction = int(round(predict[0]))
x=f'PREDICTED MATCH SCORE : {my_prediction-0} to {my_prediction+4}'
a=my_prediction


b1, b3 = st.columns(2)

with b1:
    oversi = st.number_input('Pick a number', 5, 19)
    # oversi =st.selectbox('Select the overs ',('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'))

oversi=int(oversi)
a=runs/overs
b=my_prediction/20
if(a>b):
    c=a-b
    k=1
else:
    c=b-a
    k=0
if (oversi-overs != 0):
    c=c/(20-overs)
c=c*(oversi-overs)
if(k==1):
    c=(a)-c
else:
    c=a+c
c=math.ceil(c*oversi)
if(k==1):
    x=f'PREDICTED MATCH SCORE FOR {oversi} OVERS IS: {c-5}'
else:
    x=f'PREDICTED MATCH SCORE FOR {oversi} OVERS IS: {c-5}'

c1, c2, c3 = st.columns(3)
with c2:
    if st.button(f'Predict Score for {oversi} Overs'):
        with b3:
            st.write("                         ")
            st.success(x)
st.markdown("---")



# ef, gh, ij = st.columns(3)
if(temp=='Rainy-DLS'):
   rovers=st.number_input('Enter the Total reduced overs',min_value=8,max_value=18,value=8,step=1)
   if st.button('Predict Score for reduced overs'):
       my_prediction=((runs//overs)*rovers)
       x=f'PREDICTED MATCH SCORE : {my_prediction-5} to {my_prediction+5}'

    
       #st.write('Expected run rate -', round((my_prediction/20) * 1, 2))

       st.success(x)
else:

    if st.button('Predict Score'):
    #Call the ML Model
        my_prediction = int(round(predict[0]))
      
        if(temp=='Overcast'):
            
            x=f'PREDICTED MATCH SCORE : {my_prediction-0} to {my_prediction+5}'
        elif(temp=='Sunny'):
            x=f'PREDICTED MATCH SCORE : {my_prediction-0} to {my_prediction+10}'
        elif(temp=='Rainy'):
            x=f'PREDICTED MATCH SCORE : {my_prediction-10} to {my_prediction+3}'
        elif(temp=='Humid'):
            x=f'PREDICTED MATCH SCORE : {my_prediction-7} to {my_prediction+2}'
        st.success(x)

st.markdown("---")
st.markdown("""---""")

st.markdown('<h1 style="color:#FFFF00"> IPL Fourth Umpire Post Innings</h1>', unsafe_allow_html=True)
st.image('https://pbs.twimg.com/media/EzGeQNVXIAUBfJv.jpg',width=600)
a=[]
b=[]
a.append(batting_team)
b.append(bowling_team)
bat2=st.selectbox('Batting Team',b)
bowl2=st.selectbox('Bowling Team',a)
target=st.number_input('Target',my_prediction,my_prediction)

a1, b1, c1, d1 = st.columns(4)

#Enter the Current Ongoing Over
with a1:
    overs = st.number_input('Enter the Current Over',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with d1:
#Enter Current Run
    runs = st.number_input('Enter the Current runs',min_value=0,max_value=500,step=1,format='%i')

ab, bc , ca = st.columns(3)

with bc:
    st.write("Current Run Rate: ", round((runs/overs),2))
    

#Wickets Taken till now
wickets =st.slider('Enter Current Wickets Fallen',0,9,1)
wickets=int(wickets)








col5,col6=st.columns(2)

with col5:
        runs_in_prev_5 = st.number_input('Runs scored in the previous 5 overs',min_value=0,max_value=runs,step=1,format='%i')

with col6:
        wickets_in_prev_5 = st.number_input('Wickets fallen in the last 5 overs',min_value=0,max_value=10,step=1,format='%i')
prediction_array = []


prediction_array = []
  # Batting Team
if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Capitals':
    batting_team='Delhi Daredevils'
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif batting_team == 'Punjab Kings':
    batting_team='Kings XI Punjab'
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif batting_team == 'Gujarat Titans':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif batting_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]



if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Capitals':
    bowling_team = 'Delhi Daredevils'
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif bowling_team == 'Punjab Kings':
    bowling_team = 'Kings XI Punjab'
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif bowling_team == 'Gujarat Titans':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif bowling_team == 'Lucknow Super Giants':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]



'''prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)
my_prediction1 = int(round(predict[0]))
x=f'PREDICTED MATCH SCORE : {my_prediction1-0}'



st.success(my_prediction1)  
if st.button('Predict win probablity for 20 overs'):
    exprr=my_prediction/20
    rrr=(target-runs)/(20-overs)
    win_probability =(exprr/(rrr+exprr))
    st.write(win_probability)'''

st.markdown('---')
























