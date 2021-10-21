#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

class Item{
    public:

    std::string Name;
    int Key;

    //construção
    Item(std::string name, int key){
        Name = name;
        Key = key;
    }
};

//vetor com itens:
std::vector<Item> array ={
    {"bill", 3},
    {"neil", 4},
    {"john", 2},
    {"rick", 5},
    {"alex", 1},
};

//representação dos itens da array
void repr(const std::vector<Item>array){
    for (auto &e: array){
        std:: cout << "Sort Item -> Nome: " << e.Name << ", key:" << e.Key << std::endl;
        //std:: cout << "\n";
    }
};

//ordenação dos itens
bool ordem(Item& a, Item& b){
    return (a.Key < b.Key);
}

int main(void){

    std::sort(array.begin(), array.end(), ordem);
    repr(array);

return 0;
}