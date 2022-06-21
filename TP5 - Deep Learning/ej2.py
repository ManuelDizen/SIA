from tensorflow import keras

from src.vae import VAE
from src.plotting import *

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
trainset = np.concatenate([x_train, x_test], axis=0)
mnist_digits = np.expand_dims(trainset, -1).astype("float32") / 255

vae = VAE()
vae.compile(optimizer=keras.optimizers.Adam())
vae.fit(mnist_digits, epochs=1, batch_size=128)

plot_latent_space(vae)

x_train = np.expand_dims(x_train, -1).astype("float32") / 255

plot_label_clusters(vae, x_train, y_train)