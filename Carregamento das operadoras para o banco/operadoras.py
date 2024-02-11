import csv
import mysql.connector

def carregar_dados_operadoras_ativas(arquivo_csv):
    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    cursor = conn.cursor()

    num_linhas_processadas = 0

    tamanho_lote = 50

    with open(arquivo_csv, 'r', newline='', encoding='latin1') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        lote = []
        
        for linha in csv_reader:
            linha["REGISTRO_ANS"] = linha.pop("Registro_ANS")
            linha["RAZAO_SOCIAL"] = linha.pop("Razao_Social")
            linha["NOME_FANTASIA"] = linha.pop("Nome_Fantasia")
            linha["MODALIDADE"] = linha.pop("Modalidade")
            linha["LOGRADOURO"] = linha.pop("Logradouro")
            linha["NUMERO"] = linha.pop("Numero")
            linha["COMPLEMENTO"] = linha.pop("Complemento")
            linha["BAIRRO"] = linha.pop("Bairro")
            linha["CIDADE"] = linha.pop("Cidade")
            linha["TELEFONE"] = linha.pop("Telefone")
            linha["FAX"] = linha.pop("Fax")
            linha["EMAIL"] = linha.pop("Endereco_eletronico")
            linha["REPRESENTANTE"] = linha.pop("Representante")
            linha["CARGO_REPRESENTANTE"] = linha.pop("Cargo_Representante")

            lote.append(linha)
            
            if len(lote) == tamanho_lote:
                cursor.executemany("""
                    INSERT INTO operadoras_ativas (
                        REGISTRO_ANS, 
                        CNPJ, 
                        RAZAO_SOCIAL,
                        NOME_FANTASIA, 
                        MODALIDADE,
                        LOGRADOURO,
                        NUMERO,
                        COMPLEMENTO,
                        BAIRRO,
                        CIDADE,
                        UF,
                        CEP,
                        DDD,
                        TELEFONE,
                        FAX,
                        EMAIL,
                        REPRESENTANTE,
                        CARGO_REPRESENTANTE
                    )
                    VALUES (
                        %(REGISTRO_ANS)s, 
                        %(CNPJ)s, 
                        %(RAZAO_SOCIAL)s,
                        %(NOME_FANTASIA)s, 
                        %(MODALIDADE)s,
                        %(LOGRADOURO)s,
                        %(NUMERO)s,
                        %(COMPLEMENTO)s,
                        %(BAIRRO)s,
                        %(CIDADE)s,
                        %(UF)s,
                        %(CEP)s,
                        %(DDD)s,
                        %(TELEFONE)s,
                        %(FAX)s,
                        %(EMAIL)s,
                        %(REPRESENTANTE)s,
                        %(CARGO_REPRESENTANTE)s
                    )
                """, lote)
                
                conn.commit()
                
                lote = []
            
            num_linhas_processadas += 1
            
            if num_linhas_processadas % 1000 == 0:
                print(f"{num_linhas_processadas} linhas processadas.")

        if lote:
            cursor.executemany("""
                INSERT INTO operadoras_ativas (
                    REGISTRO_ANS, 
                    CNPJ, 
                    RAZAO_SOCIAL,
                    NOME_FANTASIA, 
                    MODALIDADE,
                    LOGRADOURO,
                    NUMERO,
                    COMPLEMENTO,
                    BAIRRO,
                    CIDADE,
                    UF,
                    CEP,
                    DDD,
                    TELEFONE,
                    FAX,
                    EMAIL,
                    REPRESENTANTE,
                    CARGO_REPRESENTANTE
                )
                VALUES (
                    %(REGISTRO_ANS)s, 
                    %(CNPJ)s, 
                    %(RAZAO_SOCIAL)s,
                    %(NOME_FANTASIA)s, 
                    %(MODALIDADE)s,
                    %(LOGRADOURO)s,
                    %(NUMERO)s,
                    %(COMPLEMENTO)s,
                    %(BAIRRO)s,
                    %(CIDADE)s,
                    %(UF)s,
                    %(CEP)s,
                    %(DDD)s,
                    %(TELEFONE)s,
                    %(FAX)s,
                    %(EMAIL)s,
                    %(REPRESENTANTE)s,
                    %(CARGO_REPRESENTANTE)s
                )
            """, lote)
            
            conn.commit()

    cursor.close()
    conn.close()

carregar_dados_operadoras_ativas('C:/DOCS TEST/relatorio.csv')
