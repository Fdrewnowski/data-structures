#include "BNHeap.h"
#define MAX 18
#define NONE -1

BNHeap::BNHeap() {					//initializing binary heap as table 'i' large
	this->rootArr = new Modul*[MAX];
	for (int i = 0; i < MAX; i++) {
		rootArr[i] = nullptr;
	}
}

void BNHeap::addValue(int value) {				//add value to a binary heap
	Modul* newModul = new Modul(value);
	unionBHeap(newModul->key, newModul);
}

void BNHeap::unionBHeap(int key, Modul* heap) {		//union inside heap
	Modul* dummy;
	dummy = heap;
	if (dummy->key == 0) {
		if (rootArr[0] == nullptr) {
			dummy->root = true;
			rootArr[0] = dummy;
			return;
		}
		else {
			rootArr[0]->child = dummy;
			dummy->parent = rootArr[0];
			if (rootArr[0]->data < dummy->data) {
				swap(rootArr[0]->data, dummy->data);
			}
			rootArr[0]->key++;
			dummy = nullptr;
			dummy = rootArr[0];
			rootArr[0] = nullptr;
			key = 1;
		}
	}

	while (key < MAX) {
		if (rootArr[key] == nullptr) {
			rootArr[key] = dummy;
			dummy = nullptr;
			break;
		}
		else {
			dummy->parent = rootArr[key];
			dummy->rightSibling = rootArr[key]->child;
			rootArr[key]->child->leftSibling = dummy;
			rootArr[key]->child->parent = nullptr;
			rootArr[key]->child = dummy;
			if (dummy->data < dummy->rightSibling->data) {			
				swap(dummy->data, dummy->rightSibling->data);		
				heapifyDown(dummy->rightSibling);					
			}														
			dummy->root = false;
			dummy = nullptr;
			heapifyDown(rootArr[key]);
			rootArr[key]->key++;
			dummy = rootArr[key];
			rootArr[key] = nullptr;
			key++;
		}
	}
}

void BNHeap::heapifyDown(Modul* element) {
	Modul* dummyElement = element;
	Modul* dummyChild = element->child;
	Modul* dummyRight = element->rightSibling;
	if (dummyRight != nullptr && dummyElement->data < dummyRight->data) {
		swap(dummyRight->data, dummyElement->data);
		heapifyDown(dummyRight);
	}
	if (dummyChild != nullptr && dummyElement->data < dummyChild->data) {
		swap(dummyChild->data, dummyElement->data);
		heapifyDown(dummyChild);
	}
}

void BNHeap::mergeHeaps(Modul** second) {	//merge two heaps into one	
	for (int i = 0; i < MAX; i++) {
		if (second[i] != nullptr) {
			unionBHeap(second[i]->key, second[i]);
			second[i] = nullptr;
		}
	}
}

void BNHeap::extract() {		
	int maxValue = NONE;
	int maxGroup = NONE;
	for (int i = 0; i < MAX; i++) {
		if (rootArr[i] != nullptr && maxValue < rootArr[i]->data) {
			maxValue = rootArr[i]->data;
			maxGroup = i;
		}
	}
	if (maxValue == NONE && maxGroup == NONE) {
		cout << "na" << endl;
	}
	else {
		deleteRoot(maxGroup);
	}
}

void BNHeap::deleteRoot(int group) { // deletes root of one heap
	Modul* dummy;
	Modul* leftDummy;
	if (rootArr[group]->key == 0) {
		cout << rootArr[group]->data << endl;
		delete rootArr[group];
		rootArr[group] = nullptr;
	}
	else {									
		dummy = rootArr[group]->child;
		rootArr[group]->child->parent = nullptr;
		cout << rootArr[group]->data << endl;
		delete rootArr[group];
		rootArr[group] = nullptr;

		while (dummy->rightSibling != nullptr) {
			dummy = dummy->rightSibling;
		}

		while (dummy != nullptr) {
			leftDummy = dummy->leftSibling;
			if (leftDummy != nullptr) {
				leftDummy->rightSibling = nullptr;
			}
			dummy->leftSibling = nullptr;
			dummy->root = true;
			unionBHeap(dummy->key, dummy);
			dummy = leftDummy;
		}
	}
}

void BNHeap::increaseValue(int valueOld, int valueNew) {
	Modul* dummy = nullptr;
	bool used = false;
	for (int i = 0; i < MAX; i++) {
		if (rootArr[i] != nullptr) {
			dummy = search(valueOld, rootArr[i]);
			if (dummy != nullptr && dummy->data == valueOld) {
				break;
			}
		}
	}
	if (dummy != nullptr) {
		dummy->data = valueNew;
		heapifyUp(dummy);
		used = true;
	}
	if (!used) {
		cout << "na" << endl;
	}
}

Modul* BNHeap::search(int valueOld, Modul* root) {
	Modul* dummy = root;
	Modul* increased = nullptr;
	if (dummy == nullptr) {
		return nullptr;
	}
	if (dummy != nullptr && dummy->data == valueOld) {
		return dummy;
	}
	if (dummy->rightSibling != nullptr) {
		increased = search(valueOld, dummy->rightSibling);
		if (increased != nullptr) {
			return increased;
		}
	}
	if (dummy->child != nullptr) {
		increased = search(valueOld, dummy->child);
		if (increased != nullptr) {
			return increased;
		}
	}
	return increased;
}

void BNHeap::heapifyUp(Modul* element) {
	Modul* dummyElement = element;
	Modul* dummyParent = element->parent;
	Modul* dummyLeft = element->leftSibling;
	if (dummyLeft != nullptr && dummyElement->data > dummyLeft->data) {
		swap(dummyLeft->data, dummyElement->data);
		heapifyUp(dummyLeft);
	}
	else if (dummyParent != nullptr && dummyElement->data > dummyParent->data) {
		swap(dummyParent->data, dummyElement->data);
		heapifyUp(dummyParent);
	}
}

void BNHeap::print() {
	BNHeap dummy;
	int maxValue = NONE;
	int maxGroup = NONE;
	while (true) {
		maxValue = NONE;
		maxGroup = NONE;
		for (int i = 0; i < MAX; i++) {
			if (rootArr[i] != nullptr && maxValue < rootArr[i]->data) {
				maxValue = rootArr[i]->data;
				maxGroup = i;
			}
		}
		if (maxValue == NONE && maxGroup == NONE) {
			break;
		}
		else {
			dummy.addValue(maxValue);
			deleteRoot(maxGroup);
		}
	}
	for (int i = 0; i < MAX; i++) {
		rootArr[i] = dummy.rootArr[i];
	}
}



BNHeap::~BNHeap() {
	int maxValue = -1;
	int maxGroup = -1;
	while (true) {
		maxValue = -1;
		maxGroup = -1;
		for (int i = 0; i < MAX; i++) {
			if (rootArr[i] != nullptr && maxValue < rootArr[i]->data) {
				maxValue = rootArr[i]->data;
				maxGroup = i;
			}
		}
		if (maxValue == -1 && maxGroup == -1) {
			break;
		}
		else {
			deleteRoot(maxGroup);
		}
	}
}
