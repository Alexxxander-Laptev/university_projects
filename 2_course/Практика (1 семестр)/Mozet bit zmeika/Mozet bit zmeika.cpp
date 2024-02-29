#include <SFML/Graphics.hpp>
#include <sstream>
#include "Snake.h"

using namespace sf;

int main()
{
	int playerScore = 0;
	srand(time(0));
	sf::RenderWindow window(sf::VideoMode(680, 680), "Snake");  // Окно
	window.setFramerateLimit(60);

	enum class gamestate
	{
		menu, run, pause, end
	};

	gamestate game_state = gamestate::menu;

	Font font;
	font.loadFromFile("pixel.ttf");  // Всё, что связано с текстом для вывода очков (шрифт и т.д.)
	Text text("", font, 60);
	text.setStyle(sf::Text::Bold);

	Snake snake;
	sf::Clock clock;
	sf::Time time;

	sf::Vector2i pix(13, 2);  // Начальное положение фрукта
	sf::RectangleShape rect_pix;  // Создание фрукта

	rect_pix.setFillColor(sf::Color::Red);  // Характеристики фрукта (цвет и т.п.)
	rect_pix.setSize(sf::Vector2f(40.f, 40.f));
	rect_pix.setPosition(pix.x * 40 + 40, pix.y * 40 + 40);

	sf::Texture texture;
	texture.loadFromFile("image.png");  // Изображение для меню

	sf::Sprite button_play;  // Кнопка play и её характеристики
	button_play.setTexture(texture);
	button_play.setTextureRect(sf::IntRect(0, 0, 680, 170));
	button_play.setPosition(sf::Vector2f(0.f, 170.f));

	sf::Sprite button_quit;  // Кнопка exit и её характеристики
	button_quit.setTexture(texture);
	button_quit.setTextureRect(sf::IntRect(0, 170, 680, 170));
	button_quit.setPosition(sf::Vector2f(0.f, 340.f));

	sf::Sprite button_pause;  // Меню паузы и её характеристики
	button_pause.setTexture(texture);
	button_pause.setTextureRect(sf::IntRect(0, 340, 680, 170));
	button_pause.setPosition(sf::Vector2f(0.f, 205.f));

	sf::Sprite button_game_over;  // Кнопка game over и её характеристики
	button_game_over.setTexture(texture);
	button_game_over.setTextureRect(sf::IntRect(0, 510, 680, 170));
	button_game_over.setPosition(sf::Vector2f(0.f, 205.f));

	sf::Vertex width[640];  // Сетка и её цвет
	sf::Vertex height[640];
	sf::Color color(70, 70, 70);

	for (int i = 0, w = 0; i < 640; i += 2, w += 40)  // Разлиновка по длине и по высоте
	{
		width[i] = sf::Vertex(sf::Vector2f(w, 40.f), color);
		width[i + 1] = sf::Vertex(sf::Vector2f(w, 640.f), color);
	}
	for (int i = 0, h = 0; i < 640; i += 2, h += 40)
	{
		height[i] = sf::Vertex(sf::Vector2f(40.f, h), color);
		height[i + 1] = sf::Vertex(sf::Vector2f(640.f, h), color);
	}

	while (window.isOpen())
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			switch (event.type)
			{
			case sf::Event::Closed:
				window.close();
				break;
			case sf::Event::MouseButtonPressed:
			{
				if (game_state == gamestate::menu)
				{
					float x = event.mouseButton.x;  // Реакция на мышь
					float y = event.mouseButton.y;
					if (x > 0 && x < 680)
						if (y > 170 && y < 340)
						{
							snake = Snake();  // Все необходимые данные касательно змеи
							game_state = gamestate::run;  // Переход к игре
							playerScore = 0;
						}
						else if (y > 340 && y < 510)
							window.close();  // Выход из игры
				}

				if (game_state == gamestate::end)
				{
					float x = event.mouseButton.x;
					float y = event.mouseButton.y;
					if (x > 0 && x < 680)
						if (y > 205 && y < 375)
						{
							snake = Snake();
							game_state = gamestate::menu;  // Переход в меню
						}
				}
			}
				break;
			case sf::Event::KeyPressed:  // Реакция на различные клавиши
				if (game_state == gamestate::run)
				{
					if (Keyboard::isKeyPressed(Keyboard::Escape))
						game_state = gamestate::menu;
					else if (Keyboard::isKeyPressed(Keyboard::P))
						game_state = gamestate::pause;
					if (Keyboard::isKeyPressed(Keyboard::Left))
						snake.setVectorMove(sf::Vector2i(-1, 0));
					else if (Keyboard::isKeyPressed(Keyboard::A))
						snake.setVectorMove(sf::Vector2i(-1, 0));
					if (Keyboard::isKeyPressed(Keyboard::Right))
						snake.setVectorMove(sf::Vector2i(1, 0));
					else if (Keyboard::isKeyPressed(Keyboard::D))
						snake.setVectorMove(sf::Vector2i(1, 0));
					if (Keyboard::isKeyPressed(Keyboard::Up))
						snake.setVectorMove(sf::Vector2i(0, -1));
					else if (Keyboard::isKeyPressed(Keyboard::W))
						snake.setVectorMove(sf::Vector2i(0, -1));
					if (Keyboard::isKeyPressed(Keyboard::Down))
						snake.setVectorMove(sf::Vector2i(0, 1));
					else if (Keyboard::isKeyPressed(Keyboard::S))
						snake.setVectorMove(sf::Vector2i(0, 1));
				}
				else if (game_state == gamestate::pause)
				{
					if (Keyboard::isKeyPressed(Keyboard::Escape))
						game_state = gamestate::menu;
					else if (Keyboard::isKeyPressed(Keyboard::P))
						game_state = gamestate::run;
				}
				else if (game_state == gamestate::end)
				{
					if (Keyboard::isKeyPressed(Keyboard::Escape))
						game_state = gamestate::menu;
				}
				break;
			}
		}

		if (game_state == gamestate::run)
		{
			time += clock.restart();

			if (time.asMilliseconds() > (250 - snake.getSize()))  // Скорость змеи
			{
				snake.move();
				time = sf::Time::Zero;
			}

			if (snake.collision())  // Проверка на столкновение со стенами
				game_state = gamestate::end;

			if (snake.collision(pix))  // Проверка на поедание фрукта
			{
				snake.add();
				pix = sf::Vector2i((rand() % 15), (rand() % 15));
				rect_pix.setPosition(pix.x * 40 + 40, pix.y * 40 + 40);
				playerScore++;
			}
		}

		window.clear();
		window.draw(width, 64, sf::Lines);
		window.draw(height, 64, sf::Lines);

		if (game_state != gamestate::menu)
		{
			snake.draw(window);  // Рисование содержимого окна карты
			window.draw(rect_pix);
		}
			
		switch (game_state)  // Вывод меню в случае различных исходов
		{
		case gamestate::menu:
			window.draw(button_play);
			window.draw(button_quit);
			break;
		case gamestate::pause:
			window.draw(button_pause);
			break;
		case gamestate::end:
			window.draw(button_game_over);
			break;
		}

		std::ostringstream playerScoreString;  // Всё, что связано с выводом количества очков
		playerScoreString << playerScore;
		text.setString("Score:" + playerScoreString.str());
		text.setPosition(0, -20);
		window.draw(text);

		window.display();
	}

	return 0;
}