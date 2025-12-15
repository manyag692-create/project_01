import streamlit as st
import random

# Initialize session state variables
if "human_score" not in st.session_state:
    st.session_state.human_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🎮 Rock Paper Scissors Game")
st.write("First to 5 points wins!")

# Display current scores
st.markdown(f"**Your Score:** {st.session_state.human_score} | **Computer Score:** {st.session_state.comp_score}")

# Game buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Rock"):
        user_choice = 1
        comp_choice = random.randint(1,3)
elif_choice = None
with col2:
    if st.button("📄 Paper"):
        user_choice = 2
        comp_choice = random.randint(1,3)
with col3:
    if st.button("✂️ Scissors"):
        user_choice = 3
        comp_choice = random.randint(1,3)

# Game logic
if "user_choice" in locals():
    if (user_choice == 1 and comp_choice == 3) or \
       (user_choice == 2 and comp_choice == 1) or \
       (user_choice == 3 and comp_choice == 2):
        st.session_state.human_score += 1
        st.success("✅ You won this round!")
    elif user_choice == comp_choice:
        st.info("🤝 It's a draw!")
    else:
        st.session_state.comp_score += 1
        st.error("❌ Computer wins this round!")

    # Check for game over
    if st.session_state.human_score == 5:
        st.balloons()
        st.success("🎉 You won the game!")
        st.session_state.game_over = True
    elif st.session_state.comp_score == 5:
        st.error("💻 Computer wins the game!")
        st.session_state.game_over = True

# Reset button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.human_score = 0
        st.session_state.comp_score = 0
        st.session_state.game_over = False