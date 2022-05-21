import pandas as pd

import tensorflow as tf

from extraction import embedding_w2v
from extraction import split_and_zero_padding
from extraction import ManhatDist

data_file = ''

test_df = pd.read_csv(data_file)
for a in ['answer', 'key_answer']:
    test_df[a + '_n'] = test_df[a]

embedding_dim = 300
max_seq_length = 20
test_df, embeddings = embedding_w2v(test_df, embedding_dim=embedding_dim, empty_w2v=False)

X_test = split_and_zero_padding(test_df, max_seq_length)

assert X_test['left'].shape == X_test['right'].shape

model = tf.keras.models.load_model('./data/SiameseLSTM.h5', custom_objects={'ManhatDist':ManhatDist})
model.summary()

prediction = model.predict([X_test['left'], X_test['right']])
print(prediction)