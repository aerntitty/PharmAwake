import kagglehub

# Download latest version
path = kagglehub.dataset_download("iamsouravbanerjee/cause-of-deaths-around-the-world")

print("Path to dataset files:", path)