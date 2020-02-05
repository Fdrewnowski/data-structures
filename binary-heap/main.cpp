#include "BNHeap.h"

int main() {
	int runs, numberOfGroup, numberOfSecondGroup, valueNew, valueOld;
	char character;
	BNHeap stogi[1000];

	cin >> runs;
	while (runs) {
		cin >> character;
		if (character == 'a') {
			cin >> numberOfGroup;
			cin >> valueNew;
			stogi[numberOfGroup].addValue(valueNew);
		}
		else if (character == 'e') {
			cin >> numberOfGroup;
			stogi[numberOfGroup].extract();
		}
		else if (character == 'm') {
			cin >> numberOfGroup;
			cin >> numberOfSecondGroup;
			stogi[numberOfGroup].mergeHeaps(stogi[numberOfSecondGroup].rootArr);
		}
		else if (character == 'i') {
			cin >> numberOfGroup;
			cin >> valueOld;
			cin >> valueNew;
			stogi[numberOfGroup].increaseValue(valueOld, valueNew);
		}
		else if (character == 'p') {
			cin >> numberOfGroup;
			stogi[numberOfGroup].print();
		}
		runs--;
	}
	return 1;
}