#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_spi_flash.h"

extern "C" {
    void app_main(void);
}

void app_main()
{
    printf("Hello PlatformIO!\n");
}