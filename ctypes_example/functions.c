#include <stdio.h>
#include "sum.h"
#include "functions.h"

void call_sum_func(void)
{
    int result = sum(5, 7);
    printf("%d\n", result);
}