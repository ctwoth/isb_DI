#include <ctime> 
#include <iostream> 
#include <random> 

using namespace std;


int main(){
    mt19937 mt_rand(time(NULL));
    cout << "sequence: ";
  
    for (int i = 0; i < 128; ++i){ 
        cout << mt_rand()%2;  
    } 

    return 0; 
}
