class Solution(object):
    def capitalizeTitle(self, title):
        title = title.lower()
        title = title.split(' ')

        for i in range(len(title)):
            if len(title[i]) > 2:
                title[i] = (title[i]).capitalize()

        title = ' '.join(title)
        return str(title)