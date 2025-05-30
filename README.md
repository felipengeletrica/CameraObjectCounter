# 🎯 Camera Object Counter

Detecta e **conta objetos das cores vermelha e azul** passando por uma linha no vídeo usando **OpenCV**. Suporta câmeras locais (`--camera 0`) ou IP (`--camera rtsp://...`).

---

## 🧪 Funcionalidades

- ✅ Detecta objetos vermelhos e azuis com máscaras HSV.
- ✅ Desenha contornos e calcula centroides.
- ✅ Conta quantas vezes cada objeto cruza uma linha horizontal.
- ✅ Suporte a câmeras locais e remotas (RTSP).

---

## 🧰 Requisitos

- Python 3.8+
- OpenCV
- NumPy

---

## 🔧 Instalação

### 💻 Criar ambiente virtual

#### Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 📦 Instalar dependências
```bash
pip install -r requirements.txt
```

> Conteúdo do `requirements.txt`:
> ```
> opencv-python
> numpy
> ```

---

## 🚀 Executar o programa

### ▶️ Usando a webcam local (ex: `0` ou `1`)

#### Linux / macOS:
```bash
python main.py --camera 0
```

#### Windows:
```cmd
python main.py --camera 0
```

### 🌐 Usando câmera IP (RTSP):
```bash
python main.py --camera rtsp://usuario:senha@192.168.0.100:554/stream
```

---

## 📁 Estrutura do Projeto

```
CameraObjectCounter/
├── main.py              # Código principal
├── requirements.txt     # Dependências
└── README.md            # Documentação
```

---

## ⚠️ Problemas comuns

- **Câmera não abre?** Verifique se o ID está correto (0, 1...) ou se o RTSP está acessível.
- **Sem imagem?** Teste com `cv2.imshow("debug", frame)` para inspecionar a imagem.
- **Erro de permissão?** Execute com permissões adequadas ou teste com outra câmera.

---
