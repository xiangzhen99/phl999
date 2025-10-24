import streamlit as st
st.set_page_config(page_title='音乐歌单',page_icon='🐈')
music= [{'url':"https://music.163.com/song/media/outer/url?id=461811019.mp3",
           'photo':'https://p2.music.126.net/RzeeuhXoVhvrSgRkkF9vig==/18734578627494886.jpg?param=330y280',
           'name':'歌名:屋顶 歌手👨‍🎤:周杰伦 时长⏰︎:2:32'},
          {'url': "https://music.163.com/song/media/outer/url?id=2736682437.mp3",
           'photo':'https://p1.music.126.net/SvT-8cEpiT0UrlEKzqmSJA==/109951171874589305.jpg?param=330y280',
           'name':'歌名:i like u like 歌手👨‍🎤:时代少年团 时长⏰︎:3:05'},
          {'url':"https://music.163.com/song/media/outer/url?id=1330348068.mp3",
           'photo':'https://p2.music.126.net/diGAyEmpymX8G7JcnElncQ==/109951163699673355.jpg?param=330y280',
           'name':'歌名:起风了 歌手👨‍🎤:买辣椒也用券 时长⏰︎:5:25'}
          ]
import streamlit as st
import random
st.subheader("🫶音乐歌单")
if'ind' not in st.session_state:
    st.session_state['ind']=0
    

def nextIMG():
   st.session_state['ind']=(st.session_state['ind']+1)%len(music)
    
def prevIMG():
   st.session_state['ind']=(st.session_state['ind']-1)%len(music)

def randomIMG():
    st.session_state['ind']=random.randint(0, len(music)-1)

col_cover, col_info = st.columns([1, 2])  
with col_cover:
    st.image(
        music[st.session_state['ind']]['photo'],
        use_container_width=True 
    )

with col_info:
    song_name = music[st.session_state['ind']]['name'].split(' ')[0]
    singer = music[st.session_state['ind']]['name'].split(' ')[1]
    duration = music[st.session_state['ind']]['name'].split(' ')[2]
    
    st.subheader(song_name)
    st.write(f" {singer}")
    st.write(f" {duration}")
    st.audio(music[st.session_state['ind']]['url'], format="audio/mp3")
    
col1,col2,col3=st.columns(3)
with col1:
     st.button('👆上一首',on_click=prevIMG,use_container_width=True)
with col2:
     st.button('👇下一首',on_click=nextIMG,use_container_width=True)
with col3:
     st.button('🤟随机',on_click=randomIMG,use_container_width=True)

