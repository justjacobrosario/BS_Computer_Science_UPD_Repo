#include <stdio.h>
#include <stdlib.h>


typedef struct DynamicArray{
    int size;
    int cap;
    int *arr;
} DynamicArray;

DynamicArray *d_arr_make(){
    DynamicArray *d_arr = malloc(sizeof(DynamicArray));
    (*d_arr).size = 0;
    (*d_arr).cap = 1;
    (*d_arr).arr = malloc((*d_arr).cap * sizeof(int));

    return d_arr;

}

void d_arr_append(DynamicArray *d_arr, int val){
    
    if ((*d_arr).size == (*d_arr).cap){
        (*d_arr).cap = (*d_arr).cap * 2; // multiply cap by 2 to not always malloc for every append
        int *temp_arr = malloc(((*d_arr).cap) * sizeof(int));

        int i = 0;
        while (i < ((*d_arr).size)){
            temp_arr[i] = (*d_arr).arr[i];
            i++;
        }

        temp_arr[((*d_arr).size)] = val;
        (*d_arr).size++;

        free((*d_arr).arr);
        (*d_arr).arr = temp_arr;
        // no need to free(temp_arr); bc temp_arr is now mapped to (*d_arr).arr, so no memory leaks
    }

    else{
        (*d_arr).arr[(*d_arr).size] = val;
        (*d_arr).size++;
        
    }
}

void d_arr_set(DynamicArray *d_arr, int idx, int val){

    if ((*d_arr).size + 1 >= (*d_arr).cap){
        (*d_arr).cap = (*d_arr).cap * 2;
    }


    (*d_arr).size++; // for the added value

    int *temp_arr = malloc((*d_arr).size * sizeof(int));

    int i = 0;
    while (i < idx){
        temp_arr[i] = (*d_arr).arr[i];
        i++;
    }

    temp_arr[i] = val;
    

    // notice that i is still = idx
    while (i < ((*d_arr).size - 1)){ // -1 bc we focus on the remaining elements (not including the new value)
        temp_arr[i + 1] = (*d_arr).arr[i]; // [i+1] bc we added the new value recently
        i++;
    }
    free((*d_arr).arr);
    (*d_arr).arr = temp_arr;
    // no need to free(temp_arr); bc temp_arr is now mapped to (*d_arr).arr, so no memory leaks


}

void d_arr_delete(DynamicArray *d_arr, int idx){
    int *temp_arr = malloc(((*d_arr).size - 1) * sizeof(int));

    for (int i = 0; i < idx; i++){
        temp_arr[i] = (*d_arr).arr[i];
    }

    for (int i = idx+1; i < (*d_arr).size; i++){
        temp_arr[i-1] = (*d_arr).arr[i];
    }

    (*d_arr).size--;
    free((*d_arr).arr);
    (*d_arr).arr = temp_arr;
}





// Linked list

typedef struct Node{
    int val;
    Node *next;
} Node;

typedef struct LinkedList{
    Node *head;
    Node *tail;
    int size;
} LinkedList;

LinkedList *llist_make(){
    LinkedList *llist = malloc(sizeof(LinkedList))
    (*llist).head = malloc(sizeof(Node));
    (*llist).tail = malloc(sizeof(Node));
    (*llist).size = 2;

    return llist;
}

void llist_delete(LinkedList *llist, int idx){
    int size = (*llist).size;
    Node *curr = (*llist).head;

    if (idx < size){
        int i = 0;
        while (i < idx){
            curr = (*curr).next;
        }
    }

    // finish thiss

}



int main(){
    DynamicArray *try_d_arr = d_arr_make();

    d_arr_append(try_d_arr, 67);
    d_arr_append(try_d_arr, 420);
    d_arr_append(try_d_arr, 123);

    d_arr_set(try_d_arr, 3, 246);
    d_arr_delete(try_d_arr, 3);




    int size = (*try_d_arr).size;
    printf("size: %d\n", size);


    // to display:
    int i = 0;
    while (i < size){
        if (i==0){
            printf("[");
            printf("%d, ",(*try_d_arr).arr[i]);
        }
        else{

            if (i == (size - 1)){
                printf("%d]",(*try_d_arr).arr[i]);
            }
            else{
                printf("%d, ",(*try_d_arr).arr[i]);
            }

        }
        
        i++; 
    }







    return 0;
}