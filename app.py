"""Hindi Text Translator - Simple Streamlit App"""
import streamlit as st
from translator import translate_file
from youtube_translator import translate_youtube_transcript

st.set_page_config(
    page_title="Hindi Translator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Hindi Translator")
st.markdown("Translate English text files and YouTube videos to Hindi.")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["📄 Text File", "🎥 YouTube Video"])

# Tab 1: Text File Translation (existing feature)
with tab1:
    st.markdown("### Upload English Text File")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a text file",
        type=['txt'],
        help="Upload a .txt file containing English text",
        key="file_uploader"
    )

    if uploaded_file:
        # Read file
        text_content = uploaded_file.read().decode('utf-8')
        
        # Show file info
        st.success(f"✅ File uploaded: {uploaded_file.name} ({len(text_content)} characters)")
        
        # Translate button
        if st.button("🔄 Translate to Hindi", type="primary", use_container_width=True, key="translate_file"):
            try:
                with st.spinner("Translating..."):
                    translated_text = translate_file(text_content)
                
                if translated_text:
                    st.success("✅ Translation completed!")
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Hindi Translation",
                        data=translated_text.encode('utf-8'),
                        file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}_hindi.txt",
                        mime="text/plain",
                        type="primary",
                        use_container_width=True,
                        key="download_file"
                    )
                    
                    # Show preview
                    with st.expander("📄 Preview Translation"):
                        st.text_area(
                            "Hindi Text",
                            translated_text,
                            height=300,
                            disabled=True,
                            key="preview_file"
                        )
                else:
                    st.error("❌ Translation failed. Please try again.")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Please check your internet connection and try again.")
    else:
        st.info("👆 Upload a text file to begin translation")

# Tab 2: YouTube Video Translation (new feature)
with tab2:
    st.markdown("### Enter YouTube Video URL")
    st.markdown("Download English transcript from YouTube and translate to Hindi.")
    
    # YouTube URL input
    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste the URL of a YouTube video with English captions",
        key="youtube_url"
    )
    
    if youtube_url:
        # Translate button
        if st.button("🔄 Download & Translate", type="primary", use_container_width=True, key="translate_youtube"):
            try:
                with st.spinner("Downloading transcript and translating... This may take a moment for long videos."):
                    video_id, translated_transcript = translate_youtube_transcript(youtube_url)
                
                if translated_transcript:
                    st.success("✅ Transcript downloaded and translated successfully!")
                    
                    # Show transcript info
                    word_count = len(translated_transcript.split())
                    st.info(f"📊 Translated transcript: {word_count} words")
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Hindi Transcript",
                        data=translated_transcript.encode('utf-8'),
                        file_name=f"youtube_{video_id}_hindi_transcript.txt",
                        mime="text/plain",
                        type="primary",
                        use_container_width=True,
                        key="download_youtube"
                    )
                    
                    # Show preview
                    with st.expander("📄 Preview Hindi Transcript"):
                        st.text_area(
                            "Hindi Transcript",
                            translated_transcript,
                            height=400,
                            disabled=True,
                            key="preview_youtube"
                        )
                else:
                    st.error("❌ Translation failed. Please try again.")
                    
            except ValueError as e:
                st.error(f"❌ Invalid URL: {str(e)}")
                st.info("💡 Please enter a valid YouTube URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Make sure the video has English captions available.")
    else:
        st.info("👆 Paste a YouTube URL to download and translate its transcript")

# Footer
st.markdown("---")
st.caption("Powered by Google Translate API & YouTube Transcript API | Built with Streamlit")
