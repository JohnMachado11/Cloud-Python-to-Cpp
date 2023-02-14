#include <curl/curl.h>
#include <iostream>
#include <string>


int main() {

    std::cout << std::endl << "Sending POST Request to Cloud Function" << std::endl << std::endl;

    CURL *curl;
    CURLcode res;
    long http_code = 0;

    curl = curl_easy_init();
    if(curl) {
        
        std::string json_data = "{\"email\":\"email here\", \"password\":\"password here\"}";
        curl_easy_setopt(curl, CURLOPT_URL, "cloud function url here");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_data.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, (long)json_data.size());

        struct curl_slist *headers = NULL;

        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        
        std::cout << "Values of 5 most recent records from BigQuery table: " << std::endl;

        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                curl_easy_strerror(res));
        else {
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &http_code);
            std::cout << std::endl << "HTTP status code: " << http_code << std::endl << std::endl;
        }

        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();

    return 0;
}
