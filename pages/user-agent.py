import requests
import streamlit as st
from streamlit.components.v1 import html
from layout_template import sidebar_template

PAGE = "🕵️ User Agent"
PROMPT = ''

answer, docs = '', []
# -------------------- Sidebar Layout --------------------
sidebar_template()

# -------------------- Page Header --------------------
st.header(PAGE, divider=True)

# JavaScript to get the user agent
user_agent_js = """
<script>
    const userAgent = window.navigator.userAgent;
    document.write(userAgent);
</script>
"""

# Display the user agent in the Streamlit app
st.write("User Agent:")
html(user_agent_js)
#html(user_agent_js)

# Get user IP from external service
ip_request = requests.get('https://api.ipify.org?format=json')
user_ip = ip_request.json()['ip']

st.write("IP Address:")
st.write(user_ip)
