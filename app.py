import streamlit as st


with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Samuel Portfolio")
    choice = st.radio("Navigation", ["About Sam","Projects","Attached files", "Contact"])
    st.info("This project application helps you understand more about Samuel and his capabilities in detail.")

if choice == "About Sam":
    st.title("Hi am Samuel Mutinda")
    
if choice == "Projects": 
    st.title("Projects done by Samuel")

if choice == "Contact":
    st.title("You can contact me via:")

if choice == "Attached files": 
    st.title("Download final project report here")
