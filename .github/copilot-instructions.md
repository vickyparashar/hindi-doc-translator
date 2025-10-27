# Hindi Document Translator - AI Agent Instructions

## Project Overview
A lightweight Python application for translating English documents (PDF/text) to Hindi. This is a file-to-file processing system with no UI for text viewing or editing - users upload files and download translated files directly.

## Key Requirements (from prd.md)

### Mandatory Constraints
- **Translation libraries**: ONLY free, open-source libraries (no paid APIs like Google Translate API, DeepL, etc.)
- **Language**: Python-only implementation
- **Architecture**: Keep it lightweight and simple
- **Performance**: Must handle large documents (1000+ pages) efficiently

### Input/Output Flow
- **Input**: PDF or .txt files in English
- **Output**: .txt or PDF files in Hindi
- **No intermediate steps**: Direct file upload → translation → file download (no text display in UI)

## Implementation Guidance

### Translation Library Selection
**Recommended: `deep-translator` library** - most reliable free option with multiple backends
```python
from deep_translator import GoogleTranslator
# Fallback to 'indictrans' or 'ai4bharat/indictrans2' for better Hindi quality if needed
```

When implementing:
- Primary: `deep-translator` (GoogleTranslator backend - free, no API key)
- Alternative: `googletrans` (less stable but widely used)
- Advanced: `IndicTrans2` models via HuggingFace transformers (better quality, higher resource usage)
- Avoid any solution requiring API keys or paid services
- Implement retry logic for rate limit handling
- Document limitations: informal text translates better than technical jargon

### PDF Processing
**Reading PDFs**: Use `pypdf` (PyPDF2's successor) or `pdfplumber` for text extraction
**Writing PDFs**: Use `reportlab` for Hindi PDF generation (better Unicode support)

```python
from pypdf import PdfReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Hindi font (Noto Sans Devanagari or similar)
pdfmetrics.registerFont(TTFont('Hindi', 'NotoSansDevanagari-Regular.ttf'))
```

Key practices:
- Extract text page-by-page to minimize memory
- Preserve paragraph structure using line spacing analysis
- Stream large PDFs (process page → translate → write incrementally)
- Include error handling for encrypted/scanned PDFs

### File Handling Patterns
```python
# Example pattern for large file processing
def process_large_file(input_path, output_path, chunk_size=100):
    # Process in chunks to handle 1000+ page documents
    # Use generators to minimize memory footprint
    pass
```

### Performance Considerations
- Process documents in batches/chunks for large files
- Consider multiprocessing for parallelizing page-by-page translation
- Monitor memory usage - avoid loading entire large PDFs into memory
- Implement progress tracking for long-running translations
- **Performance benchmarks** (from prd.md):
  - Small files (< 5 pages): Complete in < 30 seconds
  - Medium files (10-50 pages): Complete in < 2 minutes  
  - Large files (1000+ pages): Use streaming with progress indicator

### Project Structure (to be created)
```
hindi-doc-translator/
├── src/                   # Core application modules
│   ├── translator.py      # Core translation logic (deep-translator wrapper)
│   ├── pdf_processor.py   # PDF reading/writing with reportlab
│   ├── text_processor.py  # Text file handling
│   └── utils.py           # Helper functions
├── fonts/                 # Hindi fonts for PDF generation
│   └── NotoSansDevanagari-Regular.ttf
├── tests/                 # Unit and integration tests
│   └── fixtures/          # Sample test files
├── app.py                 # Streamlit web application (main entry point)
├── requirements.txt       # Python dependencies (keep minimal)
├── .env.example           # Configuration template
├── smoke-test.md          # Smoke test checklist (70+ tests)
├── prd.md                 # Product requirements document
└── README.md              # User documentation
```

**Recommended UI**: Streamlit web application for simple file upload/download
```python
# app.py - Simple Streamlit interface
import streamlit as st

st.title("Hindi Document Translator")
uploaded_file = st.file_uploader("Upload English PDF/Text", type=["pdf", "txt"])
format_choice = st.radio("Output format", ["PDF", "Text"])
if st.button("Translate"):
    # Process and provide download button
    st.download_button("Download Hindi Translation", data=result)
```

Run with: `streamlit run app.py`

## Development Workflow

### Setting Up
```bash
python -m venv venv
venv\Scripts\activate  # Windows (PowerShell)
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
# Access at http://localhost:8501
```

### Testing
- **Manual testing**: Follow `smoke-test.md` checklist (70+ test cases)
- **Automated testing**: Use Playwright with `smoke-test.md` as reference
- Test progression: Small files (1-10 pages) → Medium (10-100 pages) → Large (1000+ pages)
- Test both PDF and text inputs/outputs
- Validate Hindi output quality (informal text works better than technical jargon)
- Run `pytest tests/` for unit tests (once implemented)

### Code Quality
```bash
ruff check .        # Linting (PEP 8)
pytest tests/       # Unit tests
```

### Code Style
- Keep functions small and focused (single responsibility)
- Add type hints for better code clarity
- Comment complex translation or PDF processing logic
- Prioritize readability over cleverness (lightweight = maintainable)
- Follow PEP 8 guidelines (enforced via `ruff check .`)
- Write unit tests for all core modules (pytest)

## Common Pitfalls to Avoid
- Don't use paid translation services (Google Translate API, DeepL API, etc.) - use free libraries only
- Don't load entire 1000-page PDFs into memory - implement page-by-page streaming
- Don't forget to bundle Hindi fonts for PDF generation (Noto Sans Devanagari recommended)
- Don't add web UI complexity - Streamlit with `file_uploader` and `download_button` is sufficient for file-to-file workflow
- Don't skip error handling for: rate limits, malformed PDFs, scanned images (OCR not in scope)
- Don't display translated text in UI - go directly from upload to download (per PRD requirements)
- Remember: No text preview/editing features - direct file transformation only

## Error Handling Strategy
```python
# Handle common failure scenarios
try:
    # Translation with retry logic
    pass
except RateLimitError:
    # Implement exponential backoff
    pass
except PDFEncryptedError:
    # Return clear error message to user
    pass
except ScannedPDFError:
    # Inform user OCR is not supported
    pass
```

## References
- Product requirements: `prd.md`
- User documentation: `README.md` 
- Smoke test checklist: `smoke-test.md` (70+ atomic tests for Playwright automation)
- Current status: **Documentation-only stage** - no implementation code yet

## Testing Strategy
- Use `smoke-test.md` for manual and automated testing with Playwright
- Follow test execution order: Page Load → Upload → Format Selection → Translate → Download
- Each test in `smoke-test.md` is atomic and can be automated independently
- Run `streamlit run app.py` to start application at `http://localhost:8501`
- Verify smoke tests pass before merging changes to main branch
