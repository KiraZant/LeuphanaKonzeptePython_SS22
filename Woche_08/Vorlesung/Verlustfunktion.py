import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Set up values for linear regression with y=0.75*x
x = np.arange(0, 10, 0.5)
y = 0.75 * x
mse_errors = []
mae_errors = []

# Calculate error for different slopes
slopes = np.linspace(0, 1.5, 100)
for slope in slopes:
    y_predicted = slope * x
    mse_errors.append(mean_squared_error(y_true=y, y_pred=y_predicted))
    mae_errors.append(mean_absolute_error(y_true=y, y_pred=y_predicted))

# Plot results of loss function
fig, axs = plt.subplots()
fig.suptitle('Verlustfunktion', fontsize=16)
axs.plot(slopes, mse_errors)
axs.plot(slopes, mae_errors)
axs.legend(['Mean-Squared-Error', 'Mean-Absolute-Error'])
axs.set(xlim=(0, 1.5))
plt.tight_layout()
plt.show()
fig.savefig('Verlustfunktion.png')
