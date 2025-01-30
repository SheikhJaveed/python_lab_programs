def subject_operations():
    subjects = ["Math", "Physics", "Chemistry", "Python Programming Lab", "Data Structures"]
    
    # Display using for loop
    for subject in subjects:
        print(subject)
    
    # Display 2nd and 5th element
    print(subjects[1], subjects[4])
    
    # Display first 4 elements
    print(subjects[:4])
    
    # Display last 4 elements
    print(subjects[-4:])
    
    # Check if a subject is available
    print("Python Programming Lab" in subjects)
    
    # Demonstrate append() and insert()
    subjects.append("AI")
    subjects.insert(2, "Machine Learning")
    print(subjects)
    
    # Demonstrate remove() and pop()
    subjects.remove("Physics")
    subjects.pop()
    print(subjects)

subject_operations()
