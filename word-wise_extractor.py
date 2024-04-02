#download the library first: `!pip install wordwise`
from wordwise import Extractor

text = """
Artificial intelligence (AI) is a field of study in computer science that focuses on developing and studying intelligent machines. AI allows machines to learn from experience, adapt to new inputs, and perform human-like tasks
"""
extractor = Extractor()
keywords = extractor.generate(text, 3)
print(keywords)
# change the number of tags you want. I use 3 here to get 3 tags.
