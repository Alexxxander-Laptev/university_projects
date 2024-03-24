/* This is an interactive version of cpi */
#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double);

double f(double a)
{
    return (4.0 / (1.0 + a*a));
}

int main(int argc,char *argv[])
{
    int n, myid, numprocs, i;
    double PI25DT = 3.141592653589793238462643;
    double mypi, pi, h, sum, x;
    double startwtime = 0.0, endwtime;
    int  namelen;
    char processor_name[MPI_MAX_PROCESSOR_NAME];

    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD,&myid);
    MPI_Get_processor_name(processor_name,&namelen);

    /*
    fprintf(stdout,"Process %d of %d is on %s\n",
        myid, numprocs, processor_name);
    fflush(stdout);
    */

    if (myid == 0) {
        n = atoi(argv[1]);
        int count_thread = atoi(argv[2]);
        // Расчет ускорения
        //spped = 
        fflush(stdout);
        startwtime = MPI_Wtime();
    }
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
    h   = 1.0 / (double) n;
    sum = 0.0;
    for (i = myid + 1; i <= n; i += numprocs) {
        x = h * ((double)i - 0.5);
        sum += f(x);
    }
    mypi = h * sum;
    MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (myid == 0) {
        printf("%.16f, %.16f, ",
               pi, fabs(pi - PI25DT));
        endwtime = MPI_Wtime();
        printf("%f\n", endwtime-startwtime);         
        fflush( stdout );
        
        FILE *error;
        error = fopen("error_graphic.txt", "a");
        FILE *coef_speed;
        coef_speed = fopen("coef_speed.txt", "a");
        FILE *time;
        time = fopen("time.txt", "a");
        
        fprintf(error, "%f %d\n", fabs(pi - PI25DT), n);
        //fprintf(coef_speed, "%d %d\n", speed, count_thread);
        fprintf(error, "%f %d\n", endwtime-startwtime, n);
        
        fclose(error);
        fclose(coef_speed);
        fclose(time);
    }
    MPI_Finalize();
    return 0;
}
