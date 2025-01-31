# Press Shift+Enter to run the code
import logging


class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

    analyzer = TextAnalyzer(givenstring)
    logging.info(f"Frequency map: {analyzer.freqAll()}")
    logging.info(f"Frequency map: {analyzer.freqOf('et')}")
    logging.info(f"Frequency map: {analyzer.freqOf('diam')}")
