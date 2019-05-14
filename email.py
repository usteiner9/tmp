"""email finding by regex."""
import re

abc = """
guru99@google.com, careerguru99@hotmail.com, usteiner@munichre.com"""

emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:

    print(email)
