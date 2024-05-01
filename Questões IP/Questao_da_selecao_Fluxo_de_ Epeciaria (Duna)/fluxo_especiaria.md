**Arrakis**, também conhecido como Duna pelos fremen, é um planeta desértico e inóspito localizado nas porções mais remotas do Império. Ele é o único local conhecido onde a especiaria é encontrada naturalmente e em abundância. O **melange**, a especiaria, é uma substância vital para o controle político, econômico e religioso do Império, uma vez que ela confere habilidades mentais aumentadas e é usada para propósitos de navegação interestelar. Nesse contexto, o Imperador designou você e sua casa para administrar a produção e colheita desse recurso de valor inestimável.
![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDFwdjlqN3J0aGV2djYzY3h0cWp0NTZqaGl0ZW9neDBzOHZ2ZXVsMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RH3T4tnO50NiAfiTWY/giphy.gif)

O processo de colheita da especiaria se ampara no uso de **colheitadeiras:** grandes máquinas capazes de penetrar as camadas de areia e rocha do deserto, onde a especiaria está concentrada. Entretanto, a extração de especiaria em Arrakis é incrivelmente perigosa, principalmente devido à ameaça constante dos **vermes de areia:** grandes criaturas sensíveis às vibrações produzidas pela atividade e operação das colheitadeiras. Nesse sentido, você foi encarregado de garantir a segurança da equipe de coleta, supervisionando o processo de fabricação de melange, e para isso lhe foi entregue um sensor sísmico, capaz de detectar as vibrações na areia do deserto e identificar se um verme está à espreita. Também lhe foi entregue um manual expondo como funciona o dispositivo.

![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXh2djE4bmVtZGh3N3M5dXA2ZDh0eTVpdWNsb3JhZzFvcGVvOGQ4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zdluWXCOtwnTF57ZeX/giphy.gif)

## Manual de Instruções

> **_decodificador_fremen():_** Primeiro o sensor detecta as ondas sísmicas e as transforma em um padrão numérico fremen. **_O decodificador_** é projetado para converter valores numéricos **fremen** para valores numéricos convencionais, uma vez que **os fremen( nativos de Arrakis)** utilizam um sistema numérico distinto do convencional em que os símbolos possuem os seguintes valores e significados :
>
> **ꖔ :** Possui valor igual a 1
>
> **𐋀:** Possui valor igual a 2
>
> ꖡ : Possui valor igual a 3
>
> **𐊿:** Possui valor igual a 4
>
> **𐊾 :** Possui valor igual a 5
>
> **Ex :**
>
> Para exemplificar, o número ꖔ𐋀𐊿𐊾 é o mesmo que: 1+2+4+5, ou seja, 12.
>
> **Obs:** A ordem de disposição dos símbolos não importa, os seus valores sempre são os mesmos independente da ordem.
>
> Portanto, o decodificador traduz as ondas sísmicas representadas em padrões numéricos fremen para o nosso sistema numérico.

> **_conversor_sismico():_** O conversor utiliza dois valores numéricos inteiros ‘a’ e ‘b’ obtidos a partir do **_decodificador_fremen_** e calcula o mdc entre eles utilizando o **_algoritmo de Euclides_**, cuja lógica está explicada abaixo:
>
> Considere dois valores inteiros ‘a’ e ‘b’ dispostos na seguinte ordem (a,b) e que desejamos encontrar o mdc entre eles:
>
> 1. Se a < b, então trocamos a por b e vice-versa
> 2. Se b > 0, dividimos ‘a’ por ‘b’ , então o valor inteiro ‘r’, o resto fruto dessa divisão, é atribuído a ‘b’. Em seguida retornamos ao passo 1.
> 3. Se b = 0, então retornamos ‘a’ como mdc e encerramos o algorítimo.

> **_alerta_VermedeAreia():_** Esse compartimento é projetado para interpretar os valores obtidos a partir do **conversor sísmico** e identificar qual a fonte das vibrações produzidas na superfície da areia. Seu funcionamento ocorre da seguinte forma:
>
> Se os dois inteiros analisados pelo conversor sísmico forem primos entre si, então os abalos sísmicos são fruto da movimentação e aproximação de vermes de areia:
>
> ```python
> razao = 'Verme de Areia'
> ```
>
> Por outro lado, caso eles não sejam primos entre si, temos os seguintes cenários:
>
> 1. Se o valor inteiro obtido do conversor sísmico for maior ou igual a 2 ou menor ou igual a 6, então as vibrações são provocadas por **areia de percussão** :
>
>    ```python
>    razao = 'Areia de Percussão'
>    ```
>
> 2. Se o valor inteiro obtido do conversor sísmico for maior ou igual a 7 ou menor ou igual a 10, então as vibrações são provocadas por **atividade humana** :
>
>    ```python
>    razao = 'Atividade Humana'
>    ```
>
> 3. E finalmente, se o valor inteiro obtido do conversor sísmico for maior que 10, então as vibrações são provocadas por **atividade geológica** :
>
>    ```python
>    	razao = 'Atividade Geológica'
>    ```

Infelizmente um infortúnio ocorreu. Por alguma razão o sensor sísmico foi danificado e os seus compartimentos não estão operando da maneira como deveriam. Sendo assim, antes de coletar e analisar as vibrações sísmicas você precisa reprogramar os compartimentos para que eles voltem a funcionar adequadamente. Lembre-se de que a tecnologia fremen segue sempre uma lógica recursiva, portanto, ao reconstruir as funções dos compartimentos você precisa usar recursão, senão o aparelho não funcionará.

A princípio, você receberá um inteiro **N** que representa o total de dias que você foi encarregado de supervisionar o processo de colheita:

## Input

A princípio, você receberá um inteiro **N** que representa o total de dias que você foi encarregado de supervisionar o processo de colheita:

> N

Em seguida , em cada dia de supervisão, você receberá uma informação que indica quais são as condições climáticas referentes a aquele dia em específico, no formato de string, podendo ser nos seguintes modelos:

> ‘Tempestade de Areia’

> ‘Clima Ameno’

Quando o clima é ameno, a colheita se inicia e o sensor sísmico, cujo portador é você, é ativado. Entretanto, em circunstâncias climáticas desfavoráveis, a colheita não ocorre.

Caso a colheita ocorra e o sensor sísmico seja ativado as seguintes entradas são recebidas:

Inicialmente, você recebe um inteiro **H ,** que indica o total de horas que o sensor e as colheitadeiras devem permanecer em atividade.

> H

Em seguida você receberá as seguintes entradas **H vezes**, que são pares de ondas sísmicas registrados em cada hora de atividade e definidos no sistema numérico fremen pelo sensor **:**

> onda_sismica1

> onda_sismica2

Caso um verme de areia seja detectado, o sensor sísmico é desativado e você deve alertar os demais servos e encerrar a colheita para preservar a segurança de todos.

## Output

Após o fim da análise de cada par de ondas sísmicas é preciso informar o motivo de cada uma

**Ex:**

Se foi constatado que a onda foi provocada por Atividade Humana

> ‘Onda sísmica provocada por: {Atividade Humana}’

Além disso , o imperador exige uma fiscalização diária da colheita de melange para garantir que o fluxo de especiaria não seja interrompido. Nessa perspectiva , você deverá realizar as seguintes análises em cada dia de colheita para contribuir com a fiscalização:

- Caso a colheita seja concluída totalmente:

> ‘Dia ‘x’ | Situação: Colheita concluída’

- Caso a colheita não seja concluída, seja pela atividade de vermes ou em função de tempestades de areia:
  - Caso o motivo seja tempestade de areia:
    > ‘Dia {x} | Situação: Colheita não finalizada| Razão: Tempestade de Areia’
  - Caso o motivo seja verme de Areia:
    > ‘Dia {x} | Situação: Colheita não finalizada| Razão: Verme de Areia’
