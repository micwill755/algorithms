#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/* brute force */

#define min (a,b) (((a) < (b)) ? (a) : (b));

/* 

Time comlexity O(n^2)
Space complexity O(1)

*/
void containerMostWater(int *height, int n) {
    int max = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int x = j - i;
            int y = (height[i] < height[j]) ? height[i] : height[j];
            int area = x * y;
            if (area > max) {
                max = area;
            }
        }
    }
    printf("%d\n", max);
}

void containerMostWaterUsingPoints(int *height, int n) {
    int max = 0;
    int left = 0; int right = n;
    while (left < right) {
        int area = ((height[left] < height[right]) ? height[left] : height[right]) * (right - left);
        if (area > max) {
            max = area;
        }
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    printf("%d\n", max);
}
int main () {
    int height[] = {1,8,6,2,5,4,8,3,7};
    int n = sizeof(height) / sizeof(height[0]);
    //containerMostWater(height, n);
    containerMostWaterUsingPoints(height, n);
    return 0;
}