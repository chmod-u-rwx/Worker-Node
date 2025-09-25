from PySide6.QtCore import QTimer
from uuid import UUID
import httpx

class HeartbeatTimer:
    _instance =  None
    def  __new__(cls, url:str, worker_id: UUID, master_id: UUID, interval_ms:int = 3000):
        if cls._instance is None:
            cls._instance = super(HeartbeatTimer, cls).__new__(cls)
        return cls._instance

    def __init__(self, url:str, worker_id: UUID, master_id: UUID, interval_ms:int = 3000, ):
        if hasattr(self, "_init") and self._init:
            return
        self.websocket_url = url
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_heartbeat)
        self.timer.setInterval(interval_ms)
        self._init = True
        self.worker_id = str(worker_id)
        self.master_id = str(master_id)

    def send_heartbeat(self):
        # hardcode daw muna sabi ni emil
        worker = {
        "worker_id": self.worker_id,
        "master_id": self.master_id,
        "cpu": 2,
        "memory": 250,
        "job_slot": 1,
        "status": "STARTED",
        "code_runtime": 1.0,
        "latency": 0.18,
        "job_cache": []
        }

        try:
           print("sending to: ", f"{self.websocket_url}/heartbeat/")
           httpx.post(f"{self.websocket_url}/heartbeat/", json=worker, timeout=10)
           print("sent successfully\n")
        except Exception as e:
            raise Exception(f"Error occured when sending heartbeat: {e}")
    
    def start_timer(self):
        try:
            if not self.timer.isActive():
                self.timer.start()
            else:
                raise RuntimeError("Start timer is already running")
        except Exception as e:
            raise Exception(f"Something went wrong when running the timer {e}")
        
    def stop_timer(self):
        try:
            if self.timer.isActive():
                self.timer.stop()
            else:
                raise RuntimeError("Start timer has already stopped")
        except Exception as e:
            raise Exception(f"Something went wrong when stopping the timer {e}")