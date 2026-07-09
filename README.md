# SQMS

## Smart Queue Management System

---

### Introduction

With the increasing number of visitors to service centers such as banks, clinics, universities, and government organizations, proper queue management and ticketing has become one of the major challenges for these centers. Traditional ticketing methods often lead to congestion, increased waiting times, and user dissatisfaction.

The use of intelligent queue management systems can significantly improve service quality by better organizing the ticketing process, reducing waiting times, and providing accurate information to visitors.

---

### Problem Definition

In many service centers, visitors do not have accurate information about the queue status and their approximate waiting time. This leads to congestion, wasted time, and reduced user satisfaction.

On the other hand, staff members also lack proper tools to manage queues and control the service delivery process. Therefore, there is a need for a system that can intelligently and systematically handle the ticketing and queue management process.

---

### Project Objectives

The main objectives of this project are:

1. **Reduce visitor waiting time**
2. **Organized queue management**
3. **Increase user satisfaction**
4. **Reduce congestion in service environments**
5. **Provide accurate information about queue status**
6. **Enable management reporting**
7. **Increase operator productivity**

---

### Project Scope

The Smart Queue Management System provides the following capabilities:

- **Ticket request registration** by users
- **Automatic ticket number generation**
- **Display of number of people** currently in queue
- **Display of estimated waiting time**
- **Next ticket call** by operator
- **Ticket rejection or cancellation**
- **Service completion registration**
- **Statistical report generation**

This project is implemented as a web-based system using **Django** for the backend and **HTML/CSS/JavaScript** for the frontend.

---

### Project Stakeholders

The main stakeholders of this project are:

| Stakeholder | Description |
|-------------|-------------|
| **Users** | Individuals who enter the system to receive services and need to obtain a ticket |
| **Operators** | Staff responsible for managing queues and providing services to users |
| **System Administrator** | Person who monitors system performance and reviews management reports |
| **User Organization** | The service center that uses the queue management system to increase efficiency and customer satisfaction |

---

### Project Benefits

Implementing a Smart Queue Management System offers numerous benefits, including:

- **Reduced congestion**
- **Increased order in the ticketing process**
- **Improved user experience**
- **Reduced workload on operators**
- **Ability to statistically analyze system performance**
- **Future extensibility**

---

### System Testing Results

| # | Test | Expected Result | Result |
|---|------|-----------------|--------|
| 1 | Ticket Registration | Ticket Created | **Passed** |
| 2 | View Status | Display Information | **Passed** |
| 3 | Call Next Person | Status Change | **Passed** |
| 4 | Admin Authentication | Panel Access if Correct | **Passed** |
| 5 | Report Generation | View Reports | **Passed** |

---

### Conclusion

Given the issues present in traditional ticketing methods, developing a Smart Queue Management System can be an appropriate solution for improving service quality and increasing user satisfaction. This project has been defined with the aim of designing and implementing such a system, and the phases of analysis, design, development, and management have been reviewed accordingly.

All main system features have been successfully tested, and the results met expectations.

---

### Technology Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite / PostgreSQL
- **Authentication:** Django's built-in authentication system

---

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/queue-management-system.git

# Navigate to project directory
cd queue-management-system

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

---

### License

This project is licensed under the MIT License.

---

### Contact

For any inquiries or support, please contact the project team.
