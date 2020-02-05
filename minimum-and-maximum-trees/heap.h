#pragma once
#include <iostream>
#define TRYBOBA 3
#define TRYBMAX 2
#define TRYBMIN 1
struct modul {			//node with following values: startingNumber, index in Max tree, index in Min tree, data
	int poczatkowyNumer;
	int indexMAX;
	int indexMIN;
	unsigned int data;
};

class Heap {
public:
	Heap();
	~Heap();

	modul* tablica;					//main table in which there are values
	unsigned int rozmiar;
	void sortujheap(modul** minTab, modul** maxTab, int tryb);
	void wypisz();

	modul** minTablica;				//tree which root is minimum 
	unsigned int rozmiarMinHeap;
	void zmienKorzenMIN();
	void sortElementuMin(int indexMax);
	void minheap(int i, modul** tab);
	void minheapUP(int i, modul** tab);

	modul** maxTablica;				//tree which root is maximum
	unsigned int rozmiarMaxHeap;
	void zmienKorzenMAX();
	void sortElementuMax(int indexMin);
	void maxheap(int rodzic, modul** tab);
	void maxheapUP(int i, modul** tab);

	int rodzic(int dziecko);
	int leweDziecko(int rodzic, int size);
	int praweDziecko(int rodzic, int size);
};