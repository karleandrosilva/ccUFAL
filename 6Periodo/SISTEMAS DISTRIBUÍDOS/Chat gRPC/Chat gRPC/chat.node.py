"""
chat_node.py - Chat P2P com gRPC

Uso:
    python chat.node.py Washington 100200 localhost:200100
    python chat.node.py Karleandro 200100 localhost:100200
"""

import sys
import threading
# import time
from datetime import datetime
from concurrent import futures

import grpc
import chat_pb2
import chat_pb2_grpc


class ChatServiceServicer(chat_pb2_grpc.ChatServiceServicer):
    """Servidor que recebe mensagens."""
    
    def __init__(self, name):
        self.name = name

    def SendMessage(self, request, context):
        """Recebe mensagem unária."""
        print(f"\n[{request.timestamp}] {request.sender}: {request.content}")
        print("Você> ", end="", flush=True)
        return chat_pb2.Ack(received=True)

    def Chat(self, request_iterator, context):
        """Recebe stream de mensagens."""
        for msg in request_iterator:
            print(f"\n[{msg.timestamp}] {msg.sender}: {msg.content}")
            print("Você> ", end="", flush=True)
            yield chat_pb2.ChatMessage(sender="[ok]", content="", timestamp="")


def start_server(name, port):
    """Inicia servidor gRPC."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatServiceServicer(name), server
    )
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"[Servidor] {name} na porta {port}")
    return server


def send_messages(name, peer_address):
    """Thread que envia mensagens para o peer."""
    channel = grpc.insecure_channel(peer_address)
    stub = chat_pb2_grpc.ChatServiceStub(channel)
    
    # Aguarda conexão
    print(f"Conectando a {peer_address}...", end="", flush=True)
    for _ in range(30):
        try:
            grpc.channel_ready_future(channel).result(timeout=1)
            print(" OK!\n")
            break
        except grpc.FutureTimeoutError:
            print(".", end="", flush=True)
    
    print("Você> ", end="", flush=True)
    
    while True:
        try:
            text = input()
            if text.lower() in ("/sair", "/exit"):
                break
            if text.strip():
                msg = chat_pb2.ChatMessage(
                    sender=name,
                    content=text,
                    timestamp=datetime.now().strftime("%H:%M:%S"),
                )
                stub.SendMessage(msg)
            print("Você> ", end="", flush=True)
        except (EOFError, KeyboardInterrupt):
            break


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    name = sys.argv[1]
    port = int(sys.argv[2])
    peer = sys.argv[3]

    server = start_server(name, port)
    
    t = threading.Thread(target=send_messages, args=(name, peer), daemon=True)
    t.start()

    try:
        t.join()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nFim!")
        server.stop(grace=1)


if __name__ == "__main__":
    main()