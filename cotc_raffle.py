"""Code to randomly generate a winner for the CotC raffle"""
import streamlit as st
import numpy as np
import random


st.title("Raffle Drawer")

# Initial list of entries
if "tickets" not in st.session_state:
    st.session_state.tickets = {
                # "Marcus": 1,
                # "James": 1,
                # "Louis": 1,
                # "Richard": 1,
                # "Callum": 1,
                # "Roger": 1,
                # "Curtis": 1,
                # "Nick": 1,
                # "George": 1,
                # "Hugo": 1,
                # "Harry": 1,
                # "Carl": 1,
                # "Michael": 1
            }

# Add/edit entry
st.subheader("Add or edit entry")
name = st.text_input("Name")
tickets = st.number_input("Tickets", min_value=1, step=1)

if st.button("Add/update"):
    st.session_state.tickets[name] = tickets

# Remove entry
st.subheader("Remove entry")
remove_name = st.selectbox(
                "Select name",
                list(st.session_state.tickets.keys())
                )

if st.button("Remove"):
    del st.session_state.tickets[remove_name]

# Display entries
st.subheader("List of participants:")
for name, count in st.session_state.tickets.items():
    st.write(f"{name} has {count} tickets")


# Draw winner
st.subheader("Draw winner")
if st.button("Draw"):
    # Calculate the odds of each participant winning
    odds = st.session_state.tickets.values()
    # Select winner
    names = list(st.session_state.tickets.keys())
    winner = random.choices(names, 
                            weights=odds, 
                            k=1)[0]
    st.success(f"And the winner is... {winner}!")
