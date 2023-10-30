import streamlit as st

# Check if on Thank You page or main page
page = st.session_state.get("page", "main")

if page == "main":
    # st.title("Streamlit App")

    # Headline with highlighted text
    st.markdown("""
    <style>
        .highlight {
            background-color: yellow;
            color: black;
        }
    </style>
    <h1>How I made <span class="highlight">$5k in 5 days</span></h1>
    """, unsafe_allow_html=True)

    # Create columns for Dog image and Form
    col1, col2 = st.columns(2)

    # Dog image on the left column
    with col1:
        st.markdown(
            '<img src="https://images.dog.ceo/breeds/terrier-wheaten/clementine.jpg" width="300">',
            unsafe_allow_html=True,
        )

    # Form on the right column
    with col2:
        with st.form("user_form"):
            name = st.text_input("Name:")
            email = st.text_input("Email:")
            phone = st.text_input("Phone Number:")
            submit_button = st.form_submit_button("Yes I want this")

            if submit_button:
                st.session_state["page"] = "thank_you"
                st.session_state["name"] = name
                st.session_state["email"] = email
                st.session_state["phone"] = phone
                st.write("Redirecting...")
                st.experimental_rerun()

elif page == "thank_you":
    st.title("Thank You!")
    st.write(f"Thanks for joining our waitlist!")
    st.write(f"Here are your details:")
    st.write(f"Name: {st.session_state['name']}")
    st.write(f"Email: {st.session_state['email']}")
    st.write(f"Phone: {st.session_state['phone']}")
