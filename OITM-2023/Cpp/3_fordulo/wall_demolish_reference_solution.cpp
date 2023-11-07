#include <iostream>
#include <utility>
#include <vector>

#include "wall_demolish_inputs.cpp.inc"

const int INF_COST = 60*60*10;
std::vector<std::pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int solve_testcase(TestCase test_case, int step_cost, int demolish_cost,
                          bool one_demolish, bool multi_demolish) {
  std::vector<std::pair<int, int>> coords_todo;
  int cost1[100][100];
  int cost2[100][100];
  for (int i = 0; i < test_case.rows; ++i) {
    for (int j = 0; j < test_case.cols; ++j) {
      cost1[i][j] = INF_COST;
      cost2[i][j] = INF_COST;
    }
  }
  cost1[0][0] = 0;
  cost2[0][0] = 0;
  coords_todo.push_back(std::make_pair(0, 0));

  while (!coords_todo.empty()) {
    std::pair<int, int> act_coords = coords_todo.back();
    coords_todo.pop_back();
    int i = act_coords.first;
    int j = act_coords.second;
    for (auto [dx, dy] : directions) {
      if (i + dx >= 0 && i + dx < test_case.rows && j + dy >= 0 &&
          j + dy < test_case.cols) {
        int cost1ij = cost1[i][j];
        int cost2ij = cost2[i][j];
        bool redo = false;
        if (test_case.field[i + dx][j + dy] == 0) {
          if (cost1[i + dx][j + dy] > cost1ij + step_cost) {
            cost1[i + dx][j + dy] = cost1ij + step_cost;
            redo = true;
          }
          if (cost2[i + dx][j + dy] > cost2ij + step_cost) {
            cost2[i + dx][j + dy] = cost2ij + step_cost;
            redo = true;
          }
        } else {
          if (cost2[i + dx][j + dy] > cost1ij + demolish_cost) {
            cost2[i + dx][j + dy] = cost1ij + demolish_cost;
            redo = true;
          }
          if (multi_demolish) {
            if (cost2[i + dx][j + dy] > cost2ij + demolish_cost) {
              cost2[i + dx][j + dy] = cost2ij + demolish_cost;
              redo = true;
            }
          }
        }
        if (redo) {
          coords_todo.push_back(std::make_pair(i + dx, j + dy));
        }
      }
    }
  }
  int result = one_demolish ? cost2[test_case.rows - 1][test_case.cols - 1]
                         : cost1[test_case.rows - 1][test_case.cols - 1];
  if (result == INF_COST) {
    return -1;
  } else {
    return cost2[test_case.rows - 1][test_case.cols - 1];
  }
}

// full copy of the test case so it can be modified locally
int task1(TestCase test_case) {
  return solve_testcase(test_case, 1, INF_COST, false, false);
}

int task2(TestCase test_case) {
  return solve_testcase(test_case, 1, 1, true, false);
}

int task3(TestCase test_case) {
  return solve_testcase(test_case, 2, 3, true, true);
}

int main() {
  std::cout << "Solution for Task 1:" << std::endl;
  for (TestCase& test_case : test_cases) {
    int result = task1(test_case);
    std::cout << result << " ";
  }
  std::cout << std::endl;
  std::cout << "Solution for Task 2:" << std::endl;
  for (TestCase& test_case : test_cases) {
    int result = task2(test_case);
    std::cout << result << " ";
  }
  std::cout << std::endl;
  std::cout << "Solution for Task 3:" << std::endl;
  for (TestCase& test_case : test_cases) {
    int result = task3(test_case);
    std::cout << result << " ";
  }
  std::cout << std::endl;
  return 0;
}
