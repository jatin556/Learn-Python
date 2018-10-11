#OOPR-Assgn-13
class Classroom:
    classroom_list = []
#     def __init__(self):
#         pass
    
    @staticmethod
    def search_classroom(class_room):
        if class_room.lower() in Classroom.classroom_list:
            return "found"
        elif class_room.upper() in Classroom.classroom_list:
            return "found"
        else:
            return -1
