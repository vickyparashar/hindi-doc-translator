"""YouTube transcript downloader and translator."""
import re
from youtube_transcript_api import YouTubeTranscriptApi
from translator import translate_text


def extract_video_id(url: str) -> str:
    """
    Extract video ID from YouTube URL.
    
    Args:
        url: YouTube URL (various formats supported)
        
    Returns:
        Video ID string
        
    Raises:
        ValueError: If URL is invalid or video ID cannot be extracted
    """
    # Pattern for various YouTube URL formats
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    raise ValueError("Invalid YouTube URL. Could not extract video ID.")


def download_transcript(video_id: str, language: str = 'en') -> str:
    """
    Download transcript from YouTube video.
    
    Args:
        video_id: YouTube video ID
        language: Language code (default: 'en' for English)
        
    Returns:
        Complete transcript as a single string
        
    Raises:
        Exception: If transcript cannot be downloaded
    """
    try:
        # Create API instance and fetch transcript
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=[language])
        
        # Extract text from all snippets
        full_transcript = ' '.join([snippet.text for snippet in transcript_data.snippets])
        
        return full_transcript
        
    except Exception as e:
        raise Exception(f"Failed to download transcript: {str(e)}")


def translate_youtube_transcript(url: str) -> tuple[str, str]:
    """
    Download YouTube transcript and translate to Hindi.
    
    Args:
        url: YouTube video URL
        
    Returns:
        Tuple of (video_id, translated_transcript)
        
    Raises:
        Exception: If download or translation fails
    """
    # Extract video ID
    video_id = extract_video_id(url)
    
    # Download English transcript
    english_transcript = download_transcript(video_id, language='en')
    
    if not english_transcript:
        raise Exception("Downloaded transcript is empty.")
    
    # Split into chunks to handle large transcripts
    # Process in paragraphs (every ~500 words to avoid API limits)
    words = english_transcript.split()
    chunk_size = 500
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    # Translate each chunk
    translated_chunks = []
    for chunk in chunks:
        if chunk.strip():
            translated = translate_text(chunk)
            translated_chunks.append(translated)
    
    # Combine all translated chunks
    hindi_transcript = ' '.join(translated_chunks)
    
    return video_id, hindi_transcript
