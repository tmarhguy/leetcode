class Solution(object):
    def convertTemperature(self, celsius):
        #conversion into Kelvin
        return [celsius + 273.15, celsius * 1.8 + 32.0]
        
        
        
        
        """
        :type celsius: float
        :rtype: List[float]
        """
        