host="127.0.0.1" #Declaro qual é o endereço de ip escaneado
portas=("80" "22" "443") #Declaro quais são as portas que serão verificadas

for porta in "${portas[@]}";do #Looping para verificar porta por porta
	nc -zv "$host" "$porta" > /dev/null 2>&1 #Procura a porta no determinado endereço, pega a parte escrita e envia para /dev/null e faz um tratamento de erro.
	if [ $? -eq 0 ]; then #Condicional para verifica se a porta está aberta.
		echo "Porta $porta está aberta em $host"
	else #Em caso de não estar avise.
		echo "Porta $porta está fechada em $host"
	fi
done
