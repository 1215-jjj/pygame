import pygame
import random

class Game:
    def __init__(self):
        self.snake = [(100, 50), (90, 50), (80, 50)]
        self.direction = pygame.K_RIGHT
        self.food = self._place_food()
        self.score = 0
        self.game_over = False

    def _place_food(self):
        return (random.randint(0, 79) * 10, random.randint(0, 59) * 10)

    def start_game(self):
        self.game_over = False

    def end_game(self):
        self.game_over = True

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        if self.direction == pygame.K_UP:
            head_y -= 10
        elif self.direction == pygame.K_DOWN:
            head_y += 10
        elif self.direction == pygame.K_LEFT:
            head_x -= 10
        elif self.direction == pygame.K_RIGHT:
            head_x += 10

        new_head = (head_x, head_y)

        # Check for collisions with the walls
        if head_x < 0 or head_x >= 800 or head_y < 0 or head_y >= 600:
            self.end_game()
            return

        # Check for collisions with itself
        if new_head in self.snake:
            self.end_game()
            return

        self.snake = [new_head] + self.snake[:-1]

        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self._place_food()
            self.score += 1

    def change_direction(self, direction):
        # Prevent the snake from reversing
        if direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = direction
        elif direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = direction
        elif direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = direction
        elif direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = direction

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], 10, 10))