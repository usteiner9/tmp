"""address finding by regex."""
import re

content = """
Bobs Builders
Retail park
The Avenue
London
LDN 4DX"""
print(content)
postcodes = re.findall(r"(\w+)\s+([A-Z]{3} \d[A-Z]{2})", content)
print(postcodes)
