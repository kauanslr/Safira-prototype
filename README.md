# Safira Prototype

Este projeto foi desenvolvido como meu **Trabalho de Conclusão de Curso (TCC)**.  
Na época, coloquei tudo em um repositório apenas para não perder o código, já que eu iria formatar o computador.

Hoje resolvi tornar o repositório **público**, principalmente para mostrar que **todo mundo começa de algum lugar** — e que ninguém nasce sabendo.  
Naquele momento, eu já tinha uma noção de programação e já gostava bastante de **orientação a objetos**, mas é fácil perceber que existem **muitas melhorias possíveis** no projeto (tanto de código quanto de organização).

A ideia aqui não é mostrar um projeto perfeito, mas sim um **registro real de aprendizado**.

---

## 💡 Ideia do projeto

O projeto foi pensado para rodar em um **Raspberry Pi**, acoplado a um carrinho controlado por visão computacional.

### Hardware
- Carrinho de plástico  
- Tração **4x2 traseira**  
- Microcâmera posicionada na parte frontal  
- Raspberry Pi montado na parte superior  
- Alimentação via **power bank** (sim, bem duvidoso 😅)

### Funcionamento
A proposta era simples:

1. Utilizar **OpenCV** para detectar um **semáforo**
2. O detector era baseado em um **Cascade Classifier treinado por mim**
3. O modelo era **bem específico**, focado em um mini semáforo em escala  
   (algo em torno de ~5cm de altura)
4. Após identificar o semáforo:
   - Detectar a **cor** (vermelho ou verde)
   - Fazer o carrinho **parar ou andar**, respectivamente

---

## 🧠 Código e stack

- Linguagem: **Python**
- Gerenciamento de pacotes: `pip` + `venv`
- Principais bibliotecas:
  - `numpy`
  - `opencv-python`

Sim, o repositório contém:
- Arquivos compilados
- A pasta `venv` inteira
- Dependências versionadas no próprio repo

Isso **não é uma boa prática**, mas tem um motivo simples:  
👉 **eu nunca tinha usado GitHub na vida**.

Na época, eu literalmente só pensei:  
> “funcionou? então sobe tudo”

E foi isso. Eu só peguei e… **fiz**.

---

## 🤝 Pessoas que participaram do projeto

Este projeto não foi feito sozinho. Durante o desenvolvimento do TCC, tive a ajuda e participação de:

- **Ana Clara**
- **Adam**
- **Erika Leme**

Não tenho (ou não mantive) redes sociais deles para linkar aqui 😅, mas fica registrado o agradecimento pela colaboração e troca de ideias durante o projeto.

---

## 📌 Observações finais

- Este projeto reflete **um momento específico da minha evolução**
- Não representa minhas práticas atuais
- Serve como:
  - Registro histórico
  - Exemplo de aprendizado
  - Incentivo pra quem está começando agora

Se você está no início da sua jornada:  
**começar mal feito é infinitamente melhor do que não começar.**
