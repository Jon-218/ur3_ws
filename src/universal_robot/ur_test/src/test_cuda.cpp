#include <stdio.h>

extern "C" int fun_cuda();
int main()
{
	printf("cuda testing\n");
	fun_cuda();
	return 0;
}
