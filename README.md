# 🏦 Bank Management System

A full-featured **Bank Management System** built to simulate core banking functionalities such as account creation, deposits, withdrawals, loan management, and administrative oversight. This system supports two user roles: **User** and **Admin**, each with their own set of capabilities.

---

## ✨ Features

### 👤 User Features

- ✅ Create a bank account
- 💰 Deposit and withdraw money (only if the user has sufficient balance)
- 📊 View available balance
- 📜 Access full transaction history
- 🏦 Request a loan (up to **3 times**)
- 📝 Update profile information

> ⚠️ Users can only withdraw or transfer money if their account balance is sufficient.

---

### 🛠️ Admin Features

- ✅ Create an admin account
- 🧾 View and approve/reject loan requests

---


---

## ⚙️ Tech Stack

- **Backend**: Node.js / Express / Django / (Choose your backend stack)
- **Frontend**: React / Vue / HTML-CSS-JS (Optional)
- **Database**: MongoDB / MySQL / PostgreSQL
- **Authentication**: JWT / Session-based login

---

## 🚀 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/jabedhosenn/bank-management-system.git <br>
cd bank-management-system

---

### 2. Install Dependencies
## Backend

cd backend
npm install  # or pip install -r requirements.txt for Django

## Frontend (if applicable)

cd frontend
npm install

---

### 3. Run the Application

# Run backend
npm start  # or python manage.py runserver

# Run frontend (in another terminal)
npm run dev

---

## 🧪 Test Accounts
User: user@example.com / password123

Admin: admin@example.com / adminpass

## ✅ Future Enhancements
Transaction filters (date range, type)

Email notifications for transactions and loan approvals

Two-factor authentication

Transfer funds between users

## 📄 License
This project is licensed under the MIT License.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.
