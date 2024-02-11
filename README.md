# Mcwics-Face-merger-Machine
## How to run
Note - This project uses float32 over CPU, and float16 over over GPU, that may hinder with local PC performance

1. `git clone https://github.com/Saraaaaaad/Mcwics-Face-merger-Machine.git`
2. `cd Mcwics-Face-merger-Machine`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `python3 -m pip install fastapi streamlit streamlit_lottie accelerate diffusers uvicorn accelerator transformers`
6. `python3 -m streamlit run main.py`
