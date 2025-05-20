def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('#'):
            title = line[1:].strip()  # Remove the '# ' and strip whitespace
            return title
    raise ValueError("No h1 header found in the Markdown file.")
