#ifndef function_h
#define function_h

#include <iostream>
#include <thread>
#include <chrono>
#include <random>

#define time std::chrono::system_clock::time_point

std::chrono::duration<long double> es;
std::random_device rnd;
std::mt19937 mt(rnd());

time getTime() {
    return std::chrono::system_clock::now();
}

long double caluclate_sleep_time(time t) {
    es = getTime() - t;
    return es.count();
}

void sleep(long double sec) {
    std::this_thread::sleep_for(std::chrono::microseconds(int(sec*1000000)));
}

int get_random_value(int min, int max) {
    std::uniform_int_distribution<> get_rand(min, max);
    return get_rand(mt);
}


#endif