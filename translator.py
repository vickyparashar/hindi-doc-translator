"""Simple English to Hindi text translator."""
import ssl
import urllib3
import requests
import time

# Disable SSL warnings for corporate networks
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create unverified SSL context
def create_unverified_context(*args, **kwargs):
    context = ssl.create_default_context(*args, **kwargs)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context

ssl.create_default_context = create_unverified_context


def translate_text(text: str, max_retries: int = 3) -> str:
    """
    Translate English text to Hindi.
    
    Args:
        text: English text to translate
        max_retries: Maximum retry attempts
        
    Returns:
        Translated Hindi text
    """
    if not text or not text.strip():
        return ""
    
    for attempt in range(max_retries):
        try:
            # Use Google Translate API directly
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                'client': 'gtx',
                'sl': 'en',
                'tl': 'hi',
                'dt': 't',
                'q': text.strip()
            }
            
            session = requests.Session()
            session.verify = False
            
            response = session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            result = response.json()
            if result and len(result) > 0 and len(result[0]) > 0:
                translated = result[0][0][0]
                return translated if translated else ""
            
            return ""
            
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            else:
                raise Exception(f"Translation failed: {str(e)}")
    
    return ""


def translate_file(input_text: str) -> str:
    """
    Translate text file content from English to Hindi.
    
    Args:
        input_text: English text content
        
    Returns:
        Translated Hindi text
    """
    if not input_text:
        return ""
    
    # Split into paragraphs to maintain structure
    paragraphs = input_text.split('\n\n')
    translated_paragraphs = []
    
    for para in paragraphs:
        if para.strip():
            translated = translate_text(para)
            translated_paragraphs.append(translated)
        else:
            translated_paragraphs.append("")
    
    return '\n\n'.join(translated_paragraphs)
