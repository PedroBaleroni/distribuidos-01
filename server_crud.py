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

        pickle_string = tcp_dados.recv(500).decode('utf-8')
        pickle_string = pickle_string.rstrip('\x00')

        print("Recebido: {}".format(pickle_string))
        data = pickle.loads(pickle_string)

        db_return = {'data' : 'none'}
        #insert
        if op == 1:
            id = int(split_a[1])
            marca = split_a[2]
            preco = int(split_a[3])
            carro = Carro(id, marca, preco)
            carrosVet.append(carro)
            resp = 'Carro criado com sucesso'
            tam_resp = (len(resp)).to_bytes(2, 'big')
            tcp_dados.send(tam_resp + resp.encode())

        #update
        elif op == 2:
            id = split_a[1]
            try:
                carro = [item for item in carrosVet if item.id == int(id)][0]
                resp = str(carro)
            except:
                resp = 'Carro não encontrado'
            tam_resp = (len(resp)).to_bytes(2, 'big')
            tcp_dados.send(tam_resp + resp.encode())
        #find
        elif op == 3:
            id = split_a[1]
            try:
                carro = [item for item in carrosVet if item.id == int(id)][0]
                marca = split_a[2]
                preco = int(split_a[3])
                carro.marca = marca
                carro.preco = preco
                resp = str(carro)
            except:
                resp = 'Carro não encontrado'
            tam_resp = (len(resp)).to_bytes(2, 'big')
            tcp_dados.send(tam_resp + resp.encode())
        #delete
        else:
            id = split_a[1]
            try:
                carro = [item for item in carrosVet if item.id == int(id)][0]
                carrosVet.pop(carrosVet.index(carro))
                resp = 'Carro deletado com sucesso'
            except:
                resp = 'Carro não encontrado'
            tam_resp = (len(resp)).to_bytes(2, 'big')
            tcp_dados.send(tam_resp + resp.encode())

# Fechando os sockets
tcp_dados.close()

tcp.close()

input('aperte enter para encerrar')
