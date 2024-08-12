import math
import numpy as np
import pickle
import streamlit as st
import emoji
import folium
from streamlit_folium import st_folium


st.title('History of Indian Premier League')
st.image('https://cdn.siasat.com/wp-content/uploads/2022/06/IPL-2022.jpg',width=600)

st.caption('Inception')
st.write('The IPL was founded in 2007 by the Board of Control for Cricket in India (BCCI) as a franchise-based tournament.')
st.write('The first season of the IPL took place in 2008, featuring eight teams representing different cities in India.')
st.write('The inaugural match was held on April 18, 2008, between the Kolkata Knight Riders and the Royal Challengers Bangalore.')
st.markdown('---')


st.caption('Format and Structure:')
st.write('The IPL follows a round-robin format, where each team plays against every other team twice in a home and away format.')
st.write('The top four teams in the league standings qualify for the playoffs, which include Qualifier 1, Eliminator, Qualifier 2, and the Final.')
st.write('The team that finishes at the top of the league standings after the round-robin stage is awarded the "League Winners" title.')

st.markdown('---')
st.caption('Expansion and Team Changes:')
st.write('Over the years, the IPL has seen various changes in terms of team ownership, rebranding, and the addition of new franchises.')
st.write('The inaugural season featured eight teams: Chennai Super Kings, Delhi Daredevils (now Delhi Capitals), Kings XI Punjab (now Punjab Kings), Kolkata Knight Riders, Mumbai Indians, Rajasthan Royals, Royal Challengers Bangalore, and Deccan Chargers (now defunct).')
st.write('The Deccan Chargers franchise was replaced by the Sunrisers Hyderabad in 2013.')
st.write('In 2011, two new franchises, Pune Warriors India and Kochi Tuskers Kerala, joined the league, but both teams were terminated after the 2013 season.')
st.write('In 2016, two new teams, Rising Pune Supergiant and Gujarat Lions, were added as temporary replacements for Chennai Super Kings and Rajasthan Royals, who were suspended for two seasons due to involvement in corrupt practices. CSK and RR returned to the league in 2018.')
st.write('In 2020, the team name of Delhi Daredevils was changed to Delhi Capitals and Kngs XI Punjab to Punjab Kings and in 2022,two new teams Lucknow Super Giants(LSG) and Gujarat Titans(GT) were added')
st.markdown('---')
st.caption('Notable Performances and Records:')
st.write('Throughout the history, many players have delivered exceptional performances and set numerous records.')
st.write('Chris Gayle holds the record for the highest individual score in IPL, scoring 175 runs off 66 balls for Royal Challengers Bangalore in 2013.')
st.write('Virat Kohli is the leading run-scorer in IPL history, accumulating over 6,000 runs.')
st.write('Lasith Malinga holds the record for the most wickets in IPL, taking more than 170 wickets.')
st.write('Mumbai Indians have been the most successful team in IPL history, winning the title five times (2013, 2015, 2017, 2019, and 2020).')
st.markdown('---')
st.caption('Influence and Impact:')
st.write('The IPL has had a significant impact on Indian cricket and the global cricketing landscape.')
st.write('It has provided a platform for young domestic players to showcase their talent alongside international stars.')
st.write('The league has attracted a massive fan base and has become a major source of entertainment and revenue.')
st.write('The IPL has also contributed to the growth of franchise-based cricket leagues worldwide, inspiring similar tournaments in other countries such as Big Bash League,Carribean Premier League,RamSlam Premier League and son on')
st.markdown('---')

