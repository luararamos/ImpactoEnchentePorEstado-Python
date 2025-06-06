# 🌧️ Analise de Risco de Enchentes por Estado

Este projeto simula um sistema de monitoramento de enchentes em cinco estados brasileiros.  
A partir de dados fornecidos pelo usuário (chuva, nível do rio e dias de chuva contínua), o programa avalia se há risco de enchente na região escolhida com base em critérios definidos.

O usuário seleciona um estado, insere os dados climáticos e o sistema retorna uma análise com base em regras pré-estabelecidas.  
Além disso, o programa exibe um mapa ASCII representando o estado selecionado.

---

## 🌍 Estados Disponíveis

- **São Paulo**
- **Rio de Janeiro**
- **Bahia**
- **Paraná**
- **Pernambuco**

---

## 📊 Critérios para Análise de Risco de Enchente

| Critério                     | Valor para ser considerado crítico              |
|-----------------------------|--------------------------------------------------|
| Quantidade de chuva (mm)    | Maior que o limite suportado pelo estado        |
| Nível do rio (metros)       | Maior que 4 metros                               |
| Dias de chuva contínua      | Maior que 2 dias                                 |

---

## 💬 Mensagens do Sistema e Suas Condições

| Mensagem                                                | Condição para exibição                       |
|----------------------------------------------------------|----------------------------------------------|
| ✅ Situação sob controle. Nenhum risco de enchente.      | Menos de 2 critérios críticos são verdadeiros |
| ⚠️ Alerta: Há risco de enchente na região!               | 2 ou mais critérios críticos são verdadeiros  |

---

## 🧪 Exemplo de Análise — São Paulo

**Limite de chuva suportado: 70 mm**

### Entradas:
- Chuva registrada: 80 mm
- Nível do rio: 4.5 m
- Dias de chuva contínua: 3

### Resultado:
- Chuva > 70 mm → **crítico**
- Nível do rio > 4 m → **crítico**
- Dias de chuva > 2 → **crítico**

➡️ **Mensagem exibida:**
⚠️ Alerta: Há risco de enchente na região!



---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo `.py`, por exemplo `enchentes.py`.
3. Execute no terminal:
python ImpactoEnchentePorEstado.py

---

## 👥 Equipe do Projeto

| Nome   | RM       | E-mail                     |
|--------|----------|----------------------------|
| Luara Martins de Oliveira Ramos  | 565573   | rm565573@fiap.com.br       |
| Kaio Victtor Santos Andrade Galvão   | 566536   | rm566536@fiap.com.br       |
| Jean Pierre Andrade Feltran   | 566534   | rm566534@fiap.com.br       |

---
