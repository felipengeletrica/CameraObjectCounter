# Object Color Counter 📷🔴🔵

Este projeto detecta objetos **vermelhos** e **azuis** em tempo real, contabilizando quantos passaram por uma **linha de contagem** usando a webcam ou uma câmera RTSP.

---

## ✅ Requisitos

- Python 3.8 ou superior
- OpenCV
- NumPy

---

## 🧰 Instalação do Python 3

### Windows
1. Baixe o Python no site oficial: https://www.python.org/downloads/
2. **Marque a opção "Add Python to PATH"** durante a instalação
3. Confirme com:
   ```sh
   python --version
   ```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

## 🧪 Criando ambiente virtual

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 📦 Instalando dependências

```bash
pip install -r requirements.txt
```

---

## 🔍 Como encontrar o ID da câmera

### Windows
1. Pressione `Win + R`, digite `devmgmt.msc` e pressione Enter
2. Vá em "Dispositivos de imagem"
3. A câmera geralmente será o ID `0`. Teste com:
   ```bash
   python main.py --camera 0
   python main.py --camera 1
   ```

### Linux
1. Liste os dispositivos:
   ```bash
   ls /dev/video*
   ```
2. Use o ID retornado:
   ```bash
   python main.py --camera /dev/video0
   ```

---

## 🎬 Executando o programa

### Câmera local
```bash
python main.py --camera 0
```

### Stream RTSP
```bash
python main.py --camera "rtsp://usuario:senha@ip:554/..."
```

---

## 📁 Estrutura do projeto

```
ObjectColorCounter/
├── main.py               # Script principal
├── requirements.txt      # Dependências
└── README.md             # Este guia
```

---

## 🔒 .gitignore sugerido

```gitignore
.venv/
__pycache__/
*.pyc
.DS_Store
```

---

## 🤖 Funcionalidades

- Contagem de objetos vermelhos e azuis
- Suporte a webcam e RTSP
- Linha de contagem configurável
- Argumento de câmera via terminal

---

## 📷 Exemplo

```bash
python main.py --camera 0
```

---

## 🧠 Futuras melhorias

- Detecção de mais cores
- Exportação para CSV
- Interface com PyQt5 ou Tkinter

---

## 🧑‍💻 Autor

**Felipe Vargas**  
[LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)
