import streamlit as st
st.set_page_config(page_title='视频播放器',page_icon='🐈')
st.header("🐈视频网站")
video_url = [{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/43/90/27990229043/27990229043-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=7ee16ba434804e50a78a83d0f4caf07h&mid=0&gen=playurlv3&deadline=1761301901&nbs=1&oi=771356656&os=cosovbv&og=cos&uipk=5&platform=html5&upsig=1564a1cace5b1b31c7cce8a5bb49def2&uparams=e,trid,mid,gen,deadline,nbs,oi,os,og,uipk,platform&bvc=vod&nettype=0&bw=523785&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
    'title':'👉大耳朵图图第一季',
    'episode':'1',
    'name':'主演:🧒胡图图,👨胡英俊,👩张小丽'},
             { 'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/62/09/33301530962/33301530962-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&mid=0&nbs=1&uipk=5&os=cosovbv&oi=771356656&platform=html5&deadline=1761302106&trid=82e79d923b984c5e94873c9756aa264h&gen=playurlv3&upsig=5c1005f0529cd4144ddb7f85aa5aaa55&uparams=e,og,mid,nbs,uipk,os,oi,platform,deadline,trid,gen&bvc=vod&nettype=0&bw=534406&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
               'title':'大耳朵图图第一季',
               'episode':'2',
                'name':'主演:胡图图,胡英俊,张小丽'},
             {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/78/38/29770123878/29770123878-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302178&nbs=1&oi=771356656&platform=html5&mid=0&gen=playurlv3&os=cosovbv&trid=6571acf34f2b42c6826698666bf4265h&og=hw&uipk=5&upsig=dc748d127fcc2de2279db90553b38687&uparams=e,deadline,nbs,oi,platform,mid,gen,os,trid,og,uipk&bvc=vod&nettype=0&bw=532430&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
              'title':'大耳朵图图第一季',
    'episode':'3',
              'name':'主演:胡图图,胡英俊,张小丽'
}]
if'ind' not in st.session_state:
    st.session_state['ind']=0
st.subheader(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['episode']+'集')
st.subheader(video_url[st.session_state['ind']]['name'])
st.video(video_url[st.session_state['ind']]['url'])
             
c1,c2,c3=st.columns(3)
def play(arg):
    st.session_state['ind']=int(arg)
    
for i in range(len(video_url)):
    st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
    
    
    


