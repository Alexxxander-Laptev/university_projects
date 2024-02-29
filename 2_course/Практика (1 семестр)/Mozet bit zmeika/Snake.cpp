#include "Snake.h"

Snake::Snake()
{
	m_body.push_back(sf::Vector2i(7, 7));
	m_body.push_back(sf::Vector2i(7, 8));

	m_vector_move = sf::Vector2i(0, -1);  // ��������� ��������� ����, ���������� �������, ������ ����� ���� ���� � � ����

	m_rect.setSize(sf::Vector2f(40.f, 40.f));
	m_rect.setFillColor(sf::Color::Green);
};
void Snake::setVectorMove(const sf::Vector2i move)
{
	if (!((m_vector_move.x == move.x && m_vector_move.y != move.y) || (m_vector_move.x != move.x && m_vector_move.y == move.y)))  // ����������� ��������� �������� ����
		m_vector_move = move;
};
void Snake::add()
{
	m_body.push_back({ m_body.back() });  // ���� ����
};
void Snake::move()
{
	m_body.insert(m_body.begin(), { m_body[0] + m_vector_move });  // �������� ������
	m_body.erase(m_body.end() - 1);								   // �������� ������
};
int Snake::getSize() const
{
	return m_body.size();
};
bool Snake::collision() const
{
	for (int i = 1, n = m_body.size(); i < n; i++)  // �������� ������������ � �������
	{
		if (m_body[i] == m_body.front())
			return true;
	}
	return (m_body[0].x < 0 || m_body[0].y < 0 || m_body[0].x > 14 || m_body[0].y > 14) ? true : false;  // �������� ������ �� ������� �����
};
bool Snake::collision(sf::Vector2i pix) const
{
	return (pix == m_body.front());  // �������� ������
};
void Snake::draw(sf::RenderWindow &win)
{
	for (const sf::Vector2i v : m_body)  // ��������� ������ �������� ������ � ������ ������
	{
		m_rect.setPosition(sf::Vector2f(40.f + (v.x * 40), 40.f + (v.y * 40)));
		win.draw(m_rect);
	}
};