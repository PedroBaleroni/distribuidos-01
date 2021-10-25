import socket
# Importando cPickle para enviar dictionary
import pickle

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

general_id = 0

ip_serv = '127.0.0.1'
porta_serv = 50000
dest = (ip_serv, porta_serv)

# Conectando ao servidor TCP (handshake)
tcp.connect(dest)

op = 1

while op != 5:
    print('Digite:')
    print('1 - Registrar filme Assistido (CREATE)')
    print('2 - Ver Filme (READ)')
    print('3 - Corrigir filme (UPDATE)')
    print('4 - Excluir filme (DELETE)')
    print('5 Sair')

    op = int(input())

    if op >= 1 and op <= 4:

        if op == 1:
            print('id do filme:')
            movie_id = int(input())
            print('Nome do filme:')
            movie_name = input()
            print('Duração do filme (minutos):')
            movie_time = int(input())
            print('Diretor do filme:')
            movie_director = input()
            
            data = {'id':movie_id,'name': movie_name, 'duration': movie_time, 'director': movie_director}
            package = pickle.dumps(data, -1)
            op_b = op.to_bytes(1,'big')
            
            package_send = package + bytes(500 - len(package))

            tcp.send(op_b + package_send)
            # Lê o tamanho da mensagem de resposta
            receiver = tcp.recv(500).decode('utf-8')

            print('Resposta: ', receiver)

        elif op == 3:
            print('id do filme (UPDATE):')
            movie_id = int(input())
            print('Nome do filme (UPDATE):')
            movie_name = input()
            print('Duração do filme (minutos) (UPDATE):')
            movie_time = int(input())
            print('Diretor do filme (UPDATE):')
            movie_director = input()

            data = {'id':movie_id,'name': movie_name, 'duration': movie_time, 'director': movie_director}
            package = pickle.dumps(data, -1)
            op_b = op.to_bytes(1,'big')
            package_send = package + bytes(500 - len(package))

            tcp.send(op_b + package_send)
            # Lê o tamanho da mensagem de resposta
            receiver = tcp.recv(500).decode('utf-8')

            print('Resposta: ', receiver)
        elif op == 2 or op == 4:
            print('id do filme:')
            movie_id = int(input())

            package = pickle.dumps(data, -1)
            op_b = op.to_bytes(1,'big')
            package_send = package + bytes(500 - len(package))

            tcp.send(op_b + package_send)
            # Lê o tamanho da mensagem de resposta
            receiver = tcp.recv(500).decode('utf-8')

            print('Resposta: ', receiver)

    elif op == 5:
        op_b = op.to_bytes(1,'big')
        tcp.send(op_b)


tcp.close()
input('aperte enter para encerrar')
