class NotificationManager:
    _notifications: list[str] = []
    _handlers = []
    _has_unread = False

    @classmethod
    def register_handler(cls, handler):
        if handler not in cls._handlers:
            cls._handlers.append(handler)
        handler.update_notifications(cls._notifications, cls._has_unread)

    @classmethod
    def add_notification(cls, text: str):
        cls._notifications.append(text)
        cls._has_unread = True
        cls._broadcast()

    @classmethod
    def mark_all_as_read(cls):
        cls._has_unread = False
        cls._broadcast()

    @classmethod
    def _broadcast(cls):
        for handler in cls._handlers:
            handler.update_notifications(cls._notifications, cls._has_unread)
