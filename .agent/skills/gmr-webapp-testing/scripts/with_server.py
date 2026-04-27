#!/usr/bin/env python3
"""
Inicia um ou mais servidores, aguarda ficarem prontos, executa um comando e finaliza.

Uso:
    # Servidor único
    python scripts/with_server.py --server "npm run dev" --port 5173 -- python automacao.py

    # Múltiplos servidores (backend + frontend)
    python scripts/with_server.py \
      --server "cd backend && python server.py" --port 3000 \
      --server "cd frontend && npm run dev" --port 5173 \
      -- python teste.py
"""

import subprocess
import socket
import time
import sys
import argparse

def is_server_ready(port, timeout=30):
    """Aguarda o servidor ficar pronto verificando o port."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection(('localhost', port), timeout=1):
                return True
        except (socket.error, ConnectionRefusedError):
            time.sleep(0.5)
    return False


def main():
    parser = argparse.ArgumentParser(description='Executa comando com um ou mais servidores')
    parser.add_argument('--server', action='append', dest='servers', required=True, help='Comando do servidor (pode ser repetido)')
    parser.add_argument('--port', action='append', dest='ports', type=int, required=True, help='Porta de cada servidor (deve corresponder ao --server)')
    parser.add_argument('--timeout', type=int, default=30, help='Timeout em segundos por servidor (padrão: 30)')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='Comando a executar após servidores prontos')

    args = parser.parse_args()

    # Remove o separador '--' se presente
    if args.command and args.command[0] == '--':
        args.command = args.command[1:]

    if not args.command:
        print("Erro: Nenhum comando especificado para executar")
        sys.exit(1)

    # Valida configurações de servidores
    if len(args.servers) != len(args.ports):
        print("Erro: O número de argumentos --server e --port deve ser igual")
        sys.exit(1)

    servers = []
    for cmd, port in zip(args.servers, args.ports):
        servers.append({'cmd': cmd, 'port': port})

    server_processes = []

    try:
        # Inicia todos os servidores
        for i, server in enumerate(servers):
            print(f"Iniciando servidor {i+1}/{len(servers)}: {server['cmd']}")

            process = subprocess.Popen(
                server['cmd'],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            server_processes.append(process)

            print(f"Aguardando servidor na porta {server['port']}...")
            if not is_server_ready(server['port'], timeout=args.timeout):
                raise RuntimeError(f"Servidor falhou ao iniciar na porta {server['port']} em {args.timeout}s")

            print(f"Servidor pronto na porta {server['port']}")

        print(f"\nTodos os {len(servers)} servidor(es) prontos")

        # Executa o comando
        print(f"Executando: {' '.join(args.command)}\n")
        result = subprocess.run(args.command)
        sys.exit(result.returncode)

    finally:
        # Finaliza todos os servidores
        print(f"\nParando {len(server_processes)} servidor(es)...")
        for i, process in enumerate(server_processes):
            try:
                process.terminate()
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            print(f"Servidor {i+1} parado")
        print("Todos os servidores parados")


if __name__ == '__main__':
    main()
