#include "heap.h"
#include<limits.h>
#define PUSTE 0
#define MAX 60000
#define ZERO 0
#define ERROR 0
using namespace std;

Heap::Heap() {
	unsigned int liczba;
	std::cin >> rozmiar;
	int flaga=0;
	tablica = new modul[rozmiar];
	minTablica = new modul*[rozmiar];
	maxTablica = new modul*[rozmiar];
	this->rozmiarMaxHeap = 0;
	this->rozmiarMinHeap = 0;

	for (int i = 0; i < rozmiar; i++) {
		cin >> liczba;
		tablica[i].data = liczba;
		tablica[i].poczatkowyNumer = i;

		if (tablica[i].data > 1) {
			minTablica[rozmiarMinHeap] = &(tablica[i]);
			minTablica[rozmiarMinHeap]->indexMIN = rozmiarMinHeap;
			maxTablica[rozmiarMaxHeap] = &(tablica[i]);
			maxTablica[rozmiarMaxHeap]->indexMAX = rozmiarMaxHeap;
			this->rozmiarMaxHeap += 1;
			this->rozmiarMinHeap += 1;
		}
	}
	sortujheap(minTablica, maxTablica, TRYBOBA);
}

Heap::~Heap() {
	delete tablica;
	delete minTablica;
	delete maxTablica;
}

void Heap::wypisz() {
	for (int j = 0; j < rozmiar; j++) {
		if (tablica[j].data >= 1) {
			cout << tablica[j].data;
		}
		else if (tablica[j].data == ZERO){
			cout << "m";
		}
		cout << " ";
	}
	cout << endl;
}

void Heap::sortujheap(modul** minTab, modul** maxTab, int tryb) {
	if (tryb == 3 || tryb == 2) {
		for (int i = rozmiarMaxHeap; i >= 0; i--) {
			maxheap(i, maxTab);
		}
	}
	if (tryb == 1 || tryb == 3) {
		for (int i = rozmiarMinHeap; i >= 0; i--) {
			minheap(i, minTab);
		}
	}
}

int Heap::rodzic(int dziecko) {
	return (dziecko - 1) / 2;
}

int Heap::leweDziecko(int rodzic, int size) {
	if ((2 * rodzic + 1) <= size) {
		return (2 * rodzic + 1);
	}
	else {
		return PUSTE;
	}
}

int Heap::praweDziecko(int rodzic, int size) {
	if ((2 * rodzic + 2) <= size) {
		return (2 * rodzic + 2);
	}
	else {
		return PUSTE;
	}
}


void Heap::zmienKorzenMAX() {
	int zero = 0;
	int indexMin = maxTablica[zero]->indexMIN;
	if (maxTablica[zero]->data % 2 == 0) {
		maxTablica[zero]->data = maxTablica[zero]->data / 2;
		if (maxTablica[zero]->data == 1 && rozmiarMinHeap > zero) {
			maxTablica[rozmiarMaxHeap - 1]->indexMAX = maxTablica[zero]->indexMAX;
			minTablica[rozmiarMinHeap - 1]->indexMIN = minTablica[indexMin]->indexMIN;
			swap(maxTablica[zero], maxTablica[rozmiarMaxHeap - 1]);
			swap(minTablica[indexMin], minTablica[rozmiarMinHeap - 1]);
			this->rozmiarMinHeap -= 1;
			this->rozmiarMaxHeap -= 1;
			sortElementuMax(indexMin);
		}
		else {
			sortElementuMax(indexMin);
		}
	}
	else if (maxTablica[zero]->data % 2 == 1 && maxTablica[zero]->data!=1) {
		if (rozmiarMinHeap > zero && maxTablica[zero]->data > (UINT_MAX - 1) / 3) {
			maxTablica[zero]->data = ERROR;
			maxTablica[rozmiarMaxHeap - 1]->indexMAX = maxTablica[zero]->indexMAX;
			minTablica[rozmiarMinHeap - 1]->indexMIN = minTablica[indexMin]->indexMIN;
			swap(maxTablica[zero], maxTablica[rozmiarMaxHeap - 1]);
			swap(minTablica[indexMin], minTablica[rozmiarMinHeap - 1]);
			this->rozmiarMinHeap -= 1;
			this->rozmiarMaxHeap -= 1;
			sortElementuMax(indexMin);
		}
		else {
			maxTablica[zero]->data = (3 * (maxTablica[zero]->data)) + 1;
			sortElementuMax(indexMin);
		}
	}
}

void Heap::sortElementuMax(int indexMin) {
	maxheap(0, maxTablica);
	int ojciec = rodzic(indexMin);
	if (indexMin < rozmiarMinHeap && ojciec >= 0 && minTablica[indexMin]->data >= minTablica[ojciec]->data) {
		if (minTablica[indexMin]->data > minTablica[ojciec]->data || minTablica[indexMin]->poczatkowyNumer < minTablica[ojciec]->poczatkowyNumer) {
			minheap(indexMin, minTablica);
		}
		else if (ojciec == 0) {
			minheap(indexMin, minTablica);
		}
	}
	else if (indexMin < rozmiarMinHeap && ojciec >= 0 && minTablica[indexMin]->data <= minTablica[ojciec]->data) {
		if (minTablica[indexMin]->data < minTablica[ojciec]->data || minTablica[indexMin]->poczatkowyNumer < minTablica[ojciec]->poczatkowyNumer) {
			minheapUP(indexMin, minTablica);
		}
		else if (ojciec == 0) {
			minheap(indexMin, minTablica);
		}
	}
	else if (indexMin < rozmiarMinHeap && ojciec < 0) {
		minheap(indexMin, minTablica);
	}
	else {}
}

void Heap::maxheap(int i, modul** tab) {
	int largest = i;
	int dummy;
	int lewy = leweDziecko(i, rozmiarMaxHeap);
	int prawy = praweDziecko(i, rozmiarMaxHeap);

	if (lewy != PUSTE && lewy < rozmiarMaxHeap && tab[lewy]->data != ERROR && tab[largest]->data != ERROR && tab[lewy]->data >= tab[largest]->data) {
		if (tab[lewy]->data > tab[largest]->data || tab[lewy]->poczatkowyNumer < tab[largest]->poczatkowyNumer) {
			largest = lewy;
		}
	}
	if (prawy != PUSTE && prawy < rozmiarMaxHeap && tab[prawy]->data != ERROR && tab[largest]->data != ERROR && tab[prawy]->data >= tab[largest]->data) {
		if (tab[prawy]->data > tab[largest]->data || tab[prawy]->poczatkowyNumer < tab[largest]->poczatkowyNumer) {
			largest = prawy;
		}
	}
	if (largest != i) {
		dummy = tab[i]->indexMAX;
		tab[i]->indexMAX = tab[largest]->indexMAX;
		tab[largest]->indexMAX = dummy;
		swap(tab[i], tab[largest]);
		maxheap(largest, tab);
	}
}

void Heap::maxheapUP(int i, modul** tab) {
	int largest = i;
	int dummy;
	int ojciec = rodzic(i);

	if (ojciec >= ZERO && largest < rozmiarMaxHeap && tab[ojciec]->data != ERROR && tab[largest]->data != ERROR && tab[ojciec]->data <= tab[largest]->data) {
		if (tab[ojciec]->data < tab[largest]->data || tab[ojciec]->poczatkowyNumer > tab[largest]->poczatkowyNumer) {
			largest = ojciec;
		}
	}
	if (largest != i) {
		dummy = tab[i]->indexMAX;
		tab[i]->indexMAX = tab[largest]->indexMAX;
		tab[largest]->indexMAX = dummy;
		swap(tab[i], tab[largest]);
		maxheapUP(largest, tab);
	}
}

void Heap::zmienKorzenMIN() {
	int zero = 0;
	int indexMax = minTablica[zero]->indexMAX;
		if (minTablica[zero]->data % 2 == 0) {
			minTablica[zero]->data = minTablica[zero]->data / 2;
			if (minTablica[zero]->data == 1 && rozmiarMinHeap > zero) {
				minTablica[rozmiarMinHeap - 1]->indexMIN = minTablica[zero]->indexMIN;
				maxTablica[rozmiarMaxHeap - 1]->indexMAX = maxTablica[indexMax]->indexMAX;
				swap(minTablica[zero], minTablica[rozmiarMinHeap - 1]);
				swap(maxTablica[indexMax], maxTablica[rozmiarMaxHeap - 1]);
				this->rozmiarMinHeap -= 1;
				this->rozmiarMaxHeap -= 1;
				sortElementuMin(indexMax);
			}
			else {
				sortElementuMin(indexMax);
			}
		}
		else if (minTablica[zero]->data % 2 == 1 && minTablica[zero]->data != 1) {
			if (rozmiarMinHeap > zero && minTablica[zero]->data > (UINT_MAX - 1) / 3) {
				minTablica[zero]->data = ERROR;
				minTablica[rozmiarMinHeap - 1]->indexMIN = minTablica[zero]->indexMIN;
				maxTablica[rozmiarMaxHeap - 1]->indexMAX = maxTablica[indexMax]->indexMAX;
				swap(minTablica[zero], minTablica[rozmiarMinHeap - 1]);
				swap(maxTablica[indexMax], maxTablica[rozmiarMaxHeap - 1]);
				this->rozmiarMinHeap -= 1;
				this->rozmiarMaxHeap -= 1;
				sortElementuMin(indexMax);
			}
			else {
				minTablica[zero]->data = (3 * minTablica[zero]->data) + 1;
				sortElementuMin(indexMax);
			}
		}
}

void Heap::sortElementuMin(int indexMax) {
	minheap(0, minTablica);
	int ojciec = rodzic(indexMax);
	if (indexMax < rozmiarMaxHeap && ojciec >= 0 && maxTablica[indexMax]->data <= maxTablica[ojciec]->data) {
		if (maxTablica[indexMax]->data < maxTablica[ojciec]->data || maxTablica[indexMax]->poczatkowyNumer < maxTablica[ojciec]->poczatkowyNumer) {
			maxheap(indexMax, maxTablica);
		}
		else if (ojciec == 0) {
			maxheap(indexMax, maxTablica);
		}
	}
	else if (indexMax < rozmiarMaxHeap && ojciec >= 0 && maxTablica[indexMax]->data >= maxTablica[ojciec]->data) {
		if (maxTablica[indexMax]->data > maxTablica[ojciec]->data || maxTablica[indexMax]->poczatkowyNumer < maxTablica[ojciec]->poczatkowyNumer) {
			maxheapUP(indexMax, maxTablica);
		}
		else if (ojciec == 0) {
			maxheap(indexMax, maxTablica);
		}
	}
	else if (indexMax < rozmiarMaxHeap && ojciec < 0) {
		maxheap(indexMax, maxTablica);
	}
	else {}
}

void Heap::minheap(int i, modul** tab) {
	int smallest = i;
	int dummy;
	int lewy = leweDziecko(i, rozmiarMinHeap);
	int prawy = praweDziecko(i, rozmiarMinHeap);

	if (lewy != PUSTE && lewy < rozmiarMinHeap && tab[lewy]->data != ERROR && tab[smallest]->data != ERROR && tab[lewy]->data <= tab[smallest]->data) {
		if (tab[lewy]->data < tab[smallest]->data || tab[lewy]->poczatkowyNumer < tab[smallest]->poczatkowyNumer) {
			smallest = lewy;
		}
	}
	if (prawy != PUSTE && prawy < rozmiarMinHeap && tab[prawy]->data != ERROR && tab[prawy]->data != ERROR && tab[prawy]->data <= tab[smallest]->data) {
		if (tab[prawy]->data < tab[smallest]->data || tab[prawy]->poczatkowyNumer < tab[smallest]->poczatkowyNumer) {
			smallest = prawy;
		}
	}
	if (smallest != i) {
		dummy = tab[i]->indexMIN;
		tab[i]->indexMIN = tab[smallest]->indexMIN;
		tab[smallest]->indexMIN = dummy;
		swap(tab[i], tab[smallest]);
		minheap(smallest, tab);
	}
}

void Heap::minheapUP(int i, modul** tab) {
	int smallest = i;
	int dummy;
	int ojciec = rodzic(i);

	if (ojciec >= ZERO && smallest < rozmiarMaxHeap && tab[ojciec]->data != ERROR && tab[smallest]->data != ERROR && tab[ojciec]->data >= tab[smallest]->data) {
		if (tab[ojciec]->data > tab[smallest]->data || tab[ojciec]->poczatkowyNumer > tab[smallest]->poczatkowyNumer) {
			smallest = ojciec;
		}
	}
	if (smallest != i) {
		dummy = tab[i]->indexMIN;
		tab[i]->indexMIN = tab[smallest]->indexMIN;
		tab[smallest]->indexMIN = dummy;
		swap(tab[i], tab[smallest]);
		minheapUP(smallest, tab);
	}
}