class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if not sandwiches:
                break
            if students[0] != sandwiches[0]:
                if sandwiches[0] not in students:
                    break
                students += [students[0]]
                students.pop(0)
            else:
                sandwiches.pop(0)
                students.pop(0)
        return len(students)
