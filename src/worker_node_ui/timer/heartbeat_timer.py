from PySide6.QtCore import QTimer
import uuid
import httpx

class HeartbeatTimer:
    _instance =  None
    def  __new__(cls, url:str, interval_ms:int = 1000):
        if cls._instance is None:
            cls._instance = super(HeartbeatTimer, cls).__new__(cls)
        return cls._instance

    def __init__(self, url:str, interval_ms:int = 1000):
        if hasattr(self, "_init") and self._init:
            return
        self.websocket_url = url
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_heartbeat)
        self.timer.setInterval(interval_ms)
        self._init = True

    def send_heartbeat(self):
        # hardcode daw muna sabi ni emil
        worker = {
        "worker_id": str(uuid.uuid4()),
        "master_id": str(uuid.uuid4()),
        "cpu": 2,
        "memory": 250,
        "job_slot": 1,
        "status": "STARTED",
        "code_runtime": 1.0,
        "latency": 0.18,
        "job_cache": []
        }

        try:
            httpx.post(self.websocket_url, json=worker, timeout=10)
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