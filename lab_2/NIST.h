#pragma once
#include <boost\math\special_functions\gamma.hpp>
#include<iostream>
#include<cmath>
#include "consts.h"


using namespace std;

void print_test_result(ostream& stream, string test_name, double p_val);
double  test1(string sequence);
double  test2(string sequence);
double  test3(string sequence);
