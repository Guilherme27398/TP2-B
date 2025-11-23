# Comandos para enviar ao GitHub

## 1. Inicializar o repositório Git (se ainda não foi feito)
```bash
git init
```

## 2. Adicionar todos os arquivos
```bash
git add .
```

## 3. Fazer o primeiro commit
```bash
git commit -m "Initial commit: Sistema RPC com XML-RPC e gRPC"
```

## 4. Criar repositório no GitHub
- Vá para https://github.com/new
- Crie um novo repositório (ex: `TP2-B` ou `sistema-rpc`)
- **NÃO** inicialize com README, .gitignore ou license (já temos)

## 5. Conectar ao repositório remoto
```bash
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```
(Substitua SEU_USUARIO e NOME_DO_REPOSITORIO pelos seus valores)

## 6. Enviar para o GitHub
```bash
git branch -M main
git push -u origin main
```

---

## Comandos alternativos (se já tiver repositório Git)

Se já tiver um repositório Git inicializado:
```bash
git add .
git commit -m "Update: Correções no servidor gRPC"
git push
```

---

## Nota sobre arquivos grandes

Se o arquivo `car_prices.csv` ou `car_prices.xml` for muito grande (>100MB), considere:
1. Adicionar ao `.gitignore` (já está comentado)
2. Ou usar Git LFS:
```bash
git lfs install
git lfs track "*.csv"
git lfs track "*.xml"
git add .gitattributes
```

