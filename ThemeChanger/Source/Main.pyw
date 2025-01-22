import os

themesPath = '../Themes/'
themes = os.listdir(themesPath)
themesAmount = len(themes)

currentThemeIdFile = open('CurrentThemeID')
currentThemeId = int(currentThemeIdFile.read())

currentThemeIdFile = open('CurrentThemeID', 'w')
currentThemeId += 1 if currentThemeId < themesAmount - 1 else -currentThemeId
currentThemeIdFile.write(str(currentThemeId))
currentThemeIdFile.close()
os.system(f'''powershell.exe "start '{themesPath+themes[currentThemeId]}' -WindowStyle Hidden"''')