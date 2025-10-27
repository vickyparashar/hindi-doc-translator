# Setup Guide for Hindi Document Translator

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/vickyparashar/hindi-doc-translator.git
cd hindi-doc-translator
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Font Installation
The Noto Sans Devanagari font should already be in the `fonts/` directory. If not, download it from:
- https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari

Place `NotoSansDevanagari-Regular.ttf` in the `fonts/` directory.

### 5. Run the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Testing

### Run Unit Tests
```bash
pytest tests/ -v
```

### Run Tests with Coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

### Code Quality Check
```bash
ruff check .
```

## Usage

1. **Upload Document**: Click "Choose an English PDF or text file" and select your document
2. **Select Format**: Choose output format (PDF or Text)
3. **Translate**: Click "Translate to Hindi" button
4. **Download**: Once complete, click "Download Hindi Translation"

## Troubleshooting

### SSL Certificate Errors
If you encounter SSL certificate verification errors, this is typically a network/proxy issue. Try:
- Checking your internet connection
- Disabling VPN temporarily
- Updating Python's SSL certificates

### Font Not Found Error
If you get a font error when generating PDFs:
1. Ensure `NotoSansDevanagari-Regular.ttf` is in the `fonts/` directory
2. Check file permissions
3. Restart the application

### Memory Errors with Large Files
For very large PDFs (500+ pages):
- The application processes page-by-page to minimize memory usage
- Consider splitting very large documents into smaller files
- Ensure at least 2GB of available RAM

### Translation Rate Limits
Google Translate (free tier) has rate limits. If you encounter rate limit errors:
- Wait a few minutes before trying again
- For large documents, split them into smaller files
- The application includes automatic retry logic with exponential backoff

## Performance Optimization

### For Small Files (< 10 pages)
- Expected translation time: < 30 seconds
- No special configuration needed

### For Medium Files (10-100 pages)
- Expected translation time: 1-3 minutes
- Progress bar shows real-time status

### For Large Files (1000+ pages)
- Processes in chunks to maintain responsiveness
- Progress indicator updates per section
- Consider using text output for faster processing

## Development

### Project Structure
```
hindi-doc-translator/
├── src/                   # Core application modules
│   ├── __init__.py
│   ├── translator.py      # Translation logic
│   ├── pdf_processor.py   # PDF handling
│   ├── text_processor.py  # Text file handling
│   └── utils.py           # Helper functions
├── fonts/                 # Hindi fonts
├── tests/                 # Unit tests
├── app.py                 # Streamlit application
└── requirements.txt       # Dependencies
```

### Adding New Features

1. **New Translation Backend**: Modify `src/translator.py`
2. **Additional File Formats**: Create new processor in `src/`
3. **UI Changes**: Update `app.py`
4. **Tests**: Add tests in `tests/`

### Running in Development Mode

```bash
# Enable debug mode
streamlit run app.py --logger.level debug

# Run on different port
streamlit run app.py --server.port 8502
```

## Deployment

### Local Deployment
The application runs locally by default. No server deployment needed.

### Docker Deployment (Optional)
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t hindi-translator .
docker run -p 8501:8501 hindi-translator
```

## FAQ

**Q: Can I translate from Hindi to English?**
A: Currently, the application only supports English to Hindi. Modifying `src/translator.py` to accept language parameters would enable bidirectional translation.

**Q: What file size limit exists?**
A: Default limit is 100MB. This can be changed in `src/utils.py` (MAX_FILE_SIZE_MB).

**Q: Does it work offline?**
A: No, translation requires an internet connection to access Google Translate.

**Q: Is my document data private?**
A: Translation is performed via Google Translate's free service. Do not use for confidential documents.

**Q: Can I batch process multiple files?**
A: Currently, the app processes one file at a time. Batch processing can be added as a future enhancement.

## Support

- **Issues**: Open an issue on GitHub
- **Documentation**: See README.md and prd.md
- **Testing Guide**: See smoke-test.md

## License

This project is open source under the MIT License.
