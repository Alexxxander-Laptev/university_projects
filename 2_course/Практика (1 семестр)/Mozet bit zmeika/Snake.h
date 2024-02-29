#pragma once

#ifndef SNAKE_H
#define SNAKE_H

#include <SFML/Graphics.hpp>
#include <vector>

class Snake
{
private:
	std::vector<sf::Vector2i> m_body;
	sf::RectangleShape m_rect;
	sf::Vector2i m_vector_move;
public:
	int plaerScore;
	Snake();
	void setVectorMove(const sf::Vector2i move);
	void add();
	void move();
	int getSize() const;
	bool collision() const;
	bool collision(sf::Vector2i pix) const;
	void draw(sf::RenderWindow &win);
};

#endif