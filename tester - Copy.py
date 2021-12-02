import HelperFunctions
from HelperFunctions import Mouse
import pytesseract
import time

mouse = Mouse()
enemyPosition = [0,0,0]
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR'

def pyroBot():
    while True:
        enemyPosition = HelperFunctions.getEnemyPosition()
        if enemyPosition[2] == 1:
            codexReady = HelperFunctions.isCodexready()
            if codexReady[2] == 1:
                # First stun hero
                HelperFunctions.pressKey('w')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.4)
                # Flammepust
                HelperFunctions.pressKey('q')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.2)
                # Codex i tryne
                mouse.rightClick(codexReady[0],codexReady[1])
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.1)
                # Ulti i tryne
                HelperFunctions.pressKey('r')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])


def witchBot():
    while True:
        enemyPosition = HelperFunctions.getEnemyPosition()
        if enemyPosition[2] == 1:
            codexReady = HelperFunctions.isCodexready()
            if codexReady[2] == 1:
                # First stun hero
                HelperFunctions.pressKey('q')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.4)
                # Flammepust
                HelperFunctions.pressKey('r')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.2)
                # Codex i tryne
                mouse.rightClick(codexReady[0],codexReady[1])
                mouse.rightClick(enemyPosition[0],enemyPosition[1])
                time.sleep(0.6)
                # Ulti i tryne
                HelperFunctions.pressKey('w')
                mouse.rightClick(enemyPosition[0],enemyPosition[1])


if __name__ == "__main__":
    #pyroBot()
    witchBot()