from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


#schemas
# from schemas import TranslationRequest
import schemas





app = FastAPI()

# setup for jinja2 templates 
templates = Jinja2Templates(directory="templates")

#enable cors 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_model=schemas.TranslationRequest):
def result(self):
    pass