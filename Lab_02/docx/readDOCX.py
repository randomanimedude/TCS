import docx

doc = docx.Document("DockerBasics.docx")

all_paras = doc.paragraphs

for para in all_paras:
    print(para.text)
