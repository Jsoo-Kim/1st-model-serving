# 서버 구동

import uvicorn
import app
if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=9999, log_level="debug",
                proxy_headers=True, reload=True)