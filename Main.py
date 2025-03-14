def setup_main_screen():
    # Create the main screen
    root.configure(bg="lightgray")

    Label(root, text="Welcome to the NCR Emergency Response Chatbot!", font=("Times New Roman", 28, "bold"), bg="lightgray").pack(pady=10)
    Label(root, text="How to use: Click on the type of emergency you are facing -> Provide the Information -> Submit",
          font=("Times New Roman", 20), bg="lightgray").pack()

    # Emergency Buttons
    Button(root, text="Police Emergency", font=("Times New Roman", 24, "bold"), width=70, height=5, fg='white', bg='red', command=lambda: show_emergency_form("Police")).pack(pady=30)
    Button(root, text="Hospital Emergency", font=("Times New Roman", 24, "bold"), width=70, height=5, fg='white', bg='blue', command=lambda: show_emergency_form("Hospital")).pack(pady=30)
    Button(root, text="Fire Emergency", font=("Times New Roman", 24, "bold"), width=70, height=5, fg='white', bg='orange', command=lambda: show_emergency_form("Fire")).pack(pady=30)

    Button(root, text="View Police Emergency History", font=("Times New Roman", 14), bg="gray", fg="white",
       width=30, height=2, command=lambda: view_history("police")).place(x=400, y=900)

    Button(root, text="View Hospital Emergency History", font=("Times New Roman", 14), bg="gray", fg="white",
       width=30, height=2, command=lambda: view_history("hospital")).place(x=800, y=900)  # Increased spacing

    Button(root, text="View Fire Emergency History", font=("Times New Roman", 14), bg="gray", fg="white",
       width=30, height=2, command=lambda: view_history("fire")).place(x=1200, y=900)  # Increased spacing
    if logged_in_user:
        Button(root, text="Logout", font=("Times New Roman", 14), bg="red", fg="white", width=30, command=logout).place(x=1550, y=10)
    else:
        Button(root, text="Login", font=("Times New Roman", 14), bg="gray", fg="white", width=15, command=login).place(x=1700, y=10)
        Button(root, text="Register", font=("Times New Roman", 14), bg="blue", fg="white", width=15, command=register).place(x=1550, y=10)
