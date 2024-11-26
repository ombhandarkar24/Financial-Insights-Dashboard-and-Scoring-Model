from setuptools import find_packages,setup
from typing import List
'''
This function will return the list of requiremets
'''
Hypen_E_Dot = "-e ."
def get_requirements(file_path:str )->List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]
        if Hypen_E_Dot in requirement:
            requirement.remove(Hypen_E_Dot)
            
    return requirement
    
    
   
    
    
setup(
    name = 'Ml project',
    version = '0.0.1',
    author = 'om',
    author_email = 'ombhandarkar516@gmail.com',
    packages = find_packages(),
    install_requires =  get_requirements('requirements.txt')  
    
)