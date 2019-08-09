#include <iostream>
#include <unistd.h>

int main()
{
	std::cout << "Hello FACT user!" << std::endl;
	std::cout << "This terminal explodes in" << std::endl;
	for (int i=10; i>0; i--){
		std::cout << i << " \r" << std::flush;
		sleep(1);
	}
	std::cout << "\r" << "boooo" << std::flush;
	sleep(1);
	std::cout << "OOOOOO" << std::flush;
	sleep(1);
	std::cout << "MMMMMM" << std::flush;
	sleep(1);
	std::cout << "mmmmm!" << std::endl;
	sleep(1);
}
