# Tags Generation:
The TextToTagGenerator model is a sequence-to-sequence transformer model trained to generate tags for a given input text. It is also most commons as the keywords extractors from any text or passage.</s>

![tags_model](https://github.com/wavesoumen/Tags_Generation/blob/main/images/tags_gen1.png)
- ## Generating Tags from Text (T5_base Model):
The model generates tags based on the input text by using a pretrained transformer model (`t5-base`) which is trained to generate human-readable text given a prompt.</s>

![t5_image1](https://github.com/wavesoumen/Tags_Generation/blob/main/images/t5_tags.png)
- Here I used the [fabiochiu/t5-base-tag-generation](https://github.com/wavesoumen/Tags_Generation/blob/main/t5_base_tag_generator.py) model from the `pip transformers`.
- Also used the `nltk` for the text classification.

### Example1 (t5_base_tags_generation):
Input text as prompt:
```
Artificial intelligence (AI) is a field of study in computer science that focuses on developing and studying intelligent machines. AI allows machines to learn from experience, adapt to new inputs, and perform human-like tasks.
```
Output Tags:
```
['Ai', 'Artificial Intelligence', 'Algorithms', 'Machine Learning', 'Learning']
```
Image of the Example1: </s>

![example1](https://github.com/wavesoumen/Tags_Generation/blob/main/images/tags1.png)

- ## Key-Words Frequency Checker:
- In this part, we use the [Keyword Frequency Checker](https://github.com/wavesoumen/Tags_Generation/blob/main/word_frequency.py) that will show the keywords counts.
The key words frequency checker is a simple Python script that counts how many times each word appears in a given list of words. It can be useful to identify important keywords or phrases within a text.
- Example2 (Keyword checker):
- Input Prompt:

```
Artificial intelligence (AI) is a field of study in computer science that focuses on developing and studying intelligent machines. AI allows machines to learn from experience, adapt to new inputs, and perform human-like tasks.
```
Output:
```
[('humans', 3), ('think', 1), ('things', 1), ('technology', 1), ('science', 1), ('recognize', 1), ('process', 1), ('patterns', 1), ('machines', 1), ('large', 1), ('judge', 1), ('intelligence', 1), ('different', 1), ('decisions', 1), ('creating', 1), ('amounts', 1), ('Artificial', 1)]
```
- ## Word-Wide Model:
This model extract the widely used keywords from the given text/passage. You can also change the number of how many words do you wants. In this example I have used 5 words.
In this example, we are checking the frequency of words in a given text using the word-wide model. The output shows the keywords or key phrases that appear most frequently in the input text.</s>

Keep in mind that before use the model, must install the library:
```bash
!pip install wordwise
```
- Input Text:
```
Artificial intelligence (AI) is a field of study in computer science that focuses on developing and studying intelligent machines. AI allows machines to learn from experience, adapt to new inputs, and perform human-like tasks.
```
- Output:
```
['intelligence', 'technology', 'data', 'goal', 'large amounts']
```
#### 
For any further queries or Explanation, contact me.
#
## - [Soumen Kayal.](https://github.com/wavesoumen)
##### 
https://wavesoumen.github.io/