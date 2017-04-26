#include <stdio.h>
#include <cuda_runtime.h>

__global__ void add(int a, int b, int *c) {
	*c = a + b;
}

__global__ void hello (void)
{
	printf("Hello Wold from GPU!\n");
}

extern "C" int fun_cuda()
{
	int c;
	int *dev_c;
	cudaMalloc((void **)&dev_c, sizeof(int));
	add<<<1,1>>>(2, 7, dev_c);
	cudaMemcpy(&c, dev_c, sizeof(int), cudaMemcpyDeviceToHost);
	printf("2+7=%d\n",c);
	cudaFree(dev_c);
	hello<<<1, 10>>>();
	cudaDeviceReset();
	return 0;
}
