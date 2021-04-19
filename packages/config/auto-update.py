
import os
os.chdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\packages')
for package in os.listdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\packages'):
    if package.endswith('.json'):
        os.system(f'au update {package}')
os.system('git push -u origin master')
