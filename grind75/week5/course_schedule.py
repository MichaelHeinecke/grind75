from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_mapping = defaultdict(set)
        for course, prereq in prerequisites:
            prereq_mapping[course].add(prereq)
        visited = set()

        def dfs(course: int) -> bool:
            if not prereq_mapping[course]:
                return True

            if course in visited:
                return False

            visited.add(course)

            for req in prereq_mapping[course]:
                if not dfs(req):
                    return False

            visited.remove(course)
            prereq_mapping[course] = set()
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
