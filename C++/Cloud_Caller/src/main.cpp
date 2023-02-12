#include <iostream>


int main() {

    std::cout << "Hello Cloud!" << std::endl;

    // Send username + pw to Cloud Function endpoint. Serialize before sending.
    // Json format probably easiest. 
    // User + pw could be grabbed from environment variables.

    // Possible feature:
    // Send "compute" as a boolean in the request
    // If True, Python cloud function does number calculation
    // If false, Python grabs data, returns data to C++, C++ does calculation amd
    // Returns data to Cloud Function, auth will need to happen 2x

    return 0;
}