import streamlit as st
from PIL import Image

# Custom CSS for underlining text and adding background color
st.markdown(
    """
    <style>
    .underline {
        text-decoration: underline;
    }
    .section {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 10px;
    }
    .team-row {
        display: flex;
        align-items: center;
    }
    .team-logo {
        width: 20px;
        height: 20px;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("UCL - League Path Analysis")

col1, col2 = st.columns([0.25, 0.75])

team_points = {
    "Fenerbahce": 36.000,
    "Dynamo Kiev": 26.500,
    "Partizan": 25.500,
    "Lugano": 8.000,
    "Club Brugge": 64.000,
    "Rangers": 63.000,
    "AZ": 50.000,
    "Slavia Prague": 53.000,
    "Salzburg": 50.000,
    "Brest": 13.366,
    "Twente": 12.260,
    "Lille": 47.000,
    "Benfica": 79.000,
    "Galatasaray": 31.500,
    "Servette": 9.000,
    "Anderlecht": 14.500,
    "Union SG": 27.000,
    "Sparta Prague": 22.500,
    "Sturm Graz": 14.500
}

# Dictionary mapping team names to logo file paths
team_logos = {team: f"logos/{team.replace(' ', '_')}.png" for team in team_points.keys()}

with col1:
    option1 = st.selectbox(
        "UEL Champion?",
        ("Leverkusen", "Atalanta"))

    option7 = st.selectbox(
        "🇮🇹 Atalanta in Serie A?",
        ("Top 4", "5+"))

    option3 = st.selectbox(
        "🇦🇹 Austria Champion?",
        ("Sturm Graz", "Salzburg"))

    option4 = st.selectbox(
        "🇧🇪 Belgium 2nd?",
        ("Anderlecht", "Club Brugge", "Union SG"))

    option5 = st.selectbox(
        "🇳🇱 Netherlands 3rd?",
        ("Twente", "AZ"))

    option6 = st.selectbox(
        "🇫🇷 France 4th?",
        ("Brest", "Lille"))

    option8 = st.selectbox(
        "🇨🇭 Switzerland 2nd?",
        ("Lugano", "Servette"))

    option9 = st.selectbox(
        "🇹🇷 Türkiye Champion?",
        ("Galatasaray", "Fenerbahce"))

def display_team_with_logo(team):
    logo_path = team_logos[team]
    image = Image.open(logo_path)
    image = image.resize((20, 20))
    st.markdown(
        f"""
        <div class="team-row">
            <img src="data:image/png;base64,{image_to_base64(image)}" class="team-logo">{team}
        </div>
        """, unsafe_allow_html=True
    )

def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

with col2:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("2nd Qualifying Round")

    Q2_teams_ = [
        ("Dynamo Kiev", team_points["Dynamo Kiev"]),
        ("Partizan", team_points["Partizan"]),
        ("Fenerbahce" if option9 == "Galatasaray" else "Galatasaray",
         team_points["Fenerbahce"] if option9 == "Galatasaray" else team_points["Galatasaray"]),
        (option8, team_points[option8]),
        ("Slavia Prague", team_points["Slavia Prague"]),
        ("Sturm Graz" if option3 == "Salzburg" else "Salzburg",
         team_points["Sturm Graz"] if option3 == "Salzburg" else team_points["Salzburg"])
    ]

    Q2_teams_a = sorted(Q2_teams_, key=lambda x: x[1], reverse=True)

    if option1 == "Atalanta" and option7 == "5+":
        Q2_teams_s = Q2_teams_a
        q2_seeded_teams = Q2_teams_s[:3]
        q2_unseeded_teams = Q2_teams_s[3:]
        q2_passed_teams = []
    else:
        Q2_teams_s = Q2_teams_a[2:]
        q2_seeded_teams = Q2_teams_s[:2]
        q2_unseeded_teams = Q2_teams_s[2:]
        q2_passed_teams = Q2_teams_a[:2]

    col1_q2, col2_q2 = st.columns(2)
    with col1_q2:
        st.write('<p class="underline">Seeded Teams (Seribaşı)</p>', unsafe_allow_html=True)
        for team, _ in q2_seeded_teams:
            display_team_with_logo(team)
    with col2_q2:
        st.write('<p class="underline">Unseeded Teams (Seribaşı Olmayan)</p>', unsafe_allow_html=True)
        for team, _ in q2_unseeded_teams:
            display_team_with_logo(team)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("3rd Qualifying Round")

    Q3_teams_ = q2_seeded_teams + [
        (option6, team_points[option6]),
        (option5, team_points[option5]),
        ("Rangers", team_points["Rangers"]),
        (option4, team_points[option4])
    ] + q2_passed_teams

    if option1 == "Atalanta" and option7 == "5+":
        Q3_teams_.append(("Benfica", team_points["Benfica"]))

    Q3_teams_s = sorted(Q3_teams_, key=lambda x: x[1], reverse=True)

    q3_seeded_teams = Q3_teams_s[:4]
    q3_unseeded_teams = Q3_teams_s[4:]

    col1_q3, col2_q3 = st.columns(2)
    with col1_q3:
        st.write('<p class="underline">Seeded Teams (Seribaşı)</p>', unsafe_allow_html=True)
        for team, _ in q3_seeded_teams:
            display_team_with_logo(team)
    with col2_q3:
        st.write('<p class="underline">Unseeded Teams (Seribaşı Olmayan)</p>', unsafe_allow_html=True)
        for team, _ in q3_unseeded_teams:
            display_team_with_logo(team)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Play-Off Round")

    PO_teams_ = q3_seeded_teams

    po_seeded_teams = PO_teams_[:2]
    po_unseeded_teams = PO_teams_[2:]

    col1_po, col2_po = st.columns(2)
    with col1_po:
        st.write('<p class="underline">Seeded Teams (Seribaşı)</p>', unsafe_allow_html=True)
        for team, _ in po_seeded_teams:
            display_team_with_logo(team)
    with col2_po:
        st.write('<p class="underline">Unseeded Teams (Seribaşı Olmayan)</p>', unsafe_allow_html=True)
        for team, _ in po_unseeded_teams:
            display_team_with_logo(team)
    st.markdown('</div>', unsafe_allow_html=True)
