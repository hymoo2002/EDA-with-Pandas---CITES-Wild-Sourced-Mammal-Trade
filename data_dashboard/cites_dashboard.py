# CITES Wild-Sourced Mammal Trade — Streamlit Dashboard
# Run with:  streamlit run cites_dashboard.py

import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(
    page_title="CITES Wild Mammal Trade",
    layout="wide",
    page_icon="🐘",
)

st.title("🐘 CITES Wild-Sourced Mammal Trade")
st.caption("Legal international trade in wild-caught mammals, 2016–2024. Data: CITES Trade Database.")

# Load & clean data
@st.cache_data
def load_data():
    raw = pd.read_csv("net_imports_2026-07-11_19_22_comma_separated.csv")
    df = raw.drop(columns=["2025", "2026"], errors="ignore").dropna(subset=["Country"])
    df["Unit"] = df["Unit"].fillna("Number of specimens")

    years = [c for c in df.columns if c.isdigit()]
    df_long = df.melt(
        id_vars=["App.", "Taxon", "Term", "Unit", "Country"],
        value_vars=years,
        var_name="Year",
        value_name="Quantity",
    )
    df_long["Year"] = df_long["Year"].astype(int)
    return df_long.dropna(subset=["Quantity"])

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

year_min, year_max = int(df["Year"].min()), int(df["Year"].max())
year_range = st.sidebar.slider("Year range", year_min, year_max, (year_min, year_max))

appendices = st.sidebar.multiselect(
    "CITES Appendix",
    options=sorted(df["App."].unique()),
    default=sorted(df["App."].unique()),
)

countries = st.sidebar.multiselect(
    "Importing countries (leave empty = all)",
    options=sorted(df["Country"].unique()),
    default=[],
)

# Apply filters
mask = (
    df["Year"].between(year_range[0], year_range[1])
    & df["App."].isin(appendices)
)
if countries:
    mask &= df["Country"].isin(countries)
filtered = df[mask]

if filtered.empty:
    st.warning("No data matches the current filters. Try widening them.")
    st.stop()

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Transactions", f"{len(filtered):,}")
c2.metric("Species", filtered["Taxon"].nunique())
c3.metric("Countries", filtered["Country"].nunique())
trophy_pct = (filtered["Term"] == "trophies").sum() / len(filtered) * 100
c4.metric("Trophy share", f"{trophy_pct:.0f}%")

st.divider()

# Yearly trend
st.subheader("Trade over time")
yearly = filtered.groupby("Year").size().rename("Transactions")
st.line_chart(yearly)

# Top-10 charts in a 2x2 grid
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 importing countries")
    st.bar_chart(filtered["Country"].value_counts().head(10))

with col2:
    st.subheader("Top 10 traded species")
    st.bar_chart(filtered["Taxon"].value_counts().head(10))

col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 10 trade terms")
    st.bar_chart(filtered["Term"].value_counts().head(10))

with col4:
    st.subheader("Top 10 trophy species")
    trophy_species = filtered[filtered["Term"] == "trophies"]["Taxon"].value_counts().head(10)
    if trophy_species.empty:
        st.info("No trophy records in the current filter.")
    else:
        st.bar_chart(trophy_species)

# Raw data
st.divider()
st.subheader("Filtered data")
st.dataframe(filtered, use_container_width=True, hide_index=True)
