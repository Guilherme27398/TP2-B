# Comandos para corrigir o erro do GitHub

Os arquivos `car_prices.csv` e `car_prices.xml` são muito grandes para o GitHub.

## Solução: Remover os arquivos grandes do Git

**1. Remover os arquivos grandes do staging (mas mantê-los no disco):**
```bash
git rm --cached car_prices.csv
git rm --cached car_prices.xml
```

**2. Adicionar a atualização do .gitignore:**
```bash
git add .gitignore
```

**3. Fazer commit das mudanças:**
```bash
git commit -m "Remove arquivos grandes do Git (adicionados ao .gitignore)"
```

**4. Fazer push novamente:**
```bash
git push -u origin main
```

---

## Alternativa: Se já fez commit anteriormente

Se já fez commit com esses arquivos, precisa remover do histórico:

**1. Remover do último commit (se ainda não fez push):**
```bash
git reset --soft HEAD~1
git rm --cached car_prices.csv car_prices.xml
git add .gitignore
git commit -m "Initial commit: Sistema RPC com XML-RPC e gRPC (sem arquivos grandes)"
```

**2. Se já fez push, precisa forçar (CUIDADO!):**
```bash
git rm --cached car_prices.csv car_prices.xml
git add .gitignore
git commit -m "Remove arquivos grandes"
git push
```

---

## Nota

Os arquivos `car_prices.csv` e `car_prices.xml` continuarão no seu computador, mas não serão enviados para o GitHub. 
Se precisar compartilhar esses arquivos, considere:
- Usar Git LFS (Large File Storage)
- Ou adicionar instruções no README para gerar esses arquivos localmente

