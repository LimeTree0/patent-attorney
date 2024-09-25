사용 방법

1. ollama를 설치한다.
url : https://ollama.com/

2. huggingface에서 모델을 다운받는다.

    url : https://huggingface.co/limecoding/gemma2-2b-it-finetuned-patent/tree/main

    모델은 gguf로 된 모델을 다운받는다.

    Q4, Q8은 가볍지만 성능이 F16에 비해 상대적으로 떨어질 수 있다.
    
    자원의 상황을 고려해서 다운받는다.

3. Modelfile 만든다. 파일 이름은 Modelfile로 한다. FROM은 gguf 파일 경로를 적어준다.
```
FROM gemma2-2-it-h.Q8_0.gguf

TEMPLATE """<bos><start_of_turn>user
다음 과제해결수단을 보고 발명의 명칭, 기술분야, 청구항을 뽑아주세요.: {{.Prompt}}<end_of_turn> 
<start_of_turn>model"""

PARAMETER temperature 0
PARAMETER num_predict 3000
PARAMETER num_ctx 4096
PARAMETER stop <s>
PARAMETER stop </s>
```

4. ollama에 모델을 등록한다. ollama create <등록할 이름> -f <Modelfile 파일 경로>
```
ollama create gemma2-2-it-h.Q8_0 -f Modelfile
```

5. 파이썬 가상 환경을 만든다.
```
python -m venv 가상환경이름
```

6. 가상환경을 실행하고 streamlit과 ollama를 설치한다
```
pip install -r requirements.txt
```

7. app.py에서 등록한 모델 이름을 바꾼다.
```
response = ollama.generate(model='ollama에 등록한 모델 이름', prompt=prompt, stream=True)
```

8. app.py를 실행한다.
```
streamlit run app.py
```