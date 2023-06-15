# Experimentos de redes neurais artificiais

Atualmente, redes neurais artificiais são um dos assuntos mais comentados na área da programação, principalmente após o lançamento de algoritmos como o ChatGPT e Dalle-O. Nessa parte do curso, estaremos trabalhando com experimentos relacionados à criação de uma Rede Neural simples (talvez a mais simples possível), desde os conceitos teóricos mais fundamentais até a aplicação dela para um problema de minização, no experimento R.07.

Em uma breve introdução, as redes neurais artificiais são algoritmos usados para resolver problemas complexos ao tentar copiar o comportamento biológico de encéfalos animais, que são capazes de abstrair informações e gerar respostas compatíveis com os "inputs" ou dados de entrada. Dessa maneira, os dados de entrada são processados a cada camada de neurônio. A progressão de camadas garante diferentes interações entre diferentes neurônios, complexificando o algoritmo para níveis surpreendentes. Um conceito muito interessante associado com redes neurais é aprendizado profundo, que está relacionado com as camadas ocultas. As camadas ocultas são o bruto de uma rede neural, o miolo do algoritmo. A primeira camada é uma camada de input, ou seja de entrada dos dados. A partir dela, todas as camadas serão consideradas parte da camada oculta, com excessão da última, que será a saída. No caso de redes neurais já bem estabelecidos como o caso do ChatGPT, a Camada Oculta pode conter milhões de neurônios, espalhados em milhares de camadas. Nesse contexto, aprendizado profundo está relacionado com o uso extensivo da camada oculta ao longo de ciclos, de maneira a fazer uma rede neural aprender extremamente bem a executar seu objetivo. Cada ciclo, ou época, está melhorando as redes neurais, mudando apenas os parâmetros presentes na camada oculta.

Em cada um dos experimentos abaixo, aprendemos um conceito de redes neurais de maneira prática. Sinta-se livre para usufrui-los!

experimento R.01 - derivadas: Nesse experimento, verificamos a aplicação de derivadas em um código no python. Derivadas são essenciais para o cálculo do gradiente, parte fundamental de redes neurais.

experimento R.02 - classes: Nesse experimento, aprendemos o básico do básico de classes em python, como os métodos dunder (e aqueles que não são dunder), assim como praticamos alterar estados por dentro e por fora das classes.

experimento R.03 - construindo um grafo automaticamente: Esse experimento é bastante importante. Nele, estamos definindo como utilizar uma classe para gerar o grafo computacional. Com esse grafo, poder-se-á calcular os gradientes locais necessários para realizar o backpropagation.

experimento R.04 - computando gradientes locais: Com a classe Valor, que é o Grafo computacional produzido no experimento anterior, podemos computar os gradientes locais. Essa computação é denominada backpropagation, já que começa do vértice folha e termina no vértice raiz.

experimento R.05 - finalizando a classe Valor: Nesse experimento, finalizamos a classe Valor ao adicionar nela todas as operações possíveis de serem feitas por uma rede Neural simples.

experimento R.06 - redes neurais artificiais: Nesse experimento, organizamos em maior parte nossa primeira rede neural. Foi montado a classe Neurônio, a classe camada, e a classe MLP (relativo à rede neural Multi Layer Perceptron)

experimento R.07 - treinando uma rede neural: Nesse experimento, terminamos todo o processo de montar uma rede neural e finalmente podemos treiná-la para nos resolver um problema.

experimento R.08 - treinando uma rede neural com pytorch: Agora que já fizemos uma rede neural utilizando python puro, temos uma outra opção para trabalhar com redes neurais: utilizar o módulo neural networks (nn) da biblioteca pytorch.
