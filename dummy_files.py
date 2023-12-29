extensions = ['jpg', 'mp3', 'mp4', 'pdf', 'docx', 'png', 'py']

# CREATING DUMMY FILES FOR SORTING
for index, ext in enumerate(extensions):
    with open(f'{index}.{ext}', 'w') as f:
        pass
