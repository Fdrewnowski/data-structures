#pragma once
#include <iostream>

using namespace std;


struct Modul{				//node structure 
	Modul(int data)
	: data(data), key(NULL), child(nullptr), rightSibling(nullptr), leftSibling(nullptr), parent(nullptr), root(false) {}
	int key;
	Modul* child;
	Modul* leftSibling;
	Modul* rightSibling;
	Modul* parent;

	long int data;
	bool root;
};

class BNHeap {			// binary heap object 
public:
	Modul** rootArr;
	BNHeap();

	void addValue(int value);
	void unionBHeap(int key, Modul* heap);
	void heapifyDown(Modul* element);
	void mergeHeaps(Modul** second);
	void extract();
	void deleteRoot(int group);
	void increaseValue(int valueOld, int valueNew);
	Modul* search(int valueOld, Modul* root);
	void heapifyUp(Modul* element);
	void print();

	~BNHeap();
};