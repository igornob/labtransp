from PyPDF2 import PdfFileWriter,PdfFileReader
import re
from os import listdir
from os.path import isfile, join


onlyfiles =[f for f in listdir("/home/igor/Desktop/Cidades") if isfile(join("/home/igor/Desktop/Cidades", f))]
print(onlyfiles)


def PDFfile():
	for file in onlyfiles:
		infile = PdfFileReader(open("/home/igor/Desktop/Cidades/"+file, "rb" ))
		content = ""
		result_fixa = ""
		result_variavel = ""
		valor_atual_1 = ""
		valor_atual_2 = ""
		valor_atual_3 = ""
		valor_atual_final = ""
		final_regex = ""
		aplicacao = ""
		aplicacao = ""
		valorCotas = ""
		qtdCotas = ""
		fundo = ""
		final = ""
		cnpj = ""
		valor_atual_final = ""
		data = ""
		cnpj_final = ""
		data_final = ""
		valor_tratado = ""
		fundo_tratado = ""
		qtd_cotas = ""
		valor_atual_cota = ""
		coluna_fundo = ""
		final = ""
		coluna_fundo_final=""
		coluna_cnpj=""
		coluna_cnpj_final =""
		fundo_cnpj="" 
		coluna_data = ""
		coluna_data_final=""
		coluna_valor_cota_final = ""
		coluna_valor_cota_final_final = ""
		coluna_valor_tratado = ""
		coluna_valor_tratado_final= ""
		coluna_valor_tratado_final_final = ""
		final= ""
		lista1 = []
		lista2 = []
		lista3=[]
		lista4=[]
		s=","
		a=""
		tratamento1=""
		tratamento2=""


		
		for i in range(infile.getNumPages()):

			p = infile.getPage(i).extractText()
			content += p + "\n"
			cidade = re.findall("ENTENome"r'(.*?)[/]',content) 
			percentual = re.findall("dos Recursos do RPPS:"r'(.*?)%',content)
			cidade_1 = re.sub(":","",str(cidade))
			total_aplicado_3_informações = re.findall("Total Geral:"r'(.*?)Página',content)
			merdas =re.sub (r'(.*?)[,](.*?)[,]',"",str(total_aplicado_3_informações))
		 	#total_aplicao_bimestre = re.sub(r'(.*?)[.](.*?)[.](.*?)[,]',".",str(total_aplicado_3_informações))
			segmento = re.findall("Nº:"r'(.*?)Segmento', content)
			result_fixa = re.findall(":Renda FixaSegmento" , content)
			result_variavel = re.findall(":Renda VariávelSegmento" ,content)
			valor_atual_1 = re.findall(r'\d[.]\d\d\d[.]\d\d\d[,]\d\d[A-Z][a-z]*',content)	
			valor_atual_2 = re.findall(r'\d\d[.]\d\d\d[.]\d\d\d[,]\d\d[A-Z][a-z]*',content) 		
			valor_atual_3 = re.findall(r'\d\d\d[.]\d\d\d[.]\d\d\d[,]\d\d[A-Z][a-z]*',content)		
			final_regex = re.findall(r'[,][0-9]*[.]\d\d\d[.]\d\d\d[,]\d\d[A-Z][a-z]*',content)
			final = re.findall(r'[,][0-9]*[.]\d\d[.]\d\d\d[,]\d\d[A-Z][a-z]*',content)	
			aplicacao = re.findall("A"r'[A-Z][a-z]*\d\d\d',content)
			aplicacao_1 = re.findall(r'\d\d\d'"Aplicação",content)
			final_regex_teste = re.findall(r'[0-9]*\d\d\d[.]\d\d\d[,]\d\d["Valor Atual"]',content)	
			valorCotas = re.findall(r'[-][0-9]*[,]\d\d\d\d\d\d\d\d\d\d',content)
			qtdCotas = re.findall(r'[:][0-9](.)()',content)
			#fundo = re.findall(r'[,].*Fundo:CNPJ do Fundo:',content)
			fundo = re.findall("Instituição Financeira:Tipo"r'(.*?)Fundo:',content)
			cnpj = re.findall(":CNPJ do Fundo:"r'\d\d[.]\d\d\d[.]\d\d\d[\[/]\d\d\d\d[-]\d\d' , content) 
			valor_atual_final = re.findall(r':CNPJ do Fundo(.*?)Valor',content)
			data = re.findall(r'[:](\d\d[/]\d\d[/]\d\d\d\d["Data"])',content)
			cnpj_final = re.sub(":CNPJ do Fundo:","", str(cnpj)) 
			data_final = re.sub("D","", str(data))	
			valor_tratado = re.sub (r'[:]\d\d[.]\d\d\d[.]\d\d\d[\[/]\d\d\d\d[-]\d\d\d[,]\d\d\d\d\d\d\d\d\d\d',"", str(valor_atual_final))
			fundo_tratado = re.sub ("de Ativo:"r'(.*?)[,](.*?)[,]',"", str(fundo))
			#fundo_tratado = re.sub (":FI"r'(.*?)[,](.*?)[,]',"", str(fundo))
			qtd_cotas = re.findall("Valor Atual da Cota"r'(.*?)Quantidade' , content)
			valor_atual_cota = re.findall(":CNPJ do Fundo:"r'\d\d[.]\d\d\d[.]\d\d\d[\[/]\d\d\d\d[-]\d\d[0-9]*[,][0-9]{10}',content)
			valor_atual_cota_tratado = re.sub(":CNPJ do Fundo:"r'\d\d[.]\d\d\d[.]\d\d\d[\[/]\d\d\d\d[-]\d\d',"", str(valor_atual_cota))
			coluna_fundo =re.sub(" "," ",str(fundo_tratado))
			coluna_fundo_final=re.sub(",",","+"\n",str(coluna_fundo))
			coluna_cnpj=re.sub("'","",str(cnpj_final))
			coluna_cnpj_final =re.sub(",",","+"\n",str(coluna_cnpj))
			fundo_cnpj = coluna_fundo_final + coluna_cnpj_final
			coluna_data = re.sub("'","",str(data_final))
			coluna_data_final=re.sub(",",","+"\n",str(coluna_data))
			coluna_valor_cota_final = re.sub("'","",str(valor_atual_cota_tratado))
			coluna_valor_cota_final_final= re.sub(" ","\n",str(coluna_valor_cota_final))
			coluna_valor_tratado = re.sub("'","",str(valor_tratado))
			coluna_valor_tratado_final = re.sub(":","",str(coluna_valor_tratado))
			coluna_valor_tratado_final_final = re.sub(" ","\n",str(coluna_valor_tratado_final))
			final = coluna_fundo_final + coluna_cnpj_final+coluna_data_final+coluna_valor_cota_final+coluna_valor_tratado_final_final
			coluna_valor_tratado_final_1 = re.sub(",",".",str(coluna_valor_tratado_final))
			coluna_fundo_final_3 = re.sub("\"b","",str(coluna_fundo_final))
			coluna_fundo_final_4 = re.sub("a","",str(coluna_fundo_final_3))
			coluna_fundo_final_5 = re.sub("b","",str(coluna_fundo_final_4))
			coluna_fundo_final_6 = re.sub("\"","",str(coluna_fundo_final_5))

			aplicacao_2 = re.sub("Aplicação","",str(aplicacao_1))

		
		#lista1=fundo_tratado.split(",")
		lista2=coluna_data_final.split(",")
		lista3=coluna_cnpj_final.split(",")
		lista4=coluna_valor_cota_final.split(" ")
		lista5=valor_tratado.split(" ")
		lista6= aplicacao_2.split(",")
		lista7=segmento
		
		merdas = merdas[2:]
		merdas_1 = re.sub("\\]","",merdas)
		merdas_2 = re.sub("\\'","",merdas_1)
		# print(merdas_1)
		#print(cidade)
		# cidade_final = [intem[0] for intem in cidade_1]
		# print(cidade_final)


		# print(coluna_valor_tratado)
		#print(total_aplicao_bimestre)
		#print(segmento)
		#print(content)
		#print(aplicacao_1)
		#print(lista6)
		#print(segmento)
						

			# tratamento1=re.sub("\n","",str(fdf))
		# 	# tratamento2=re.sub("\n","",str(tratamento1))
			
		
		#print(fundo_tratado)


		
		fl = open(file+".txt", "w")

		for linha in zip(lista6,lista7,lista2,lista3,lista4,lista5,percentual):

			linha_tratada = [ re.sub("\n","",item.strip()) for item in linha ]
			linha_tratada = [ re.sub("\\[","",item) for item in linha_tratada ]
			linha_tratada = [ re.sub("\\]","",item) for item in linha_tratada ]
			#linha_tratada = [ re.sub(",",".",item) for item in linha_tratada ]
			linha_tratada = [ re.sub("'"," ",item) for item in linha_tratada ]
			linha_tratada = [ re.sub("\"b","",item) for item in linha_tratada ]
			linha_tratada = [ re.sub("\\.","",item) for item in linha_tratada ]


			# linha_tratada = [ re.sub("a","",item) for item in linha_tratada ]
			# print(",".join(linha_tratada))
			# print(merdas_1)
			# print(merdas_1+","+",".join(linha_tratada))
			fl.write(merdas_2+","+",".join(linha_tratada))
			fl.write("\n")
			
			# fl.write(merdas_1)	
			# fl.write(",".join(linha_tratada))
			# fl.write("\n")

		# fl.close()
	
			# print("INSERT INTO MYTABLE VALUES("+ ",".join(linha_tratada)+")")
			# print("\n")
		
		
		# print(len(lista1))
		# print(len(lista2))
		# print(len(lista3))
		# print(len(lista4))
		# print(len(lista5))
		# print(len(lista6))
		# print(len(lista7))
		# print(len(linha))
		# print(len(linha_tratada))
		# print(fundo_tratado)
		fl.write(cidade[0]+","+merdas_2+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x"+","+"x")	
				



PDFfile()

