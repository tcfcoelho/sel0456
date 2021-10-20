#include <stdlib.h>
#include <stdio.h>
#include <glib.h>

typedef struct {
  char *data;
  int key;
} item_t;

/* item_t array[] = {
  {"bill", 3},
  {"neil", 4},
  {"john", 2},
  {"rick", 5},
  {"alex", 1},
}; */

//comparação da ordem dos itens da lista
gint compare(gconstpointer k1, gconstpointer k2){
  if(((item_t*)k1)->key < ((item_t*)k2)->key){
    return -1;
  }

  else if(((item_t*)k1)-> key > ((item_t*)k2)-> key){
    return 1;
  }

  else
    return 0;
}

//impressão dos itens da lista
void print(gpointer data, gpointer user_data){
  int *i = (int *)user_data;
  printf("Nº %d -> key = %d: %s \n", *i +1, ((item_t*)data)-> key, ((item_t*)data)-> data);

  (*i)++;
}


//inicialização
item_t *init(char *data, int key){
  item_t *self = malloc(sizeof(item_t));
  self -> key = key;
  self -> data = strdup(data);

  return self;
}

//destrutor
void destroy(gpointer _self, gpointer unused_data){
  item_t *self = (item_t *) _self;
  free(self->data);
  free(self);
}


int main (void){

  //criação da lista e adição do primeiro item:
  GList *list = g_list_append(NULL, init("bill", 3));
  
  //adição de item por meio do ponteiro:
  char *nome = "neil";
  list = g_list_insert_sorted(list, init(nome, 4), compare); //necessário uso do compare para garantir ordenação

  //reutilização do ponteiro para nova adição de item:
  nome = "john";
  list = g_list_insert_sorted(list, init(nome, 2), compare);

  list = g_list_insert_sorted(list, init("rick", 5), compare);
  list = g_list_insert_sorted(list, init("sara", 7), compare);
  list = g_list_insert_sorted(list, init("alex", 1), compare);


  list = g_list_first(list);

  int i = 0;
  g_list_foreach(list, print, &i); //exerce função do for(){print}

  
  //desalocação:
  list = g_list_first(list);
  g_list_foreach(list, destroy, NULL);
  g_list_free(list);

  return 0;
}
