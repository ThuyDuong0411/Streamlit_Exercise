import streamlit as st
st.title("My Project")
st.header("This is header")
st.subheader("This is subheader")
st.text("AI Vietnam")
st.caption("This is a caption")

st.divider()
st.markdown("# Heading 1")
st.markdown("[AI Viet Nam](https://huce.edu.vn)")
st.markdown("""
            1. Machine Learning
            2. Deep Learning
            """)
st.markdown(r"$ \sqrt{2x} $")
st.divider()
st.latex('\sqrt{2x}')
st.write("I love Viet Nam")
st.write("# Heading 1")
st.write("[DHXDHN](https://huce.edu.vn)")

st.write("This is text")
st.image('logo.png', caption='Logo của ứng dụng')
st.image("dogs.jpeg",caption="Funny dog")
st.audio("audio.mp4")
st.video("video.mp4")
st.divider()
agree = st.checkbox("I agree!")
print(agree)
if agree:
    st.write("Thank")
status = st.radio("Your Favourite Color",["Yellow", "Blue"], captions=["Vàng","Xanh"])
print(status)
status = st.selectbox("Your Contact", ["Email","Adress"])
print(status)
st.multiselect("Color",["Green","Yellow","Blue"],"Yellow")
opiton = st.select_slider("Your Color",["Red","Yellow","Blue"])
st.divider()
if st.button("Say hello"):
    st.write("hello")
else:
    st.write("goodbye")
value = st.text_input("Your name", value="Duong")
st.write(value)
st.file_uploader("Choose One Files")
upload_files = st.file_uploader("Choose Multi Files",accept_multiple_files=True)
for upload_file in upload_files:
    read_f = upload_file.read()
    st.write("File name: ", upload_file.name)
st.divider()

with st.form("My form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("Name:")
    f_age = col2.text_input("Age: ")
    submited = st.form_submit_button("Submit")
    if submited:
        st.write(f" Name: {f_name}, Age:{f_age}")
st.divider()
import random
value = random.randint(1,10)
if 'key' not in st.session_state:
    st.session_state['key'] = value
st.write(st.session_state.key)
