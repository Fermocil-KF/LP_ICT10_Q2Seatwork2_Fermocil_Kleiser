from pyscript import document

def compute_grade(event):

    # 1. Get input values (grades and name)
    try:
        # Get grades and convert them to floats
        science = float(document.getElementById('science').value)
        english = float(document.getElementById('english').value)
        ict = float(document.getElementById('ict').value)
        math = float(document.getElementById('math').value)
        filipino = float(document.getElementById('filipino').value)
        pe = float(document.getElementById('pe').value)
        
        # Get student name
        first_name = document.getElementById('firstNameInput').value
        last_name = document.getElementById('lastNameInput').value
        
    except ValueError:
        # Handle cases where input fields are empty or not valid numbers
        document.getElementById('show1').innerText = "!Please enter valid numerical grades for all subjects!"
        document.getElementById('show2').innerText = ""
        document.getElementById('average').innerText = ""
        document.getElementById('show').innerText = ""
        return

    # 2. Calculate the average
    total_subjects = 6
    average_grade = (science + english + ict + math + filipino + pe) / total_subjects
        
    # Format the name
    full_name = f"{first_name.capitalize()} {last_name.capitalize()}" if first_name and last_name else "Student"

    # 3. Display the results in the HTML elements
    document.getElementById('output1').innerText = f"Science: {science}"
    document.getElementById('output2').innerText = f"English: {english}"
    document.getElementById('output3').innerText = f"ICT: {ict}"
    document.getElementById('output4').innerText = f"Math: {math}"
    document.getElementById('output5').innerText = f"Filipino: {filipino}"
    document.getElementById('output6').innerText = f"PE: {pe}"
    
    # Display final results
    document.getElementById('show1').innerText = f"Student Name: {full_name}"
    document.getElementById('average').innerText = f"Overall Average: {average_grade:.2f}"