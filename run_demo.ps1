
# Demo script for Local-Brain-Search
Write-Host "Starting Demo..." -ForegroundColor Cyan

# 1. Index the test data
Write-Host "Indexing test_data/..." -ForegroundColor Yellow
python src/main.py index ./test_data

# 2. Search for a known fact
Write-Host "`nSearching for 'When did the meeting with external vendors happen?'..." -ForegroundColor Yellow
python src/main.py search "When did the meeting with external vendors happen?"

# 3. Search for another fact
Write-Host "`nSearching for 'login bug'..." -ForegroundColor Yellow
python src/main.py search "login bug"

Write-Host "`nDemo Complete!" -ForegroundColor Cyan
