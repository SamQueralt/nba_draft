# streamlit run nba_draft.py

import streamlit as st
import pandas as pd

def interpolate_color(rating, start_color, end_color):
    if rating < 50:
        return start_color
    
    start_color = start_color.lstrip('#')
    end_color = end_color.lstrip('#')
    start_r = int(start_color[0:2], 16)
    start_g = int(start_color[2:4], 16)
    start_b = int(start_color[4:6], 16)
    end_r = int(end_color[0:2], 16)
    end_g = int(end_color[2:4], 16)
    end_b = int(end_color[4:6], 16)
    
    interp_r = int(start_r + (end_r - start_r) * ((rating - 40) / 60))
    interp_g = int(start_g + (end_g - start_g) * ((rating - 40) / 60))
    interp_b = int(start_b + (end_b - start_b) * ((rating - 40) / 60))
    
    return f'#{interp_r:02x}{interp_g:02x}{interp_b:02x}'

start_color = '#e46b14'  # Red
end_color = '#29a393'    # Green

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

st.text("NBA Draft Scouting 2024")

sel_pos = st.selectbox('Positions', ['All', 'PG', 'SG', 'SF', 'PF', 'C'], placeholder='All')

if sel_pos != 'All':
    filtered_sam = sam[sam['Pos'].str.contains(sel_pos, case=False)].reset_index()
else:
    filtered_sam = sam

col1, col2 = st.columns(2)

with col1:
    st.header("Sam")
    for index, row in filtered_sam.iterrows():
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
        espn = row['ESPN']
        ceil = row['Ceiling']
        floor = row['Floor']
        desc = row['Description']

        color = interpolate_color(rating, start_color, end_color)

        st.markdown(f"""
            <h3>{rank}. {name}, {team}:
                <span style='color:{color};'>{rating}</span>
            </h3>
            """, unsafe_allow_html=True)
        
        col11, col12, col13 = st.columns([3,1,1])

        with col11:
            st.code(f"{pos} - {ht}, {wt} lbs\n{ceil} ceiling\n{floor} floor")

        with col12:
            st.code(f"{pts} PPG\n{ast} APG\n{reb} RPG")

        with col13:
            st.code(f"{fg} FG%\n{p3} 3P%\n{ft} FT%")

        st.markdown(f"**ESPN Big Board Rank: {espn}**")
        st.caption(desc)
        
with col2:
    st.header("Adam")
    for index, row in filtered_sam.iterrows():
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
        espn = row['ESPN']
        ceil = row['Ceiling']
        floor = row['Floor']
        desc = row['Description']

        color = interpolate_color(rating, start_color, end_color)

        st.markdown(f"""
            <h3>{rank}. {name}, {team}:
                <span style='color:{color};'>{rating}</span>
            </h3>
            """, unsafe_allow_html=True)
        
        col21, col22, col23 = st.columns([3,1,1])

        with col21:
            st.code(f"{pos} - {ht}, {wt} lbs\n{ceil} ceiling\n{floor} floor")

        with col22:
            st.code(f"{pts} PPG\n{ast} APG\n{reb} RPG")

        with col23:
            st.code(f"{fg} FG%\n{p3} 3P%\n{ft} FT%")

        st.markdown(f"**ESPN Big Board Rank: {espn}**")
        st.caption(desc)
        
        
        
