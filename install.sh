echo "(1) Criando ambientes virtuais..."
. scripts/create_venv.sh 

echo "(2) Instalando dependencias..."
. scripts/install_requirements.sh

echo "(3) Criando arquivos de logs..."
. scripts/create_logs.sh

echo "(4) Alterando permissoes..."
. scripts/ch_exec_perm.sh

echo "... Finalizado"