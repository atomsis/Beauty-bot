# Дисклеймер - не особо понимаю как нужна дать: в формате питон файла или текстового? Сделаю ответ как пришло в голову 😂

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions_for_webh import function1, function2

# мы также ещё добавим логирование всяких ошибок и тд
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

function_mapping = {
    "function1": function1,
    "function2": function2,
}


class Webhook(BaseModel):
    function: str
    data: dict


@app.post("/Datalore")
async def datalore_webhook(request: Webhook):
    try:
        func_name = request.function

        if func_name not in function_mapping:
            logging.warning(f"Unknown function '{func_name}' requested")
            raise HTTPException(status_code=400, detail=f"Unknown function '{func_name}'")

        result = function_mapping[func_name](request.data)
        return result
    except Exception as e:
        logging.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
