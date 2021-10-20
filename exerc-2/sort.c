#include <stdlib.h>
#include <stdio.h>
#include <glib.h>
#include <string.h>

typedef struct {
  char *data;
  int key;
} item_t;

gint compare_item(gconstpointer a, gconstpointer b) {
  if (((item_t *)a)->key < ((item_t *)b)->key)
    return -1;
  else if (((item_t *)a)->key > ((item_t *)b)->key)
    return 1;
  else
    return 0;
}

void print_item(gpointer data, gpointer user_data) {
  int *i = (int *) user_data;
  printf("No. %d -> key=%d: %s\n", *i + 1, ((item_t *)data)->key, ((item_t *)data)->data);
  (*i)++;
}

item_t * item_init(char * data, int key) {
  item_t * self = malloc(sizeof(item_t));
  self->key = key;
  self->data = strdup(data);
  return self;
}

void item_destroy(gpointer _self, gpointer unused_data) {
  item_t *self = (item_t *) _self;
  free(self->data);
  free(self);
}

char s1[40];

int main(void) {
  char *s = "bill";
  GList *list = g_list_append(NULL, item_init(s, 3));
  s = "neil";
  list = g_list_insert_sorted(list, item_init(s, 4), compare_item);
  strcpy(s1, "john");
  list = g_list_insert_sorted(list, item_init(s1, 2), compare_item);
  strcpy(s1, "sara");
  list = g_list_insert_sorted(list, item_init(s1, 7), compare_item);
  list = g_list_insert_sorted(list, item_init("rick", 5), compare_item);
  list = g_list_insert_sorted(list, item_init("alex", 1), compare_item);

  /* printf("The first item is '%s'\n", ((item_t *)g_list_first(list)->data)->data); */

  /* list = g_list_next(list); */

  /* printf("The second item is '%s'\n", ((item_t *)list->data)->data); */

  list = g_list_first(list);

  int i = 0;
  g_list_foreach(list, print_item, &i);

  /* limpando toda a lista e suas estruturas */
  list = g_list_first(list);
  g_list_foreach(list, item_destroy, NULL);
  g_list_free(list);

  return 0;
}
