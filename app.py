"""
app.py — CareerLens AI
Entry point. Loads CSS, renders sidebar, routes to pages.
All ML/NLP logic lives in src/. All UI components in components/. All pages in pages/.
"""

import streamlit as st
from components.ui import load_css

st.set_page_config(
    page_title  = "CareerLens AI",
    page_icon   = "◈",
    layout      = "wide",
    initial_sidebar_state = "expanded",
)

load_css()

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    # Brand
    st.markdown("""
    <div style="padding:24px 20px 20px 20px;border-bottom:1px solid rgba(99,102,241,0.12)">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
            <div style="width:32px;height:32px;border-radius:8px;
                        background:linear-gradient(135deg,#6366f1,#8b5cf6);
                        display:flex;align-items:center;justify-content:center;
                        color:#fff;font-size:1rem;font-weight:700;
                        box-shadow:0 4px 12px rgba(99,102,241,0.4)">◈</div>
            <div>
                <div style="color:#e2e8f0;font-size:0.95rem;font-weight:700;
                            letter-spacing:-0.2px">CareerLens AI</div>
                <div style="color:#475569;font-size:0.62rem;letter-spacing:0.5px">
                    Resume Intelligence Platform</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # Navigation
    NAV_ITEMS = [
        ("◈",  "Dashboard"),
        ("◆",  "Resume Analyzer"),
        ("◉",  "ATS Analysis"),
        ("◎",  "Job Matching"),
        ("◇",  "Skill Gap"),
        ("▲",  "Optimization"),
        ("⟳",  "Simulation"),
        ("?",  "Interview Prep"),
        ("≡",  "Candidate Ranking"),
        ("▦",  "Analytics"),
        ("⚙",  "Settings"),
    ]

    page = st.radio(
        "nav",
        [item[1] for item in NAV_ITEMS],
        format_func=lambda x: next(
            f"{icon}  {x}" for icon, name in NAV_ITEMS if name == x
        ),
        label_visibility="collapsed",
    )

    # Session status indicator
    has_results = "results" in st.session_state
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="margin:0 8px;padding:10px 14px;border-radius:8px;'
        f'background:{"rgba(16,185,129,0.08)" if has_results else "rgba(99,102,241,0.06)"};'
        f'border:1px solid {"rgba(16,185,129,0.2)" if has_results else "rgba(99,102,241,0.12)"}">'
        f'<div style="color:{"#10b981" if has_results else "#475569"};font-size:0.68rem;'
        f'font-weight:600;letter-spacing:0.5px">'
        f'{"● Analysis loaded" if has_results else "○ No analysis yet"}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

# ── Page router ────────────────────────────────────────────────────────────
if page == "Dashboard":
    from pages.dashboard       import render; render()
elif page == "Resume Analyzer":
    from pages.resume_analyzer import render; render()
elif page == "ATS Analysis":
    from pages.ats_analysis    import render; render()
elif page == "Job Matching":
    from pages.job_matching    import render; render()
elif page == "Skill Gap":
    from pages.skill_gap       import render; render()
elif page == "Optimization":
    from pages.optimization    import render; render()
elif page == "Simulation":
    from pages.simulation      import render; render()
elif page == "Interview Prep":
    from pages.interview       import render; render()
elif page == "Candidate Ranking":
    from pages.ranking         import render; render()
elif page == "Analytics":
    from pages.analytics       import render; render()
elif page == "Settings":
    from pages.settings        import render; render()
