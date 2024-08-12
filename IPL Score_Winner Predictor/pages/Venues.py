import math
import numpy as np
import pickle
import streamlit as st
import emoji
import folium
from streamlit_folium import st_folium


st.title('M Chinnaswamy Stadium,Bengaluru')
st.image('https://www.royalchallengers.com/PRRCB01/public/styles/1061x767_landscape/public/2020-03/chinnaswamystadium_1.jpg?h=08b25f12&itok=hamzv-PF',width=600)
st.write('Chinnaswamy Stadium, officially known as M. Chinnaswamy Stadium, is a cricket stadium located in Bangalore, Karnataka, India. It is one of the premier cricket venues in the country and serves as the home ground for the Karnataka state cricket team and the Royal Challengers Bangalore (RCB) franchise in the Indian Premier League (IPL).')
st.write('Location:   Chinnaswamy Stadium is situated in the heart of Bangalore, near the MG Road area. The full address is M Chinnaswamy Stadium, MG Road, Bangalore - 560001, Karnataka, India.')
st.write('Capacity:   The stadium has a seating capacity of around 45000 spectators, making it one of the smaller stadiums in terms of capacity in the IPL. However, it is known for its electric atmosphere and enthusiastic crowd support during matches.')
st.write('Architecture:    Chinnaswamy Stadium is known for its unique design, with most of the seating arranged in two tiers around the playing field. It has a predominantly circular shape and features multiple stands, including the Pavilion Stand, Grand Stand, and others.')
st.write('Facilities:     The stadium is equipped with various facilities to cater to the needs of spectators. It has food and beverage stalls, restrooms, parking facilities, and entry gates for smooth crowd management.')
st.write('Pitch and Ground:    The pitch at Chinnaswamy Stadium is known to be batsman-friendly, with good pace and bounce. It has produced high-scoring matches in the past, often favoring stroke play. The outfield is well-maintained, providing fast and true bounce for fielders.')
st.write('Iconic Features:    Chinnaswamy Stadium is famous for its distinctive red soil, which gives it a unique appearance. It is also known for the "V," the area between mid-off and mid-on, where the ball travels quickly off the bat due to the favorable pitch conditions.')
st.write('Major Matches:    Chinnaswamy Stadium has hosted several memorable matches, including international fixtures such as Test matches, One-Day Internationals (ODIs), and T20 Internationals. It has also hosted multiple IPL matches, including playoffs and finals.')
st.write('History:    The stadium was established in 1969 and has hosted a wide range of domestic and international cricket matches. It has been a regular venue for IPL matches, including numerous home games for the Royal Challengers Bangalore franchise.')
st.write('Accessibility:    The stadium is well-connected to various parts of Bangalore and is easily accessible by public transport, including buses, metro, and taxis. It is situated in a central location, making it convenient for spectators to reach the venue.')
st.markdown('---')

st.title('Arun Jaitley Stadium,New Delhi')
st.image('https://cricreads.com/wp-content/uploads/2023/04/2bb07fc7e3e0f24ff4fbe7fb1e28824d.jpg',width=600)
st.write('Location: Arun Jaitley Stadium is situated in the city of Delhi, specifically in the Feroz Shah Kotla area, near the Kotla Fort and adjacent to the Yamuna River. The full address is Jawaharlal Nehru Marg, Feroze Shah Kotla, Raj Ghat, New Delhi, Delhi 110002, India.')
st.write('Capacity: The stadium has a seating capacity of approximately 75000 spectators. It is one of the oldest cricket stadiums in India and has undergone several renovations to enhance its facilities and capacity.')
st.write('Architecture: The stadium features a traditional cricket stadium design, with seating arranged in multiple tiers around the field. It has various stands, including the Pavilion End, Inderjit Singh Gill Stand, R.P. Mehra Block, and more.')
st.write('Facilities: Arun Jaitley Stadium offers various facilities for spectators, including food and beverage outlets, restrooms, and parking facilities. It also has practice facilities and dressing rooms for players.')
st.write('Pitch and Ground: The pitch at Arun Jaitley Stadium generally offers assistance to spin bowlers. It is known for its slow and low bounce, making it challenging for batsmen at times. The outfield is well-maintained, providing good playing conditions.')
st.write('Iconic Features: The stadium has a rich history and is known for hosting numerous historic matches. It has seen several memorable performances and records, including the likes of Anil Kumbles ten-wicket haul in a Test match against Pakistan in 1999.')
st.write('History: The stadium has a long history and has hosted international cricket matches since 1948. It has witnessed a range of matches, including Test matches, One-Day Internationals (ODIs), and T20 Internationals. Over the years, it has been a regular venue for domestic cricket as well.')
st.write('Major Matches: Arun Jaitley Stadium has hosted many significant matches, including international fixtures such as Test matches and ODIs. It has also hosted IPL matches, including home games of the Delhi Capitals franchise.')
st.write('Accessibility: The stadium is located in the central part of Delhi, making it easily accessible. It is well-connected by various modes of transportation, including buses, metro, and taxis. The nearest metro station to the stadium is Delhi Gate Metro Station.')
st.markdown('---')

st.title("Eden Gardens,Kolkata")
st.image('https://www.iplt20.com/assets/images/stadiumimage/eden-garden-small-new.jpg',width=600)
st.write('Eden Gardens is a historic cricket stadium located in Kolkata, West Bengal, India. It is one of the most iconic and largest cricket stadiums in the world, known for its electric atmosphere and passionate cricket fans. Here are some details about Eden Gardens:')
st.write('Capacity: Eden Gardens has a seating capacity of around 90000 spectators, making it the largest cricket stadium in India and the third-largest in the world.')
st.write('Establishment: The stadium was established in 1864 and has since undergone several renovations and expansions.')
st.write('Location: Eden Gardens is situated in B.B.D. Bagh area in Kolkata, adjacent to the famous Victoria Memorial.')
st.write('Home Team: Eden Gardens is the home ground of the Kolkata Knight Riders (KKR) franchise in the Indian Premier League (IPL). The stadium has also hosted numerous international matches featuring the Indian cricket team.')
st.write('Pitch and Ground Conditions: The pitch at Eden Gardens is known to be generally batting-friendly, offering good bounce and carry. The outfield is well-maintained, and the ground provides a picturesque setting for cricket.')
st.write('Historic Matches: Eden Gardens has witnessed several historic matches, including the 1987 World Cup final between Australia and England, the 1996 World Cup semi-final between India and Sri Lanka, and the 2001 Test match between India and Australia, famously known as the "VVS Laxmans 281" Test.')
st.write('Floodlights: Eden Gardens is equipped with floodlights, enabling day-night matches to be played at the stadium.')
st.write('Surrounding Facilities: The stadium complex also includes practice grounds, indoor cricket facility, a clubhouse, and other amenities to support cricket activities.')
st.markdown('---')


st.title('Wankhade Stadium,Mumbai')
st.image('https://library.sportingnews.com/styles/twitter_card_120x120/s3/2023-04/banner-1.jpg?itok=ikHsFuT3',width=600)
st.write('Wankhede Stadium is a prominent cricket stadium located in Mumbai, Maharashtra, India. It has a rich history and is known for hosting several memorable cricket matches, including the Indian Premier League (IPL) matches and international matches. Here are some details about Wankhede Stadium:')
st.write('Capacity: Wankhede Stadium has a seating capacity of approximately 80000 spectators for international matches and around 45,000 spectators for IPL matches.')
st.write('Establishment: The stadium was established in 1974 and has undergone renovations and upgrades since then, including a major redevelopment before the 2011 ICC Cricket World Cup.')
st.write('Location: Wankhede Stadium is situated in the Churchgate area of South Mumbai, near the Arabian Sea.')
st.write('Architecture: The stadium is known for its modern and aesthetically appealing architecture. It features multiple stands, including the Garware Pavilion and Tata Stand, which offer excellent viewing angles for spectators.')
st.write('Pitch and Ground Conditions: The pitch at Wankhede Stadium is traditionally known to support batsmen, offering good bounce and pace. The outfield is well-maintained, and the ground provides a fast and lively surface for cricket.')
st.write('Home Team: Wankhede Stadium is the home ground of the Mumbai Indians (MI) franchise in the Indian Premier League. The team has won several IPL titles, creating a strong association between the stadium and the Mumbai Indians.')
st.write('Memorable Matches: Wankhede Stadium has witnessed numerous historic matches. It hosted the final of the 2011 ICC Cricket World Cup, where India emerged as the champions by defeating Sri Lanka. The stadium also witnessed Sachin Tendulkars farewell Test match in 2013 and various thrilling IPL encounters.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, a gymnasium, a swimming pool, and other amenities to support cricket activities.')
st.write('Accessibility: Wankhede Stadium is well-connected and easily accessible via various modes of transportation, including trains, buses, and taxis.')
st.markdown('---')

st.title('P.A Chidambaram Stadium,Chennai')
st.image('https://upload.wikimedia.org/wikipedia/commons/a/a2/MA_Chidambaram_Stadium_In_the_Night_during_a_CSK_Game.jpg',width=600)
st.write('Chidambaram Stadium, officially known as the M. A. Chidambaram Stadium, is a renowned cricket stadium located in Chepauk, Chennai, Tamil Nadu, India. It is one of the oldest cricket grounds in India and has hosted numerous domestic and international cricket matches. Here are some details about Chidambaram Stadium:')
st.write('Capacity: Chidambaram Stadium has a seating capacity of around 55000 spectators for international matches. It is known for its intimate atmosphere, which allows fans to be close to the action.')
st.write('Establishment: The stadium was established in 1916 and is named after M. A. Chidambaram, a former President of the Board of Control for Cricket in India (BCCI).')
st.write('Location: Chidambaram Stadium is located in the heart of Chennai, near the Marina Beach, making it easily accessible for fans.')
st.write('Architecture: The stadium has a traditional design with multiple stands that offer good visibility for spectators. The Anna Pavilion Stand and the V Pattabhiraman Gate End Stand are notable features of the stadium.')
st.write('Pitch and Ground Conditions: Chidambaram Stadium is known for its spin-friendly pitches, which tend to assist the slow bowlers. The outfield is well-maintained, and the ground has a good drainage system, allowing matches to take place even during monsoons.')
st.write('Home Team: Chidambaram Stadium is the home ground of the Chennai Super Kings (CSK) franchise in the Indian Premier League (IPL). The team has a strong fan base, and the stadium often witnesses a sea of yellow during CSK matches.')
st.write('Memorable Matches: The stadium has witnessed several historic matches. It hosted the 2011 ICC Cricket World Cup matches, including the quarter-final clash between India and Australia. Chidambaram Stadium has also seen many thrilling IPL encounters and has been a fortress for the Chennai Super Kings.')
st.write('Renovations: The stadium has undergone renovations and upgrades over the years to meet international standards. The most recent renovation took place before the 2011 World Cup, which included the construction of new stands, improved facilities, and a revamped media center.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, dressing rooms, a gymnasium, and other amenities to cater to the needs of players and officials.')
st.write('Vibrant Atmosphere: Chidambaram Stadium is known for its passionate cricket fans who create an electrifying atmosphere during matches. The "Chepauk Roar" is famous among cricket enthusiasts.')
st.markdown('---')

st.title('Rajiv Gandhi International Stadium,Hyderabad')
st.image('https://www.mykhel.com/img/1200x60x675/2023/04/rajiv-gandhi-international-stadium-ipl-1680458844.jpg',width=600)
st.write('The Hyderabad Cricket Stadium, also known as the Rajiv Gandhi International Cricket Stadium, is a prominent cricket stadium located in Uppal, Hyderabad, Telangana, India. It serves as the home ground for the Sunrisers Hyderabad (SRH) franchise in the Indian Premier League (IPL) and has also hosted numerous international cricket matches. Here are some details about the Hyderabad Cricket Stadium:')
st.write('Capacity: The stadium has a seating capacity of around 750000 spectators for international matches and IPL matches.')
st.write('Establishment: The Hyderabad Cricket Stadium was established in 2004 and was later renamed after the former Prime Minister of India, Rajiv Gandhi.')
st.write('Location: The stadium is situated in Uppal, on the outskirts of Hyderabad, making it easily accessible for fans.')
st.write('Architecture: The stadium has a modern design with multiple stands that provide a good view of the playing field. The Pavilion End and the VVS Laxman Stand are notable features of the stadium.')
st.write('Pitch and Ground Conditions: The pitch at the Hyderabad Cricket Stadium generally favors batsmen, with good bounce and true pace. The outfield is well-maintained, and the ground provides a fast surface for cricket.')
st.write('Home Team: The Sunrisers Hyderabad (SRH) franchise represents Hyderabad in the Indian Premier League (IPL), and the Hyderabad Cricket Stadium serves as their home ground. The team has a strong fan base, and the stadium witnesses enthusiastic support for the home team during IPL matches.')
st.write('Memorable Matches: The stadium has hosted several memorable matches, including IPL matches and international encounters. It has seen thrilling IPL encounters, where both high-scoring matches and close finishes have taken place.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, dressing rooms, media facilities, and other amenities to support cricket activities.')
st.write('Vibrant Atmosphere: The Hyderabad Cricket Stadium offers a vibrant and lively atmosphere during matches, with passionate fans cheering for their favorite teams. The atmosphere is often electrifying during IPL matches.')
st.markdown('---')

st.title('SMS Stadium,Jaipur')
st.image('https://www.jaipurcityblog.com/wp-content/uploads/2014/04/SMS-Stadium-Jaipur-2012-999-news-1.jpg',width=600)
st.write('The Sawai Mansingh Stadium is a renowned cricket stadium located in Jaipur, Rajasthan, India. It is one of the major cricket venues in the country and has hosted several domestic and international cricket matches. Here are some details about the Sawai Mansingh Stadium:')
st.write('Capacity: The stadium has a seating capacity of approximately 23000 spectators. However, during IPL matches, temporary seating arrangements are made to accommodate a larger audience.')
st.write('Establishment: The Sawai Mansingh Stadium was established in 1969 and has since become a popular destination for cricket enthusiasts in Jaipur and across the state of Rajasthan.')
st.write('Location: The stadium is situated in the heart of Jaipur, near the Rambagh Circle.')
st.write('Architecture: The stadium has a traditional design with multiple stands that offer good views of the playing field. The pavilion and the north stand are notable features of the stadium.')
st.write('Pitch and Ground Conditions: The pitch at Sawai Mansingh Stadium is generally batting-friendly, providing good bounce and pace. The outfield is well-maintained, and the ground offers a fast and true surface for cricket.')
st.write('Home Team: The Sawai Mansingh Stadium is the home ground of the Rajasthan Royals (RR) franchise in the Indian Premier League (IPL). The team has a strong fan base in Jaipur and enjoys significant support during home matches.')
st.write('Memorable Matches: The stadium has witnessed several memorable matches, including IPL encounters, domestic matches, and international games. It has hosted high-scoring matches, close finishes, and historic moments in cricket.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, dressing rooms, media facilities, and other amenities required to support cricket activities.')
st.write('Vibrant Atmosphere: The Sawai Mansingh Stadium offers a vibrant and energetic atmosphere during matches, with passionate fans cheering for their favorite teams. The IPL matches at the stadium are known for their lively atmosphere and enthusiastic crowd.')
st.markdown('---')

st.title('Inderjit Bindra Stadium,Mohali')
st.image('https://smedia2.intoday.in/indiatoday/images/stories/2014March/punjab_650_041114054907.jpg',width=600)
st.write('The Mohali Cricket Stadium, officially known as the Punjab Cricket Association IS Bindra Stadium, is a prominent cricket stadium located in Mohali, Punjab, India. It is one of the premier cricket grounds in India and has hosted numerous domestic and international cricket matches. Here are some details about the Mohali Cricket Stadium:')
st.write('Capacity: The stadium has a seating capacity of approximately 26,950 spectators. However, during IPL matches or high-profile matches, temporary seating arrangements can be made to accommodate a larger audience.')
st.write('Establishment: The Mohali Cricket Stadium was established in 1993 and has since become a well-regarded venue for cricket in the country.')
st.write('Location: The stadium is situated in Phase 9 of Mohali, near Chandigarh, the capital city of Punjab and Haryana.')
st.write('Architecture: The stadium has a modern design with multiple stands that offer excellent views of the playing field. The pavilion and the north stand are notable features of the stadium.')
st.write('Pitch and Ground Conditions: The pitch at the Mohali Cricket Stadium is known for its good bounce and pace, which makes it conducive for both batsmen and fast bowlers. The outfield is well-maintained, and the ground offers a fast and true surface for cricket.')
st.write('Home Team: The Mohali Cricket Stadium serves as the home ground for the Punjab Kings (formerly Kings XI Punjab) franchise in the Indian Premier League (IPL). The team enjoys significant support from the local crowd during their home matches.')
st.write('Memorable Matches: The stadium has hosted several memorable matches, including IPL encounters, domestic matches, and international fixtures. It has witnessed high-scoring matches, thrilling finishes, and notable performances from players.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, dressing rooms, media facilities, and other amenities required to support cricket activities.')
st.write('Vibrant Atmosphere: The Mohali Cricket Stadium offers a vibrant and energetic atmosphere during matches, with passionate fans cheering for their favorite teams. The stadium is known for its lively atmosphere, especially during IPL matches.')
st.markdown('---')

st.title('Narendra Modi Stadium,Ahmedabad')
st.image('https://im.rediff.com/cricket/2021/feb/24inside-motera1.jpg',width=600)
st.write('The Narendra Modi Stadium, formerly known as the Sardar Patel Stadium, is a world-class cricket stadium located in Motera, Ahmedabad, Gujarat, India. It is the largest cricket stadium in the world by seating capacity and serves as a prominent venue for domestic and international cricket matches. Here are some details about the Narendra Modi Stadium:')
st.write('Capacity: The Narendra Modi Stadium has a seating capacity of approximately 132,000 spectators, making it the largest cricket stadium globally in terms of capacity. The stadium can accommodate a massive audience for matches.')
st.write('Establishment: The stadium was originally constructed in 1983, but it underwent a major redevelopment and was rebuilt between 2016 and 2020. The revamped stadium was inaugurated in February 2020.')
st.write('Location: The stadium is located in Motera, on the outskirts of Ahmedabad, Gujarat. It is easily accessible for spectators.')
st.write('Architecture: The Narendra Modi Stadium features a modern and futuristic design. It has a unique circular structure with a large roof canopy that covers most of the seating areas, providing shade and protection to the spectators.')
st.write('Pitch and Ground Conditions: The pitch at the Narendra Modi Stadium is known to offer good bounce and carry, providing an exciting contest between bat and ball. The outfield is well-maintained, and the ground provides a fast and true surface for cricket.')
st.write('Home Team: The Titans (GCA) utilizes the Narendra Modi Stadium as its home ground for domestic cricket matches. It has also hosted several IPL matches.')
st.write('Memorable Matches: The stadium has already witnessed some historic moments. It hosted the third Test match between India and England in February 2021, which was the first international match played at the revamped stadium. The stadium has also hosted IPL matches and knockout matches of various cricket tournaments.')
st.write('Surrounding Facilities: The stadium complex includes practice facilities, dressing rooms, media facilities, and other amenities required to support cricket activities. It also includes modern facilities for players, officials, and spectators.')
st.write('Vibrant Atmosphere: The Narendra Modi Stadium offers a vibrant and electric atmosphere during matches, with the massive crowd creating an incredible ambiance. The enthusiastic fans make it an exhilarating experience for players and spectators alike.')
st.markdown('---')



st.title(' BRSABV Ekana Stadium,Lucknow')
st.image('https://cdn-wp.thesportsrush.com/2023/04/303280a6-atal-bihari-vajpayee-stadium-t20-records.jpg',width=600)
st.write('The Ekana Cricket Stadium, officially known as the Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, is a cricket stadium located in Lucknow, Uttar Pradesh, India. It is a relatively new stadium and has quickly gained prominence as a venue for domestic and international cricket matches. Here are some details about the Ekana Cricket Stadium:')
st.write('Capacity: The Ekana Cricket Stadium has a seating capacity of approximately 50,000 spectators. It can accommodate a significant number of fans during matches.')
st.write('Establishment: The stadium was established in 2017 and was officially inaugurated in November 2018. It is named after the former Prime Minister of India, Atal Bihari Vajpayee.')
st.write('Location: The Ekana Cricket Stadium is situated in Gomti Nagar, Lucknow, which is the capital city of Uttar Pradesh. It is easily accessible for spectators.')
st.write('Architecture: The stadium has a modern design with multiple stands that offer excellent views of the playing field. It features state-of-the-art facilities and infrastructure.')
st.write('Pitch and Ground Conditions: The pitch at the Ekana Cricket Stadium is known to be batting-friendly, with good bounce and carry. The outfield is well-maintained, and the ground provides a fast and true surface for cricket.')
st.write('Home Team: The Lucknow Super Giants cricket team utilizes the Ekana Cricket Stadium as its home ground for domestic cricket matches. It has also hosted a few international matches.')
st.write('Memorable Matches: The stadium has hosted several domestic matches, including Ranji Trophy matches and Syed Mushtaq Ali Trophy matches. It has also hosted a few international matches, making it an important venue for cricket in the region.')
st.write('Facilities: The stadium complex includes practice facilities, dressing rooms, media facilities, and other amenities required to support cricket activities. It also offers modern amenities for players, officials, and spectators.')
st.write('Surrounding Infrastructure: The stadium is part of a larger sports complex that includes a multipurpose arena, a sports academy, and other sporting facilities. The complex aims to promote various sports in the region.')
st.write('Vibrant Atmosphere: The Ekana Cricket Stadium offers a vibrant and enthusiastic atmosphere during matches, with fans cheering for their favorite teams. The modern amenities and the excitement of the crowd make it an enjoyable experience for spectators.')
st.markdown('---')

















         
