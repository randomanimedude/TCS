FROM python:3

COPY readDOCX.py /
COPY DockerBasics.docx /

RUN pip install flask python-docx

CMD ["python", "./readDOCX.py" ]
