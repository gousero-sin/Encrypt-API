# 🔐 Encrypt API

A **Encrypt API** é uma interface criptográfica moderna, construída com **Python** e **Flask**, com foco em segurança, modularidade e escalabilidade. Seu principal objetivo é fornecer um serviço robusto de criptografia simétrica utilizando o padrão **AES**, com geração automática de chaves e integração futura com sistemas de autenticação como o **Keycloak**.

---

## 📌 Visão Geral

A API permite a **criptografia e descriptografia de dados sensíveis**, com suporte para operação via **terminal** ou **requisições HTTP REST** (em desenvolvimento). As chaves de criptografia são geradas de forma aleatória a cada requisição e protegidas contra vazamentos. Futuramente, um painel autenticado permitirá o gerenciamento dessas chaves.

---

## 🚀 Funcionalidades

- 🔒 **Criptografia AES (128, 256, 512 bits)**
- 🔑 Geração de chave aleatória por requisição
- 🧠 Derivação via **SHA-512** para chaves de 512 bits
- 📤 Interface em linha de comando (CLI) para uso local
- 📥 Descriptografia via identificador de chave
- 🔐 Encapsulamento completo da chave (nunca exposta)
- 📘 Documentação futura em OpenAPI 3.1
- 🛂 Integração futura com Keycloak para login e painel web

---

## 🧪 Modos de Uso

### 🔧 Modo CLI (Terminal)
Permite criptografar e descriptografar senhas diretamente no terminal, ideal para testes locais e aplicações scripts.

### 🌐 Modo API (Futuro)
Requisições REST para `/encrypt` e `/decrypt` com autenticação via Keycloak.

---

## ⚙️ Algoritmos e Segurança

- **AES** no modo CBC com padding PKCS7
- **Chaves de 512 bits** são derivadas com **SHA-512**
- A chave é criptograficamente segura, com `os.urandom`
- Nenhuma chave é exposta diretamente pela API
- As chaves são identificadas por **IDs únicos seguros**
- Falsas tentativas de descriptografia podem ser auditadas

---

## 📦 Tamanhos de Chave Suportados

| Tamanho | Geração                        | Algoritmo de Derivação     |
|---------|--------------------------------|-----------------------------|
| 128     | Aleatória                      | `os.urandom(16)`           |
| 256     | Aleatória                      | `os.urandom(32)`           |
| 512     | SHA-512 sobre uma semente      | `hashlib.sha512().digest()`|

> ⚠️ O suporte a 64 bits foi removido por questões de segurança.

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3.x
- **Framework Web:** Flask
- **Criptografia:** `cryptography` (Fernet, AES, PBKDF2, etc.)
- **Hashing:** SHA-512
- **Autenticação:** Keycloak (futuramente)
- **Documentação:** Swagger / OpenAPI 3.1
- **Banco de dados:** Planejado (para armazenar identificadores de chave)

---

## 📈 Estrutura Modular Planejada

| Módulo             | Responsabilidade                           |
|--------------------|---------------------------------------------|
| `app.py`           | Ponto de entrada da aplicação Flask         |
| `routes/encrypt.py`| Rota de criptografia                        |
| `routes/decrypt.py`| Rota de descriptografia                     |
| `core/crypto.py`   | Funções de criptografia, geração e hashing  |
| `cli.py`           | Interface de linha de comando               |
| `config.py`        | Configurações globais e variáveis seguras   |

---

## 🔮 Expansões Futuras

- Painel de gerenciamento web com Keycloak
- Logs criptografados de atividade
- Tokens temporários de descriptografia
- Exportação de chaves com proteção assimétrica
- Compatibilidade com algoritmos pós-quânticos

---

## 🧑‍💻 Autor

**Marcos Oliveira**  
PUC Goiás – Engenharia da Computação  
GitHub: [github.com/seuusuario]  
Telegram: [@seutelegram]  
API criada como projeto de estudo e aprimoramento em segurança da informação.

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para utilizar, contribuir e aprimorar.

---

## 💬 Contato

Caso tenha dúvidas, sugestões ou queira contribuir, sinta-se à vontade para entrar em contato!

