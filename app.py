import streamlit as st

st.title("AI Resume & Portfolio Builder")

name = st.text_input("Enter Your Name")
email = st.text_input("Enter Your Email")
skills = st.text_area("Enter Skills (comma separated)")

if st.button("Generate Resume"):
    st.subheader("Generated Resume")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Skills: {skills}")