import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("📄 Hello! This is my first app using Streamlit")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)
st.header('This is a header')
st.subheader('This is a subheader')
st.text('AI VIET NAM')
st.caption('This is a caption')

st.divider()

st.markdown('# Heading 1')
st.markdown('[AI VIET NAM](http://aivnlearning.edu.vn)')
st.markdown("""
            1. Machine Learning
            2. Deep Learning
""")
st.markdown(r'$ \sqrt{2x} $')

st.divider()

st.latex('\sqrt{2x}')

st.divider()

st.write('AI Viet Nam')
st.write('# Heading 1')
st.write('[Google](http://google.com)')
st.write(r'$\sqrt{2x}$')
st.write('1 - 1 = ', 2)

st.divider()
st.code("""
    import random
    value = random.randint(3, 10)
    print(value)
""")

def get_year():
    return '2003'

with st.echo():
    st.write('This is a text')
    def get_name():
        return 'Vang'
    
    name = get_name()
    year = get_year()
    st.write(name, year)

st.divider()

st.logo('/workspaces/Module-1-Streamlit/logo.png')
st.image('/workspaces/Module-1-Streamlit/image.jpg', caption='Robot and AI', use_column_width='always')

st.divider()

def get_full_name():
    return 'Vang'

agree = st.checkbox('I agree!', on_change=get_full_name)
if agree:
    st.write('Thank!')

status = st.radio('Your favorite color:', ['Yellow', 'Blue'], captions=['Yellow', 'Blue'])
print(status)

status = st.selectbox('Your contact', ['Email', 'Address'])
print(status)

options = st.multiselect('Colors:', ['Green', 'Yellow', 'Blue'])
print(options)

st.select_slider('Your colors:', [0, 1, 2])

st.divider()

if st.button('Say Hello'):
    st.write('Hi! How can I help')
else:
    st.write('Goodbye')

value = st.text_input('Your name:', value='Vang')
st.write(value)

st.divider()

upload_files = st.file_uploader('Choose Files:', accept_multiple_files=True)
for upload_file in upload_files:
    read_f = upload_file.read()
    st.write('File name: ', upload_file.name)

st.divider()

with st.form('my form'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('Name:')
    f_age = col2.text_input('Age:')

    submited = st.form_submit_button('Submit')
    if submited:
        st.write(f'Name: {f_name}, Age: {f_age}')

st.divider()

import random
value = random.randint(1, 10)

if 'key' not in st.session_state:
    st.session_state['key'] = value
    st.session_state['password'] = value
st.write(st.session_state.key)

st.divider()