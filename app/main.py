from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import asyncio
import os



app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "../static/CEI-EWP_2025_02920.pdf")
# CEI-EWP/2025/02920
#CEI-EWP_2025_02920.pdf
#https://eodb-assam-gov-in.up.railway.app/eslive/t/ctxrFFZC93PP

#CEI-EWP/2025/02920                    https://eodb-assam-gov-in.up.railway.app/eslive/t/ctxrFFZC93PP

@app.get("/eslive/t/ctxrFFZC93PP")
async def download():
	try:

		doc_path = "static/CEI-EWP_2025_02920.pdf"

		return FileResponse(doc_path, media_type="application/pdf", filename="CEI-EWP_2025_02920.pdf")

	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
