FROM pytorch/pytorch

WORKDIR /DigitClassifier

COPY ./requirements.txt /DigitClassifier/requirements.txt

RUN pip install --no-cache-dir -r /DigitClassifier/requirements.txt

COPY ./main.py /DigitClassifier/main.py

COPY ./database.py /DigitClassifier/database.py

COPY ./classifier.py /DigitClassifier/classifier.py

COPY ./model /DigitClassifier/model

CMD python database.py

CMD streamlit run main.py --server.port=8501 --server.address=0.0.0.0