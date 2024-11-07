import pickle

# Load the datasets
with open('data/names.pkl', 'rb') as f:
    names = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    faces_data = pickle.load(f)

# Truncate the larger dataset to match the smaller one
if len(names) > len(faces_data):
    names = names[:len(faces_data)]
elif len(faces_data) > len(names):
    faces_data = faces_data[:len(names)]

# Save the truncated datasets
with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)

with open('data/faces_data.pkl', 'wb') as f:
    pickle.dump(faces_data, f)

print("Datasets are now consistent.")


