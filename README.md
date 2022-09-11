# Solicita-o_XML_Receita_PR
Solicita o XML das notas emitidas ou destinadas contra as empresas que estão numa planilha de Excel

Print de como é o padrão da planilha que precisa estar na mesma pasta desse código para funcionar: ![image](https://user-images.githubusercontent.com/106564039/189552162-201145fd-1142-4da7-ade1-c529c35d7681.png)

O código utiliza selenium, pandas e datetime para solicitar no primeiro dia do mês seguinte ao que deseja solicitar o XML de notas fiscais emitidas ou destinadas contra a empresa que está com o CNPJ na planilha Excel.
O selenium é utilizado para controlar o navegador Google Chrome para automatizar o processo repetitivo de solicitar XML de várias empresas, que nesse caso estão em um login de contador da Receita PR. A versão anterior do código logava através de certificado digital, o que fazia com que o código ficasse mais lento e menos performatico, pois precisava ficar saindo e logando novamente com vários certificados digitais diferentes.
O pandas é utilizado para ler o arquivo Excel que possui as informações da empresa que deseja solicitar.
O datetime é utilizado para deixar o código com atualização automatica mensal. Lembrando que o código foi montado para solicitar todo dia 01 do mês seguinte ao que deseja solicitar. Exemplo: Desejo solicitar os documentos que foram emitidos e destinados contra a empresa no mês de Agosto, vou solicitar no dia 01/09.
