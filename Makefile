all:
	gcc -o scan-nfc scan-nfc.c -lnfc

clean:
	rm -f nfc *.o
