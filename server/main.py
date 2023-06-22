from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from function5 import func5
import sentry_sdk

# @sentry_sdk.trace
def func1():
    return "func1"

# @sentry_sdk.trace
def func2():
    return "func2"

# @sentry_sdk.trace
def func3():
    return "func3"

def func4():
    return "func4"


# functions_to_trace = [
#     {"qualified_name": "main.func1"},
#     {"qualified_name": "main.func2"},
#     {"qualified_name": "main.func3"},
#     {"qualified_name": "main.func4"},
# ]





sentry_sdk.init(
    dsn="https://c200cb512f43423eb20731b14bd43640@o1407376.ingest.sentry.io/4504091267497984",
    traces_sample_rate=1.0,
    debug=True,
#     functions_to_trace=[
#     {"qualified_name": "main.func1"},
#     {"qualified_name": "main.func2"},
#     {"qualified_name": "main.func3"},
#     {"qualified_name": "main.func4"},
#     {"qualified_name": "function5.func5"}
# ],
    # functions_to_trace=functions_to_trace
)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/food")
async def food():
    return {"message": ["apple", "pizza", "candy", "burger"] }

@app.get("/error")
async def error():
    raise ReferenceError("TestingError")

@app.get("/Valueerr")
async def vel():
    raise ValueError('value')

@app.get("/testing")
async def test():
    return templates.template()

@app.get("/func")
async def func():
    return func2() + func3() + func4() + func1() + func5()

@app.get("/func_two")
async def func_two():
    return func6()

@app.get("/valueA")
async def a():
    print(a)
    return a
