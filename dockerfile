FROM python 

WORKDIR .

COPY programa.py .

CMD ["python", "programa.py"]
