# SweetHalloween
Pratical Assignment

*#Portuguese*

**1. Introdução**
Este projeto consiste em um jogo desenvolvido em Python utilizando a biblioteca Pygame.
O jogo é um shoot 'em up, onde o jogador controla um personagem que se move horizontalmente e atira em inimigos que possuem diferentes comportamentos.

**2. Objetivo do Jogo**
O objetivo principal do jogo é sobreviver ao ataque de diferentes tipos de inimigos e acumular itens suficientes para avançar pelas fases.
O jogo termina com uma tela de vitória caso o jogador colete itens suficientes ou uma tela de derrota se o jogador for atingido duas vezes.

**3. Funcionalidades do Jogo**
- Movimento do Jogador: O jogador se move horizontalmente ao longo da tela e pode atirar em qualquer direção com base na posição do mouse.
- Sistema de Tiro: O jogador atira projeteis em direção à posição do mouse.
- Escudo do Jogador: O jogador começa com um escudo que o protege de um ataque. Se o jogador for atingido, o escudo é desativado e o jogador ganha um breve período de invulnerabilidade.
- Sistema de Fases: O jogo possui 3 fases. O jogador coleta itens que caem dos inimigos. Ao acumular 10 itens, o jogador passa de fase.
- Inimigos:
  - Inimigo Red Eye: Se move horizontalmente e atira periodicamente.
  - Inimigo Blob: Atira mais rapidamente que o inimigo vermelho.
  - Inimigo Ghost: Se move diagonalmente.
- Itens de Coleta: Ao derrotar inimigos, ocasionalmente, eles derrubam itens. Esses itens devem ser coletados pelo jogador, e ao juntar 10 deles, o jogador passa de fase.
- Sistema de Derrota: Se o jogador for atingido sem o escudo ativo, o jogo exibe uma tela de derrota com as opções: "Voltar ao Menu" ou "Sair".
- Sistema de Vitória: Ao juntar 10 itens na fase 3, o jogo exibe uma tela de vitória com as opções: "Voltar ao Menu" ou "Sair".

**4. Menus**
Menu Principal: O jogador pode escolher entre as opções "Jogar", "Créditos", ou "Sair".
Tela de Vitória: Ao coletar 10 itens na fase 3 o jogador vê a mensagem "Você ganhou" com opções para voltar ao menu principal ou sair do jogo.
Tela de Derrota: Se o jogador perder, é exibida a mensagem "Você perdeu", com as opções de voltar ao menu ou sair do jogo.

**5. Conclusão**
Este projeto de jogo em Pygame demonstra o uso de conceitos fundamentais de desenvolvimento de jogos, como sistemas de movimentação, colisão, mecânicas de escudo e fases. A interface gráfica foi desenvolvida de forma clara, com feedback visual adequado para o jogador.

O jogo pode ser expandido com mais fases, tipos de inimigos, armas, e elementos de narrativa, tornando-o um projeto com grande potencial para crescimento.

*# English:*

**1. Introduction**
This project is a game developed in Python using the Pygame library.
The game is a shoot 'em up, where the player controls a character that moves horizontally and shoots at enemies with different behaviors.

**2. Game Objective**
The main objective of the game is to survive attacks from various types of enemies and collect enough items to progress through the levels.
The game ends with a victory screen if the player collects enough items or a defeat screen if the player is hit twice.

**3. Game Features**
- Player Movement: The player moves horizontally across the screen and can shoot in any direction based on the mouse position.
- Shooting System: The player fires projectiles towards the mouse position.
- Player Shield: The player starts with a shield that protects them from one attack. If the player is hit, the shield is deactivated, and the player gains a brief period of invulnerability.
- Level System: The game has 3 levels. The player collects items dropped by enemies. By collecting 10 items, the player advances to the next level.
- Enemies:
  - Red Eye Enemy: Moves horizontally and shoots periodically.
  - Blob Enemy: Shoots more rapidly than the red enemy.
  - Ghost Enemy: Moves diagonally.
- Collectible Items: Enemies occasionally drop items when defeated. These items must be collected by the player, and collecting 10 of them advances the player to the next level.
- Defeat System: If the player is hit without the shield active, the game displays a defeat screen with options: "Return to Menu" or "Exit."
- Victory System: Upon collecting 10 items in level 3, the game displays a victory screen with options: "Return to Menu" or "Exit."

**4. Menus**
Main Menu: The player can choose between "Play," "Credits," or "Exit."
Victory Screen: After collecting 10 items in level 3, the player sees the message "You Won" with options to return to the main menu or exit the game.
Defeat Screen: If the player loses, the message "You Lost" is displayed, with options to return to the menu or exit the game.

**5. Conclusion**
This Pygame project demonstrates the use of fundamental game development concepts, such as movement systems, collision detection, shield mechanics, and level progression. The graphical interface was developed clearly, with appropriate visual feedback for the player.

The game can be expanded with additional levels, enemy types, weapons, and narrative elements, making it a project with significant growth potential.
