// lab4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

#include "stdafx.h"
#include "glut.h"

using namespace std;

float point[350][3]; int n = 0, i, j; bool tP = false; void Draw();
void Mouse(int button, int state, int x, int y); void MenuChek(int v);
void CurveBezier(); void Line();

void main() {
	//Инициализируем режим отображения окна OpenGL
	//GLUT_DOUBLE - окно с двойной буферизацией
	//GLUT_RGB - режим RGBA glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(350, 350); //устанавливаем размер окна glutCreateWindow("Кривая Безье"); //создаем окно с заголовком glutDisplayFunc(Draw); //устанавливаем функцию отрисовки glutMouseFunc(Mouse); //устанавливаем функцию обработки нажатий мыши

	//Установить цвет и значение альфа, используемые при очистке буферов цвета glClearColor(0, 0, 0, 0); //цвет фона (RGBA) glMatrixMode(GL_PROJECTION); //Определяем стек матриц (матрица проекций) glLoadIdentity(); //установить текущую матрицу равной еденичной

	//Установить границы объема отсечения glOrtho(0, 350, 0, 350, 0, 1);
	glColor3f(1.0, 0, 1.0); //Установить текущий цвет (R,G,B)

	glutCreateMenu(MenuChek); //Меню вызываемое нажатием ПКМ glutAddMenuEntry("Удалить последнюю точку", 0); //Пункт меню glutAddMenuEntry("Очистить", 1); //Пункт меню glutAttachMenu(GLUT_RIGHT_BUTTON);

	glutMainLoop(); //Запуск основного цикла обработки GLUT
}

void Draw() {
	glClear(GL_COLOR_BUFFER_BIT); //Очистка буфера цвета Line();
	if (n > 1)
		CurveBezier();
	glutSwapBuffers(); //Переключить буферы в режиме двойной буферизации
}

void Mouse(int button, int state, int x, int y) {
	if (button == GLUT_LEFT_BUTTON) {
		if (tP && (x > 0 && x < 350) && (350 > y && y < 700)) {
			point[j][0] = x;
			point[j][1] = 350 - y;
		}
		else if (state == GLUT_DOWN && n != 0 && !tP) for (i = 0; i <= n; i++)
			if ((x<point[i][0] + 30 && x>point[i][0] - 30) && (320 -
				y<point[i][1] && 380 - y>point[i][1])) {
				tP = true; j = i; break;
			}
		if (state == GLUT_UP) {
			if (!tP) {
				point[n][0] = x;
				point[n][1] = 350 - y; n++;
			}
			tP = false;
		}
	}
	glutPostRedisplay(); //Обновить текущее окно
}

void MenuChek(int v) {
	if (v == 0 && n > 0)
		n--;
	else if (v == 1)
		n = 0;
	glutPostRedisplay();
}

void Line() {
	glPointSize(5); glColor3f(0.75, 0, 1);

	//Контрольные точки glBegin(GL_POINTS);
	for (i = n - 1; i >= 0; i--) glVertex2fv(point[i]);
	glEnd();

	//Пунктирные линии glLineStipple(2, 58360); glEnable(GL_LINE_STIPPLE); glBegin(GL_LINES);
	for (i = 0; i < n - 1; i++) {
		glVertex2fv(point[i]); glVertex2fv(point[i + 1]);
	}
	glEnd(); glDisable(GL_LINE_STIPPLE); glPointSize(1);
}

void CurveBezier() {
	//glMap1f - Функция оценки, генерирующая координаты.
	//Параметры:
	// GL_MAP1_VERTEX_3 -	тип генерируемых данных,
	// 0.0f - нижняя граница параметра u (первая точка),
	// 100.0f - верхняя граница(последняя точка),
	// 3 - расстояние между точками данных,
	// n - число точек,
	// &P[0][0] - массив контрольных точек glMap1f(GL_MAP1_VERTEX_3, 0.0f, 100.0f, 3, n, &point[0][0]); glEnable(GL_MAP1_VERTEX_3);

	glLineWidth(2); glColor3f(0.0f, 1.0f, 0.0f);
	glBegin(GL_LINE_STRIP); //точки соединяются ломанной линией for (i = 0; i <= 100; i++)
	//Оценка кривой в точке. Функция принимает параметрическое значение, и вычисляет точку
	glEvalCoord1f(float(i)); glEnd();
	glLineWidth(1);
}

Приложение Б.
#include <stdlib.h> #include "glut.h" #include <math.h> #include <stdio.h>
#pragma warning (disable:4996) GLfloat ctrlpoints[6][6][3];

void initlights(void)

{

	GLfloat ambient[] = { 1.0, 1.0, 1.0, 1.0 };

	GLfloat position[] = { 0.0, 0.0, 2.0, 1.0 };

	GLfloat mat_diffuse[] = { 1.0, 1.0, 1.0, 1.0 };

	GLfloat mat_specular[] = { 1.0, 1.0, 1.0, 1.0 }; GLfloat mat_shininess[] = { 50.0 }; glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	glLightfv(GL_LIGHT0, GL_AMBIENT, ambient); glLightfv(GL_LIGHT0, GL_POSITION, position); glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse); glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular); glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
}
unsigned int angle = 0; void display(void)

{
	int i, j; while (true)
	{
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glPushMatrix(); glRotatef(angle++, 1, 1, 0);
		glEvalMesh2(GL_POINT, 0, 10, 0, 10); // изменение отображения glPopMatrix();


		glFlush();
		_sleep(10);
	}

}

void init(void)

{

	float x, y; int i, j;
	for (i = 0; i < 6; i++)

	{

		x = 3.1415 / 5.0 * (float)i; for (j = 0; j < 6; j++)
		{

			y = 3.1415 / 5.0 * (float)j;

			ctrlpoints[i][j][0] = x / 2; ctrlpoints[i][j][1] = y / 2; ctrlpoints[i][j][2] = sinf(x + y) / 2;
		}
	}
	glClearColor(0.0, 0.0, 0.0, 0.0); glEnable(GL_DEPTH_TEST); glMap2f(GL_MAP2_VERTEX_3, 0, 4, 3, 4,
		0, 4, 18, 4, &ctrlpoints[0][0][0]); glEnable(GL_MAP2_VERTEX_3); glEnable(GL_AUTO_NORMAL); glMapGrid2f(10, 0.0, 4.0, 10, 0.0, 4.0);
	initlights();	/* for lighted version only */

}

void reshape(int w, int h)

{

	glViewport(100, 0, 1000, 1000); glMatrixMode(GL_PROJECTION); glLoadIdentity();
	glOrtho(-1.0, 2.0, -1.0, 2.0, -2.0, 2.0);

	glMatrixMode(GL_MODELVIEW); glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)

{

	switch (key) {

	case 27:

		exit(0); break;
	}

}

int main(int argc, char** argv)

{

	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH); glutInitWindowSize(1000, 1000);
	glutInitWindowPosition(0, 0); glutCreateWindow(argv[0]); init(); glutReshapeFunc(reshape); glutDisplayFunc(display); glutKeyboardFunc(keyboard); glutMainLoop();
	return 0;

}
