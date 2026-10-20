from pyscript import document

club_members = ["Sean Lee", "Guia Suarez", "Loriz Santos", "Damien Francisco"]

def check_membership(e):
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()
    candidate_name = f"{first_name} {last_name}"
    
    is_member = candidate_name in club_members
    
    messages = [
        f"Sorry {candidate_name}, your name is not on the list.",
        f"Congratulations {candidate_name}! You are now part of the SS club."
    ]
    
    result_message = messages[is_member]
    
    document.getElementById("result-area").innerHTML = result_message