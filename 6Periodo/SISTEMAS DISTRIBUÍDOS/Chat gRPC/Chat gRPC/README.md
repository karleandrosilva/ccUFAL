# Chat gRPC - Peer-to-Peer

Chat descentralizado usando gRPC em Python. Mensagens enviadas e recebidas simultaneamente com threads.

## Instalação

```bash
pip install grpcio grpcio-tools
```

## Como Usar

**Terminal 1 (Alice):**
```bash
python chat.node.py Washington 100200 localhost:200100
```

**Terminal 2 (Bob):**
```bash
python chat.node.py Karleandro 200100 localhost:100200
```

Você pode digitar enquanto recebe mensagens (usa threads para não bloquear).

## Arquivos

- **chat.proto** - Definição do protocolo gRPC
- **chat_pb2.py** e **chat_pb2_grpc.py** - Gerados automaticamente do .proto
- **chat.node.py** - Implementação do chat P2P

## Como Funciona

1. Cada nó tem um **servidor gRPC** que recebe mensagens
2. Cada nó tem um **cliente gRPC** que envia mensagens para o outro nó
3. **Thread separada** para envio não bloqueia a recepção
