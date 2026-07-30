#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
	int main() {
	int32_t arr32[] = {10, 20, 30, 40, 50};
	int64_t arr64[] = {100, 200, 300, 400, 500};
	int32_t *p32 = arr32 + 3;
	int64_t *p64 = arr64 + 2;
	printf("%" PRId32 "\n", *p32); // "%" PRId32 "\n" becomes "%d\n" in Linux
	printf("%" PRId64 "\n", *p64); // "%d" PRId64 "\n" becomes "%ld\n" in Linux
	printf("%ld\n", p32 - arr32);
	printf("%ld\n", p64 - arr64);
	printf("%ld\n", (char*)p32 - (char*)arr32);
	printf("%ld\n", (char*)p64 - (char*)arr64);
	return 0;
}