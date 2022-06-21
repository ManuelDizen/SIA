from tensorflow import keras
from src.variational_autoencoder import VariationalAutoencoder
from src.plotting import *

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
trainset = np.concatenate([x_train, x_test], axis=0)
mnist_digits = np.expand_dims(trainset, -1).astype("float32") / 255

vae = VariationalAutoencoder()
vae.compile(optimizer=keras.optimizers.Adam())
vae.fit(mnist_digits, epochs=1, batch_size=128)

plotLatent(vae)

x_train = np.expand_dims(x_train, -1).astype("float32") / 255

plotAverages(vae, x_train, y_train)