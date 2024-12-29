# switchbot_auth

A Python script for authenticating with the [SwitchBot API v1.1](https://github.com/OpenWonderLabs/SwitchBotAPI), enabling seamless integration and management of SwitchBot devices. This repository is specifically designed to function as a **Home Assistant custom component**, making it easy to incorporate SwitchBot devices into your smart home setup.

## Features
- Authenticate with the SwitchBot API v1.1 using your token and secret.
- Integrates directly with Home Assistant as a custom component.
- Lightweight and extensible for adding additional SwitchBot functionalities.
- Facilitates programmatic interaction with SwitchBot devices for automation.

---

## Home Assistant Integration
This repository is structured to function directly as a **Home Assistant custom component**. Follow the steps below to add it to your setup.

### Steps to Install
1. Locate the `custom_components` directory within your Home Assistant configuration folder. If it does not exist, create it:
   ```bash
   mkdir -p ~/.homeassistant/custom_components/

	2.	Clone or copy the switchbot_auth directory into the custom_components folder:

cd ~/.homeassistant/custom_components/
git clone https://github.com/yourusername/switchbot_auth.git


	3.	Restart Home Assistant to enable the custom component:
	•	You can restart from the Home Assistant UI (Settings > System > Restart) or via the command line:

sudo systemctl restart home-assistant

Configuration

To configure the custom component, update your configuration.yaml file with the following details:

switchbot_auth:
  token: YOUR_SWITCHBOT_TOKEN
  secret: YOUR_SWITCHBOT_SECRET

Replace YOUR_SWITCHBOT_TOKEN and YOUR_SWITCHBOT_SECRET with the values from your SwitchBot account. You can obtain these by referring to the SwitchBot API documentation.

Save the configuration.yaml file and restart Home Assistant again for the changes to take effect.

Requirements
	•	Home Assistant: Latest version recommended.
	•	Python: Version 3.7 or later.
	•	Dependencies: Ensure the requests library is installed. You can add it to your Python environment as follows:

pip install requests

Usage as a Standalone Script

You can also use the sensor.py script independently of Home Assistant to authenticate and interact with the SwitchBot API.

Steps to Run
	1.	Clone this repository:

git clone https://github.com/yourusername/switchbot_auth.git
cd switchbot_auth


	2.	Set the required authentication details as environment variables:

export SWITCHBOT_TOKEN='your_token'
export SWITCHBOT_SECRET='your_secret'


	3.	Run the script:

python sensor.py

File Structure

The repository is structured as follows:
	•	sensor.py: The main script for authenticating and interacting with the SwitchBot API.
	•	manifest.json: Metadata file for Home Assistant integration.
	•	__init__.py: Initialization file for the custom component.
	•	README.md: Documentation for the project.
	•	.gitignore: Files and directories to exclude from version control.
	•	LICENSE: License information.

License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, subject to the terms outlined in the LICENSE file.

Documentation

For more information, visit the SwitchBot API documentation.
