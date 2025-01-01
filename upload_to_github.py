import os
import git

def upload_to_github(repo_path, file_path, commit_message, branch='main'):
    try:
        repo = git.Repo(repo_path)
        repo.git.add(file_path)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push(branch)
        print("File successfully uploaded to GitHub.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Calling fucntion to upload data file.
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/apple.csv'  # Path to the file you want to add
commit_message = 'Added CSV data file using Python.'
upload_to_github(repo_path, file_path, commit_message)

# Calling fucntion to upload code file.
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/Final_Code.py'
commit_message = 'Added code file using python.'
upload_to_github(repo_path, file_path, commit_message)

# Calling function to upload forecasted prices csv file 
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/forecasted_prices.csv'
commit_message = 'Added forecasted prices data file using python.'
upload_to_github(repo_path, file_path, commit_message)

# Calling function to upload graph 1
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/Close vs 50-Day SMA.png'
commit_message = 'Added Close vs 50-Day SMA graph using python.'
upload_to_github(repo_path, file_path, commit_message)

# Calling function to upload graph 2
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/Close vs 200-Day SMA.png'

upload_to_github(repo_path, file_path, commit_message)

# Calling function to upload graph 3 
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository

commit_message = 'Added Close vs Forecasted Prices graph using python.'
upload_to_github(repo_path, file_path, commit_message)

# Calling function to upload the code file to upload files to github.com
repo_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction'  # Path to your cloned repository
file_path = 'C:/Users/talha/OneDrive/Desktop/Stock-Market-Prediction/upload_to_github.py'
commit_message = 'Added the said file using python.'

upload_to_github(repo_path, file_path, commit_message)


