class Solution(object):
    def generate(self, numRows):
        master = [[1],[1,1]]
        while len(master) < numRows:

            prev = master[-1]
            len_of_list = len(prev)
            temp_list = [1]

            for i in range(len_of_list-1):
                temp_list.append(prev[i] + prev[i+1])
            temp_list.append(1)
            master.append(temp_list)


        return master[:numRows]