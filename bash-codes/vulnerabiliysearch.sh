sistema="Ubuntu" #Declaring the system scanned
versao="20.04" #Declaring the system version

vulnerability=$(grep "$sistema $versao" cve_database.txt) #running by the system searching by a vulnerability existing in database

if[ -n "$vulnerability" ];then #output conditional.
	echo "Vulnerabilidade conhecida encontrada. "
else
	echo "Nenhuma vulnerabilidade conhecida encontrada. "
fi
