class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        #helper to find distance between points
        def distance(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

        distances  =[distance(p1,p2), distance(p1,p3), distance(p1,p4), 
                    distance(p2,p3), distance(p2,p4), distance(p3,p4)]
        distances.sort()

        state_1 = (distances[0]==distances[1]==distances[2]==distances[3])
        state_2 = (distances[4]==distances[5])
        state_3 = distances[0] > 0

        return state_1 and state_2 and state_3