from setuptools import find_packages,setup
from typing import List


def git_requirements()->List[str]:
    '''
    This function will return a list of requirement.txt
    '''
    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace characters and append to the list
                requirement_list.append(line.strip())
    except FileNotFoundError:
        print("The requirements.txt file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    return requirement_list


setup(
    name = "sensor",
    version = "0.0.1",
    author="Prashant yadav",
    author_email="fprashantyadav@gmail.com",
    packages = find_packages(),
    install_requires=git_requirements(),#['pymongo == 4.2.0'],
)

'''
 run this 'python setup.py install' in cmd to create your own package so that you can share your code with others.
 but if you use -e . in your requirement.txt file it you dont need to use this python setup.py install you can 
 directly use pip install -r requirements.txt because -e is same as find_packages().
 '''