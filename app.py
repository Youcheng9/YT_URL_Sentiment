import streamlit as st

st.title("YouTube Sentiment Analyzer")
url = st.text_input("Enter YouTube URL")

if st.button("Fetch Comments"):
    video_id = get_video_details(url)
    if video_id:
        with st.spinner("Fetching comments..."):
            comments = get_video_details(video_id)
            st.success(f"Fetched {len(comments)} comments.")
            for c in comments:
                st.write(f"- {c}")
    else:
        st.error("Invalid YouTube URL")

