#include <stdlib.h>
#include <stdio.h>

typedef struct {
  char data[4096];
  int key;
} item_t;

item_t array[] = {
  {"bill", 3},
  {"neil", 4},
  {"john", 2},
  {"rick", 5},
  {"alex", 1},
};

void sort(item_t * a, int n) {
  int i = 0, j = 0;
  int s = 1;

  for(; i < n && s != 0; i++) {
    s = 0;
    
    for(j = 0; j < n-1; j++){ // bug: falta da abertura de chave

      if(a[j].key > a[j+1].key){
        item_t t = a[j];
        a[j] = a[j+1];
        a[j+1] = t;
        s++;
      }
    }
    //n--;    // bug: linha impede o ordenamento correto 
  }
}

int main(void) {
  sort(array,5);
  for(int i = 0; i < 5; i++)
    printf("array[%d] = {%s, %d}\n", i, array[i].data, array[i].key);
}
