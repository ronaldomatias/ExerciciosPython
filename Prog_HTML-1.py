title = input("Digite o titulo: ")
nome = input("Qual seu nome? ")

htmlString = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> '''+title+''' </title>
  <style>
    body {
      width: 100%;
      height: 100%;
      background-color: yellow;
    }
    .divContainer {
      height: 100px;
      width: 100px;
      background-color: green;
    }
    @media (max-width: 480px) {
        body {
            background-color: gray;
        }
    }
  </style>
</head>
<body class="container">

  <div class="divContainer"><img class="img" src="https://images8.alphacoders.com/105/thumb-1920-1054256.jpg"/></div>
  <div class="divNome"><h1> Olá, '''+nome+''' </h1></div>

  <script>
    const bodyScript = document.querySelector(".container")
    const divContainer = document.querySelector(".divContainer")
    bodyScript.addEventListener("click", () => {
      divContainer.innerHTML = "Teste"
    });
  </script>

</body>
</html>'''

with open("C:\\Users\\ronal\\OneDrive\\Documentos\\Documentos faculdade\\2 SEMESTRE\\Programação Estruturada\\ATIVIDADES\\LISTA05\\Prog_HTML.html", 'w') as html:
    html.write(htmlString)