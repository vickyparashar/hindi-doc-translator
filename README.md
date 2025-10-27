# Hindi Document Translator

A lightweight Python web application that translates English documents (PDF/text files) to Hindi using free, open-source translation libraries.

## Features

- 📄 **Multiple Input Formats**: Upload PDF or text files in English
- 🔄 **Multiple Output Formats**: Download translations as PDF or text files
- 🚀 **High Performance**: Handles large documents (1000+ pages) efficiently
- 🌐 **Web Interface**: Simple Streamlit-based UI for easy file upload/download
- 💯 **Free & Open Source**: No paid APIs or services required

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vickyparashar/hindi-doc-translator.git
cd hindi-doc-translator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download Hindi font (if not included):
   - Download [Noto Sans Devanagari](https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari)
   - Place the `.ttf` file in the `fonts/` directory

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser at `http://localhost:8501`

3. Upload your English document (PDF or text file)

4. Select output format (PDF or Text)

5. Click "Translate" and download the Hindi translation

## Project Structure

```
hindi-doc-translator/
├── src/
│   ├── translator.py      # Core translation logic
│   ├── pdf_processor.py   # PDF reading/writing
│   ├── text_processor.py  # Text file handling
│   └── utils.py           # Helper functions
├── fonts/                 # Hindi fonts for PDF generation
│   └── NotoSansDevanagari-Regular.ttf
├── tests/                 # Unit tests
│   └── fixtures/          # Sample test files
├── app.py                 # Streamlit web application
├── requirements.txt       # Dependencies
├── smoke-test.md          # Smoke test checklist
└── README.md              # This file
```

## Technology Stack

- **Translation**: `deep-translator` (free, no API key required)
- **PDF Reading**: `pypdf` 
- **PDF Writing**: `reportlab` with Unicode support
- **Web UI**: `streamlit`
- **Language**: Python 3.8+

## Limitations

- Does not support scanned PDFs (OCR not implemented)
- Cannot process encrypted/password-protected PDFs
- Translation quality depends on source text (informal text works better than technical jargon)
- May encounter rate limits with very large documents (implemented with retry logic)

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
This project follows PEP 8 guidelines. Run linting with:
```bash
ruff check .
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Translation powered by `deep-translator`
- Hindi font: Noto Sans Devanagari by Google Fonts
- Built with Streamlit

## Support

For issues or questions, please open an issue on GitHub.
