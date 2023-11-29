import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from Dependencies import sign_up, fetch_users  

st.set_page_config(page_title='LiftR', page_icon='🐍', initial_sidebar_state='collapsed')


users = fetch_users()
emails = []
usernames = []
passwords = []

for user in users:
    emails.append(user['key'])
    usernames.append(user['username'])
    passwords.append(user['password'])

credentials = {'usernames': {}}
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

# credentials = {'usernames': {}, 'passwords': {}}
# for user in users:
#     username = user['username']
#     password = user['password']
#     credentials['usernames'][username] = username
#     credentials['passwords'][username] = password


Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

info, info1 = st.columns(2)

if not authentication_status:
    sign_up()

if username:
    if username in usernames:
        if authentication_status:
            # let User see app

            st.title('Liftr: Squats Analysis')
            st.sidebar.success("Select a page above")    
            recorded_file = 'sample.mp4'
            sample_vid = st.empty()
            sample_vid.video(recorded_file)
            st.sidebar.subheader(f'Welcome {username}')
            Authenticator.logout('Log Out', 'sidebar')

            st.subheader('This is the home page')
            

        elif not authentication_status:
            with info:
                st.error('Incorrect Password or username')
        else:
            with info:
                st.warning('Please feed in your credentials')
    else:
        with info:
            st.warning('Username does not exist, Please Sign up')



#    st.success('Refresh Page')



