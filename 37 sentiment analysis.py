# 38 sentiment analysis
import nltk 
import string
import re

text = open(r"E:\Blackcoffeer assignment\result_text\37.txt",encoding="ISO-8859-1").read()
text = text.lower()

exclude = set(string.punctuation)
text_data = ''.join(char for char in text if char not in exclude)
text_data = nltk.word_tokenize(text_data)


stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_Auditor.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_Currencies.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_DatesandNumbers.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_Generic.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_GenericLong.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_Geographic.txt",encoding="ISO-8859-1").read().lower()
stopword= open(r"E:\Blackcoffeer assignment\data\StopWords_Names.txt",encoding="ISO-8859-1").read().lower()
stopword = stopword.split("\n")
# print(stopword)

clean_list = []
for words in text_data:
    if words not in stopword and words not in string.punctuation:
        clean_list.append(words)

# no. of words
num_words =nltk.word_tokenize(text)
num_words = [re.sub('[^a-zA-Z]+', '', _) for _ in num_words]
total_no_words = len(num_words)

# no of sentences
no_sentences = []
data = nltk.sent_tokenize(text)
for t in data:
    no_sentences.append(t)

total_sentences = len(no_sentences)


# print(clean_list)

dict_positive_word = open(r"E:\Blackcoffeer assignment\data\positive-words.txt",encoding="ISO-8859-1").read()
dict_positive_word = dict_positive_word.lower()

exclude = set(string.punctuation)
pose_dict= ''.join(char for char in dict_positive_word if char not in exclude)
positive_dict = nltk.word_tokenize(pose_dict)
# print(positive_dict)

dict_negative_word = open(r"E:\Blackcoffeer assignment\data\negative-words.txt",encoding="ISO-8859-1").read()
dict_negative_word = dict_negative_word.lower()

exclude = set(string.punctuation)
neg_dict= ''.join(char for char in dict_negative_word if char not in exclude)
negative_dict = nltk.word_tokenize(neg_dict)
# print(negative_dict)


# positive_score
positive_score = 0
for words in clean_list:
    if words in positive_dict:
        positive_score += 1

# negative_score
negative_sc = 0
for words in clean_list:
    if words in negative_dict:
        negative_sc -= 1 
negative_score = negative_sc *(-1)


# syllable count
def syllable_count(words):
    count = 0
    vowels = "aeiouy"
    for word in words:
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("es" and "ed"):
            count -= 1
        if count == 0:
            count += 1
    return count

pronounRegex = re.compile(r'I|we|my|ours|us',re.I)
pronouns = pronounRegex.findall(text)



# polarity_score
polarity_score = (positive_score - negative_score)/((positive_score + negative_score) + 0.000001)

# subjectivity_score
subjectivity_score = (positive_score + negative_score)/(len(clean_list)+(0.000001))

# average sentence length 
avg_sent_len= (total_no_words / total_sentences)

# length of clean list
len_clean_list = len(clean_list)

# Syllable Count Per Word
complex_count = syllable_count(clean_list)

# percentage of complex word
per_complex_word = (complex_count/total_no_words)

# fog index
fog_index = (0.4 * (avg_sent_len + per_complex_word))

# average no of words per sentences
avg_words_per_sentences = (total_no_words/total_sentences)

# pronouns count
count_pronouns = len(pronouns)

# total no of character in each word
req = " ".join(text_data)
count_char = []
for word in req:
     for char in word:
        count = count_char.append(char)

no_characters = len(count_char)

# average word length 
average_word_length = (no_characters/total_no_words)


print("positive_score :-", positive_score)
print("negative_score :-", negative_score)
print("polarity_score :-",polarity_score)
print("subjectivity_score :-",subjectivity_score)
print("no_sentences :-",total_sentences)
print("total_no. of words :-",total_no_words)
print("avg_sent_len :-",avg_sent_len)
print("complex word count :-",complex_count)
print("percentage of complex words",per_complex_word)
print("Fog index :-", fog_index)
print("avg words per sentences :-", avg_words_per_sentences)
print("length_clean_list :-",len_clean_list)
print("syllable count", complex_count)
print("pronouns count :-", count_pronouns)
print("average word length :-",average_word_length )














