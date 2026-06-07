int main() {
    // Purely stack-allocated
    LinkedList stack = {.head = NULL, .size = 0};
 
    Node s3 = {.data = 30, .next = NULL};
    Node s2 = {.data = 20, .next = &s3};
    Node s1 = {.data = 10, .next = &s2};
    stack.next = &s1;
    stack.size = 3;
 
    // Purely heap-allocated
    LinkedList *heap = malloc(sizeof(LinkedList));
    heap->head = NULL;
    heap->size = 0;
 
    Node *h3 = make_node(30, NULL);
    Node *h2 = make_node(20, h3);
    Node *h1 = make_node(10, h2);
    heap->head = h1;
    heap->size = 3;
 
    free(heap);
    free(h1);
    free(h2);
    free(h3);
}