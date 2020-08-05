#ifndef Connection_h
#define Connection_h

#include "function.h"

class Connection {
private:
    time send;
public:
    Connection(uint id) {
        return;
    }
    void main_process() {
        send = getTime();
        sleep(get_random_value(0, 35)/100);
        sleep(0.5-caluclate_sleep_time(send));
        std::cout << caluclate_sleep_time(send) << std::endl;
    }
};

#endif