#include <stdio.h>
#include <stdlib.h>

typedef struct DynamicArray {
    int cap;
    int size;
    int *arr;
} DynamicArray;

DynamicArray *make_darr(){
    DynamicArray *darr = malloc(sizeof(DynamicArray));
    (*darr).cap = 2;
    (*darr).size = 0;
    (*darr).arr = malloc((*darr).cap * sizeof(int));
}

void append_darr(DynamicArray *darr, int x){
    if ((*darr).cap >= ((*darr).size + 1)){
        (*darr).arr[(*darr).size] = x;
        (*darr).size++;
    }
    else{
        int new_cap = (*darr).cap * 2; // doubled it to reduce frequent arr duplication
        int *new_arr = malloc(new_cap * sizeof(int));

        for (int i = 0; i < (*darr).size; i++){ // duplicating
            new_arr[i] = (*darr).arr[i];
        }
        new_arr[(*darr).size] = x; // appending
        (*darr).size++;

        (*darr).arr = new_arr;
        (*darr).cap = new_cap; // update arr and cap


    }
}

void pop_darr(DynamicArray *darr){
    if ((*darr).size > 0){
        (*darr).size--;
    }
}

void set_darr(DynamicArray *darr, int idx, int x){
    if (idx == (*darr).size){
        append_darr(darr, x);
    }
    else{
        if (((*darr).size + 1) < (*darr).cap){
            int *new_arr = malloc((*darr).cap * sizeof(int)); // no need to expand since it still fits

            for (int i = 0; i < idx; i++){
                new_arr[i] = (*darr).arr[i];
            }
            new_arr[idx] = x;
            (*darr).size++;

            for (int j = idx + 1; j < (*darr).size; j++){
                new_arr[j] = (*darr).arr[j-1];
            }

            (*darr).arr = new_arr;
        }
        else{
            int new_cap = (*darr).cap * 2;
            int *new_arr = malloc(new_cap * sizeof(int));
            
            for (int i = 0; i < idx; i++){
                new_arr[i] = (*darr).arr[i];
            }

            new_arr[idx] = x;
            (*darr).size++;

            for (int j = idx + 1; j < (*darr).size; j++){
                new_arr[j] = (*darr).arr[j-1];
            }

            (*darr).arr = new_arr;
            (*darr).cap  = new_cap;
            
        }
    }
}

void del_darr(DynamicArray *darr, int idx){
    if (idx == (*darr).size){
        pop_darr(darr);
    }
    else{
        
        for (int i = idx + 1; i < (*darr).size; i++){
            (*darr).arr[i-1] = (*darr).arr[i];
        }
        (*darr).size--;

    }

}



typedef struct Node {
    int val;
    struct Node *prev; // struct Node, instead of just Node since the typedef Node is not yet done
    struct Node *next;
} Node;

typedef struct LinkedList {
    int size;
    Node *head;
    Node *tail;
} LinkedList;


LinkedList *make_llist(){
    LinkedList *l_list = malloc(sizeof(LinkedList));
    (*l_list).size = 0;
    (*l_list).head = NULL;
    (*l_list).tail = NULL;

    return l_list;
}

void append_llist(LinkedList *l_list, int x){
    (*l_list).size ++;

    Node *new_node = malloc(sizeof(Node));
    (*new_node).val = x;
    (*new_node).prev = NULL;
    (*new_node).next = NULL;

    if ((*l_list).head == NULL){
        (*l_list).head = new_node;
        (*l_list).tail = new_node;
    }
    else{
        (*((*l_list).tail)).next = new_node;
        (*new_node).prev = (*l_list).tail;
        (*l_list).tail = new_node;
    }

}






int main(){
    DynamicArray *d_arr = make_darr();
    
    /*
    Dynamic Array
    - accessing : d_arr[idx]
    - appending : append_darr(d_arr, x)
    - popping : pop_darr(d_arr, x)
    - setting : set_darr(d_arr, idx, x)
    - deleting : del_darr(d_arr, idx)   
    */

    /*
    int i = 0;
    for (int x = 0; x < 10; x++){
        if (x == 5){
            printf("popped\n");
            pop_darr(d_arr);
        }
        else{
            append_darr(d_arr, x);
        }
        

        printf("x: %d, size: %d, cap: %d\n", x, (*d_arr).size,(*d_arr).cap);
        
        while ((*d_arr).size > i){
            printf("%d", (*d_arr).arr[i]);
            i++;
        }
        i = 0;
        printf("\n");
        printf("===\n");


    }

    */


    // ====

    LinkedList *llist = make_llist();

    append_llist(llist, 1);
    append_llist(llist, 3);

    Node *curr_node = (*llist).head; 
    while (curr_node != NULL){
        printf("%d", (*curr_node).val);
        curr_node = (*curr_node).next;
    }


    return 0;
}