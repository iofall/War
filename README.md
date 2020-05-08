# Game of War

This is a simple CLI Python game created to emulated the War Card Game.

Simply download the `war.py` Python file and execute it in the command line to play the game.

### Description

War is a card game played between two players. The game is completely based on chance.

**From Wikipedia**

War is a simple card game played between two players, where the goal is to win all the cards. 

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war". Both players place the next card of their pile face down (some variants have three face down cards) and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

Most descriptions of War are unclear about what happens if a player runs out of cards during a war. n some variants, that player immediately loses. In others, the player may play the last card in their deck as their face-up card for the remainder of the war or replay the game from the beginning.

### Implementation

This project implements the game with similar rules as above but with the below variation:

- In case of war, we draw three cards face down and one card face up for comparison from each player.
- During comparison in a war, if again both the cards are of equal rank again `war_routine()` is called which draws three cards face down and one card face up from each player as described above and comparison is made. This routine continues until a player's card ranks higher than the other or one of the players runs out of cards.
- In this project, when a player runs out of cards, the player immediately loses.
- `war_single_routine()` function is also implemented, which is a variation of the `war_routine()`. In this case one card gets drawn face down and one is drawn face up from each player for comparison. The function has been commented out, just uncomment it and comment `war_routine()` to play this implementation.

### Notes

- It is important to remember that `strings` are iterable, when using `list.extend()`. This can cause problems especially when only one card which is a string is supplied to this `.extend()` method, because it adds every character in the `string` to the list.

- When adding cards to a `hand`, we are shuffling them inside the `.add()` method of the hand class.

  This is done to avoid an infinitely running game, because unless shuffling of cards occurs, it is possible to have an infinitely running game provided the player's initial hands are oriented to facilitate this. This can easily happen by chance, since a deck only has 52 cards.

### Acknowledgements

This project was created with reference to **Jose Portilla's Full Stack Django Development Course**, although it has been heavily modified.
