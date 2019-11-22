# String Interpolation

name = 'Kristine'
greeting = f'hi {name}'
print(greeting)

# heredoc
name = 'kristine'      #variable name
product = 'Python elearning course'  #variable product
# below is set to a heredoc with the """ after the format flag (f)
email_content = f"""  
hi {name} 

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(email_content)
