#include <iostream>
#include <thread>
#include "function.h"
#include "Connectoin.h"

const uint LOOP = 500;
const float PERIOD = 0.1;
const uint TARGET_COUNT = 2;

void p1(int n) {
    Connection* connection = new Connection(1);
    for (int i = 0; i < 10; i++) {
        connection->main_process(0.5);
    }
}
void p2(int n) {
    Connection* connection = new Connection(1);
    for (int i = 0; i < 10; i++) {
        connection->main_process(1.0);
    }

}
int main(void) {
    std::thread thr1(p1, 1);
    std::thread thr2(p2, 1);
    thr1.join();
    thr2.join();
    return 0;
}



