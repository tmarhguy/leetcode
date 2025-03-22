class Solution(object):
    def plusOne(self, digits):
        return (list(map(int,str(int((''.join(map(str,digits)))) + 1))))
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        