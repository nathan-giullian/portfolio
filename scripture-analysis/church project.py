import requests
import sys
from bs4 import BeautifulSoup
import unicodedata

# Section to get all urls for each chapter in the Book of Mormon
url_main = 'https://www.churchofjesuschrist.org/study/scriptures/bofm?lang=eng'
response_main = requests.get(url_main)
soup_main = BeautifulSoup(response_main.text, 'html.parser')
urlparts = soup_main.find('div', id='app')
# Find all <a> tags and extract 'href' values
if urlparts:
    hrefs = [a.get('href') for a in urlparts.find_all('a') if a.get('href') is not None]
else:
    hrefs = []

print(hrefs)

start_value = '/study/scriptures/bofm/1-ne/_contents?lang=eng'
end_value = '/study/scriptures/bofm/moro/10?lang=eng'

# Find indices
start_index = hrefs.index(start_value) if start_value in hrefs else None
end_index = hrefs.index(end_value) if end_value in hrefs else None
# Extract items between start and end values, if both indices are found
if start_index is not None and end_index is not None and start_index < end_index - 1:
    items_between = hrefs[start_index + 1:end_index + 1]
else:
    items_between = []  # No items found or invalid indices

print("The Book of Mormon has " + str(end_index - start_index) + " chapters.")

html_content = str(soup_main)
# Define the file name
file_name = "Scripture Scrape/html/bofm.html"

# Open the file for writing
with open(file_name, 'w') as html_file:
    html_file.write(html_content)

print(f"File '{file_name}' has been saved.")

# For each chapter in the Book of Mormon, get the verses
for item in items_between:
        if 'contents' not in item:
            # URL
            url = 'https://www.churchofjesuschrist.org' + item
            from urllib.parse import urlparse, unquote
            print(url)

            # Parse the URL
            parsed_url = urlparse(url)

            # Access the path part of the URL
            path = parsed_url.path

            # Optional: decode the path to convert percent encodings back to characters
            decoded_path = unquote(path)

            # Now, extract the specific part you're interested in
            # Assuming the structure is known and consistent, you can split by '/' and access the relevant parts
            parts = decoded_path.split('/')
            # The parts list will contain ['', 'study', 'scriptures', 'bofm', 'omni', '1'], so you can join the parts you need
            specific_part = ''.join(parts[-2:])  # This will join 'omni' and '1'

            print(specific_part)  # Output: omni1


            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # This removes the superscripts
            for sup_tag in soup.find_all('sup'):
                sup_tag.decompose()

            # This removes the verse numbers
            for span_tag in soup.find_all('span'):
                span_tag.decompose()

            # header = soup.find('h1', id='title1')
            # chapter = soup.find('p', id='title_number1')
            # summary = soup.find('p', id='study_summary1')
            verses = soup.find('div', class_='body-block')

            # Clean code from special characters
            text = "This is an example text with special character â."
            normalized_text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

            print(normalized_text)

            # If you need to work with the text within this header, you can access it with .text or .get_text()
            # header_text = header.text
            # chapter_text = chapter.text
            # summary_text = summary.text
            verses_text = verses.text

            # print(header_text)
            # print(chapter_text)
            # print(summary_text)
            print(verses_text)
            html_content = str(soup)
            # Define the file name
            file_name = "Scripture Scrape/html/"+specific_part+".html"

            # Open the file for writing
            try:
                with open(file_name, 'x') as html_file:
                    html_file.write(html_content)
                    print(f"File '{file_name}' created successfully.")
            except FileExistsError:
                print(f"File '{file_name}' already exists.")

            print(f"File '{file_name}' has been saved.")
# Pause the code
sys.exit()

# print(soup)

# Extract scripture text; the class or id will vary based on the website's structure
scripture_text = soup.find(class_='some_class').text

print(scripture_text)
sys.exit()

#Basic Word Frequency Analysis
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

