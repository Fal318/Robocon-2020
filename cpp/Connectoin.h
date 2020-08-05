#ifndef Connection_h
#define Connection_h

#include "function.h"

class Connection {
private:
    time send;
    bool conect();
    bool reconect();
    void send_data(int data);
public:
    Connection(uint id) {
        return;
    }
    void main_process(double delay) {
        Connection::send = getTime();
        sleep(get_random_value(0, 35)/100);
        sleep(delay-caluclate_sleep_time(Connection::send));
        std::cout << caluclate_sleep_time(Connection::send) << std::endl;
    }
};

#endif