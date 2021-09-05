from processing import filter
from analyzing import analyze

# Text Pre-processing
filter('SiriusData.csv', 'Processed_text.txt')

# Text Analyzing and Report
analyze('Processed_text.txt', 'report.txt')

