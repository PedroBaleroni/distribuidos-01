import socket
import pickle

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ''
porta = 50000
origem = (ip, porta)

database = []

# Vincula com a porta e IP usados
tcp.bind(origem)

# Aguarda a chegada de uma conexão TCP
# Se chegar mais de uma, as demais serão recusadas
tcp.listen(1)

# Aceitar a conexão TCP recebida a mais tempo
tcp_dados, client = tcp.accept()

op = 1

while op != 5:

    op = int.from_bytes(tcp_dados.recv(1), 'big')

    if op >= 1 and op <= 4:

        pickle_data = pickle.loads(tcp_dados.recv(500))
        data = pickle_data
        print(data)
        

        db_return = {'data' : 'none'}
        #insert
        if op == 1:
    
            database.append(data)
            resp = 'CREATED'
            package_send = str.encode(resp)
            package_send = package_send + bytes(500 - len(package_send))

            tcp_dados.send(package_send)

        #update
        elif op == 3:
            id = data['id']
            try:
                info = [item for item in database if item['id']== int(id)][0]
                name = data['name']
                duration = data['duration']
                director = data['director']
                info['name'] = name
                info['duration'] = duration
                info['director'] = director
                resp = 'UPDATED'
            
            except:
                resp = 'Filme não encontrado'
            package_send = str.encode(resp)
            package_send = package_send + bytes(500 - len(package_send))

            tcp_dados.send(package_send)
        #find
        elif op == 2:
            
            id = data['id']
            try:
                info = [item for item in database if item['id'] == int(id)][0]
                resp = str(info)
            except:
                resp = 'Filme não encontrado'
            package_send = str.encode(resp)
            package_send = package_send + bytes(500 - len(package_send))

            tcp_dados.send(package_send)
        #delete
        else:
            id = data['id']
            try:
                info = [item for item in database if item['id'] == int(id)][0]
                database.pop(database.index(info))
                resp = 'DELETED'
            except:
                resp = 'Filme não encontrado'
            package_send = str.encode(resp)
            package_send = package_send + bytes(500 - len(package_send))

            tcp_dados.send(package_send)

# Fechando os sockets
tcp_dados.close()

tcp_dados.close()

input('aperte enter para encerrar')
