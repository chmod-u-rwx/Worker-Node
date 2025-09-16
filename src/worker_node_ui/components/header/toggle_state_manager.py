class ToggleStateManager:
    _checked = True 
    _listeners = []

    @classmethod
    def set_state(cls, value: bool):
        cls._checked = value
        for callback in cls._listeners:
            callback(value)

    @classmethod
    def get_state(cls):
        return cls._checked

    @classmethod
    def register_listener(cls, callback):
        cls._listeners.append(callback)
