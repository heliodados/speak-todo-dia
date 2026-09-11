# Speak Todo Dia na Play Store: o que colocar em cada campo

## Arquivos desta pasta
- `SpeakTodoDia.aab` (na pasta do app, gerado por `gradlew bundleRelease`): é o que se envia na loja. O APK é só para instalar direto.
- `icone-512.png`: ícone do app (512 x 512).
- `destaque-1024x500.png`: imagem de destaque.
- `tela-*.png`: capturas de tela do celular (412 x 824).
- Política de privacidade: https://heliodados.github.io/speak-todo-dia/privacidade.html

## Detalhes do app
- **Nome do app:** Speak Todo Dia
- **Descrição breve (até 80 caracteres):**
  Inglês do dia a dia para crianças: ouça, repita no microfone e jogue.
- **Descrição completa:**

  O Speak Todo Dia ensina palavras em inglês do dia a dia de um jeito que criança gosta: ouvindo, falando e jogando.

  🔊 540 palavras e frases, todas com voz de verdade, em 27 temas: casa, escola, comida, animais, animais do mar, corpo, família, cores, números, roupas, cidade, futebol, videogame, super-heróis, carros, barcos, natureza, tempo, sentimentos, profissões, verbos, perguntas, frases e conversa.

  🎤 Aba Falar: o app fala a palavra, a criança repete no microfone e vê lado a lado o que disse e a palavra certa, com uma nota de quanto ficou parecido.

  🎮 Jogo com três níveis: no Iniciante ela escolhe a resposta, no Médio também fala, no Difícil também escreve. Cada tema vale até 3 estrelas.

  🏁 Corrida de palavras: a criança corre contra o Pipo, o papagaio mascote. Cada acerto o carro anda uma casa. Quem chega primeiro na bandeira ganha.

  📚 Dicionário: procure qualquer palavra em português ou em inglês e ouça a pronúncia.

  🔤 Verbos: 40 verbos com as três formas, "I eat, you eat, he eats", faladas em voz alta.

  📈 Evolução: dias seguidos de treino e uma linha do tempo com tudo o que a criança fez.

  Sem anúncios, sem compras, sem cadastro. Funciona sem internet: só o microfone usa o reconhecimento de voz do Android, que precisa de conexão.

  Feito por um pai para o filho de 10 anos, em português do Brasil.

- **Categoria:** Educação
- **E-mail de contato:** heliodados@gmail.com
- **Política de privacidade:** https://heliodados.github.io/speak-todo-dia/privacidade.html

## Formulários (respostas)
- **Acesso ao app:** todas as funções estão disponíveis sem login.
- **Anúncios:** não, o app não contém anúncios.
- **Classificação de conteúdo (questionário IARC):** categoria "Referência, notícias ou educacional"; responder "não" para violência, sexo, linguagem imprópria, drogas, apostas, compras, interação entre usuários, compartilhamento de localização. Resultado esperado: Livre (L).
- **Público-alvo:** marque as faixas de 6 a 8, 9 a 12 e 13 a 15 anos, além de adultos. Como inclui crianças, o app entra na política "Famílias": ele cumpre, porque não tem anúncios, compras nem coleta de dados. Na pergunta "o app pode atrair crianças involuntariamente?", responda que ele é feito para crianças.
- **Segurança de dados:**
  - Coleta ou compartilha dados do usuário? **Não.**
  - Os dados são criptografados em trânsito? Não se aplica (nada é enviado).
  - Permite pedir exclusão de dados? Não se aplica (nada é guardado fora do aparelho).
  - Observação para o formulário de permissões: a permissão de microfone é usada só na atividade "Falar"; o áudio é processado pelo reconhecimento de voz do próprio Android e o app recebe apenas o texto.
- **Apps governamentais / notícias / financeiros / saúde:** não.
- **Declaração de permissões (RECORD_AUDIO):** uso principal, "a criança repete palavras em inglês e o app confere a pronúncia".

## Teste fechado (conta pessoal nova)
Antes da publicação aberta, o Google exige 14 dias de teste fechado com 12 testadores que aceitem o convite e mantenham o app instalado. Crie a faixa "Teste fechado", adicione os e-mails dos testadores (família e amigos), envie o link que a loja gera, e depois de 14 dias peça o "acesso à produção" no painel.

## Cada versão nova
1. Subir `versionCode` (e `versionName`) em `android/app/build.gradle.kts`.
2. `gradlew bundleRelease` na pasta `android/` (com JAVA_HOME apontando para o Java do Android Studio).
3. Enviar o `.aab` novo em Produção ou na faixa de teste.
