# Placement_Records_Digitisation

## Introduction

This project aims to digitize the placement records for SSN College of Engineering. It allows users to view the placement details of students and filter them by department, company, CTC range, and more. This system helps streamline the management of placement data and makes it easily accessible for students, faculty, and administrative staff.

## Features

- **User Authentication**: Secure login for different types of users (students, faculty, admin).
- **View Placement Records**: Access detailed placement records of all students.
- **Filter by Department**: Filter placement records based on the student's department.
- **Filter by Company**: View records of students placed in specific companies.
- **Filter by CTC Range**: Filter records based on the offered CTC (Cost to Company).
- **Add and Manage Records**: Admins can add new placement records and manage existing ones.
- **Responsive Design**: User-friendly interface accessible on various devices.

## Requirements

To run this project, you need the following Python packages:

- `pillow==10.4.0`

You can install these packages using the following commands:
```sh
python -m venv venv
source venv/bin/activate
```
```sh
pip install -r requirements.txt
```
## Setting up Environment Variables

- Create a .env file in the root directory of your project and add the following environment variables with your MySQL database credentials:

- PATH_TO_CSV_FILE = path_to_your_csv_file_containing_student_data

## Running the Application
- Run by the following command:
```sh
python3 manage.py runserver
```
- Create a new user through admin site or by running the command:
```sh
python3 manage.py createsuperuser
```

## Existing Credentials for Login
- admin : testpass123 (or) testpass1234 if previous password doesn't work
- adm : 1234