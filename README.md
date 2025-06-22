🧪 Automation Testing Framework with Cucumber, Selenium & Secure Data Handling
This is a robust automation testing framework built using Cucumber (Behave) with Python and Selenium WebDriver. It supports secure password encryption, centralized test data management, and modular step definitions for scalable test development.

🔧 Features
✅ Cucumber BDD (Behave) for behavior-driven development

🕸️ Selenium WebDriver for browser automation

🔐 Encrypted password handling using cryptography

📄 YAML-based test data for easy configuration of XPaths, usernames, and other app data

📸 Automatic screenshot capture and console output export

📁 Organized test structure with support for tags, parallel execution, and custom runners

🔐 Secure Credentials
Passwords are encrypted using the cryptography library and stored in a .key file. The decryption mechanism ensures that credentials are never exposed in plain text during test execution.

📚 Test Data Management
Test locators (like XPaths), usernames, and other input data are stored in easily maintainable .yaml files. This promotes cleaner test scripts and reduces duplication.

Folder Structure Overview

PROJECT1/
│
├── App_data/                  # YAML configuration for XPaths, usernames, etc.
│   └── app_data.yml
│
├── Exports/                  # Reports and exported data
│   ├── Job_Export.xlsx
│   ├── Generate_Report/
│   └── Results/
│
├── Screenshots/              # Captured screenshots on test failure or steps
│
├── Test_Scripts/             # Organized test scenarios
│   ├── feature1/
│   └── feature2/
│
├── Users/                    # Encrypted user credentials and scripts
│   ├── amaiti9509@gmail.com_encrypted.txt
│   ├── Encrypt_Decrypt.py
│
├── utils/                    # Utility scripts
│   ├── Encrypt_Decrypt.py
│   └── take_screenshot.py
│
├── .gitignore
├── run_behave.py             # Executes Behave with setup
├── run_report.log            # Logs from execution
├── runner_config.yml         # Custom runner configuration
├── runner.py                 # Custom test runner
└── README.md                 # Project documentation


🚀 How to Run
Run Behave Tests:

Terminal
python run_behave.py
