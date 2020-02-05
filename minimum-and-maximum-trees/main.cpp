#include"heap.h"

int main() {
	Heap kopiec;
	int liczbaWykonan;
	int liczbaOperacji;
	char operacja;
	std::cin >> liczbaWykonan;
	while (liczbaWykonan > 0) {
		std::cin >> liczbaOperacji;
			std::cin >> operacja;
			if (operacja == 's') {
				while (liczbaOperacji > 0) {
					kopiec.zmienKorzenMIN();
					liczbaOperacji--;
				}
				/*
				std::cout << "??????????DIAGNOZ?????????????????" << std::endl;
				for (int i = 0; i < kopiec.rozmiar; i++) {
					std::cout << kopiec.tablica[i].poczatkowyNumer << "   " << kopiec.tablica[i].data << std::endl;
				}
				std::cout << "min" << std::endl;

				for (int i = 0; i < kopiec.rozmiarMinHeap; i++) {
					std::cout << kopiec.minTablica[i]->poczatkowyNumer << "   " << kopiec.minTablica[i]->data << std::endl;
				}
				std::cout << "max" << std::endl;

				for (int i = 0; i < kopiec.rozmiarMaxHeap; i++) {
					std::cout << kopiec.maxTablica[i]->poczatkowyNumer << "   " << kopiec.maxTablica[i]->data << std::endl;
				}
				*/
			}
			else if(operacja == 'l') {
				while (liczbaOperacji > 0) {
					kopiec.zmienKorzenMAX();
					liczbaOperacji--;
				}
				/*
				std::cout << "??????????DIAGNOZA?????????????????" << std::endl;
				for (int i = 0; i < kopiec.rozmiar; i++) {
					std::cout << kopiec.tablica[i].poczatkowyNumer << "   " << kopiec.tablica[i].data << std::endl;
				}
				std::cout << "min" << std::endl;

				for (int i = 0; i < kopiec.rozmiarMinHeap; i++) {
					std::cout << kopiec.minTablica[i]->poczatkowyNumer << "   " << kopiec.minTablica[i]->data << std::endl;
				}
				std::cout << "max" << std::endl;

				for (int i = 0; i < kopiec.rozmiarMaxHeap; i++) {
					std::cout << kopiec.maxTablica[i]->poczatkowyNumer << "   " << kopiec.maxTablica[i]->data << std::endl;
				}
				*/
			}
		liczbaWykonan--;
	}
	kopiec.wypisz();
	return 0;
}