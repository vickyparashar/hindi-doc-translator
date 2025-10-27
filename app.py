"""Hindi Text Translator - Simple Streamlit App"""
import streamlit as st
from translator import translate_file

st.set_page_config(
    page_title="Hindi Text Translator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Hindi Text Translator")
st.markdown("Translate English text files to Hindi instantly.")

# File upload
uploaded_file = st.file_uploader(
    "Upload English Text File",
    type=['txt'],
    help="Upload a .txt file containing English text"
)

if uploaded_file:
    # Read file
    text_content = uploaded_file.read().decode('utf-8')
    
    # Show file info
    st.success(f"✅ File uploaded: {uploaded_file.name} ({len(text_content)} characters)")
    
    # Translate button
    if st.button("🔄 Translate to Hindi", type="primary", use_container_width=True):
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
                    use_container_width=True
                )
                
                # Show preview
                with st.expander("📄 Preview Translation"):
                    st.text_area(
                        "Hindi Text",
                        translated_text,
                        height=300,
                        disabled=True
                    )
            else:
                st.error("❌ Translation failed. Please try again.")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Please check your internet connection and try again.")
else:
    st.info("👆 Upload a text file to begin translation")

# Footer
st.markdown("---")
st.caption("Powered by Google Translate API | Built with Streamlit")
