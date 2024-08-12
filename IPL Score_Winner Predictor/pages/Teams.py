import math
import numpy as np
import pickle
import streamlit as st
import emoji
import folium
from streamlit_folium import st_folium


m = folium.Map(location=[23.09748778024757, 77.47956616512867], zoom_start=5)

fg = folium.FeatureGroup(name="State bounds")

fg.add_child(folium.Marker(location=(12.979342225591477, 77.59989293313774),popup="M. Chinnaswamy Stadium",tooltip="Royal Challengers Bangalore"))

fg.add_child(folium.Marker(location=(18.938861764140903, 72.82577019141024),popup="Wankhede Stadium",tooltip="Mumbai Indians"))

fg.add_child(folium.Marker(location=(28.63809246954008, 77.24315203933661),popup="Arun Jaitley Stadium",tooltip="Delhi Capitals"))

fg.add_child(folium.Marker(location=(30.691082722195834, 76.73747735287895),popup="Mohali Stadium",tooltip="Punjab Kings"))

fg.add_child(folium.Marker(location=(26.89627707383817, 75.80445509696862),popup="Sawai Mansingh Stadium",tooltip="Rajasthan Royals"))

fg.add_child(folium.Marker(location=(22.564766599665468, 88.34322158153684),popup="Eden Gardens",tooltip="Kolkata Knight Riders"))

fg.add_child(folium.Marker(location=(23.091917332650027, 72.59735026434956),popup="Narendra Modi Stadium",tooltip="Gujarat Titans"))

fg.add_child(folium.Marker(location=(26.81151765006424, 81.01528107810981),popup="Ekana Sports City",tooltip="Lucknow Super Giants"))

fg.add_child(folium.Marker(location=(17.406616037982147, 78.55050261004655),popup="Rajiv Gandhi International Cricket Stadium",tooltip="Sunrisers Hyderabad"))

fg.add_child(folium.Marker(location=(13.062995678404961, 80.27915862128015),popup="M. A. Chidambaram Stadium",tooltip="Chennai Super Kings"))

out = st_folium(
    m,
    feature_group_to_add=fg,
    # center=5,
    height=700, 
    width=700
)







team_options = ["Chennai Super Kings","Gujarat Titans","Lucknow Super Gaints","Mumbai Indians","Royal Challengers Bangalore","Rajasthan Royals","Kolkata Knight Riders","Punjab Kings","Delhi Capitals","SunRisers Hyderabad"]

team_selected =  st.selectbox("Which team Description you would like to see ?",options = team_options)



if team_selected == "Chennai Super Kings" :

    st.markdown(
        """
         <style>
         .stApp {
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGB7Chrhmcw_DNAslK1ewwr1xxMDIP3P2sQg&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }
         </style>
        """,
         unsafe_allow_html=True)
   
    st.write("1.Chennai Super Kings (CSK) is a professional cricket franchise based in Chennai, Tamil Nadu, India.")
    st.write("2.The team was founded in 2008 and plays its home matches at the M. A. Chidambaram Stadium in Chennai.")
    st.write("3.CSK is owned by India Cements through its Chennai Super Kings Cricket Limited holding company.")
    st.write("4.They have won a record five Indian Premier League (IPL) titles, sharing the record with Mumbai Indians.")
    st.write("5.CSK has appeared in a record 10 IPL finals and has qualified for the playoff stages 12 times out of the 14 seasons they have played, which is the highest among all teams.")
    st.write("6.The team has been captained by MS Dhoni since its inception and is currently coached by Stephen Fleming.")
    st.write("7.CSK became India's first unicorn sports enterprise in January 2022.")
    st.write("8.The team was suspended for two years from the IPL starting in July 2015 due to the involvement of its owners in the 2013 IPL betting case.")
    st.write("9.CSK made a successful comeback in the IPL in 2018 by winning the title in their comeback season.")
    st.write("10.The franchise is valued at approximately $1.15 billion as of 2022, making it one of the most valuable IPL franchises.")



    

elif(team_selected == "Gujarat Titans" ):

    st.write("1. Gujarat Titans (GT) is a professional cricket team based in Ahmedabad, Gujarat, India, competing in the Indian Premier League (IPL).")
    st.write("2. The team was founded in 2021 and plays their home matches at the Narendra Modi Stadium in Motera.")
    st.write("3. The franchise is owned by CVC Capital Partners, a consortium of companies or individuals.")
    st.write("4. Hardik Pandya, an Indian cricketer, is the captain of the Gujarat Titans.")
    st.write("5. The team is coached by Ashish Nehra, a former Indian cricketer.")
    st.write("6. In their debut season in 2022, the Gujarat Titans won their maiden IPL title.")
    st.write("7. A total of 22 companies showed interest, and CVC Capital Partners secured the rights to operate the Ahmedabad franchise with a bid of ₹5,625 crore (US$700 million) in October 2021.")
    st.write("8. The Board of Control for Cricket in India allowed a consortium of three companies or individuals to bid for each franchise.")
    st.write("9. Ahead of the IPL 2022 auctions, the Gujarat Titans drafted Hardik Pandya as their captain.")
    st.write("10. The franchise's debut season in 2022 turned out to be successful, with them clinching their first IPL title.")

elif(team_selected == "Lucknow Super Gaints"):
    st.write("1. Lucknow Super Giants (LSG) is a professional franchise cricket team based in Lucknow, Uttar Pradesh, India.")
    st.write("2. LSG was founded in 2021 and played its home matches at the BRSABV Ekana Cricket Stadium in Lucknow.")
    st.write("3. The team is owned by the RPSG Group, which previously owned the Rising Pune Supergiant franchise from 2016 to 2017.")
    st.write("4. KL Rahul, an Indian cricketer, serves as the captain of the Lucknow Super Giants.")
    st.write("5. The head coach of the team is Andy Flower, a former Zimbabwean cricketer and coach.")
    st.write("6. Gautam Gambhir, a former Indian cricketer, acts as the team mentor for LSG.")
    st.write("7. In their debut season, Lucknow Super Giants qualified for the play-offs, indicating a successful start to their IPL journey.")
    st.write("8. The franchise was secured by the RPSG Group through a bid of ₹7,090 crores during the invitation to tender process conducted by the IPL Governing Council.")
    st.write("9. Before the IPL 2022 mega auction, LSG announced KL Rahul as their captain, who became one of the highest-paid players in the league with a bid of ₹17 crore.")
    st.write("10. In 2023,LSG decided to wear the iconic green-maroon jersey in one match to pay tribute to the long and rich football history of Mohun Bagan")
 
elif(team_selected == "Mumbai Indians"):
    st.write("1. The Mumbai Indians is a professional franchise cricket team based in Mumbai, Maharashtra, that competes in the Indian Premier League (IPL).")
    st.write("2. It was founded in 2008 and is owned by Reliance Industries, India's biggest conglomerate, through its subsidiary Indiawin Sports.")
    st.write("3. The team plays its home matches at the Wankhede Stadium in Mumbai, with a seating capacity of 33,108.")
    st.write("4. Mumbai Indians became the first IPL franchise to cross the $100 million mark in brand value in 2017.")
    st.write("5. As of 2019, the brand value of Mumbai Indians was estimated to be around ₹809 crore ($115 million), the highest among all IPL franchises for the fourth consecutive year.")
    st.write("6. Mumbai Indians have been highly successful in the IPL and have won the tournament a record-breaking five times.")
    st.write("7. The team is currently captained by Rohit Sharma, who is also the leading run-scorer for the team.")
    st.write("8. Mahela Jayawardene has been the head coach of Mumbai Indians since the 2017 season.")
    st.write("9. The Mumbai Indians franchise was acquired by Reliance Industries for $111.9 million, making it the most expensive team in the IPL at the time of sale.")
    st.write("10. CSK and MI have the most intense rivalry in the IPL, often referred to as the 'El Clasico' of the league.")


elif(team_selected == "Royal Challengers Bangalore"):
    st.write("1. Royal Challengers Bangalore (RCB) is a professional franchise cricket team based in Bengaluru, Karnataka, and participates in the Indian Premier League (IPL).")
    st.write("2. The team was founded in 2008 by United Spirits and is named after the liquor brand Royal Challenge, owned by the company.")
    st.write("3. Despite being a prominent team in the IPL, RCB has not won the tournament yet but has finished as the runner-up on three occasions between 2009 and 2016.")
    st.write("4. RCB holds the record for both the highest team total in the IPL, scoring 263/5, and the lowest team total, being bundled out for just 49 runs.")
    st.write("5. The franchise was purchased by Vijay Mallya in 2008 for USDollar 111.6 million, making it the second-highest bid for a team during the auction process.")
    st.write("6. The rivalry between Kolkata Knight Riders (KKR) and Royal Challengers Bangalore (RCB) is one of the oldest in the IPL.")
    st.write("7. The Hyderabad franchises, DC SRH, have have a competitive rivalry because they are successful in winning key matches including IPL finals twice ")
    st.write("8. Another significant rivalry is CSK, known as the 'Kaveri derby', The rivalry stems from the Kaveri River water dispute between Karnataka and Tamil Nadu.")
    st.write("9. RCB's head Coach is Sanjay Bangar")
    st.write("10. RCB's favourite Slogan is 'Ee Sala Cup Namde'") 

elif(team_selected == "Rajasthan Royals"):
    st.write("1. Rajasthan Royals (RR) is a professional franchise cricket team based in Jaipur,.")
    st.write("2. In a remarkable display of resilience and skill, the Rajasthan Royals clinched the title in the inaugural edition of the IPL in 2008") 
    st.write("3. In a setback resulting from a 2013 betting scandal, the Rajasthan Royals, along with the Chennai Super Kings, were suspended for two years by a panel appointed by the Supreme Court of India.") 
    st.write("4. However, the Rajasthan Royals made a strong comeback and reentered the IPL competition in 2018, determined to reclaim their standing as a formidable team in the league.") 
    st.write("5. Sanju Samson holds the record for the highest number of runs scored by a Rajasthan Royals player, amassing an impressive total of 3138 runs in the history of the franchise") 
    st.write("6. Shane Watson, a former player for the Rajasthan Royals, holds the distinction of being their leading wicket-taker, having taken 67 wickets during his time with the team.") 
    st.write("7. The franchise is currently owned by Emerging Media IPL Ltd, led by Manoj Badale, holding a majority stake of 65%. Notable minority stakeholders include Lachlan Murdoch and RedBird Capital Partners.") 
    st.write("8. Have achieved commercial success, recording a pre-tax profit of $7.5 million in 2009.") 
    st.write("9. The Rajasthan Royals were initially expelled from the IPL in 2010 by the BCCI, leading to a legal battle and appeals filed by the team.") 
    st.write("10. The Sawai Mansingh Stadium in Jaipur is the home venue of the Rajasthan Royals cricket team ") 


elif(team_selected == "Kolkata Knight Riders"):
    st.write("1. Kolkata Knight Riders (KKR) is a professional franchise cricket team in the Indian Premier League (IPL) representing the city of Kolkata.")
    st.write("2. In 2008, KKR was bought by Shah Rukh Khan's company Red Chillies Entertainment, Juhi Chawla, and Jay Mehta for a price of $75.09 million.")
    st.write("3. KKR plays its home matches at the iconic Eden Gardens stadium in Kolkata.")
    st.write("4. KKR became IPL champions in 2012 by defeating Chennai Super Kings in the final.")
    st.write("5. They achieved their second IPL title in 2014 by defeating Kings XI Punjab.")
    st.write("6.The team's name, Knight Riders, is a reference to the popular 1980s American television series Knight Rider.")
    st.write("7. KKR holds the record for the longest winning streak by any Indian team in T20s, winning 14 matches in a row.")
    st.write("8. Gautam Gambhir is the all-time leading run-scorer for KKR.")
    st.write("9. KKR is currently coached by Stephen Fleming.Chandrakant Pandit")
    st.write("10. The official theme of KKR is 'Korbo, Lorbo, Jeetbo Re,' which translates to We will perform, fight, and win! and  the official colors are purple and gold.")

elif(team_selected == "Punjab Kings"):
    st.write("1. Punjab Kings (formerly Kings XI Punjab) is an IPL cricket team based in Mohali, Punjab.")
    st.write("2. The franchise was established in 2008 and is jointly owned by Mohit Burman, Ness Wadia, Preity Zinta, and Karan Paul.")
    st.write("3. The team plays its home matches at the PCA Stadium in Mohali and has also played in Dharamsala and Indore.")
    st.write("4. They topped the league table and finished as runners-up in the 2014 IPL season.")
    st.write("5. Punjab Kings made their only other playoff appearance in the IPL in 13 seasons.")
    st.write("6. In the 2022 IPL auction, Punjab Kings made the highest-ever bid in IPL history, acquiring Sam Curran for Rs 18.50 crores.")
    st.write("7. The franchise was purchased for $76 million in the 2008 auction.")
    st.write("8. The catchment areas for the team included Kashmir, Jammu, Himachal Pradesh, Punjab, and Haryana.")
    st.write("9. The team's logo features the letter sequence 'K J H P H' representing the catchment areas.")
    st.write("10. The franchise continues to participate in the IPL, striving for greater success in future seasons.")

elif(team_selected == "Delhi Capitals" ):
    st.write("1. Delhi Capitals, formerly known as Delhi Daredevils, is a professional franchise cricket team in the Indian Premier League (IPL), based in Delhi.")
    st.write("2. The team's ownership is a joint venture between the GMR Group and the JSW Group.")
    st.write("3. The franchise's home ground is the Arun Jaitley Stadium, previously known as Feroz Shah Kotla, located in New Delhi.")
    st.write("4. The team is coached by Ricky Ponting, the former Australian cricketer and captain.")
    st.write("5. In 2020, the Delhi Capitals reached their first IPL final, where they faced the Mumbai Indians.")
    st.write("6. The Delhi Daredevils franchise was acquired by the GMR Group in February 2008 for a price of US$84 million.")
    st.write("7. In 2018, GMR Group sold a 50percent stake in the Delhi Daredevils to JSW Sports for ₹550 crore (approximately US$69 million).")
    st.write("8. In December 2018, the team underwent a name change and became the Delhi Capitals.")
    st.write("9. The name change was motivated by the significance of Delhi as the capital city of India and its status as the power center of the country.")
    st.write("10. The new name, Delhi Capitals, represents the team's aspiration to be the center of all action, aligning with the city's identity and spirit.")

else:
    st.write("1. Sunrisers Hyderabad (SRH) is a professional cricket team based in Hyderabad, India, and competes in the Indian Premier League (IPL).")
    st.write("2. The franchise was established in 2012 after the termination of the Deccan Chargers, another IPL team based in Hyderabad.")
    st.write("3. Sunrisers Hyderabad is owned by Kalanithi Maran of the SUN Group.")
    st.write("4. The team is currently coached by Brian Lara and captained by Aiden Markram.")
    st.write("5. Their primary home ground is the Rajiv Gandhi International Cricket Stadium in Hyderabad, with a capacity of 55,000.")
    st.write("6. Sunrisers Hyderabad made their IPL debut in 2013 and reached the playoffs in their first season, finishing fourth.")
    st.write("7. They won their maiden IPL title in the 2016 season, defeating the Royal Challengers Bangalore in the final.")
    st.write("8. Since 2016, the team has consistently qualified for the playoff stage of the tournament.")
    st.write("9. Sunrisers Hyderabad is known for having a strong bowling lineup and is often praised for its ability to defend low totals.")
    st.write("10. David Warner is the leading run scorer for the team, winning the Orange Cap three times, while Bhuvneshwar Kumar is the leading wicket-taker, winning the Purple Cap twice.")


    
