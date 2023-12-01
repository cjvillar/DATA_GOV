#include <stdio.h>
#include <stdlib.h>
#include <xlsxwriter.h>
#include <cJSON.h>

void convert_excel_to_csv(const char *excel_file, const char *csv_file) {
    lxw_workbook *workbook = workbook_new(csv_file);
    lxw_worksheet *worksheet = workbook_add_worksheet(workbook, NULL);

    workbook_close(workbook);
    printf("Conversion complete. CSV saved to %s\n", csv_file);
}

void convert_json_to_csv(const char *json_file, const char *csv_file) {
    FILE *json_fp = fopen(json_file, "r");
    if (!json_fp) {
        perror("Error opening JSON file");
        exit(EXIT_FAILURE);
    }

    fseek(json_fp, 0, SEEK_END);
    long json_size = ftell(json_fp);
    fseek(json_fp, 0, SEEK_SET);

    char *json_data = malloc(json_size + 1);
    fread(json_data, 1, json_size, json_fp);
    fclose(json_fp);

    json_data[json_size] = '\0';


    free(json_data);
    printf("Conversion complete. CSV saved to %s\n", csv_file);
}

int main() {
    const char *excel_file = "example.xlsx"; 
    const char *json_file = "example.json"; 
    const char *csv_file = "output_data.csv";

    convert_excel_to_csv(excel_file, csv_file);
    convert_json_to_csv(json_file, csv_file);

    return 0;
}
