#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

#define MAX_ROWS 100
#define MAX_COLS 100

typedef struct {
    int row;
    int col;
} Coordinate;

typedef struct {
    int best_path;
} OptimalSolution;

void openMaze(const char *filename, char maze[MAX_ROWS][MAX_COLS], int *rows, int *cols) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return;
    }

    *rows = 0;
    *cols = 0;

    while (fscanf(file, "%s", maze[*rows]) != EOF) {
        (*rows)++;
        if (*cols == 0) {
            *cols = strlen(maze[0]);
        }
    }

    fclose(file);
}

Coordinate findCharacter(char maze[MAX_ROWS][MAX_COLS], int rows, int cols, char character) {
    Coordinate position = { -1, -1 };

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (maze[i][j] == character) {
                position.row = i;
                position.col = j;
            }
        }
    }

    return position;
}

Coordinate findPortal(char maze[MAX_ROWS][MAX_COLS], int rows, int cols, Coordinate initial, char letter) {
    Coordinate portal = { -1, -1 };

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (maze[i][j] == letter && (i != initial.row || j != initial.col)) {
                portal.row = i;
                portal.col = j;
            }
        }
    }

    return portal;
}

bool isPossible(int row, int col, char maze[MAX_ROWS][MAX_COLS], int rows, int cols) {
    return row >= 0 && row < rows && col >= 0 && col < cols && maze[row][col] != '#';
}

int calculateDistance(Coordinate origin, Coordinate exit) {
    return abs(origin.row - exit.row) + abs(origin.col - exit.col);
}

void solveMaze(int row, int col, char maze[MAX_ROWS][MAX_COLS], int rows, int cols, int visited[MAX_ROWS][MAX_COLS], int count, OptimalSolution *best_solution, Coordinate exit) {
    float accumulated_distance = calculateDistance((Coordinate){row, col}, exit);
    
    if (accumulated_distance > best_solution->best_path && best_solution->best_path != -1) {
        return;
    }

    if (maze[row][col] == 'S') {
        if (count < best_solution->best_path || best_solution->best_path == -1) {
            best_solution->best_path = count;
        }
        return;
    }

    visited[row][col] = 1;
    int movements[4][2] = { {1, 0}, {0, -1}, {-1, 0}, {0, 1} };

    for (int i = 0; i < 4; i++) {
        int newRow = row + movements[i][0];
        int newCol = col + movements[i][1];

        if (maze[row][col] != '#' && maze[row][col] != '.' && maze[row][col] != 'E' && maze[row][col] != 'S') {
            Coordinate otherPortal = findPortal(maze, rows, cols, (Coordinate){row, col}, maze[row][col]);
            maze[row][col] = '.';
            maze[otherPortal.row][otherPortal.col] = '.';
            solveMaze(otherPortal.row, otherPortal.col, maze, rows, cols, visited, count + 1, best_solution, exit);
        } else if (isPossible(newRow, newCol, maze, rows, cols) && visited[newRow][newCol] != 1) {
            solveMaze(newRow, newCol, maze, rows, cols, visited, count + 1, best_solution, exit);
        }
    }

    visited[row][col] = 0;
}

int main() {
    char maze[MAX_ROWS][MAX_COLS];
    int rows, cols;
    openMaze("laberinto.txt", maze, &rows, &cols);
    Coordinate entrance = findCharacter(maze, rows, cols, 'E');
    Coordinate exit = findCharacter(maze, rows, cols, 'S');
    int visited[MAX_ROWS][MAX_COLS] = {0};
    OptimalSolution best_solution;
    best_solution.best_path = -1;
    solveMaze(entrance.row, entrance.col, maze, rows, cols, visited, 0, &best_solution, exit);

    printf("Mejor solucion: %d\n", best_solution.best_path);
    printf("Presiona Enter para salir...");
    getchar();

    return 0;
}
