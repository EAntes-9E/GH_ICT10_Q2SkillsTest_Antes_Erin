from pyscript import display, document


clubs = {
{ 
    Club Name: "Communications Art"
 Description: "The Communications Art Club focuses on enhancing students' skills in various forms of communication, including writing, public speaking, and digital media. Members participate in workshops, competitions, and collaborative projects to develop their abilities and express their creativity."
 Meeting Time: "Friday at 2:30 PM"
 Location: "Room 101"
 Club Moderator: "Mr. Loreto"
 Number of Members: "40"
}
{
    Club Name: "Social Science"
 Description: "The Social Science Club is dedicated to exploring the various aspects of human society and social relationships. Members engage in discussions, research projects, and community service activities that promote understanding of social issues and encourage civic engagement."
 Meeting Time: "Tuesday at 2:15 PM"
 Location: "Room 703"
 Club Moderator: "Ms. Libramonte"
 Number of Members: "19"
}
{
    Club Name: "Science Club"
 Description: "The Science Club aims to foster a love for science and scientific inquiry among students. Members participate in experiments, science fairs, and field trips to explore different scientific disciplines and stay updated on the latest scientific discoveries."
 Meeting Time: "Tuesday at 2:30 PM"
 Location: "Highschool Laboratory"
 Club Moderator: "Mr. Calpo"
 Number of Members: "20"

}
}

def display_club_info(club_name):
    club_info = clubs.get(club_name, None)
        club_info:
        info = (
            f"Club Name: {club_info['Club Name']}\n"
            f"Description: {club_info['Description']}\n"
            f"Meeting Time: {club_info['Meeting Time']}\n"
            f"Location: {club_info['Location']}\n"
            f"Club Moderator: {club_info['Club Moderator']}\n"
            f"Number of Members: {club_info['Number of Members']}"
        )
        display(info, target="result")
   
