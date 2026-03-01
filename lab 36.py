import numpy as np

# Provided vectors (edit if you want different values)
feature = np.array([[30.0, 50.0, 10.0]])
weights = np.array([[0.05],
                    [0.8],
                    [-0.1]])

scalar = 3
scaled_feature = scalar * feature
scaled_weights = scalar * weights


feature_norm = np.linalg.norm(feature)
weights_norm = np.linalg.norm(weights)


print("Feature norm:", feature_norm)
print("Weights norm:", weights_norm)
print("Scaled feature:", scaled_feature)
print("Scaled weights:", scaled_weights)
print("feature shape:", feature.shape)
print("weights shape:", weights.shape)
