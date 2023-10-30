import streamlit as st
import requests
import os


def notify_signup_via_text(name, email, phone):
  api_token = "ec19b0234d6ef0ab43b3d89d788a8f5d"
  account_phone_number = "3235451278"
  your_phone_number = "12247257844"

  message = f"New affiliate sign-up: Name: {name}, Email: {email}, Phone: {phone}"

  url = "https://app2.simpletexting.com/v1/send"

  payload = {
      "token": api_token,
      "phone": your_phone_number,
      "from": account_phone_number,
      "message": message
  }

  response = requests.post(url, data=payload)

  if response.status_code == 201:
    print("Text message sent successfully!")
  else:
    print(f"Failed to send text message. Status Code: {response.status_code}")


def calculate_earnings(num_referrals, commission_rate, course_price):
  return num_referrals * (course_price * commission_rate / 100)


# Initial layout
st.title("Do you want to make money sharing my course?")
st.subheader(
    "Earn 50% commission on each student that enrolls in the course... Without limits."
)

st.write("""
For example, if the course is priced at $300... You'll make $150 on each student enrolling.

If you genuinely love the course and think your friends or family will get benefit from this... Get this course in their hands ASAP.

If you refer 7 paying customers... That's $1,000 ;).
""")

# Slider
st.markdown('# Referral Calculator')
num_referrals = st.slider("", 0, 100, 7)

# Constants
COMMISSION_RATE = 50  # 50% commission rate
COURSE_PRICE = 300  # Course price in dollars

# Earnings Calculation
earnings = calculate_earnings(num_referrals, COMMISSION_RATE, COURSE_PRICE)
st.markdown(f"# Make ${earnings}")
st.markdown(f"### ...on referring {num_referrals} students ❤️")

# Form for user details
with st.form(key='signup_form'):
  name = st.text_input("Name:")
  phone = st.text_input("Phone:")
  email = st.text_input("Email:")
  submit_button = st.form_submit_button(
      label='Yes, I Want to Join this Referral Program!')

# On form submission
if submit_button:
  st.write(
      "You're locked in. Someone from Clever Programmer will text you or email you shortly. Keep an eye on your inbox 💪"
  )
  notify_signup_via_text(name, email, phone)
