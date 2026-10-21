# Drill 2
from pyscript import display, document

grade_seven = {
    'Kenneth Concepcion', 
    'Vita De Guzman', 
    'Franchesca Dela Rosa'}
grade_eight = {
    'Raver Estacio', 
    'Jia Hadji Gapor', 
    'Miguel Jimenez'}
grade_nine = {
    'Gurleen Kaur', 
    'MJ Madrelejos', 
    'Chalanie Lumbang'}
grade_ten = {
    'Destiny Reyes', 
    'Santiago Valdez', 
    'Jesse Villante'}
students = grade_seven | grade_eight | grade_nine| grade_ten #union (joins)

def new_member(e):
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    students.add(firstname + ' ' + lastname) #adds the new member
    document.getElementById("output").innerHTML = (f" Updated Members: {students} <br> Total Members: {len(students)}") #gets the number of students
    
    document.getElementById("output").innerHTML = (
        f"<p><b>Updated Members:</b></p>"
        f"<p>{'<br>'.join(sorted(students))}</p>"
        f"<p style='margin-top: 20px;'><b>Total Members:</b> {len(students)}</p>"
    )