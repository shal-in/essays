import re

def validate_date_format(date_string):
    # Define the regular expression pattern for the date format YYYY-MM-DD
    pattern = r'^202[4]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    
    # Use the re.match function to check if the string matches the pattern
    if re.match(pattern, date_string):
        return True
    else:
        return False
    
def dynamic_type(dynamic):
    if validate_date_format(dynamic):
        return 'date'
    
    # elif

    else:
        return None

def convert_to_html(string):
    html_output = """"""

    paragraphs = string.split('\n\n')
    paragraph_i = 0

    for paragraph in paragraphs:
        content = """"""
        pattern = r'(<.*?>)'

        parts = re.split(pattern, paragraph)

        # Filter out empty parts
        parts = [part for part in parts if part]

        for part in parts:
            if part[0] == '<':
                cleaned_string = part.replace('<', '').replace('>', '')
                # Split the cleaned string at '*'
                cleaned_string = cleaned_string.split('*')

                data = cleaned_string[0]
                text = cleaned_string[1]

                data = data.split(' ')

                classes = []
                hyperlink = None
        
                for i in range(len(data)):
                    if data[i] == 'hyperlink':
                        classes.append(data[i])
                        hyperlink = data[i+1]
                        break
                    else:
                        classes.append(data[i])
                
                content += f"""<span class="{' '.join(classes)}" {hyperlink}>{text}</span>"""
            else:
                content += part

        html_output += f'<p id="essay-paragraph-{paragraph_i}" class="essay">{content}</p>'
        paragraph_i += 1

    return html_output
    