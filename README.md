# LinkedIn Job Application Bot
A Python automation tool using Selenium WebDriver to streamline job searching and application processes on LinkedIn, featuring automated login, job searching, and application saving.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-red)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Integration-green)
![Jobs](https://img.shields.io/badge/Job-Application-orange)

## 🎯 Overview
This project creates an automated job search tool that:
1. Handles LinkedIn login
2. Performs job searches
3. Filters for Easy Apply
4. Saves job listings
5. Automates interactions

## 🤖 Bot Features
### Automation Elements
- Automated login process
- Job search functionality
- Easy Apply filtering
- Job saving capabilities
- Page scrolling management

### Process Management
- Chrome WebDriver control
- Element interaction
- Search customization
- Location filtering
- Result processing

Note: Currently, the bot saves jobs instead of applying to them. This is a temporary measure while an AI model is being developed to handle application surveys intelligently. Future versions will include automated application submission once the survey handling capability is implemented.

## 🔧 Technical Components
### LinkedIn Automation System
```python
def search_for_jobs(self, job_description, location):
    search_input = self.wait.until(ec.presence_of_element_located((
        By.CSS_SELECTOR, "input[type='text']")))
    search_input.send_keys(job_description)
    search_input.send_keys(Keys.ENTER)
    
    jobs_button = self.wait.until(ec.presence_of_element_located((
        By.CSS_SELECTOR, 'li[class="search-reusables__primary-filter"] button')))
    jobs_button.click()
```

### Key Features
1. **Platform Navigation**
   - Automated login
   - Job search automation
   - Filter application
   - Result handling

2. **Search Optimization**
   - Location targeting
   - Job description matching
   - Easy Apply filtering
   - Result scrolling

3. **Job Processing**
   - Listing detection
   - Job saving
   - Page navigation
   - Error handling

## 💻 Implementation Details
### Class Structure
- `Linkedin`: Main automation class
  - Login management
  - Search functionality
  - Job processing
  - Page interaction

### Process Management
- Secure credential handling
- Search parameter control
- Result processing
- Action timing

## 🚀 Usage
1. Install required packages:
```bash
pip install selenium
```

2. Set up environment variables:
```bash
export LINKEDIN_EMAIL="your_email"
export LINKEDIN_PASSWORD="your_password"
```

3. Run the bot:
```bash
python main.py
```

## 🎯 Bot Rules
1. Configure credentials
2. Set search parameters
3. Run automation
4. Monitor progress
5. Check saved jobs

## 🛠️ Project Structure
```
linkedin-job-bot/
├── main.py           # Entry point
└── linkedin.py       # Bot implementation
```

## 📊 Features
### Input Processing
- Credential validation
- Search parameter handling
- Location filtering
- Job criteria matching

### Output Management
- Job listing detection
- Save functionality
- Progress tracking
- Status reporting

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL