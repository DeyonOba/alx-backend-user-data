#!/usr/bin/env python3

"""
Query content in database
"""
import sqlite3
import requests

con = sqlite3.connect("a.db")
cur = con.cursor()

email="bob@bob.com"
password="mySuperPwd"

s = requests.Session()
r = s.post(
    "http://127.0.0.1:5000/users",
    data={"email": email, "password": password}
)
print("Create new user")
print(r.text)

r = s.post(
    "http://127.0.0.1:5000/sessions",
    data={"email": email, "password": password}
)
print("Created new session")
print(r.cookies.get("session_id"))

for obj in cur.execute("SELECT * FROM users"):
    print(obj)

r = s.get("http://127.0.0.1:5000/profile", cookies={"session_id": r.cookies.get("session_id")})
print(r.json())

r = s.delete("http://127.0.0.1:5000/sessions", cookies={"session_id": r.cookies.get("session_id")})
print(r.json())
print(cur.execute("SELECT * FROM users").fetchone())
