#include<stdlib.h>
typedef struct  tagnode
{
    /* data */
    int Data;
    struct tagnode* nextnode;//the pointer to nextnode

}Node;
//operation of linkedlist

Node* SLL_CreateNode(int newData){
    Node* NewNode =(Node*)malloc(sizeof(Node));//동적 할당을 하여야 이 함수가 끝나도 새 노드가 남는다

    NewNode->Data=newData;//첫 노드에 들어갈 값
    NewNode->nextnode=NULL;//생성 함수에서는 다음 노드를 가리키지 않는다.

    return NewNode;//노드의 주소를 반환한다. 왜? 왜?
}
// 포인터 관력 책 읽어야겠네.
void SLL_AppendNode(Node** Head, Node* NewNode){
    
}
