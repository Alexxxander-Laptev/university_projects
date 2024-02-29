#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAXGRID 258 //максимальный размер сетки с границами
#define COORDINATOR 0//номер управляющего процесса
#define TAG 0// не используется 

static void Coordinator (int,int,int);
static void Worker (int,int,int,int,int);

void main (int argc, char *argv[]) 
{
    int myid, numIters;
    int numWorkers, gridSize;//предполагается, что 
    int stripSize;//gridSize кратно numWorkers

    MPI_Init (&argc, &argv);//инициализация MPI 
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);
    MPI_Comm_size(MPI_COMM_WORLD, &numWorkers);
    numWorkers--;//один управляющий, остальные - рабочие
//???????   прочитать gridSize и numIters; вычислить stripSize;
    gridSize = atoi(argv[1]);
    numIters = atoi(argv[2]);
    stripSize = gridSize / numWorkers;

    if (myid == COORDINATOR)
        Coordinator(numWorkers, stripSize, gridSize);
    else
        Worker (myid, numWorkers, stripSize, gridSize, numIters);
    MPI_Finalize();//окончание работы
}

static void Coordinator (int numWorkers, int stripSize, int gridSize)
{
    double grid[MAXGRID][MAXGRID];
    double mydiff = 0.0, maxdiff = 0.0;
    int i, worker, startrow, endrow;
    MPI_Status status;
//получить окончательные значения в сетке от Workers
    for (worker=1;worker <= numWorkers; worker ++)
    {
        startrow = (worker-1)*stripSize + 1;
        endrow = startrow +stripSize  -1;
            for (i=startrow; i<=endrow;i++)
                MPI_Recv(&grid[i][1], gridSize, MPI_DOUBLE, worker,
                TAG, MPI_COMM_WORLD, &status);
    }
//редукция погрешностей от Workers
    MPI_Reduce(&mydiff, &maxdiff, 1 ,MPI_DOUBLE,
        MPI_MAX, COORDINATOR, MPI_COMM_WORLD);
//??????? вывести результаты;
    printf("%.16f\n", maxdiff);
    fflush( stdout );
}

static void Worker (int myid, int numWorkers,
                    int stripSize, int gridSize, int numIters)
{
    double grid [2][MAXGRID][MAXGRID];
    double mydiff, maxdiff;
    int i, j, iters;
    int current = 0, next = 1;//текущая и следующая сетки
    int left, right;
    MPI_Status status;
//????? инициализировать матрицы; определить соседей left и right;
    for (int i = 0; i < gridSize; i++)
    {
        for (int j = 0; j < gridSize; j++)
        {
            if ((i == 0) || (i == gridSize - 1)) {
                grid[current][i][j] = 1.0;
                grid[next][i][j] = 1.0;
            }
            else if ((j == 0) || (j == gridSize - 1)) {
                grid[current][i][j] = 0.0;
                grid[next][i][j] = 0.0;
            }
            else
            	grid[current][i][j] = 0.0;
        }
    }
    
    for (int i = 1; i < gridSize - 1; i++)
    {
        for (int j = 1; j < gridSize - 1; j++)
        {
            if (i != gridSize)
                right = grid[current][i + 1][j];
            else if (i != 1)
                left = grid[current][i - 1][j];
                        
            for (iters = 1; iters<=numIters; iters++)
            {//обмен границами с соседями
                if (right !=0) MPI_Send (&grid[next][stripSize][1],
                    gridSize, MPI_DOUBLE, right, TAG, MPI_COMM_WORLD);
                if (left !=0) MPI_Send (&grid[next][1][1],gridSize,
                    MPI_DOUBLE, left, TAG, MPI_COMM_WORLD);
                if (left !=0) MPI_Recv(&grid[next][0][1], gridSize,
                    MPI_DOUBLE, left, TAG, MPI_COMM_WORLD, &status);
                if (right !=0) MPI_Recv(&grid[next][stripSize+1][1],
                    gridSize, MPI_DOUBLE, right, TAG,
                    MPI_COMM_WORLD, &status);
        // обновить свои точки
                for (i = 1; i<stripSize - 1; i++)
                    for (j = 1; j<gridSize - 1; j++)
                        grid[next][i][j] = (grid[current][i-1][j]+
                        grid[current][i+1][j] + grid[current][i][j-1] + 
                        grid[current][i][j+1]) * 0.25;
                current = next; next = 1-next;//поменять местами сетки
            }
        }
    }

    
//отправить строки окончательной сетки управляющему процессу
     for (i=1;i<=stripSize;i++)
    {
        MPI_Send(&grid[current][i][1], gridSize, MPI_DOUBLE,
        COORDINATOR, TAG, MPI_COMM_WORLD);
    }
//?????? вычислить  mydiff;
    for (int i = 1; i < gridSize; i++)
    {
        for(int j = 1; j < gridSize; j++)
        {
            mydiff = fmax(mydiff, abs(grid[current][i][j] - grid[next][i][j]));
        }
    }
//редукция mydiff в управляющем процессе
    MPI_Reduce(&mydiff, &maxdiff, 1, MPI_DOUBLE,
                MPI_MAX, COORDINATOR, MPI_COMM_WORLD);
                
    FILE *graph;
    graph = fopen("jacobi.txt", "w");
    for (int i = 0; i < gridSize; i++)
    {
        for (int j = 0; j < gridSize; j++)
        {
            fprintf(graph, "%d\t%d\t%f\n", i, j, grid[next][i][j]);
        }
    }
    fclose(graph);
}
