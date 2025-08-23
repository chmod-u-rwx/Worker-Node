from ..models.node import Node, NodeUpdates
from ..config import CORE_API_URI
import requests

class MetricService():
    
    def send_job_slots(self, job_slots: int):
        updates = NodeUpdates(job_slots=job_slots)
        return self.update_worker_node(updates)
    
    def send_resource_usage(self, cpu_usage: float, memory_usage: int, cache_usage: int):
        updates = NodeUpdates(cpu_usage=cpu_usage,
                              memory_usage=memory_usage,
                              cache_size_usage=cache_usage)
        return self.update_worker_node(updates)

    def send_resource_allocation(self, cpu_count_allocated: int, cpu_percentage_allocated: float, memory_allocated: int, cache_size_allocated: int) -> Node:
        updates = NodeUpdates(cpu_count_allocated=cpu_count_allocated,
                              cpu_percentage_allocated=cpu_percentage_allocated,
                              memory_allocated=memory_allocated,
                              cache_size_allocated=cache_size_allocated)
        return self.update_worker_node(updates)
   
    def update_worker_node(self, node_updates: NodeUpdates) -> Node:
        try:
            updates = node_updates.model_dump(exclude_unset=True, exclude_defaults=True, exclude_none=True)
            
            response = requests.post(f"{CORE_API_URI}/worker-node/update", json=updates)
            if response.status_code == 404:
                raise KeyError("Error while updating worker node: Worker node not found in db")
            elif response.status_code == 409 or response.status_code == 422:
                raise ValueError(f"Error while updating worker node: Invalid input: {response.status_code}")
            elif response.status_code != 200:
                raise RuntimeError(f"Error while updating worker node: Unexpected error HTTP: {response.status_code} {response.text}")

            return Node(**response.json())
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error while updating worker node: Request Error {str(e)}")
