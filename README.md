# Patient anonymity executable

Due to HIPAA laws, keeping patient data anonymous is crucial. Create a .exe or .py file that can be run in a folder along with the .xlsx file containing the patient data. This .exe or .py file should:
-remove all columns with identifying information
-give each patient an ID number

Then, create a reverse of this process, restoring the data with another .exe or .py file. 


To run:
- Install dependencies
- Run from terminal using the command
```
pip install requirements.txt
python3 remove.py
python3 restore.py
```