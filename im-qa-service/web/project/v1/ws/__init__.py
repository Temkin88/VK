from typing import List, Optional

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from starlette.responses import FileResponse

ws_router = APIRouter(prefix='/ws')


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, except_ws: Optional[WebSocket] = None):
        for connection in filter(
                lambda x: x != except_ws,
                self.active_connections
        ):
            await connection.send_text(message)


manager = ConnectionManager()


@ws_router.get('/')
async def index():
    return FileResponse('project/v1/ws/static/index.html')


@ws_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(
                f"Client #{client_id} says: {data}",
                websocket
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
