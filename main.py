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

# Home Page
if st.session_state.page == "Home":
    st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://github.com/Roshan11032005/QUBIT/blob/main/WhatsApp%20Image%202024-11-07%20at%207.12.18%20PM-removebg-preview.jpg?raw=true" alt="Logo" style="width:100px;">
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    "<h1 style='text-align: center; font-size: 50px; color: #4A90E2;'>Welcome to Qubit 2024!</h1>",
    unsafe_allow_html=True
)


    
    
    
   
    # Fest Title
   
    # Tagline and Fest Intro
    st.markdown("""
    <div style='text-align: center; font-size: 24px; margin-top: -20px;'>
        <em>The Ultimate Tech Fest at Mahatma Gandhi Institute of Technology</em>
    </div>
    """, unsafe_allow_html=True)
    
    # Main Content
    st.write("""
    **Qubit 2024** is back, and it's bigger and better! Join us for a thrilling two-day event packed with exciting competitions, cutting-edge workshops, and unforgettable experiences where technology, creativity, and passion collide.
    """)

    # Why Attend Section with Key Highlights
    st.markdown("<h2 style='color: #FF6347;'>Why Attend Qubit 2024?</h2>", unsafe_allow_html=True)
    st.write("""
    - **Inspiration from Industry Leaders**: Gain insights from expert speakers and learn about the latest in technology.
    - **Unleash Your Potential**: Showcase your skills in competitions designed to challenge and inspire.
    - **Collaborate and Connect**: Build your network with tech enthusiasts, industry professionals, and peers.
    - **Exciting Prizes and Recognition**: Compete for amazing prizes and take home the glory!
    - **Fun and Festivity**: Enjoy entertainment, games, and a chance to make lasting memories.
    """)

    # Registration and Event List Buttons
 
    # Teaser Image or Background (optional, replace with a suitable image link if available)
    #Centrailzed Event LIst
    st.markdown(
    '''
    <div style="display: flex; justify-content: center; margin-top: 10px;">
        <a href="?page=event_list" style="text-decoration: none;">
            <button style="width:100%; max-width: 150px; padding:10px; background-color:transparent; color:#FF6347; font-size:16px; border:2px solid #FF6347; border-radius:5px; cursor:pointer;">
                View Event List
            </button>
        </a>
    </div>
    ''',
    unsafe_allow_html=True
    )
    if st.query_params.get("page") == "event_list":
        st.session_state.page = "Event List"
        st.rerun()


    # Footer
    st.write("---")
    st.markdown("<div style='text-align: center; font-size: 16px; color: grey;'>Organized by the Students of MGIT...</div>", unsafe_allow_html=True)
         
# Event List Page
#Changed The event list button to be more centred
if st.session_state.page == "Event List":
    st.title("🎉 List of Events 🎉")
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.query_params.page="home"
        st.rerun()
    # Displaying each event button in a fixed-size layout
    col1, col2 = st.columns(2)  # Two-column layout for a cleaner look

    with col1:
        if st.button("Bug Hunt and Reverse Coding", key="Laser Escape", help="View details for Laser Escape", 
                     use_container_width=True):
            st.session_state.selected_event = "Bug Hunt and Reverse Coding"
            st.session_state.page = "Bug Hunt and Reverse Coding"
            st.rerun()

        if st.button("Smash Karts", key="Bug Hunt", help="View details for Smash Karts", 
                     use_container_width=True):
            st.session_state.selected_event = "Bug Hunt and Reverse Coding"
            st.session_state.page = "Smash Karts"
            st.rerun()
       
        if st.button("Website Development Contest", key="Website Development", help="View details for Website Development Contest", 
                     use_container_width=True):
            st.session_state.selected_event = "Website Development Contest"
            st.session_state.page = "Website Development Contest"
            st.rerun()
        
        #Pushed this UP
        if st.button("Logic Link", key="Logic Link", help="View details for Meme Making Contest", 
                     use_container_width=True):
            st.session_state.selected_event = "Meme Making Contest"
            st.session_state.page = "Logic Link"
            st.rerun()

        if st.button("IdeaOrbit", key="IdeaOrbit", help="View details for IdeaOrbit", use_container_width=True):
            st.session_state.selected_event = "IdeaOrbit"
            st.session_state.page = "ideaOrbit"
            st.rerun()
        
        
        if st.button("IPL Auction", key="IPL Auction", help="View details for IPL Auction", use_container_width=True):
            st.session_state.selected_event = "IPL Auction"
            st.session_state.page = "IPL Auction"
            st.rerun()

        #Pushed this up too
        if st.button("Minute to Win It", key="Minute to Win It", help="View details for Minute to Win It", 
                     use_container_width=True):
            st.session_state.selected_event = "Minute to Win It"
            st.session_state.page = "Minute to Win It"
            st.rerun()    
    
        if st.button("Meme Making Contest", key="Meme Making Contest", help="View details for Meme Making Contest", 
                     use_container_width=True):
            st.session_state.selected_event = "Meme Making Contest"
            st.session_state.page = "Meme Making Contest"
            st.rerun()

        

    with col2:
        if st.button("Snake and Ladders", key="Snake and Ladders", help="View details for Meme Making Contest", 
                     use_container_width=True):
            st.session_state.selected_event = "Meme Making Contest"
            st.session_state.page = "Snake and Ladders"
            st.rerun()
        
        if st.button("Dum Charades", key="Dum Charades", help="View details for Dum Charades", 
                     use_container_width=True):
            st.session_state.selected_event = "Bug Hunt and Reverse Coding"
            st.session_state.page = "Dum Charades"
            st.rerun()

        

        if st.button("Treasure Hunt", key="Treasure Hunt", help="View details for Treasure Hunt", use_container_width=True):
            st.session_state.selected_event = "Treasure Hunt"
            st.session_state.page = "Treasure Hunt"
            st.rerun()

        if st.button("Aptitude Trivia", key="Aptitude Trivia", help="View details for Aptitude Trivia", 
                     use_container_width=True):
            st.session_state.selected_event = "Aptitude Trivia"
            st.session_state.page = "Aptitude Trivia"
            st.rerun()

        if st.button("AI Art Gallery", key="AI Art Gallery", help="View details for AI Art Gallery", 
                     use_container_width=True):
            st.session_state.selected_event = "AI Art Gallery"
            st.session_state.page = "AI Art Gallery"
            st.rerun()

        if st.button("Squid Game", key="Squid Game", help="View details for Squid Game", use_container_width=True):
            st.session_state.selected_event = "Squid Game"
            st.session_state.page = "Squid Game"
            st.rerun()

        if st.button("Anybody Can Draw", key="Anybody Can Draw", help="View details for Anybody Can Draw", 
                     use_container_width=True):
            st.session_state.selected_event = "Anybody Can Draw"
            st.session_state.page = "Anybody Can Draw"
            st.rerun()

if st.session_state.page == "Bug Hunt and Reverse Coding":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🕵️‍♂️ Bug Hunt and Reverse Coding")
    st.subheader("Put Your Debugging and Coding Skills to the Test!")

    # Event Overview
    st.markdown("""
    Welcome to the **Bug Hunt and Reverse Coding** event! This is the perfect opportunity for all coding enthusiasts to showcase their debugging skills, engage in exciting reverse coding tasks, and tackle challenges head-on.
    Get ready for three thrilling levels of coding puzzles, from basics to advanced!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Debugging Basics
    - **Objective**: Identify and fix bugs in simple programs.
    - **Difficulty**: Beginner

    ### Level 2: Intermediate Debugging and Reverse Coding
    - **Objective**: Solve complex coding problems and start reverse coding.
    - **Difficulty**: Intermediate

    ### Level 3: Advanced Challenges
    - **Objective**: Face time-bound debugging of complex code and solve advanced reverse coding puzzles.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹50 for 1 person
      - ₹70 for 2 persons
    - **How to Register**: Sign up as a solo participant or team up with a friend to unlock more savings!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate coding challenge!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1gLFJY6IPkMOPa3ODGJbOZw20X7AniR8JCVR75bycOs8/edit"
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Treasure Hunt":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🗺️ Treasure Hunt")
    st.subheader("Join the Adventure and Unlock the Hidden Treasures!")

    # Event Overview
    st.markdown("""
    Welcome to the **Treasure Hunt**! Embark on an exciting journey filled with clues, puzzles, and challenges that will test your wit, teamwork, and problem-solving skills.
    Prepare for three thrilling levels as you navigate your way to the final treasure!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Clue Discovery
    - **Objective**: Solve basic riddles to unlock the next clue.
    - **Difficulty**: Beginner

    ### Level 2: Puzzle Challenges
    - **Objective**: Complete intermediate puzzles and tasks to reveal the next location.
    - **Difficulty**: Intermediate

    ### Level 3: Final Treasure Chase
    - **Objective**: The final clue leads to the treasure, testing teamwork and strategy to the fullest.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹120 for 3 persons
      - ₹150 for 4 persons
      - ₹180 for 5 persons
    - **How to Register**: Gather your team and register together to unlock your spot in the hunt!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate Treasure Hunt adventure!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1nnfYE2BVTJhSoLTE7ceT7DjzePJxB5D_9Hd0yRSYjdw/edit" # Replace with your link
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Website Development Contest":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🌐 Website Development Contest")
    st.subheader("Showcase Your Creativity and Technical Skills!")

    # Event Overview
    st.markdown("""
    Welcome to the **Website Development Contest**! This event is a fantastic opportunity for aspiring web developers to showcase their creativity, technical skills, and design prowess.
    Compete through three exciting levels, from concept to final presentation, and impress the judges with your website!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Concept Submission
    - **Objective**: Present your website idea along with rough designs and wireframes.
    - **Difficulty**: Beginner

    ### Level 2: Development Phase
    - **Objective**: Create a functional prototype based on your submitted concept.
    - **Difficulty**: Intermediate

    ### Level 3: Final Presentation
    - **Objective**: Demonstrate and defend your website before a panel of judges, highlighting its features and design.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹50 for 1 person
      - ₹70 for 2 persons
    - **How to Register**: Sign up solo or partner up to take on this development challenge!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate Website Development Contest!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1d1p1ZvkwD1ZxGl1N_qqWcgGQyvIfWb_pvkJVim1dcuQ/edit" # Replace with your link
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Aptitude Trivia":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🧠 Aptitude Trivia")
    st.subheader("Put Your Mental Agility to the Ultimate Test!")

    # Event Overview
    st.markdown("""
    Welcome to the **Aptitude Trivia**! This event is perfect for those who love challenging their minds with logical reasoning, speed, and quick thinking.
    Compete through three intense levels, from a preliminary quiz to a thrilling final face-off!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Preliminary Quiz
    - **Objective**: A written test covering general aptitude and logical reasoning.
    - **Difficulty**: Beginner

    ### Level 2: Speed Round
    - **Objective**: Timed quiz with quick-response questions to test mental agility.
    - **Difficulty**: Intermediate

    ### Level 3: Final Face-Off
    - **Objective**: Top contenders face off in a buzzer round to crown the champion.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
      - ₹65 for 2 persons
    - **How to Register**: Sign up individually or bring a friend to take on the challenge together!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate Aptitude Trivia challenge!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1-7Rr1xyT0S7cA1lImcpFS8aFHYdkbIgSnIZKi6vLQ98/edit"  # Replace with your link
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "ideaOrbit":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🌟 ideaOrbit")
    st.subheader("Pitch Your Ideas and Bring Them to Life!")

    # Event Overview
    st.markdown("""
    Welcome to **ideaOrbit**! This is the ultimate platform for innovators and visionaries to present their groundbreaking ideas. Compete through three levels, refining your concept and presentation, and pitch live to a panel of judges and an audience!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Idea Submission
    - **Objective**: Submit a brief description of your innovative concept.
    - **Difficulty**: Beginner

    ### Level 2: Semi-Final Pitch
    - **Objective**: Present a detailed proposal with visuals or prototypes to showcase your idea.
    - **Difficulty**: Intermediate

    ### Level 3: Grand Finale
    - **Objective**: Deliver a live pitch in front of judges and an audience, followed by a Q&A session to defend your idea.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹50 for 1 person
      - ₹70 for 2 persons
      - ₹100 for 4 persons
    - **How to Register**: Register solo, with a partner, or as a team to bring your ideas to the stage!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate ideaOrbit competition!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1T8vhcyIsO7alrs8hRLwm-YdjUTLTMUowUsoy2CUsyeg/edit"  # Replace with your link
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()



if st.session_state.page == "AI Art Gallery":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🎨 AI Art Gallery")
    st.subheader("Create, Exhibit, and Compete with AI-Generated Art!")

    # Event Overview
    st.markdown("""
    Welcome to the **AI Art Gallery**! This unique event invites participants to generate artwork using AI based on a given theme. Join us in celebrating creativity through technology, with your artwork showcased and judged in an exhibition.
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Artwork Creation
    - **Objective**: Submit an AI-generated artwork based on the event's theme.
    - **Difficulty**: Beginner

    ### Level 2: Exhibition
    - **Objective**: Selected works will be displayed in an exhibition for public viewing and appreciation.
    - **Difficulty**: Intermediate

    ### Level 3: Judging Panel
    - **Objective**: Final assessment by a panel of art and AI experts, with additional audience votes to select the winning pieces.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**: ₹40 for 1 person
    - **How to Register**: Sign up as a solo participant to showcase your AI-generated creativity!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate AI Art Gallery showcase!** 🏆")
    registration_link ="https://docs.google.com/forms/d/1bniWIn98KjqeBVtGBem44Td2TPEWccDUyR5yWYUsQSE/edit" # Replace with your link
    st.markdown(f'<a href="{registration_link}" target="_blank"><button style="width:100%; padding:10px; background-color:#4CAF50; color:white; font-size:16px;">Register Now!</button></a>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            .css-145kmo2 { 
                color: #3A3A3A;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "IPL Auction":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🏏 IPL Auction")
    st.subheader("Strategize, Bid, and Build Your Ultimate Team!")

    # Event Overview
    st.markdown("""
    Welcome to the **IPL Auction**! This thrilling event allows participants to engage in a simulated auction experience, where you can form your dream cricket team through strategic bidding. Compete through three exciting levels, from team formation to the final auction, and showcase your management skills!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Team Formation
    - **Objective**: Register your team and receive a briefing on the auction rules and guidelines.
    - **Difficulty**: Beginner

    ### Level 2: Mock Auction
    - **Objective**: Participate in a practice auction to familiarize yourself with bidding strategies and team building.
    - **Difficulty**: Intermediate

    ### Level 3: Final Auction
    - **Objective**: Engage in the live auction, bid for players, and strategize to build the strongest virtual team for the tournament.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
      - ₹70 for 2 persons
      - ₹110 for 3 persons
      - ₹140 for 4 persons
      - ₹180 for 5 persons
      - ₹210 for 6 persons
    - **How to Register**: Sign up individually or form a team of up to six members to participate in the auction together!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and secure your spot in the ultimate IPL Auction challenge!** 🏆")
    registration_link ="https://docs.google.com/forms/d/1C7zZu70KSraW9thvK-fWTn5Dc0TkfjJHtV8XeZjacmQ/edit"  # Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#4CAF50; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #4CAF50;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()

if st.session_state.page == "Squid Game":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🦑 Squid Game")
    st.subheader("Compete in Thrilling Challenges Inspired by the Series!")

    # Event Overview
    st.markdown("""
    Welcome to the **Squid Game** event! Inspired by the popular series, this competition will challenge your skills, strategy, and endurance through three intense levels. Only the strongest and most strategic participants will make it to the final round!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Initial Game
    - **Objective**: Participate in basic challenges inspired by the series, such as **Red Light, Green Light**.
    - **Difficulty**: Beginner

    ### Level 2: Intermediate Challenge
    - **Objective**: Tackle more complex games, which may include puzzles or team-based tasks to test your collaboration and problem-solving skills.
    - **Difficulty**: Intermediate

    ### Level 3: Final Round
    - **Objective**: Compete in the ultimate game that decides the last survivor. Only the strongest will prevail!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹50 for 1 person
      - ₹70 for 2 persons
      - ₹110 for 3 persons
    - **How to Register**: Register solo or team up with friends to test your skills and see who will emerge as the ultimate survivor!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and take your chance in the ultimate Squid Game challenge!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1eARoKHEiXULbwS1_6R8n-UU9LHonbrfhlvz6MXOCaNk/edit"  # Replace with the actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FF6347; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FF6347;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FF4500;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()

if st.session_state.page == "Laser Escape":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🔦 Laser Escape")
    st.subheader("Dodge, Duck, and Outsmart the Laser Maze!")

    # Event Overview
    st.markdown("""
    Welcome to **Laser Escape**! Get ready to navigate through increasingly challenging laser mazes, testing your agility, critical thinking, and timing. Will you make it through to the final escape?
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Basic Maze
    - **Objective**: Navigate through an entry-level laser maze with minimal obstacles.
    - **Difficulty**: Beginner

    ### Level 2: Intermediate Maze
    - **Objective**: Face a denser laser field and trickier paths, demanding more agility and focus.
    - **Difficulty**: Intermediate

    ### Level 3: Advanced Escape
    - **Objective**: Conquer a time-constrained, high-density laser maze, where critical thinking and fast reflexes are key to survival.
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**: ₹40 for 1 person
    - **How to Register**: Sign up solo to see if you have what it takes to make it through the ultimate laser escape!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and prepare for the ultimate Laser Escape challenge!** 🏆")
    registration_link ="https://docs.google.com/forms/d/156su1O5h5RoQfNN1_Apsagp10a_QL5D7hEd2Gql807M/edit"  # Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FF4500; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FF4500;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FF6347;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Meme Making Contest":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("😂 Meme Making Contest")
    st.subheader("Unleash Your Creativity and Humor in the Ultimate Meme Battle!")

    # Event Overview
    st.markdown("""
    Welcome to the **Meme Making Contest**! If you’ve got a knack for humor and a love for memes, this event is your chance to shine. Compete through three rounds, from submission to audience voting, and finally, a judge’s selection for the most creative and hilarious memes!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Submission Round
    - **Objective**: Create and submit original memes based on given themes. Show us your best work!
    - **Difficulty**: Beginner

    ### Level 2: Community Voting
    - **Objective**: Your memes will be displayed for public voting. Gain support from the crowd and rise to the top!
    - **Difficulty**: Intermediate

    ### Level 3: Judge's Choice
    - **Objective**: The top memes are evaluated by a panel of judges based on creativity, humor, and originality. May the best meme win!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
      - ₹60 for 2 persons
    - **How to Register**: Register solo or as a duo and showcase your meme-making skills to the world!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now to join the Meme Making Contest and let the laughs begin!** 🏆")
    registration_link ="https://docs.google.com/forms/d/1SUFg7Vu2FAm9gjTBkoaHhzaMwrrFGhnFH4WpeH_8ZKs/edit"# Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FFD700; 
                color:black; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FFD700;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FFC107;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()

if st.session_state.page == "Anybody Can Draw":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🎨 Anybody Can Draw")
    st.subheader("Unleash Your Inner Artist and Showcase Your Talent!")

    # Event Overview
    st.markdown("""
    Welcome to **Anybody Can Draw**! This event invites participants of all skill levels to express their creativity through drawing. Whether you're a seasoned artist or just starting out, come and join us in a fun and supportive environment!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Basic Sketching
    - **Objective**: Create drawings based on simple themes. Perfect for beginners to get started!
    - **Difficulty**: Beginner

    ### Level 2: Thematic Drawing
    - **Objective**: Participants create art based on a more complex theme, allowing for greater creativity and expression.
    - **Difficulty**: Intermediate

    ### Level 3: Final Display
    - **Objective**: The top drawings are showcased and judged for creativity and technique. Shine in front of our panel of judges!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹30 for 1 person
      - ₹50 for 2 persons
    - **How to Register**: Sign up solo or as a duo and let your creativity flow!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and embrace your artistic journey!** 🏆")
    registration_link = "https://docs.google.com/forms/d/16SRyDfV3asjdKXnIXORt9BBK7EpcXF9p2Z0DMAL4YFU/edit"  # Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FF69B4; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FF69B4;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FF1493;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Snake and Ladders":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🎲 Snake and Ladders")
    st.subheader("Climb the Ladders and Avoid the Snakes to Win!")

    # Event Overview
    st.markdown("""
    Welcome to **Snake and Ladders**! A classic game with a twist, this event invites participants to navigate through fun and challenging matches. Test your luck and strategy as you climb the ladders and dodge the snakes to claim victory!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Initial Matches
    - **Objective**: Participate in basic games to qualify for the next rounds. It’s all about getting started!
    - **Difficulty**: Beginner

    ### Level 2: Intermediate Rounds
    - **Objective**: Experience increased board complexity and additional challenges that will keep you on your toes!
    - **Difficulty**: Intermediate

    ### Level 3: Finals
    - **Objective**: The final board decides the ultimate winner. Only the best will claim the title!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
    - **How to Register**: Join us for an exciting experience and see if you have what it takes to win!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and roll the dice for your chance to win!** 🏆")
    registration_link ="https://docs.google.com/forms/d/1hGoTWiB3kvcZKZvNoQym1hcPLR7ZHPd5p_2AjwFF-Z0/edit" # Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FFD700; 
                color:black; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FFD700;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FFC107;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
if st.session_state.page == "Dum Charades":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🎭 Dum Charades")
    st.subheader("Act It Out and Guess to Win!")

    # Event Overview
    st.markdown("""
    Welcome to **Dum Charades**! Gather your friends and join this fun-filled event where teams act out phrases without speaking. It's all about creativity, teamwork, and having a great time!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Qualifying Round
    - **Objective**: Teams act out simple phrases to qualify for the next round. Get ready for some fun!
    - **Difficulty**: Beginner

    ### Level 2: Intermediate Level
    - **Objective**: Teams face more complex and tricky phrases that will challenge their acting skills.
    - **Difficulty**: Intermediate

    ### Level 3: Grand Finals
    - **Objective**: The top teams face off in challenging and time-bound acting rounds. Only the best will emerge victorious!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
      - ₹60 for 2 persons
    - **How to Register**: Join with a friend or solo and show off your acting skills!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and bring your best acting game!** 🏆")
    registration_link = "https://docs.google.com/forms/d/1j-foDGW4X19wJgFqRRDGeQo2JGEXnMmpxc6BovncrFc/edit"  # Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#FF4500; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #FF4500;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #FF6347;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()


# Page Navigation
if st.session_state.page == "Logic Link":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()
    
    # Event Header
    st.title("💻 Logic Link")
    st.subheader("Test Your Coding Skills and Break the Bugs!")

    # Event Overview
    st.markdown("""
    Welcome to the **Logic Link**! Prepare yourself for 20 quick-fire coding puzzles in C, Python, or Java. It's a test of debugging skills, logical thinking, and speed. Can you solve the most challenges within the time limit and become the ultimate code-breaker? Let's get coding!
    """)

    # How to Play
    st.header("How to Play")
    st.markdown("""
    - Participants will receive code challenges with snippets that may contain errors or require rearrangement.
    - Players have to identify and fix as many issues as possible within the allotted time.
    """)

    # Categories
    st.header("Categories")
    st.markdown("""
    - **Category 1**: **C Language** (3 minutes) - Exclusive to 1st-year students.
    - **Category 2**: **Python or Java** (5 minutes) - Choose only one of these languages. Choose wisely!
    """)

    # Pricing
    st.header("Pricing")
    st.markdown("""
    - **Solo**: ₹40 per person
    - **Duo**: ₹60 for two people
    """)

    # Call to Action
    st.markdown("#### 🎉 **Register now and put your coding skills to the test!** 🎉")
    registration_link = "https://docs.google.com/forms/d/1O4eoU4d7QrXljObGBykNNFdfRRFGZ9BesLj5sU291Lo/edit" # Replace with actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#007BFF; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #007BFF;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
    

# Page Navigation

if st.session_state.page == "Minute to Win It" :
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()
    
    # Event Header
    st.title("🎉 Minute to Win It - Non-technical Event 🎉")
    st.subheader("Are you ready for the ultimate 60-second challenge?")

    # Event Overview
    st.markdown("""
    Welcome to the ultimate **“Minute to Win It”** face-off! Get ready for a high-energy battle where teams tackle hilarious, fast-paced challenges designed to test your balance, aim, and speed. 
    From balancing cups and stacking dice to bouncing ping-pong balls with precision, you'll have just **60 seconds** to complete each task.
    It's fun, frantic, and all about teamwork and quick reflexes. Are you up for the challenge?
    """)

    # Game Descriptions
    st.header("Games")
    
    # Game 1: Stacking Cups
    st.subheader("Game 1: Stacking Cups")
    st.markdown("""
    It’s a game of stacking cups where each of the two individual players uses one of their hands and stacks the cups!
    """)

    # Game 2: Throw-A-Ball
    st.subheader("Game 2: Throw-A-Ball")
    st.markdown("""
    In this game, players take turns tossing a ping pong ball into the cups arranged on a table. Scores are assigned based on the distance of the player from the cup. 
    The longer the distance, the higher the score! After a minute, the team with the highest score wins.
    """)

    # Game 3: Tilt-A-Cup
    st.subheader("Game 3: Tilt-A-Cup")
    st.markdown("""
    The ping pong ball bounced by one player should be caught with a cup by the other player and, once caught, a cup should be stacked with another cup and the game continues.
    The team with the highest number of cups after a minute shall win.
    """)

    # Game 4: Surprise Challenge
    st.subheader("Game 4: Surprise Challenge")
    st.markdown("""
    **Expect the unexpected!** Game 4 is a mystery round—you’ll have to show up and be ready for anything! No hints, no sneak peeks—just pure excitement and a twist you won’t see coming.
    Get ready to think on your feet and tackle a challenge that’s full of surprises!
    """)

    # Pricing
    st.header("Pricing")
    st.markdown("""
    - **Solo**: ₹50 per person
    - **Duo**: ₹70 for two people
    """)

    # Call to Action
    st.markdown("#### 🎉 **Register now and join the fun!** 🎉")
    registration_link = "https://docs.google.com/forms/d/1SPRrMWWInoi_1E52U7rj2DcagUkKRddEZKXXixQlJkE/edit"  # Replace with actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#007BFF; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #007BFF;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()


if st.session_state.page == "Smash Karts":
    if st.button("Return to Home"):
        st.session_state.page = "Home"
        st.rerun()

    # Event Header
    st.title("🏎️ Smash Karts")
    st.subheader("Rev Up Your Engines and Race to Victory!")

    # Event Overview
    st.markdown("""
    Welcome to **Smash Karts**! Get ready to race against the clock and your competitors in a thrilling karting event. From qualification heats to the grand finale, only the fastest and most skilled racers will prevail!
    """)

    # Event Details
    st.header("Event Levels")
    st.markdown("""
    ### Level 1: Qualification Heats
    - **Objective**: Participants compete in initial kart races to secure their spot in the semi-finals.
    - **Difficulty**: Beginner

    ### Level 2: Semi-Finals
    - **Objective**: The top racers from the heats face off with added challenges and obstacles.
    - **Difficulty**: Intermediate

    ### Level 3: Grand Finale
    - **Objective**: The final race determines the champion. Only the best will cross the finish line first!
    - **Difficulty**: Advanced
    """)

    # Registration Information
    st.header("Registration Details")
    st.markdown("""
    - **Fee**:
      - ₹40 for 1 person
    - **How to Register**: Race solo or team up with a friend and put your driving skills to the test!
    """)

    # Call to Action
    st.markdown("#### 🏆 **Register now and get ready to smash your way to victory!** 🏆")
    registration_link ="https://docs.google.com/forms/d/156su1O5h5RoQfNN1_Apsagp10a_QL5D7hEd2Gql807M/edit"# Replace with your actual registration link
    st.markdown(f'''
        <a href="{registration_link}" target="_blank">
            <button style="
                width:100%; 
                padding:10px; 
                background-color:#1E90FF; 
                color:white; 
                font-size:16px; 
                border:none; 
                border-radius:5px;
                cursor:pointer;">
                Register Now!
            </button>
        </a>
    ''', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("For more information or queries, please contact [Event Organizer](mailto:event.organizer@example.com).")

    # Customize layout and style
    st.markdown("""
        <style>
            /* Center the text and apply primary color */
            .css-1d391kg { 
                text-align: center; 
                color: #1E90FF;
            }
            /* Adjust the color for secondary text */
            .css-145kmo2 { 
                color: #3A3A3A;
            }
            /* Enhance button hover effect */
            a > button:hover {
                background-color: #00BFFF;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("View Event List"):
        st.session_state.page = "Event List"
        st.rerun()
