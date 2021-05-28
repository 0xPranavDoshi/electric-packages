import os
os.chdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\packages')
for package in os.listdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\packages'):
    print(package)
    if package.endswith('.json'):
        os.system(f'au update {package}')
    os.system('git add .')
    os.system(f'git commit -m "Updated {package} to Latest Version"')

os.system('git add .')
os.system('git commit -m "Updated Packages"')
os.system('git push -u origin master')
