# 💬 Python Chat Application (Client-Server)

A simple **real-time multi-user chat application** built using Python.
This project uses **socket programming and multithreading** to enable communication between multiple clients through a central server.


## 📌 Features

* 💬 Real-time messaging
* 👥 Multiple users can chat simultaneously
* 🧵 Multithreaded server
* 🏷️ Custom usernames
* ⏱️ Timestamped messages
* 📢 Join/leave notifications
* 📋 Commands:

  * `/users` → Show online users
  * `/quit` → Exit chat
* ❌ Handles disconnections gracefully

---



##  Project Structure

```bash
.
├── server.py   # Chat server
├── client.py   # Chat client
└── README.md
```

---

## ▶️ How to Run

###  Start Server

Open terminal and run:

```bash
python server.py
```

You should see:

```
✅ Server started on 127.0.0.1:5555
✅ Waiting for clients...
```

---

###  Start Client(s)

Open **one or more terminals** and run:

```bash
python client.py
```

---

###  Join Chat

* Enter your username
* Start chatting 🎉

---

##  Example

```
[12:00:01] Alice joined the chat 👋
[12:00:05] Bob joined the chat 👋

💬 [12:00:10] Alice: Hello!
💬 [12:00:12] Bob: Hi!
```

---

## 📋 Commands

| Command | Description       |
| ------- | ----------------- |
| /users  | Show online users |
| /quit   | Leave chat        |

---

## ⚙️ Configuration

In both files:

```python
HOST = "127.0.0.1"
PORT = 5555
```

### Notes:

* Use `127.0.0.1` → same computer
* Use your local IP → allow others on same network

---

## 🧠 How It Works

###  Server

* Accepts client connections
* Stores active users
* Broadcasts messages
* Handles commands
* Removes disconnected users

###  Client

* Connects to server
* Sends messages
* Receives messages in background thread

---

##  Limitations

* No encryption
* No private messaging
* No chat history
* Local network only



##  Future Improvements

* 🔐 Encryption (SSL/TLS)
* 🌐 Internet support
* 💬 Private messaging
* 🖼️ GUI version
* 🗂️ Message history
* 👤 Login system


---
