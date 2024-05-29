log_file="arquivo.qualquer"
try_range=5

tries=$(grep "Failed Password" "log_file" | wc -l)

if [ "$tries" -ge "try_range" ];then
	echo "Possível ataque de força bruta detectado"
else
	echo "Nenhuma atividade de força bruta detectada"
fi
