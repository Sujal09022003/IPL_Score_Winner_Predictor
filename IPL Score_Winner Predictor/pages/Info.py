import math
import numpy as np
import pickle
import streamlit as st
import emoji

st.title("Description")

st.image("https://gumlet.assettype.com/newslaundry%2F2023-03%2Fd9540563-1c6f-45cc-84c6-6401dd484730%2Fipl.jpg?auto=format%2Ccompress&fit=max&format=webp&w=480&dpr=2.6", width=600)
st.write(" Cricket fans worldwide eagerly follow the Indian Premier League (IPL), a prestigious Twenty20 cricket tournament held annually in India. With its high intensity and star-studded lineups,predicting the score of IPL matches becomes a captivating endeavor. Accurate score predictions in IPL matches havimmense value for teams, analysts, and fans. While traditional methodsrelied on subjective judgments, the advent of machine learning and dataanalysis has opened new avenues for developing data-driven models thatcan leverage historical IPL match data. By incorporating factors such as the batting team, bowling team, current score, overs played, and otherrelevant variables, machine learning algorithms can discern patterns and relationships crucial for predicting the final score. This predictive capability can aid teams in strategic decision-making, enable analysts to assess player performance, and enhance the overall engagement and excitement of the IPL fans")
st.markdown('---')

st.title('Match Outcome Prediction')
st.image("Logos/logos.png", width=600)
st.write('The tool can analyze various factors such as team composition, past performance, player statistics, pitch conditions, and weather conditions to predict the likely outcome of IPL matches. This can be useful for fans, analysts, and cricket enthusiasts who want to make informed predictions about which team is likely to win a particular match.')
st.markdown('---')

st.title('LIVE Match Analysis')
st.image('https://i.gadgets360cdn.com/large/ipl_2021_mumbai_indians_chennai_super_kings_image_ron_gaunt_sportzpics_for_bcci_1632132402425.jpg',width=600)
st.write('During live matches, the tool can provide real-time updates on the expected scores, run rates, and potential outcomes based on the current match situation. This can be useful for fans who want to track the progress of a match and understand the impact of different events on the final result.')
st.markdown('---')

st.title('Player performence analysis')
st.image('https://media.licdn.com/dms/image/D5612AQHiTxXetoO2sg/article-cover_image-shrink_720_1280/0/1685987848135?e=2147483647&v=beta&t=_KA8X8vqOaJ2Qcvt1XA11MfpuuyXWk_YKIebJFuXlHY',width=600)
st.write(' The tool can analyze player statistics and historical data to predict the performance of individual players in upcoming matches. This can be valuable for team coaches and selectors who can use the insights to make decisions regarding player selection, batting order, bowling strategies, and field placements.')
st.write('The predictors insights into expected scores and win probabilities provide a benchmark against which team performance can be evaluated. Owners and coaches can compare the actual outcomes with the predicted results to assess the teams performance, identify areas for improvement, and make necessary adjustments in training and strategies.')
st.markdown('---')

st.title('Fantasy Cricket')
st.image('https://cdn0.desidime.com/cdn-cgi/image/fit=contain,f=auto,onerror=redirect,w=1200,h=675,q=90/topics/photos/1559488/original/FC.jpg',width=600)
st.write('Fantasy cricket is a popular online game where participants create virtual teams of real players and earn points based on their performance in actual matches. The IPL score predictor and probabilistic analysis tool can help users optimize their team selection by providing insights into player performance, match conditions, and probable scores. This can enhance the chances of winning fantasy cricket contests.')
st.markdown('---')


st.title('Broadcasting and Commentary')
st.image('https://maharashtratimes.com/photo/msid-90374289,imgsize-281827/pic.jpg',width=600)
st.write('Broadcasters and commentators can use the tool to enhance their analysis during IPL matches. By incorporating the predictions and probabilistic analysis into their commentary, they can provide viewers with insights into the likely course of the match, key turning points, and expected scores.')
st.markdown('---')

st.title('Team Strategies')
st.image('https://c.ndtvimg.com/2022-05/bb702c18_rcb-bcci_625x300_25_May_22.jpg?im=FeatureCrop,algorithm=dnn,width=1200,height=675',width=600)
st.write(' IPL teams can use the tool to analyze opponent strengths and weaknesses, historical performance, and other relevant data to develop effective strategies. It can assist teams in making data-driven decisions regarding team composition, batting orders, bowling plans, and fielding strategies.')
st.markdown('---')

st.title('Fan Engagement')
st.image('https://i0.wp.com/cricketaddictor.com/wp-content/uploads/2021/02/Wankhede-Stadium-Twitter.jpg?resize=780%2C681&ssl=1',width=600)
st.write('Stadiums can use the predictors analysis to engage the crowd during IPL matches. By displaying predicted scores and win probabilities on scoreboards or digital screens, spectators can get real-time insights into the expected outcome and excitement levels of the match. This enhances the fan experience and keeps the crowd engaged throughout the game.')
st.write('The IPL score predictor can be utilized by fan-centric platforms or applications to engage and entertain cricket enthusiasts. Fans can make predictions about match outcomes, top performers, or specific events like the number of boundaries or sixes. The tool can provide them with a probabilistic framework to make informed predictions and foster fan interaction.')
st.markdown('---')

st.title('Promoting IPLT20 Fan Parks')
st.image('https://th-i.thgim.com/public/news/national/andhra-pradesh/article23875819.ece/alternates/FREE_1200/14VJPAGE3CRICKETFANS',width=600)
st.write('Engaging Fan Contests: Fan parks can organize contests or prediction games based on the projected scores and win probabilities from the predictor. Fans can participate by making their own predictions and compete for prizes or recognition. This creates an interactive and engaging environment for fans, encouraging them to actively follow the matches and stay involved.')
st.write('Large-Scale Screen Displays: Fan parks typically have large screens or LED displays where matches are broadcasted. They can incorporate the projected scores and win probabilities as on-screen graphics during the matches. This allows fans to visually track the progress of the game and stay updated on the changing dynamics, making the viewing experience more informative and exciting')
st.markdown('---')


st.title('In Game Promotions')
st.image('https://assets.telegraphindia.com/telegraph/2022/Feb/1645174413_cms-size-900x506.jpg',width=600)
st.write('Stadiums can leverage the score and win probability predictor for in-game promotions and sponsor activations. For instance, if the win probability increases during a crucial phase of the match, the stadium can trigger special promotions, such as discounted merchandise, exclusive offers, or giveaways, to boost fan enthusiasm and drive sales. It can create a sense of anticipation and excitement among the crowd.')
st.markdown('---')         

st.title('Auction Strategies')
st.image('https://images.indianexpress.com/2019/12/ipl-auction-1200-1.jpg',width=600)
st.write('Before IPL auctions or player recruitment, the predictor can be used to evaluate potential players and assess their impact on the performance. Owners and coaches can consider players who align with the team needs and have a higher probability of contributing to the success of the team based on the analysis.')
st.markdown('---')


st.title('Long-term Planning for coaches,owners and mentors')
st.image('https://cdn.dnaindia.com/sites/default/files/styles/full/public/2022/03/17/1090599-punjab-kings-twitter.jpg',width=600)
st.write('The predictors analysis of win probabilities and performance trends can be valuable for long-term planning. Owners and coaches can use this information to assess the teams overall performance over time, identify patterns, and make strategic decisions regarding team building, retention of players, and investments in infrastructure and resources.')
st.markdown('---')


st.title('Matchday Preparations')
st.image('https://imgnew.outlookindia.com/public/uploads/articles/2021/4/6/IPL-Red-Carpet-Clean-BCCI.jpg',width=600)
st.write('The predictors insights can assist ground staff in understanding the significance and anticipated competitiveness of specific matches. They can take these factors into account while preparing the pitch, outfield, and other playing areas. Ground staff can ensure optimal conditions that align with the expected match outcomes, thereby contributing to the overall quality of the game.')
st.write('Schedule Planning: Ground staff can refer to the predicted match outcomes and schedules provided by the IPL score and win probability predictor to plan their work effectively. They can anticipate the duration of matches, potential result scenarios, and allocate resources accordingly. This helps in organizing their tasks, such as pitch preparation, ground maintenance, and facility setup, in a systematic manner.')
st.markdown('---')

st.title('Match Promotions,Sponsorships and Endorsements')
st.image('https://sportsmintmedia.com/wp-content/uploads/2022/03/Disney-Star-secures-multiple-sponsors-for-TATA-IPL.jpg',width=600)
st.write('Stadiums can utilize the predictors analysis as part of their promotional campaigns for IPL matches. By highlighting the expected high-scoring encounters or closely contested matches, stadiums can attract more spectators and create anticipation among fans. The predictors insights can be used in marketing materials, advertisements, and social media promotions to generate excitement and increase ticket sales.')
st.markdown('---')

st.title('News Articles,Reports,Media')
st.image('https://pbs.twimg.com/media/EbfsKYuU8AAhOqy.jpg',width=600)
st.write('Media outlets can use the predictor to generate data-driven news articles and reports. They can provide insights into the projected scores, win probabilities, and key factors influencing the match outcome. This allows them to deliver informative and engaging content to their readers.')
st.markdown('---')

st.title('Capturing turning points by cameraman')
st.image('https://images.news18.com/static-guju/uploads/2023/03/WhatsApp-Image-2023-03-10-at-12.10.42.jpeg',width=600)
st.write('Cameramen can use theinsights to anticipate and focus on key moments during the match. For example, if the predictor indicates a high win probability for a team in a crucial phase of the game, the cameramen can position themselves to capture the reactions, celebrations, and emotions of the players and fans during that period.')
st.markdown('---')

st.title('Celebrating moments')
st.image('https://im.rediff.com/cricket/2013/may/15cheer1.jpg',width=600)
st.write('Cheer girls can pay attention to the projected turning points or match-deciding moments. When these moments occur, they can perform routines or cheers that celebrate the achievements of the teams involved. This adds to the excitement and atmosphere in the stadium, enhancing the overall experience for the spectators.')
st.write('Cheer girls can adapt their routines based on the projected scores and win probabilities. For example, if the predictor indicates a close contest or a tense situation, they can design routines that build anticipation and reflect the intensity of the match. Similarly, if a team is expected to dominate, they can create routines that celebrate the win')
st.markdown('---')

st.title('Decision-making Assistance for Umpirirng')
st.image('https://circleofcricket.com/post_image/post_image_cf8df5c.jpg',width=600)
st.write('The  insights can help umpires stay aware of the dynamics and potential turning points in the game. By understanding the projected scores and win probabilities, umpires can anticipate critical moments and be prepared for potential game-changing situations. This allows them to maintain focus, make accurate decisions, and manage the match effectivel')
st.write('Umpires can use the predictor projections to engage in discussions with players during the match. It can serve as a topic of conversation, allowing umpires to interact with players, provide context, and address any concerns or questions related to the match outcome')
st.markdown('---')         
         



st.title('Matchday Operations')
st.image('https://images.newindianexpress.com/uploads/user/imagelibrary/2023/4/2/w900X450/matches.jpg?w=400&dpr=2.6',width=600)
st.write('The predictors analysis of expected scores and win probabilities can aid in matchday operations for stadiums. Stadium authorities can adjust their logistics and operations based on the predicted outcomes. For example, they can plan for additional security or crowd management measures for high-scoring matches or matches with a close win probability. This helps ensure the smooth running of the event and enhances the overall matchday experience for spectators.')
st.markdown('---')


st.title('VIP and Hospitality Services')
st.image('https://i.pinimg.com/originals/eb/39/b7/eb39b78769e3fd24a4714c4b074bd454.png',width=600)
st.write('Stadiums can use the predictors analysis to enhance hospitality and VIP services during IPL matches. Premium ticket holders and corporate guests can receive exclusive access to the predictors insights, allowing them to make more informed assessments and predictions about the match. This adds value to their hospitality experience and provides them with engaging content to discuss and enjoy during the event.')

st.title('..............................and many more')





















































