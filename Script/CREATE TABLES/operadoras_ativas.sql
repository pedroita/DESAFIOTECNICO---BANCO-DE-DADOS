CREATE TABLE Operadoras_ativas (
    REGISTRO_ANS VARCHAR(10) NOT NULL PRIMARY KEY,
    CNPJ VARCHAR(20),
    RAZAO_SOCIAL VARCHAR(200),
    NOME_FANTASIA VARCHAR(200),
    MODALIDADE VARCHAR(100),
    LOGRADOURO VARCHAR(50),
    NUMERO VARCHAR(30),
    COMPLEMENTO VARCHAR(100),
    BAIRRO VARCHAR(50),
    CIDADE VARCHAR(100),
    UF VARCHAR(2),
    CEP VARCHAR(20),
    DDD VARCHAR(2),
    TELEFONE VARCHAR(20),
    FAX VARCHAR(20),
    EMAIL VARCHAR(100),
    REPRESENTANTE VARCHAR(130),
    CARGO_REPRESENTANTE VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR (10),
    DATA_REGISTRO_ANS VARCHAR (30)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;