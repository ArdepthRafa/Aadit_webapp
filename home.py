import streamlit as st
tab1, tab2, tab3 = st.tabs(["About", "Hobbies", "Contact"])
with tab1:
    col1, col2 = st.columns([0.2, 0.5])
    with col1: 
        st.image("Aadit.jpg", width = 170)
        st.subheader("Aadit Srivastava :sunglasses:")
    with col2: 
        st.write("Hi! I am Aadit and I am 12 years old. I am in sixth grade at Mills Park Middle School. My favorite subjects are math and science, and I want to be a tennis player when I grow up. I live in North Carolina with my parents, my sister, and a lonely fish named Fins.")
        st.write("Our parents need a way to track their expenses efficiently because they find it challenging to track them manually. So, I, being a junior engineer, fashioned this website to help parents solve this problem and have more overall free time.")
with tab2:
    st.write("Some things I like to do in my free time include playing tennis and chess, reading, learning languages, and doing math. I know Hindi, English, and French.")
with tab3:
    st.write("E-mail:")
    st.write("asrivastava8@students.wcpss.net")
    st.write(" ")
    st.write("Website Link:")
    st.write("http://tinyurl.com/eb34m788")