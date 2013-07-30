// travel.cpp -- using structures with functions
#include <iostream>

struct travel_time {
    int hours;
    int mins;
};

const int MINS_PER_HOUR = 60;

travel_time sum(travel_time t1, travel_time t2);
void show_time(travel_time t);

int main() {
    using namespace std;

    travel_time day1 = {5, 45};  // 5 hrs, 45 min
    travel_time day2 = {4, 55};  // 4 hrs, 55 min

    travel_time trip = sum(day1, day2);
    cout << "Two-day total: ";
    show_time(trip);

    travel_time day3 = {4, 32};
    cout << "Three-day total: ";
    show_time(sum(trip, day3));

    return 0;
}

travel_time sum(travel_time t1, travel_time t2) {
    travel_time total;

    total.mins = (t1.mins + t2.mins) % MINS_PER_HOUR;
    total.hours = t1.hours + t2.hours + (t1.mins + t2.mins) / MINS_PER_HOUR;

    return total;
}

void show_time(travel_time t) {
    std::cout << t.hours << " hours " << t.mins << " minutes\n";
}
