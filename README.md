# LinkedIn Profile Analyzer

This Python script allows you to analyze a LinkedIn profile by extracting and displaying various details such as the person's name, current position, current company, education, skills, and summary. It utilizes the `linkedin_api` library to interact with the LinkedIn API.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed on your system
- The `getpass` library installed (`pip install getpass`)
- The `linkedin_api` library installed (`pip install linkedin_api`)

## Usage

1. Open the terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the command `python analyze_linkedin_profile.py`.
4. You will be prompted to enter your LinkedIn username and password. This information is required to authenticate with the LinkedIn API.
5. Enter the LinkedIn profile URL of the person you want to analyze in the `url` variable. Replace the `"Enter LinkedIn Profile URL"` placeholder with the actual URL.
6. The script will retrieve the profile data using the LinkedIn API and extract the necessary details.
7. Finally, the script will display a profile summary containing the person's name, current position, current company, education, skills, and summary.

Note: The script does not store or transmit your LinkedIn username and password. It uses the `getpass` library to securely prompt for and receive the password input.

## Code

```python
from getpass import getpass
from linkedin_api import Linkedin

# Prompt the user to enter their LinkedIn username and password
username = input("Enter your LinkedIn username: ")
password = getpass("Enter your LinkedIn password: ")

# Initialize the LinkedIn API client
linkedin = Linkedin(username, password)

# Replace <PROFILE_URL> with the URL of the LinkedIn profile you want to analyze
url = "Enter LinkedIn Profile URL"

# Extract the LinkedIn profile ID from the URL
profile_id = url.split("/")[-2]

# Get the LinkedIn profile data using the API client
profile_data = linkedin.get_profile(profile_id)

# Extract the name, current position, current company, education, skills, and summary of the person from the profile data
name = profile_data.get('firstName', '') + ' ' + profile_data.get('lastName', '')
current_position = profile_data.get('headline', '')
current_company = profile_data.get('companyName', 'Unknown')
education_data = profile_data.get('educations', [])
if education_data:
    education = [e['schoolName'] for e in education_data]
else:
    education = []
skills_data = profile_data.get('skills', [])
if skills_data:
    skills = [s['skill']['name'] for s in skills_data]
else:
    skills = []
summary = profile_data.get('summary', '')

# Create a profile for the person
mentor_profile = f"{name} is currently working as a {current_position} at {current_company}. "
if education:
    mentor_profile += f"{name} has a background in {', '.join(education)} and "
mentor_profile += f"is skilled in {', '.join(skills)}. "
mentor_profile += f"{name}'s summary: {summary}"

# Print the mentor profile
print(mentor_profile)
```

Replace the `"Enter LinkedIn Profile URL"` placeholder with the actual LinkedIn profile URL you want to analyze.

## Limitations

- The script relies on the `linkedin_api` library, which may have its own limitations or restrictions when interacting with the LinkedIn API. Ensure you comply with the library's usage guidelines and any rate limits imposed by LinkedIn.
- The script assumes that the LinkedIn profile URL provided is valid and accessible. If the URL is incorrect or the profile is not publicly

 visible, the script may fail to retrieve the necessary data.

## Disclaimer

This script is provided as-is. Use it at your own risk. The author bear no responsibility for any issues or damages arising from its use.
