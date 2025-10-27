# Hindi Text Translator - AI Agent Instructions

## Project Overview
**Current State**: Production-ready text-only translator (PDF support removed for simplicity)
- Lightweight Streamlit app translating English `.txt` files to Hindi
- Direct Google Translate API integration (no external libraries like deep-translator)
- UV package manager for dependency management
- 155 lines total code (2 files: `app.py` + `translator.py`)

## Architecture Evolution
**Important**: Original PRD specified PDF support, but implementation simplified to text-only
- ❌ **Removed**: PDF processing, deep-translator, reportlab, fonts folder, complex src/ structure
- ✅ **Current**: Minimal dependencies (streamlit + requests), direct API calls, flat structure
- See `smoke-test.md` TBug001 for critical bug fix history (multi-segment translation)

## Critical Implementation Details

### Translation Engine (`translator.py`)
**Key Pattern**: Google Translate API returns long text as **multiple segments**
```python
# CRITICAL: Must combine ALL segments, not just first one
translated_parts = [segment[0] for segment in result[0] if segment and segment[0]]
translated = ''.join(translated_parts)  # Join all parts
```
**Bug History**: TBug001 - originally took only `result[0][0][0]`, causing incomplete translations

### SSL Bypass for Corporate Networks
```python
# Required at module level in translator.py
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl.create_default_context = create_unverified_context  # Monkey patch
session.verify = False  # In requests call
```

### File Structure Preservation
- Split on `\n\n` (paragraphs), translate individually, rejoin with `\n\n`
- Preserves paragraph boundaries in output files

## Development Workflow

### Environment Setup (UV Package Manager)
```bash
# UV is the ONLY supported method (not pip/venv)
uv sync                    # Install dependencies from pyproject.toml
uv run streamlit run app.py  # Always use 'uv run' prefix
```

**Dependencies** (in `pyproject.toml`):
- `streamlit>=1.30.0` - Web UI
- `requests>=2.31.0` - HTTP for translation API
- Python 3.12+ required

### Running & Testing
```bash
# Start app (runs in background)
uv run streamlit run app.py
# Access at http://localhost:8501 (port increments if busy: 8502, 8503...)

# Automated testing with Playwright
# See smoke-test.md for 37 test cases - all marked [x] (100% pass rate)
```

### Project Structure (Actual)
```
├── app.py              # 65 lines - Streamlit UI
├── translator.py       # 90 lines - Translation logic
├── pyproject.toml      # UV config (2 dependencies)
├── smoke-test.md       # Test checklist with bug tracking (TBug001)
├── prd.md              # Original requirements (NOTE: PDF removed post-PRD)
├── .venv/              # UV-managed environment
└── test-sample.txt     # Test fixture
```

## Code Patterns & Conventions

### Error Handling
- **Retry logic**: 3 attempts with 1-second delay between retries
- **Graceful failures**: Return empty string on final failure, raise Exception with details
- **User-facing errors**: Streamlit shows errors with st.error() + helpful hints

### Streamlit UI Flow
1. File upload → decode UTF-8 → show character count
2. Translate button → spinner → call `translate_file()`
3. Success → download button + preview expander (text_area, disabled=True)
4. No inline editing - direct file transformation only

## Common Pitfalls

### ❌ Don't Do This
- Use `pip install` or `python -m venv` (UV only!)
- Import deep-translator, pypdf, reportlab (removed dependencies)
- Load entire file into memory for large docs (already handled via paragraph chunking)
- Forget SSL bypass (corporate networks will fail)
- Take only first API segment (causes TBug001 regression)

### ✅ Do This
- Always use `uv run` for Python commands
- Combine all API response segments with `''.join()`
- Test with `tbug001-test.txt` (559-char paragraph) to verify multi-segment handling
- Check `smoke-test.md` before merging changes

## Testing Strategy
**Playwright-driven smoke tests** (see smoke-test.md):
- Page load → file upload → translate → download → verify Hindi content
- All 37 tests pass with 100% rate
- TBug001 documents critical multi-segment translation fix
- Screenshot evidence in `.playwright-mcp/` folder

## References
- **smoke-test.md**: Test cases + bug tracking (TBug001 fix details)
- **prd.md**: Original vision (PDF support) - simplified in implementation
- **pyproject.toml**: Source of truth for dependencies
- Port conflicts: App auto-increments (8501 → 8502 → 8503)
