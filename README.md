# validação-de-ips

## Projeto em Python para Validação de Endereços IP e Demonstração de Conceitos de Erros

Este projeto em Python tem como objetivo principal validar endereços IPv4, além de ilustrar conceitos fundamentais de erros em programação e técnicas de tratamento de exceções. Foi desenvolvido como parte de uma atividade prática do curso Mentorama.

## Descrição Detalhada

O projeto consiste em um único script Python (`PY4.py`) que executa as seguintes tarefas:

1.  **Validação de Endereços IPv4:**
    * O script lê uma lista de endereços IP a partir de um arquivo de entrada chamado `entrada_ips.txt`. Este arquivo é criado automaticamente pelo script com alguns exemplos, mas pode ser modificado para incluir outros endereços.
    * Cada endereço IP é validado para garantir que segue o formato correto (quatro octetos separados por pontos) e que cada octeto esteja dentro do intervalo válido (0 a 255).
    * Os endereços válidos e inválidos são separados e os resultados são escritos em um arquivo de saída chamado `relatorio_ips.txt`. Além disso, os resultados são impressos no console para facilitar a visualização.

2.  **Conceitos de Erros em Programação:**
    * O script inclui exemplos concisos para demonstrar os três tipos principais de erros que podem ocorrer em programação:
        * **Erro de Sintaxe:** Ocorre quando o código não segue a sintaxe correta da linguagem Python (por exemplo, parênteses não fechados, erros de digitação). Esses erros impedem a execução do programa.
        * **Erro de Tempo de Execução:** Ocorre durante a execução do programa, geralmente devido a operações inválidas ou entradas inesperadas (por exemplo, tentar converter uma string não numérica em um inteiro, dividir por zero).
        * **Erro Semântico:** Ocorre quando o código executa sem gerar erros, mas o resultado obtido não é o esperado devido a um erro na lógica do programa (por exemplo, usar a fórmula errada para calcular uma média).

3.  **Tratamento de Erros com `try`, `except`, `else` e `finally`:**
    * O script demonstra como usar o bloco `try-except-else-finally` para lidar com exceções, especificamente no contexto de entrada de dados do usuário.
    * A função `entrada_idade()` solicita ao usuário que digite sua idade.
        * O bloco `try` tenta converter a entrada do usuário para um inteiro. Se a entrada não for um número válido, um `ValueError` é levantado.
        * O bloco `except ValueError` captura esse erro e imprime uma mensagem de erro amigável para o usuário.
        * Se a conversão for bem-sucedida (ou seja, não houver exceção), o bloco `else` é executado e imprime a idade digitada.
        * O bloco `finally` é sempre executado, independentemente de ocorrer ou não uma exceção, e imprime uma mensagem de encerramento.

## Instalação

Para executar este projeto, você precisa ter o Python instalado em sua máquina. A versão 3.x é recomendada.

1.  **Verifique a versão do Python:** Abra o terminal ou prompt de comando e execute o seguinte comando para verificar se o Python está instalado e qual versão está sendo usada:

    ```bash
    python --version
    ```

2.  **Clone o repositório:** Use o Git para clonar o repositório para o seu computador. Se você não tiver o Git instalado, você pode baixar o código como um arquivo ZIP e extraí-lo.

    ```bash
    git clone [https://github.com/Yurigomes007/validacao-de-ips](https://github.com/Yurigomes007/validacao-de-ips)
    ```

3.  **Navegue até o diretório do projeto:**

    ```bash
    cd validacao-de-ips
    ```

## Como Usar

1.  **Validação de Endereços IP:**

    * **Arquivo de entrada (`entrada_ips.txt`):**
        * O script cria automaticamente este arquivo com alguns endereços IP de exemplo.
        * Você pode modificar este arquivo para incluir os endereços IP que deseja validar. Cada endereço IP deve estar em uma linha separada.
        * Exemplo de conteúdo de `entrada_ips.txt`:

            ```
            200.135.80.9
            192.168.1.1
            8.35.67.74
            257.32.4.5
            85.345.1.2
            1.2.3.4
            9.8.234.5
            192.168.0.256
            ```

    * **Executar o script:**
        * Abra o terminal e certifique-se de que você está no diretório do projeto.
        * Execute o script Python:

            ```bash
            python PY4.py
            ```

    * **Resultados:**
        * O script irá imprimir os endereços IP válidos e inválidos no console.
        * Além disso, ele irá gerar um arquivo chamado `relatorio_ips.txt` no mesmo diretório, contendo os resultados da validação.

2.  **Exemplo de Tratamento de Erros:**

    * Ao executar o script `PY4.py`, a função `entrada_idade()` será chamada.
    * O script irá solicitar que você digite sua idade.
    * **Entrada válida:** Se você digitar um número inteiro válido, o script irá imprimir a idade digitada.
    * **Entrada inválida:** Se você digitar qualquer coisa que não seja um número inteiro (por exemplo, letras, símbolos), o script irá capturar o `ValueError` e imprimir uma mensagem de erro informando que você deve digitar um número inteiro válido.
    * Em ambos os casos, o script irá imprimir a mensagem "Encerrando programa." ao final, demonstrando o uso do bloco `finally`.

## Funcionalidades Principais

* **Validação de endereços IPv4:** Implementação de uma função que verifica se um endereço IP está no formato correto e se os octetos estão dentro do intervalo válido (0-255).
* **Leitura de endereços IP de um arquivo:** Capacidade de ler uma lista de endereços IP a partir de um arquivo de texto (`entrada_ips.txt`).
* **Escrita de resultados em um arquivo:** Geração de um arquivo de relatório (`relatorio_ips.txt`) contendo a lista de endereços IP válidos e inválidos.
* **Impressão de resultados no console:** Exibição dos resultados da validação no terminal para feedback imediato.
* **Demonstração de conceitos de erros:** Exemplos claros e concisos de erros de sintaxe, tempo de execução e semânticos.
* **Tratamento de exceções:** Uso do bloco `try-except-else-finally` para lidar com a entrada de dados do usuário e garantir que o programa não quebre devido a entradas inválidas.

## Estrutura do Projeto

A estrutura do projeto é simples e organizada:
validacao-de-ips/

├── PY4.py           # Script Python principal
├── README.md        # Este arquivo (documentação)
├── entrada_ips.txt  # Arquivo de entrada com os IPs a serem validados
└── relatorio_ips.txt # Arquivo de saída com os resultados da validação

* `PY4.py`: Contém o código Python que realiza a validação de IP, demonstra os conceitos de erros e implementa o tratamento de exceções.
* `README.md`: Este arquivo, que fornece documentação sobre o projeto.
* `entrada_ips.txt`: Arquivo de texto que contém a lista de endereços IP a serem validados.
* `relatorio_ips.txt`: Arquivo de texto gerado pelo script, contendo os resultados da validação.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria, correção de bugs ou novas funcionalidades, sinta-se à vontade para contribuir com o projeto.

Para contribuir:

1.  **Fork o repositório:** Crie uma cópia do repositório na sua conta do GitHub.
2.  **Crie um branch:** Crie um branch para a sua alteração. Use um nome descritivo para o branch (por exemplo, `feature/nova-funcionalidade` ou `bugfix/correcao-de-bug`).

    ```bash
    git checkout -b feature/nova-funcionalidade
    ```

3.  **Faça as alterações:** Implemente as alterações desejadas. Certifique-se de que o código esteja bem comentado e siga as convenções de estilo do Python (PEP 8).
4.  **Faça o commit das alterações:**

    ```bash
    git commit -am 'Adiciona nova funcionalidade ou Corrige bug'
    ```

    Use uma mensagem de commit clara e descritiva.

5.  **Faça o push para o branch:**

    ```bash
    git push origin feature/nova-funcionalidade
    ```

6.  **Abra um Pull Request:** Envie um Pull Request para o branch `main` do repositório original. Descreva claramente as alterações que você fez e o motivo delas.

## Licença

Este projeto é licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).

A licença MIT é uma licença de código aberto permissiva que permite que outros usem, copiem, modifiquem, combinem, publiquem, distribuam, sublicenciem e/ou vendam cópias do software.

Para mais detalhes, consulte o arquivo [LICENSE.md](LICENSE.md).

## Autor

Yuri Dos Anjos

---
```
