<div align="center">

# QR Attendance System

![image](https://github.com/AzeemIdrisi/QR-Attendance-System/assets/112647789/dbc0c061-76d0-45bb-b5da-7f4373ffd073)

</div>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributions](#contributions)
- [Developers](#develpers)

## Overview

The QR Code Attendance System is an efficient,fast and user-friendly tool for tracking attendance using QR codes. It utilizes HTML, CSS, and Django to create a web-based interface for marking attendance. This system is designed to work seamlessly when devices are connected to the __Same College Local Network__.

The teacher/faculty can display the QR Code using classroom projector so that present students can scan and mark their attendance.

## Features

- **Automatic IP Fetching:** It fetch your IPv4 address automatically and Generate a QR code based on that IP to enable connections within the classroom.
- **Faculty Panel:** It has a Faculty View Panel that enables the teacher to remove duplicate or proxy attendances based on count.
- **User-Friendly Interface:** A straightforward web interface for effortless attendance management.
- **Real-Time Tracking:** Mark attendance by scanning QR codes with real-time updates.
- **Accessibility:** Easily access attendance records for quick reference.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- **Python3**
- **Django**
- **qrcode**
- **Web Browser:** Required for accessing the system interface.

## Setup

1. **Clone the Repository:**

   ```
   git clone https://github.com/AzeemIdrisi/QR-Attendance-System
   ```

2. **Navigate to the Project Directory:**

   ```
   cd QR-Attendance-System
   ```


4. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```
4. **Run the Django Server:**

   ```
   python manage.py runserver 0.0.0.0:8000 
   ```

5. **Access the System:**

   Open your web browser and go to `http://localhost:8000` to use the system.

### Setting up Firewall settings for the first time

- Open Windows Defender Firewall Settings:

   - Press Win + S to open the search bar.
   - Type "Windows Defender Firewall" and select the corresponding result.

- Create an Inbound Rule:

   - On the left panel, click on "Advanced settings."
   - In the left panel, select "Inbound Rules."
   - In the right panel, click on "New Rule..." to open the New Inbound Rule Wizard.

- Select Rule Type:

   - Choose "Port" and click "Next."

- Specify Port and Protocol:

   - Choose "Specific local ports" and enter the port number your Django server is running on (e.g., 8000).
   - Click "Next."

- Choose Action:

   - Choose "Allow the connection" and click "Next."

- When Does the Rule Apply?

   - Keep all three options (Domain, Private, Public) checked.
   - Click "Next."

- Specify Rule Name:

   - Enter a name for your rule (e.g., "Django Server").
   - Optionally, provide a description.
   - Click "Finish."

- Check the Inbound Rules:

   - In the left panel, click on "Inbound Rules."
   - Find your newly created rule in the list.

- Test the Connection:

   On another device within the same local network, try to access your Django server using the local IP address and port number or By simply scanning the displayed QR Code.

## Usage

1. **Open the System in Your Web Browser:**

   Access the system by opening your web browser and visiting `http://localhost:8000`.


2. **Display QR Codes:**

   Display the QR codes to students or attendees.

3. **Mark Attendance:**

   To mark attendance, scan the QR codes using a device connected to the same local network.

4. **Real-Time Tracking:**

   The attendance records will be updated in real-time, ensuring accurate tracking.

## Screenshots

### Admin Page
![image](https://github.com/AzeemIdrisi/QR-Attendance-System/assets/112647789/e4c9f2d8-6b8e-44de-a63d-f7e5db45383e)

### Student Page
![image](https://github.com/AzeemIdrisi/QR-Attendance-System/assets/112647789/a8e2f4a7-831c-4ac5-8e1b-c917a9ca9001)

### Submission Successful Page
![image](https://github.com/AzeemIdrisi/QR-Attendance-System/assets/112647789/0f77779e-7648-4356-84c0-7db58b3e786c)


## Contributions

We welcome contributions from the community! If you'd like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## Developers
Created by __Team Hokage__ during __Live The Code 2.0__ Hackathon.

Contributors : [Mohd Azeem](https://github.com/AzeemIdrisi), [Dheeraj Jha](https://github.com/Dheerajjha451), [Shantanu Pant](https://github.com/Shanty34)
