from datetime import datetime

class StatusService:
    def get_status(self):
        return {
            "status": "running",
            "message": "Smart Doc Processing API is up and running!",
            "timestamp": datetime.now().isoformat()
        }