from getpass import getpass
from linkedin_api import Linkedin

# Prompt the user to enter their LinkedIn username and password
username = input("Enter your LinkedIn username: ")
password = getpass("Enter your LinkedIn password: ")

# Initialize the LinkedIn API client
linkedin = Linkedin(username, password)

# Replace <PROFILE_URL> with the URL of the LinkedIn profile you want to analyze
url = "https://www.linkedin.com/in/h-s-umer-farooq/"

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

# Create a mentor profile for the person
mentor_profile = f"{name} is currently working as a {current_position} at {current_company}. "
if education:
    mentor_profile += f"{name} has a background in {', '.join(education)} and "
mentor_profile += f"is skilled in {', '.join(skills)}. "
mentor_profile += f"{name}'s summary: {summary}"

# Print the mentor profile
print(mentor_profile)