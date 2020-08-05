#include <iostream>
#include "function.h"
#include "Connectoin.h"

const uint LOOP = 500;
const float PERIOD = 0.1;
const uint TARGET_COUNT = 2;

int main(void) {
    Connection* connection = new Connection(1);
    for (int i = 0; i < 10; i++) {
        connection->main_process();
    }
    return 0;
}



