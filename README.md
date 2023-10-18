<!DOCTYPE html>
<html>

<head>
  <title>Kivy Currency Exchange App</title>
</head>

<body>

  <h1>Kivy Currency Exchange App</h1>

  <p>Este projeto é um aplicativo simples de câmbio de moeda construído usando o Kivy, um framework Python para o desenvolvimento de aplicativos com tela sensível ao toque.</p>

  <h2>Recursos</h2>

  <ul>
    <li>Exibe as taxas de câmbio para USD/BRL, EUR/BRL, BTC/BRL e ETH/BRL.</li>
    <li>Obtém as taxas de câmbio da [AwesomeAPI](https://economia.awesomeapi.com.br/).</li>
    <li>Utiliza o framework Kivy para a interface gráfica do usuário (GUI).</li>
  </ul>

  <h2>Instalação e Configuração</h2>

  <ol>
    <li>Clone o repositório:
      <pre>
git clone https://github.com/seu_nome_de_usuario/kivy-currency-exchange-app.git
cd kivy-currency-exchange-app
      </pre>
    </li>

    <li>Instale os pacotes necessários. Certifique-se de ter o Python e o pip instalados.
      <pre>
pip install kivy requests
      </pre>
    </li>

    <li>Execute a aplicação:
      <pre>
python main.py
      </pre>
    </li>
  </ol>

  <h2>Como Usar</h2>

  <ol>
    <li>A aplicação obtém as taxas de câmbio em tempo real para USD/BRL, EUR/BRL, BTC/BRL e ETH/BRL.</li>
    <li>Inicie a aplicação para visualizar as taxas de câmbio das moedas especificadas.</li>
  </ol>

  <h2>Como Funciona</h2>

  <ul>
    <li>A aplicação usa a AwesomeAPI para obter as últimas taxas de câmbio para as moedas especificadas (USD, EUR, BTC, ETH).</li>
    <li>O Kivy é utilizado para criar a interface gráfica do usuário (GUI).</li>
    <li>As taxas de câmbio são exibidas na GUI ao iniciar a aplicação.</li>
  </ul>

  <h2>Contribuições</h2>

  <p>Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:</p>

  <ol>
    <li>Faça um fork do repositório.</li>
    <li>Crie um novo branch para sua funcionalidade ou correção de bug: <code>git checkout -b feature/sua-funcionalidade</code> ou <code>git checkout -b bugfix/sua-correcao</code>.</li>
    <li>Faça suas alterações e as comite: <code>git commit -m 'Descrição das suas alterações'</code>.</li>
    <li>Envie para o branch: <code>git push origin feature/sua-funcionalidade</code> ou <code>git push origin bugfix/sua-correcao</code>.</li>
    <li>Crie uma pull request no GitHub.</li>
  </ol>

  <h2>Licença</h2>

  <p>Este projeto está licenciado sob a [Licença MIT](LICENSE).</p>

  <h2>Agradecimentos</h2>

  <ul>
    <li>[Kivy](https://kivy.org/): Framework Python de código aberto para o desenvolvimento de aplicativos multi-touch.</li>
    <li>[AwesomeAPI](https://economia.awesomeapi.com.br/): API usada para obter as taxas de câmbio em tempo real.</li>
  </ul>

</body>

</html>

