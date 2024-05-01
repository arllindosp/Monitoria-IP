# Festival de Outono🎃🍂

MEUU DEUS?? JÁ É OUTONO! E os preparativos para Feira do Vale do Orvalho já começaram ! A feira é um evento especial que acontece anualmente em Stardew Valley e é organizada pelo Prefeito Lewis. Durante a festividade os participantes podem interagir com os moradores locais e disputar concursos diversos. Participar da feira é uma grande oportunidade para exibir os recursos produzidos e cultivados durante a estação de Outono. E Elisandrade, uma fazendeira local, está determinada em não deixar essa chance passar despercebida.

![fall](https://github.com/arllindosp/Monitoria-IP/assets/134821451/e462edfc-58c5-4857-ac19-4b35cb6c28d6)

Elisa está ansiosa para concorrer na **Exposição de Produtos**, uma competição realizada durante a feira. Nessa disputa, os fazendeiros selecionam os itens de sua colheita e os apresentam em bancadas decoradas e dispostas em uma configuração matricial,ou seja, no formato de uma matriz de duas dimensões.Nesse sentido, os juízes irão escolher e premiar a bancada mais atraente. Determinados em impulsioar as chances de vitória , você e Elisa decidem consultar o **Oráculo** no **Estande da Clarevidência** para descobrir a melhor maneira de criar a apresentação mais visualmente atraente. Com sua habilidade para antecipar o futuro , o Oráculo usa sua magia e fornece um algorítimo para construir uma exposição capaz de encantar os olhos dos avaliadores.Entretanto,Elisandrade sofre de **Perda de Memória Recente** e em virtude disso esqueceu as instruções providas pelo Oráculo, porém, o acompanhente de Elisa, que nesse contexto é você, ainda se recorda de tudo e vai ajuda-la a vencer a competição.

## Input

A princípio, as percepções do oráculo indicam que você recebrá um linha no seguinte formato:

> **M x N**

Onde **M** e **N** são números que constituem o conjunto dos inteiros positivos, e cujos valores definem as dimensões da matriz que representa a bancada de exposião. **M** representa o número de linhas e **N** o de colunas.

Em seguida você recebrá um inteiro **E**:

> **E**

Onde **E** Define o total de elementos que Elisandrade troxue consigo para exibir no concurso.

Após isso , você recebrá a seguinte entrada E-vezes:

> **a (i,j)**

Onde **a** é um inteiro que representa o nível de atratividade de um elemento da bancada e **i** ,**j** são inteiros positivos que definem respectivamente a linha e a coluna nas quais **a** tem de ser posicionado. $$ a, i, j \in \mathbb{Z}^+ $$

**Exemplo:**

Se a entra for:

> **8 (2,3)**

Então isso significa que o elemento representado pelo número 8 (que também representa o valor da sua atratividade), deve ser posicionado,a princípio, na linha 2 e coluna 3 da nossa matriz.

Seguindo as orientações do Oráculo, depois você receberá linhas no seguinte modelo uma quantidade indefinida de vezes:

> **Operacao1**
>
> **Operacao2**
>
> **Oprecao3**
>
> .
>
> .
>
> .
>
> **Fim**

Onde cada operação indica uma ação de reordenação da bancada representada no modelo matricial. Existem três tipos distintos de operações de ordenção, cujas definições estão listadas abaixo:

1. Se a operação for **'Substituir'** então você receberá uma nova entrada:

   > (i,j) (k,l)

   após isso você deve realizar a permutação dos elementos localizados nas coordenadas (i,j) e (k,l) da matriz, trocando seus valores respectivos entre si.

2. Se a operação for **'Transposição'** então você deverá performar a operação de transposição na matriz que define nossa bacada de exposição, ou seja, você precisa obter a sua transposta.

   **Obs:**
   A transposição de uma matriz é uma operação que consiste em trocar suas linhas pelas colunas e vice-versa, resultando em uma nova matriz.

   $$
   A = \begin{bmatrix}
   a & b \\
   c & d \\
   e & f
   \end{bmatrix}
   $$

   $$

   A^T = \begin{bmatrix}
   a & c & e \\
   b & d & f
   \end{bmatrix}


   $$

💡Dica: Para mais informações sobre matriz transposta —> **[Clique aqui](https://www.todamateria.com.br/matriz-transposta/)**

3. Por outro lado se a operação for igual a 'Remover':

   Você deve buscar o elemento com o menor nível de atratividade e remove-lo da bancada de exibição.

   **Atenção**: Funcões como Max(), Min() e afins estão proibidas nessa questão

4. Finalmente, se a Operação for igual a **'Fim'** nenhuma nova operação será recebida e o processo de ordenção da bancada se encerra.

💡Dica: O método **split()** pode ser muito útil

💡Dica: Usar string **slicing** pode auxiliar na questão

## Output

Por fim, após todas as operações de rearranjo orientadas pelas previsões do Oráculo serem concluídas, você deve printar a estrutura da matriz na disposição em que ela se encontra após todas as oprações terrem sido efetuadas no seguinte modelo:

$
\text{Atual arranjo:}\\
\begin{matrix}
a_{11} & a_{12} & \cdots & a_{1q} \\
a_{21} & a_{22} & \cdots & a_{2q} \\
\vdots & \vdots & \ddots & \vdots \\
a_{p1} & a_{p2} & \cdots & a_{pq}
\end{matrix} 
$
