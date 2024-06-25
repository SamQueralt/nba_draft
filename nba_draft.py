# streamlit run nba_draft.py

import streamlit as st
import pandas as pd

stats = pd.read_pickle('stats.pkl')
sam = pd.read_pickle('sam.pkl')
# adam = pd.read_pickle('')

sam = pd.merge(sam, stats, on='Name')

## sort by rating
sam = sam.sort_values(by = 'Rating', ascending=False).reset_index()

st.set_page_config(
     page_title='NBA Draft 2024',
     page_icon = "🏀",
     layout="wide",
)

st.title("NBA Draft Scouting 2024")

col1, col2 = st.columns(2)

with col1:
    st.header("Sam")
    for index, row in sam.iterrows():
        # Name	Rating	Team	Ht	Wt	Age	Pos	Pts	Reb	Ast	FG%	3P%	FT%	FTR	Ceiling	Floor	Description
        rank = index + 1
        name = row['Name']
        rating = row['Rating']
        team = row['Team']
        ht = row['Ht']
        wt = row['Wt']
        age = row['Age']
        pos = row['Pos']
        pts = row['Pts']
        reb = row['Reb']
        ast = row['Ast']
        fg = row['FG%']
        p3 = row['3P%']
        ft = row['FT%']
        ftr = row['FTR']
        ceil = row['Ceiling']
        floor = row['Floor']
        desc = row['Description']

        st.subheader(f"{rank} - {name}, {team}")
        
        col11, col12, col13 = st.columns([2,1,1])

        with col11:
            st.code(f"{pos} - {ht}, {wt} lbs\n{ceil} ceiling\n{floor} floor")

        with col12:
            st.code(f"{pts} PPG\n{ast} APG\n{reb} RPG")

        with col13:
            st.code(f"{fg} FG%\n{p3} 3P%\n{ft} FT%")


        st.caption(desc)
        
with col2:
    st.header("Adam")
    for index, row in sam.iterrows():
        # Name	Rating	Team	Ht	Wt	Age	Pos	Pts	Reb	Ast	FG%	3P%	FT%	FTR	Ceiling	Floor	Description
        rank = index + 1
        name = row['Name']
        rating = row['Rating']
        team = row['Team']
        ht = row['Ht']
        wt = row['Wt']
        age = row['Age']
        pos = row['Pos']
        pts = row['Pts']
        reb = row['Reb']
        ast = row['Ast']
        fg = row['FG%']
        p3 = row['3P%']
        ft = row['FT%']
        ftr = row['FTR']
        ceil = row['Ceiling']
        floor = row['Floor']
        desc = row['Description']

        st.subheader(f"{rank} - {name}, {team}")
        
        col21, col22, col23 = st.columns([2,1,1])

        with col21:
            st.code(f"{pos} - {ht}, {wt} lbs\n{ceil} ceiling\n{floor} floor")

        with col22:
            st.code(f"{pts} PPG\n{ast} APG\n{reb} RPG")

        with col23:
            st.code(f"{fg} FG%\n{p3} 3P%\n{ft} FT%")


        st.caption(desc)
        
        
        
