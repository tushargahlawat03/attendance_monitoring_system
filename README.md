# attendance_monitoring_system
This is a simple Python-based Attendance Management System that records attendance for multiple persons over multiple days based on their in-time and out-time.


📌 Attendance Management System (Python)
📖 Description

This is a simple Python-based Attendance Management System that records attendance for multiple persons over multiple days based on their in-time and out-time.

The program:

Takes input for 2 persons

Records attendance for 7 days each

Classifies attendance into:

✅ Present

⏰ Late

🕒 Short Day

🌓 Half Day

❌ Absent

Displays total attendance summary at the end.

🚀 How It Works

For each person and each day:

User enters:

In Time

Out Time

The system checks conditions:

If a <= 8 and b >= 17 → Present

If a <= 10 and b >= 17 → Late

If early leave conditions → Short Day

If partial working hours → Half Day

Otherwise → Absent

Totals are calculated and displayed at the end.

🛠 Technologies Used

Python 3

Basic loops (for)

Conditional statements (if-elif-else)

Counters

🎯 Features

Multiple persons support

Weekly attendance tracking

Automatic classification

Simple and beginner-friendly logic

Console-based interaction

