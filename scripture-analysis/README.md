# Scripture Analysis Project

A Python-based project for web scraping and statistical analysis of LDS scriptures.

## Project Overview

**Objective**: Scrape text data from the LDS scriptures available online, and perform basic statistical analysis to uncover insights such as word frequency, sentiment analysis, and usage of unique words across different books.

## Installation

### Installing Python

If you're new to Python, follow these steps to install it on your system:

#### Windows
1. Download the latest Python installer from the [official Python website](https://www.python.org/downloads/windows/)
2. Run the installer. Make sure to check "Add Python to PATH" during installation
3. Verify the installation by opening Command Prompt and typing:
   ```
   python --version
   ```

#### macOS
1. Install Homebrew (if not already installed):
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python using Homebrew:
   ```
   brew install python
   ```
3. Verify the installation:
   ```
   python3 --version
   ```

#### Linux
Most Linux distributions come with Python pre-installed. If not:
```
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Setting Up a Virtual Environment (Recommended)

It's good practice to create a virtual environment for your projects:

```
# Install virtualenv
pip install virtualenv

# Create a virtual environment
python -m venv env

# Activate the environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### Installing Required Libraries

Once Python is installed and your virtual environment is activated, install the required libraries:

```
pip install beautifulsoup4 requests pandas nltk matplotlib seaborn
```

## Tools and Libraries

- **Python 3**: The programming language we'll be using
- **BeautifulSoup**: A Python library for web scraping
- **Requests**: A library to make HTTP requests in Python
- **Pandas**: A library for data manipulation and analysis
- **NLTK (Natural Language Toolkit)**: A library for working with human language data (text) for Python
- **Matplotlib/Seaborn**: Libraries for data visualization

## Project Steps

### Step 1: Setting Up Your Environment

1. Ensure you have Python installed.
2. Install necessary libraries using pip:
   ```
   pip install beautifulsoup4 requests pandas nltk matplotlib seaborn
   ```

### Step 2: Choosing Your Data Source

1. Select the scriptures you're interested in analyzing from the Church of Jesus Christ of Latter-day Saints website.
2. For simplicity, start with one book, such as the Book of Mormon.

### Step 3: Web Scraping

1. Use the `requests` library to fetch the content of the scripture page.
2. Apply `BeautifulSoup` to parse the HTML content and extract the scripture text.

### Step 4: Data Cleaning

1. Remove any HTML tags, punctuation, and unnecessary whitespace from the scraped text.
2. Normalize the text to a consistent case (e.g., lower case) for accurate analysis.

### Step 5: Basic Statistical Analysis

1. **Word Frequency Analysis**: Use NLTK to find the most common words.
2. **Unique Word Analysis**: Identify and count unique words used in the text.
3. **Sentiment Analysis (Optional)**: Use NLTK's sentiment analysis tools to gauge the overall sentiment of the text.

### Step 6: Data Visualization

1. Use Matplotlib or Seaborn to create visualizations of your findings, such as word frequency histograms.

### Step 7: Insights and Conclusion

1. Summarize your findings.
2. Reflect on what the statistical analyses might indicate about the themes or language used in the scriptures.

## Example Code Snippets

Here are a few snippets to get you started:

### Web Scraping with BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

# Example URL
url = 'https://www.churchofjesuschrist.org/study/scriptures/bofm/enos/1?lang=eng'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract scripture text based on specific elements
title = soup.find(id='title1').text  # Page title
chapter_name = soup.find(id='title_number1').text  # Chapter name
summary = soup.find(id='study_summary1').text  # Chapter summary
verses = soup.find('div', class_='body-block').text  # Verses

# Remove footnotes and references
for note in soup.find_all(class_='study-note-ref'):
    note.decompose()
for sup in soup.find_all('sup'):
    sup.decompose()

print(f"Title: {title}")
print(f"Chapter: {chapter_name}")
print(f"Summary: {summary}")
print("Verses:")
print(verses)
```

### Basic Word Frequency Analysis

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Tokenize words
words = word_tokenize(scripture_text.lower())

# Filter out stopwords
words_filtered = [word for word in words if word not in stopwords.words('english')]

# Frequency distribution
freq_dist = nltk.FreqDist(words_filtered)
freq_dist.most_common(10)
```

## Project Tips

- **Start Small**: Begin with a small scope, such as analyzing a single chapter, then expand as you get more comfortable.
- **Respect the Website's Rules**: Ensure you're allowed to scrape the website and follow any guidelines they provide.
- **Data Privacy and Ethics**: Be mindful of ethical considerations, especially when working with religious texts.

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/your-username/scripture-analysis.git
   cd scripture-analysis
   ```
2. Set up your environment and install dependencies (see Installation section)
3. Run the example scripts to start analyzing scripture data:
   ```
   python scraper.py
   ```

## Contributing

As this is a personal learning project, formal contributions aren't expected. However, if you'd like to suggest improvements or report issues:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/suggestion`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some suggestion'`)
5. Push to the branch (`git push origin feature/suggestion`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Nathan Giullian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributors

- Nathan Giullian - Initial work and project development

## Acknowledgments

- Church of Jesus Christ of Latter-day Saints for making scripture texts available online
- The developers of BeautifulSoup, NLTK, and other libraries that make this analysis possible
