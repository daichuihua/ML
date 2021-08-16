from __future__ import absolute_import, division, print_function, unicode_literals


import tensorflow_datasets as tfds
import tensorflow as tf
print(tf.__version__)

import tensorflow_datasets as tfds
import tensorflow as tf
print(tf.__version__)
# Get the data
# dataset, info = tfds.load('imdb_reviews/subwords8k', with_info=True, as_supervised=True)
# train_dataset, test_dataset = dataset['train'], dataset['test']
dataset, info = tfds.load('imdb_reviews/subwords8k', with_info=True, as_supervised=True)
train_dataset, test_dataset = dataset['train'].take(4000), dataset['test'].take(1000)

tokenizer = info.features['text'].encoder

print(info)

BUFFER_SIZE = 100
BATCH_SIZE = 100

train_dataset = train_dataset.shuffle(BUFFER_SIZE).take(1000)
train_dataset = train_dataset.padded_batch(BATCH_SIZE)
test_dataset = test_dataset.padded_batch(BATCH_SIZE).take(1000)

vocab_size = 1000
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, 8),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(8, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(8)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

NUM_EPOCHS = 10
history = model.fit(train_dataset, epochs=NUM_EPOCHS, validation_data=test_dataset)

import matplotlib.pyplot as plt


def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()

plot_graphs(history, 'accuracy')
plot_graphs(history, 'loss')