from typing import Union
import mysql.connector
from mysql.connector import Error


class DbSend:
    def __init__(self) -> None:
        try:
            self.mydb = mysql.connector.connect(
                host="localhost", user="root", password="", database="biometric"
            )
            self.cursor = self.mydb.cursor()
            print("Connected to MySQL")
        except Error as e:
            print("Error connecting to MySQL:", e)
            self.mydb = None

    def check_username_exist(self, username: str) -> Union[bool, int]:
        if not self.mydb:
            print("No database connection")
            return -2
        try:
            sql = "SELECT * FROM doctors WHERE username = %s"
            self.cursor.execute(sql, (username,))
            result = self.cursor.fetchone()
            return bool(result)
        except Error as e:
            print("Error checking username existence:", e)
            return False

    def insert_user(self, username: str, password: str, fullname: str) -> None:
        if not self.mydb:
            print("No database connection")
            return -2
        try:
            sql = (
                "INSERT INTO doctors (username, password, fullname) VALUES (%s, %s, %s)"
            )
            val = (username, password, fullname)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            print("User inserted successfully")
        except Error as e:
            print("Error inserting user:", e)

    def check_user_credentials(self, username: str, password: str) -> Union[bool, int]:
        if not self.mydb:
            print("No database connection")
            return -2
        try:
            sql = "SELECT * FROM doctors WHERE username = %s AND password = %s"
            self.cursor.execute(sql, (username, password))
            result = self.cursor.fetchone()
            return bool(result)
        except Error as e:
            print("Error checking user credentials:", e)
            return False

    def insert_patient(
        self, first_name: str, last_name: str, hospital_number: int, phone_number: int
    ) -> Union[bool, int]:
        """Insert a new patient into the database"""
        if not self.mydb:
            print("No database connection")
            return -2
        try:
            sql = "INSERT INTO patients (firstname, lastname, hospital_no, phone) VALUES (%s, %s, %s, %s)"
            val = (first_name, last_name, hospital_number, phone_number)
            self.cursor.execute(sql, val)
            self.mydb.commit()
            print("Patient inserted successfully")
            return True
        except Error as e:
            print("Error inserting patient:", e)
            return -1

    def fetch_patient_list(self):
        """Fetches the list of patients from the database"""
        if not self.mydb:
            print("No database connection")
            return []

        try:
            sql = "SELECT * FROM patients"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print("Error fetching patient list:", e)
            return []

    def check_patients_exist(self, phone: int) -> Union[bool, int]:
        if not self.mydb:
            print("No database connection")
            return -2
        try:
            sql = "SELECT * FROM patients WHERE phone = %s"
            self.cursor.execute(sql, (phone,))
            result = self.cursor.fetchone()
            return bool(result)
        except Error as e:
            print("Error checking Phone existence:", e)
            return False
