import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences=[
    'I love my dog',
    'I love my cat',
    'You love my dog!',
    'Do you think my dog is amazing'
]

tokenizer = Tokenizer(num_words = 100,oov_token="<OOV>")  #取100个词作为关键词,没有的词汇使用oov来代替
tokenizer.fit_on_texts(sentences) #根据句子进行编码
word_index = tokenizer.word_index


sequences = tokenizer.texts_to_sequences(sentences)  #序列化

padded = pad_sequences(sequences) #统一编码后句子长度一致性
# padded = pad_sequences(sequences,padding='post') #统一编码后句子长度一致性
# padded = pad_sequences(sequences,padding='post',maxlen=5) #统一编码后句子长度一致性
# padded = pad_sequences(sequences,padding='post',truncating='post',maxlen=5) #统一编码后句子长度一致性

print(word_index)
print(sequences)
print(padded)

# 下面是测试集
test_data=[
    'i really love my dog',
    'my dog loves my manatee'
]

test_seq = tokenizer.texts_to_sequences(test_data)
print(test_seq)