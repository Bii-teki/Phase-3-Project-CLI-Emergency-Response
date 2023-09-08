# Emergency Response Management System
### Table of Contents

    Introduction
    Features
    Installation
    Usage
        Hospital Management
        Patient Management
        Transport Coordination
    Database
    Contributing
    License

## Introduction

The Emergency Response Management System is a command-line interface (CLI) application designed to streamline and enhance the coordination of patients, hospitals, and transportation resources during emergency scenarios, such as natural disasters or large-scale accidents. This system aims to ensure efficient and timely responses to emergencies.
Features

   ### Hospital Management:
        Add hospitals with information like name, contact, location, address, and bed capacity.
        Real-time updates on hospital statuses.

   ### Patient Management:
        Register and manage patient details, including name, contact, location, address, and admission status.
        Basic input validation to ensure data integrity.

   ### Transport Coordination:
        Allocate patients to hospitals, optimizing bed usage and response times.
        Simulate the allocation of patients to available hospitals.

   ### Database Integration:
        Utilizes database integration (e.g., SQLite) to securely store and manage crucial data.
        Ensures data reliability, accessibility, and historical tracking for future reference and analysis.

   ### Menu System:
        Provides an interactive menu-driven interface for users to access the system's functionalities.

## Installation

To use this Emergency Response Management System, follow these steps:

    Clone this repository to your local machine:

    bash

git clone https://github.com/Bii-teki/Phase-3-Project-CLI-Emergency-Response.git

Navigate to the project directory:

bash

cd emergency-response-system

Install the required dependencies. You may want to set up a virtual environment first:

bash

pip install -r requirements.txt

### Run the application:

bash

    python main.py

Usage
#### Hospital Management

    To add a hospital, select option 1 from the menu, then provide hospital details such as name, contact, location, address, and bed capacity.

    To view hospital details, select option 2, enter the hospital's name, and the system will display the information.

    To delete a hospital, choose option 3, enter the hospital's name, and the system will remove it from the records.

    To view a list of all hospitals in the database, select option 4.

#### Patient Management

    To add a patient, choose option 1 from the menu, then provide patient details, including name, contact, location, address, and admission status (yes/no).

    To view patient details, select option 2, enter the patient's name, and the system will display the information.

    To delete a patient, select option 3, enter the patient's name, and the system will delete the patient record.

    To view a list of all patients in the database, choose option 4.

#### Transport Coordination

    To simulate patient allocation to a hospital, select option 1 from the menu, and the system will assign a patient to an available hospital.

    To view patients who have not been admitted to a hospital, choose option 2.

    To delete a patient's record, select option 3, enter the patient's name, and the system will delete the patient record.

    To view a list of all patients in the database, choose option 4.

## Database

This system utilizes database integration, which is essential for data reliability and historical tracking. The database is managed internally, and users do not need to interact with it directly.

## Contributing

We welcome contributions to improve this Emergency Response Management System. If you have suggestions, bug reports, or feature requests, please open an issue on the GitHub repository or submit a pull request. 
License

## MIT License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software following the terms of the license.


#### Copyright (c) 2023 Geoffrey Bii

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
