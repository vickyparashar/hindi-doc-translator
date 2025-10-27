# Smoke Test Checklist - Hindi Document Translator

## Page Load & UI Elements

- [ ] Application starts successfully with `streamlit run app.py`
- [ ] Page loads at `http://localhost:8501` without errors
- [ ] Page title "Hindi Document Translator" is visible
- [ ] No console errors in browser developer tools
- [ ] Page layout renders correctly (no broken CSS)

## File Upload Component

- [ ] File uploader widget is visible
- [ ] File uploader accepts `.pdf` files
- [ ] File uploader accepts `.txt` files
- [ ] File uploader rejects unsupported file types (e.g., `.docx`, `.jpg`)
- [ ] Upload button is clickable
- [ ] Selected file name displays after upload
- [ ] File size is shown after upload
- [ ] Can clear/remove uploaded file

## Output Format Selection

- [ ] Output format radio buttons are visible
- [ ] "PDF" option is selectable
- [ ] "Text" option is selectable
- [ ] Only one option can be selected at a time
- [ ] Default selection is visible on page load

## Translation Button

- [ ] "Translate" button is visible
- [ ] "Translate" button is disabled when no file is uploaded
- [ ] "Translate" button is enabled when file is uploaded
- [ ] Button text is clear and readable
- [ ] Button is clickable when enabled
- [ ] Button shows loading state during translation

## Translation Process

- [ ] Progress indicator appears during translation
- [ ] No application crash during translation
- [ ] Translation completes without timeout errors
- [ ] Success message appears after translation
- [ ] Error message displays for unsupported files
- [ ] Error message displays for encrypted PDFs
- [ ] Error message displays for scanned PDFs (if applicable)

## Download Component

- [ ] Download button appears after successful translation
- [ ] Download button label is "Download Hindi Translation"
- [ ] Download button is clickable
- [ ] Downloaded file has correct extension (`.pdf` or `.txt`)
- [ ] Downloaded file is not empty (size > 0 bytes)
- [ ] Downloaded file opens without errors
- [ ] Downloaded file contains Hindi text (visual verification)

## Small File Test (< 10 pages)

- [ ] Upload small PDF file (1-5 pages)
- [ ] Translation completes in reasonable time (< 30 seconds)
- [ ] Download PDF output successfully
- [ ] Upload small text file (< 1 KB)
- [ ] Translation completes quickly (< 10 seconds)
- [ ] Download text output successfully

## Medium File Test (10-100 pages)

- [ ] Upload medium PDF file (10-50 pages)
- [ ] Translation shows progress indicator
- [ ] Translation completes without memory errors
- [ ] Download works for medium-sized output

## Error Handling

- [ ] Uploading empty file shows error message
- [ ] Uploading corrupted PDF shows error message
- [ ] Uploading password-protected PDF shows error message
- [ ] Network error during translation shows user-friendly message
- [ ] Error messages are clearly visible and readable
- [ ] App remains functional after error occurs

## Browser Compatibility

- [ ] Works in Chrome/Edge
- [ ] Works in Firefox
- [ ] Works in Safari (if applicable)
- [ ] Mobile responsive layout (optional)

## Performance Checks

- [ ] Page loads in < 3 seconds
- [ ] Small file translation (< 5 pages) completes in < 30 seconds
- [ ] No memory leaks after multiple translations
- [ ] Application remains responsive during translation

## Accessibility

- [ ] All buttons have readable labels
- [ ] Color contrast is sufficient for text
- [ ] Tab navigation works for all interactive elements
- [ ] Screen reader can read main UI elements (optional)

---

## Test Execution Notes

**Date**: _________________  
**Tester**: _________________  
**Browser**: _________________  
**OS**: _________________  
**Test Duration**: _________________  

**Critical Failures**: _________________  
**Minor Issues**: _________________  
**Pass Rate**: _____ / _____ tests passed
