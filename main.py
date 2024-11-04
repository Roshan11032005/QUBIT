import streamlit as st

# Set up the page title, layout, and theme
st.set_page_config(page_title="Qubit - MGIT Technical Fest", layout="centered")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# CSS for custom styles
st.markdown("""
<style>
    /* Background and title color */
    .css-18e3th9 h1 { color: #FF4500; }
    .css-18e3th9, .css-1d391kg, .css-1j49p6r { background-color: #111; color: #fff; }
    
    /* Button styling */
    .css-18e3th9 button {
        background-color: #FF4500;
        color: #fff;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Show balloons when the page loads
st.balloons()

# Navigation logic
if st.session_state.page == "Home":
    # Home Page
    st.title("Qubit - MGIT Technical Fest")
    st.write("""
    Welcome to **Qubit 2023**, the annual technical fest organized by **Mahatma Gandhi Institute of Technology**!
    Join us to experience a wide array of events, competitions, and workshops where technology and innovation come together.
    """)

    # Why Attend Section
    st.header("Why Attend Qubit 2023?")
    st.write("""
    - **Learn from Experts**: Attend workshops and talks by industry leaders.
    - **Network with Peers**: Connect with like-minded individuals and build your professional network.
    - **Showcase Your Skills**: Participate in exciting competitions and hackathons.
    - **Have Fun**: Enjoy a variety of entertainment events and activities.
    """)

    # Buttons for registration and event list
    registration_link = "https://docs.google.com/forms/d/e/1FAIpQLSeeRZlHuPQ0E3Y2eyb3TYgjk6Kig3ct-i2xZlht8Drh5zqw7Q/viewform"
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Button to go to Event List page
    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.experimental_rerun()

elif st.session_state.page == "Event List":
    # Event List Page
    st.title("List of Events and Registration Fees")

    events = {
        "1. Bug Hunt and Reverse Coding": "1 person - ₹50, 2 persons - ₹70",
        "2. Treasure Hunt": "3 persons - ₹120, 4 persons - ₹150, 5 persons - ₹180",
        "3. Website Development Contest": "1 person - ₹50, 2 persons - ₹70",
        "4. Aptitude Trivia": "1 person - ₹40, 2 persons - ₹65",
        "5. IdeaOrbit": "1 person - ₹50, 2 persons - ₹70, 4 persons - ₹100",
        "6. AI Art Gallery": "1 person - ₹40",
        "7. IPL Auction": "1 person - ₹40, 2 persons - ₹70, 3 persons - ₹110, 4 persons - ₹140, 5 persons - ₹180, 6 persons - ₹210",
        "8. Squid Game": "1 person - ₹50, 2 persons - ₹70, 3 persons - ₹110",
        "9. Laser Escape": "1 person - ₹40",
        "10. Meme Making Contest": "1 person - ₹40, 2 persons - ₹60",
        "11. Smash Karts": "1 person - ₹30, 2 persons - ₹50",
        "12. Anybody Can Draw": "1 person - ₹30, 2 persons - ₹50",
        "13. Snake and Ladders": "1 person - ₹40",
        "14. Dum Charades": "1 person - ₹40, 2 persons - ₹60",
    }

    for event, fee in events.items():
        st.write(f"**{event}** - {fee}")

    # Button to go back to Home page
    if st.button("Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
